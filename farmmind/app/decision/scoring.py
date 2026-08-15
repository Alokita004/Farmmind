from __future__ import annotations


def score_market(price_change_percent: float) -> int:
    if price_change_percent >= 8:
        return 90
    if price_change_percent >= 4:
        return 80
    if price_change_percent >= 1:
        return 70
    if price_change_percent >= -2:
        return 60
    if price_change_percent >= -5:
        return 45
    return 30


def score_profit(roi_percent: float) -> int:
    if roi_percent >= 60:
        return 90
    if roi_percent >= 35:
        return 80
    if roi_percent >= 15:
        return 65
    if roi_percent >= 0:
        return 50
    return 25


def score_health(health_score: float) -> int:
    return max(0, min(100, int(health_score)))


def score_sustainability(sustainability_score: float) -> int:
    return max(0, min(100, int(sustainability_score)))


def calculate_sustainability_score(
    water_usage: float,
    fertilizer_usage: float,
    soil_health: float,
    crop_rotation: bool,
    resource_efficiency: float,
    environmental_impact: float,
) -> dict:
    base = 100
    base -= min(water_usage, 70) * 0.35
    base -= min(fertilizer_usage, 70) * 0.25
    base -= max(0, 70 - soil_health) * 0.2
    if crop_rotation:
        base += 8
    base += min(resource_efficiency, 100) * 0.15
    base -= environmental_impact * 0.12
    score = max(0, min(100, round(base)))

    if score >= 80:
        water_efficiency = "Good"
        soil_health_label = "Good"
        resource_efficiency_label = "Good"
    elif score >= 60:
        water_efficiency = "Moderate"
        soil_health_label = "Moderate"
        resource_efficiency_label = "Good"
    else:
        water_efficiency = "Low"
        soil_health_label = "Poor"
        resource_efficiency_label = "Needs Improvement"

    return {
        "sustainability_score": score,
        "water_efficiency": water_efficiency,
        "soil_health": soil_health_label,
        "resource_efficiency": resource_efficiency_label,
        "recommendations": [
            "Use crop rotation",
            "Optimize irrigation",
            "Reduce unnecessary fertilizer usage",
        ],
    }
