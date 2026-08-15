from __future__ import annotations

from farmmind.app.tools.sustainability_tools import calculate_sustainability


class SustainabilityAgent:
    def __init__(self):
        self.tool = calculate_sustainability

    def run(
        self,
        water_usage: float,
        fertilizer_usage: float,
        soil_health: float,
        crop_rotation: bool,
        resource_efficiency: float,
        environmental_impact: float,
    ) -> dict:
        return self.tool(
            water_usage=water_usage,
            fertilizer_usage=fertilizer_usage,
            soil_health=soil_health,
            crop_rotation=crop_rotation,
            resource_efficiency=resource_efficiency,
            environmental_impact=environmental_impact,
        )
