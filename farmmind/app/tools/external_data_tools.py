from __future__ import annotations

from farmmind.app.services.weather_service import WeatherService
from farmmind.app.services.iot_service import IoTSensorService
from farmmind.app.services.satellite_service import SatelliteService


def get_weather_snapshot(location: str, crop: str | None = None) -> dict:
    service = WeatherService()
    return service.get_weather(location=location, crop=crop)


def get_iot_snapshot(location: str, crop: str | None = None) -> dict:
    service = IoTSensorService()
    return service.get_iot_readings(location=location, crop=crop)


def get_satellite_snapshot(location: str, crop: str | None = None) -> dict:
    service = SatelliteService()
    return service.get_satellite_summary(location=location, crop=crop)
