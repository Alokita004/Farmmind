from __future__ import annotations

from pydantic import BaseModel


class CropHealthInput(BaseModel):
    crop: str
    location: str
    symptoms: str
    soil_moisture: float
    temperature: float


def analyze_crop_health(
    crop: str,
    location: str,
    symptoms: str,
    soil_moisture: float,
    temperature: float,
) -> dict:
    input_data = CropHealthInput(
        crop=crop,
        location=location,
        symptoms=symptoms,
        soil_moisture=soil_moisture,
        temperature=temperature,
    )

    adjusted_score = 88
    if "yellow" in input_data.symptoms.lower():
        adjusted_score -= 14
    if input_data.soil_moisture < 45:
        adjusted_score -= 8
    if input_data.temperature > 30:
        adjusted_score -= 5

    health_score = max(30, min(95, adjusted_score))
    status = "Low Risk" if health_score >= 80 else "Moderate Risk" if health_score >= 60 else "High Risk"
    issues = []
    if "yellow" in input_data.symptoms.lower():
        issues.append("Nitrogen deficiency")
    if input_data.soil_moisture < 45:
        issues.append("Water stress")
    if not issues:
        issues = ["Monitor for nutrient imbalance"]

    actions = []
    if "yellow" in input_data.symptoms.lower():
        actions.append("Check soil nitrogen")
    if input_data.soil_moisture < 45:
        actions.append("Monitor irrigation")
    if not actions:
        actions = ["Inspect crop canopy and soil conditions"]

    return {
        "crop": input_data.crop,
        "health_score": health_score,
        "status": status,
        "possible_issues": issues,
        "recommended_actions": actions,
    }
