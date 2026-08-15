from __future__ import annotations


def make_recommendation(
    health_score: float,
    market_score: float,
    profit_score: float,
    sustainability_score: float,
    crop: str,
) -> dict:
    overall_score = (
        health_score * 0.25
        + market_score * 0.20
        + profit_score * 0.30
        + sustainability_score * 0.25
    )

    if overall_score >= 80:
        risk_level = "Low"
        recommendation = f"Continue {crop} cultivation with optimized irrigation and consider selling a portion of the crop."
    elif overall_score >= 60:
        risk_level = "Moderate"
        recommendation = f"Maintain current {crop} practices, improve monitoring, and adjust inputs to reduce risk."
    else:
        risk_level = "High"
        recommendation = f"Reassess the {crop} plan, prioritize soil and water management, and consider alternative crops."

    key_factors = []
    if market_score >= 70:
        key_factors.append("Strong market trend")
    if profit_score >= 60:
        key_factors.append("Positive estimated ROI")
    if health_score < 80:
        key_factors.append("Moderate crop health risk")
    if sustainability_score >= 70:
        key_factors.append("Good sustainability score")

    if not key_factors:
        key_factors = ["Monitor field performance closely"]

    return {
        "overall_score": round(overall_score, 2),
        "risk_level": risk_level,
        "recommendation": recommendation,
        "key_factors": key_factors,
    }
