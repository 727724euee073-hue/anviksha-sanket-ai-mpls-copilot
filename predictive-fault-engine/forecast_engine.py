"""Forecast future utilization from synthetic telemetry using Prophet.

This module loads telemetry.csv, trains a Prophet model on the utilization trend,
and produces a forecast dataframe for the next 50 intervals.

If Prophet is not available in the local environment, the script falls back to a
simple linear trend forecast so the pipeline can still run.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

try:
    from prophet import Prophet  # type: ignore
except ImportError:  # pragma: no cover - handled at runtime
    Prophet = None  # type: ignore


def load_telemetry(csv_path: str | Path | None = None) -> pd.DataFrame:
    """Load telemetry data from telemetry.csv."""
    if csv_path is None:
        csv_path = Path(__file__).resolve().parent / "telemetry.csv"

    telemetry = pd.read_csv(csv_path, parse_dates=["timestamp"])
    telemetry = telemetry.sort_values("timestamp").reset_index(drop=True)
    return telemetry


def fit_prophet_forecast(
    telemetry: pd.DataFrame,
    forecast_periods: int = 50,
) -> pd.DataFrame:
    """Fit a forecasting model and return the forecast dataframe."""
    required = {"timestamp", "utilization_percent"}
    missing = required - set(telemetry.columns)
    if missing:
        raise ValueError(f"Telemetry data is missing required columns: {sorted(missing)}")

    training_frame = telemetry[["timestamp", "utilization_percent"]].copy()
    training_frame = training_frame.rename(columns={"timestamp": "ds", "utilization_percent": "y"})
    training_frame = training_frame.sort_values("ds").reset_index(drop=True)

    if Prophet is not None:
        model = Prophet(
            interval_width=0.95,
            daily_seasonality=False,
            weekly_seasonality=False,
            yearly_seasonality=False,
            changepoint_prior_scale=0.05,
        )
        model.fit(training_frame)

        future = model.make_future_dataframe(periods=forecast_periods, freq="5min")
        forecast = model.predict(future)

        return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].copy()

    # Fallback forecast when Prophet cannot be imported.
    x = np.arange(len(training_frame))
    y = training_frame["y"].to_numpy(dtype=float)

    slope, intercept = np.polyfit(x, y, 1)
    future_x = np.arange(len(training_frame), len(training_frame) + forecast_periods)
    yhat = slope * future_x + intercept

    residuals = y - (slope * x + intercept)
    std_residual = float(residuals.std()) if len(residuals) > 1 else 0.0
    lower = yhat - 1.96 * std_residual
    upper = yhat + 1.96 * std_residual

    future_dates = pd.date_range(
        start=training_frame["ds"].iloc[-1] + pd.Timedelta(minutes=5),
        periods=forecast_periods,
        freq="5min",
    )
    return pd.DataFrame(
        {
            "ds": future_dates,
            "yhat": yhat,
            "yhat_lower": lower,
            "yhat_upper": upper,
        }
    )


def main() -> None:
    """Load telemetry, fit the forecast, and save it to an output CSV."""
    base_dir = Path(__file__).resolve().parent
    telemetry = load_telemetry(base_dir / "telemetry.csv")
    forecast = fit_prophet_forecast(telemetry, forecast_periods=50)

    output_dir = base_dir / "output"
    output_dir.mkdir(exist_ok=True)
    forecast_path = output_dir / "forecast.csv"
    forecast.to_csv(forecast_path, index=False)

    print(f"Forecast saved to {forecast_path}")
    print(forecast.head().to_string(index=False))


if __name__ == "__main__":
    main()
