from __future__ import annotations


class WeatherService:
    def get_weather(self, location: str, crop: str | None = None) -> dict:
        return {
            "temperature": 31,
            "humidity": 72,
            "rainfall_mm": 12,
            "forecast": "Moderate rainfall",
            "location": location,
            "crop": crop or "unknown",
        }
