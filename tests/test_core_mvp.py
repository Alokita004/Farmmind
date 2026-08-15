from farmmind.app.decision.recommendation import make_recommendation
from farmmind.app.tools.crop_tools import analyze_crop_health
from farmmind.app.tools.market_tools import get_market_prices
from farmmind.app.tools.profit_tools import calculate_profit
from farmmind.app.decision.scoring import calculate_sustainability_score


def test_profit_calculation():
    result = calculate_profit(
        crop="Rice",
        farm_size_acres=5,
        expected_yield=50,
        selling_price=2450,
        seed_cost=5000,
        fertilizer_cost=3500,
        labor_cost=7000,
        irrigation_cost=3000,
        other_cost=2000,
    )
    assert result["estimated_profit"] > 0
    assert result["roi_percent"] > 0


def test_sustainability_score():
    result = calculate_sustainability_score(
        water_usage=60,
        fertilizer_usage=40,
        soil_health=70,
        crop_rotation=True,
        resource_efficiency=80,
        environmental_impact=25,
    )
    assert 0 <= result["sustainability_score"] <= 100


def test_crop_health_tool():
    result = analyze_crop_health(
        crop="Rice",
        location="Odisha",
        symptoms="yellow leaves and slow growth",
        soil_moisture=42,
        temperature=31,
    )
    assert result["health_score"] > 0
    assert result["status"]


def test_market_tool():
    result = get_market_prices(crop="Rice", location="Odisha")
    assert result["crop"] == "Rice"
    assert "trend" in result


def test_recommendation_engine():
    result = make_recommendation(
        health_score=71,
        market_score=78,
        profit_score=72,
        sustainability_score=80,
        crop="Rice",
    )
    assert result["overall_score"] > 0
    assert result["risk_level"] in {"Low", "Moderate", "High"}
    assert result["recommendation"]
