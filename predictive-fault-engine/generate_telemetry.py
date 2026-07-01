"""Generate synthetic MPLS telemetry for a congestion drift scenario.

This script creates a CSV file with ~500 rows of telemetry sampled every 5 minutes.
The synthetic data shows utilization growing gradually from around 60% toward 95%
with realistic noise, while latency and jitter rise in a loosely correlated way.
"""

from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd


def generate_telemetry(rows: int = 500, interval_minutes: int = 5, start_time: datetime | None = None) -> pd.DataFrame:
    """Create a synthetic telemetry dataset for a congesting network link."""
    if start_time is None:
        start_time = datetime(2026, 1, 1, 0, 0)

    rng = np.random.default_rng(42)
    time_index = np.arange(rows)

    # Build a gradual congestion trend that rises from ~60% to ~95%.
    trend = 60 + 35 * (1 - np.exp(-0.007 * time_index))

    # Add realistic noise so the path looks natural rather than perfectly smooth.
    noise = (
        0.8 * np.sin(time_index / 16)
        + 0.5 * np.cos(time_index / 9)
        + rng.normal(0, 1.8, size=rows)
    )
    utilization = np.clip(trend + noise, 55.0, 98.0)

    # Make latency and jitter rise as congestion worsens, but with some noise.
    latency = 18 + 0.45 * utilization + rng.normal(0, 2.4, size=rows)
    jitter = 3 + 0.08 * np.maximum(0, utilization - 70) + rng.normal(0, 0.8, size=rows)

    timestamps = [start_time + timedelta(minutes=interval_minutes * i) for i in range(rows)]

    df = pd.DataFrame(
        {
            "timestamp": timestamps,
            "utilization_percent": utilization,
            "latency_ms": latency,
            "jitter_ms": jitter,
        }
    )
    return df


def main() -> None:
    """Generate telemetry and save it to telemetry.csv in the current folder."""
    output_dir = Path(__file__).resolve().parent
    output_path = output_dir / "telemetry.csv"

    telemetry = generate_telemetry()
    telemetry.to_csv(output_path, index=False)

    print(f"Generated {len(telemetry)} telemetry rows at {output_path}")
    print(telemetry.head().to_string(index=False))


if __name__ == "__main__":
    main()
