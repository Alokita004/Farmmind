from __future__ import annotations

import pandas as pd


def calculate_profit(
    crop: str,
    farm_size_acres: float,
    expected_yield: float,
    selling_price: float,
    seed_cost: float,
    fertilizer_cost: float,
    labor_cost: float,
    irrigation_cost: float,
    other_cost: float,
) -> dict:
    data = pd.DataFrame(
        [{
            "crop": crop,
            "farm_size_acres": float(farm_size_acres),
            "expected_yield": float(expected_yield),
            "selling_price": float(selling_price),
            "seed_cost": float(seed_cost),
            "fertilizer_cost": float(fertilizer_cost),
            "labor_cost": float(labor_cost),
            "irrigation_cost": float(irrigation_cost),
            "other_cost": float(other_cost),
        }]
    )

    revenue = data["expected_yield"] * data["selling_price"]
    total_cost = (
        data["seed_cost"]
        + data["fertilizer_cost"]
        + data["labor_cost"]
        + data["irrigation_cost"]
        + data["other_cost"]
    )
    profit = revenue - total_cost

    revenue_value = float(revenue.iloc[0])
    total_cost_value = float(total_cost.iloc[0])
    profit_value = float(profit.iloc[0])
    roi_value = (profit_value / total_cost_value * 100) if total_cost_value else 0.0

    return {
        "revenue": round(revenue_value, 2),
        "total_cost": round(total_cost_value, 2),
        "estimated_profit": round(profit_value, 2),
        "roi_percent": round(roi_value, 2),
    }
