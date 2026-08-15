from __future__ import annotations


class IoTSensorService:
    def get_iot_readings(self, location: str, crop: str | None = None) -> dict:
        return {
            "location": location,
            "crop": crop or "unknown",
            "soil_moisture": 42,
            "soil_temperature": 27,
            "ph": 6.5,
            "moisture_status": "Slightly dry",
        }
