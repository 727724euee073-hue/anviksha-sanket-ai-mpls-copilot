"""Run the full predictive fault analytics pipeline from one command."""

from __future__ import annotations

from pathlib import Path

from forecast_engine import fit_prophet_forecast, load_telemetry
from generate_telemetry import generate_telemetry
from impact_calc import calculate_impact, load_forecast
from output_generator import create_chart


def run_pipeline() -> None:
    """Generate telemetry, train the forecast, calculate the alert, and save outputs."""
    base_dir = Path(__file__).resolve().parent
    output_dir = base_dir / "output"
    output_dir.mkdir(exist_ok=True)

    telemetry = generate_telemetry(rows=500)
    telemetry_path = base_dir / "telemetry.csv"
    telemetry.to_csv(telemetry_path, index=False)

    loaded_telemetry = load_telemetry(telemetry_path)
    forecast = fit_prophet_forecast(loaded_telemetry, forecast_periods=50)
    forecast_path = output_dir / "forecast.csv"
    forecast.to_csv(forecast_path, index=False)

    alert = calculate_impact(forecast, now_time=loaded_telemetry["timestamp"].iloc[-1])
    alert_path = output_dir / "prediction_alert.json"
    alert_path.write_text(__import__("json").dumps(alert, indent=2), encoding="utf-8")

    chart_path = output_dir / "forecast_chart.png"
    create_chart(loaded_telemetry, forecast, alert, chart_path)

    print("Pipeline completed successfully.")
    print(f"Telemetry: {telemetry_path}")
    print(f"Forecast: {forecast_path}")
    print(f"Alert: {alert_path}")
    print(f"Chart: {chart_path}")


if __name__ == "__main__":
    run_pipeline()
