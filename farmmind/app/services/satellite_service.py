from __future__ import annotations


class SatelliteService:
    def get_satellite_summary(self, location: str, crop: str | None = None) -> dict:
        return {
            "location": location,
            "crop": crop or "unknown",
            "ndvi": 0.72,
            "vegetation_status": "Healthy",
            "notes": "Moderate vegetation vigor and stable field pattern.",
        }
