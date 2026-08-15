from __future__ import annotations

from farmmind.app.services.market_service import MarketDataService


def get_market_prices(crop: str, location: str | None = None) -> dict:
    service = MarketDataService()
    data = service.get_price_for_crop(crop, location)
    current = float(data["current_price"])
    previous = float(data["previous_price"])
    change = ((current - previous) / previous) * 100 if previous else 0.0
    if change >= 3:
        recommendation = "Hold"
        trend = "Increasing"
    elif change >= 0:
        recommendation = "Hold"
        trend = "Stable"
    else:
        recommendation = "Consider Selling"
        trend = "Decreasing"
    return {
        "crop": crop,
        "current_price": current,
        "trend": trend,
        "price_change_percent": round(change, 2),
        "selling_recommendation": recommendation,
        "source": "Mock market feed",
    }
