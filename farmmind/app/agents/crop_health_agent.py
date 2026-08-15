from __future__ import annotations

from farmmind.app.tools.crop_tools import analyze_crop_health


class CropHealthAgent:
    def __init__(self):
        self.tool = analyze_crop_health

    def run(self, crop: str, location: str, symptoms: str, soil_moisture: float, temperature: float) -> dict:
        return self.tool(crop, location, symptoms, soil_moisture, temperature)
