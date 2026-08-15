from __future__ import annotations

from farmmind.app.tools.market_tools import get_market_prices


class MarketAgent:
    def __init__(self):
        self.tool = get_market_prices

    def run(self, crop: str, location: str) -> dict:
        return self.tool(crop=crop, location=location)
