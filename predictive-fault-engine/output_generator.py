"""Create a visualization and a structured alert JSON for the forecast.

This script combines the historical telemetry, the forecast, and the breach
threshold into a single chart and writes the alert payload to output/prediction_alert.json.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from impact_calc import calculate_impact, load_forecast
from forecast_engine import load_telemetry


def create_chart(
    telemetry: pd.DataFrame,
    forecast: pd.DataFrame,
    alert: dict,
    output_path: str | Path,
) -> None:
    """Plot historical utilization, forecast, threshold, and breach marker."""
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(telemetry["timestamp"], telemetry["utilization_percent"], label="Historical utilization", color="royalblue")
    ax.plot(forecast["ds"], forecast["yhat"], label="Forecast", color="tomato")
    ax.fill_between(forecast["ds"], forecast["yhat_lower"], forecast["yhat_upper"], color="tomato", alpha=0.2)

    threshold = 90.0
    ax.axhline(threshold, linestyle="--", color="darkorange", label="SLA threshold (90%)")

    breach_row = forecast[forecast["yhat"] >= threshold].iloc[0]
    ax.scatter(breach_row["ds"], breach_row["yhat"], color="red", s=80, zorder=5, label="Predicted breach")

    ax.set_title("Forecasted Link Congestion Risk")
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("Utilization (%)")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best")

    fig.tight_layout()
    fig.savefig(output_path, dpi=180)
    plt.close(fig)


def main() -> None:
    """Generate the alert JSON and the forecast chart."""
    base_dir = Path(__file__).resolve().parent
    telemetry = load_telemetry(base_dir / "telemetry.csv")
    forecast = load_forecast(base_dir / "output" / "forecast.csv")
    alert = calculate_impact(forecast, now_time=telemetry["timestamp"].iloc[-1])

    output_dir = base_dir / "output"
    output_dir.mkdir(exist_ok=True)

    chart_path = output_dir / "forecast_chart.png"
    create_chart(telemetry, forecast, alert, chart_path)

    alert_path = output_dir / "prediction_alert.json"
    alert_path.write_text(json.dumps(alert, indent=2), encoding="utf-8")

    print(f"Chart saved to {chart_path}")
    print(f"Alert saved to {alert_path}")
    print(json.dumps(alert, indent=2))


if __name__ == "__main__":
    main()
