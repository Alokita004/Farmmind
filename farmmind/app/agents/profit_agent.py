from __future__ import annotations

from farmmind.app.tools.profit_tools import calculate_profit


class ProfitAgent:
    def __init__(self):
        self.tool = calculate_profit

    def run(
        self,
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
        return self.tool(
            crop=crop,
            farm_size_acres=farm_size_acres,
            expected_yield=expected_yield,
            selling_price=selling_price,
            seed_cost=seed_cost,
            fertilizer_cost=fertilizer_cost,
            labor_cost=labor_cost,
            irrigation_cost=irrigation_cost,
            other_cost=other_cost,
        )
