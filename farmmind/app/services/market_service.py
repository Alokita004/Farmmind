from __future__ import annotations

import json
from pathlib import Path

from farmmind.app.core.config import BASE_DIR


class MarketDataService:
    def __init__(self, source_path: str | None = None):
        self.source_path = Path(source_path or BASE_DIR / "data" / "market_data.json")

    def load_market_data(self) -> dict:
        if not self.source_path.exists():
            return self._default_market_data()
        with self.source_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else self._default_market_data()

    def get_price_for_crop(self, crop: str, location: str | None = None) -> dict:
        data = self.load_market_data()
        crops = data.get("crops", {})
        crop_key = crop.lower()
        record = crops.get(crop_key)
        if not record:
            fallback = {"crop": crop, "current_price": 2100, "previous_price": 2000, "unit": "INR/quintal", "trend": "Stable"}
            return fallback
        return {
            "crop": crop,
            "current_price": record.get("current_price", 2100),
            "previous_price": record.get("previous_price", 2000),
            "unit": record.get("unit", "INR/quintal"),
            "trend": record.get("trend", "Stable"),
        }

    @staticmethod
    def _default_market_data() -> dict:
        return {
            "crops": {
                "rice": {"current_price": 2450, "previous_price": 2380, "unit": "INR/quintal", "trend": "Increasing"},
                "wheat": {"current_price": 2300, "previous_price": 2250, "unit": "INR/quintal", "trend": "Stable"},
                "maize": {"current_price": 1900, "previous_price": 1850, "unit": "INR/quintal", "trend": "Increasing"},
                "mustard": {"current_price": 4200, "previous_price": 4050, "unit": "INR/quintal", "trend": "Increasing"},
            }
        }
