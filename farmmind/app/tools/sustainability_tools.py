from __future__ import annotations

from farmmind.app.decision.scoring import calculate_sustainability_score


def calculate_sustainability(
    water_usage: float,
    fertilizer_usage: float,
    soil_health: float,
    crop_rotation: bool,
    resource_efficiency: float,
    environmental_impact: float,
) -> dict:
    return calculate_sustainability_score(
        water_usage=water_usage,
        fertilizer_usage=fertilizer_usage,
        soil_health=soil_health,
        crop_rotation=crop_rotation,
        resource_efficiency=resource_efficiency,
        environmental_impact=environmental_impact,
    )
