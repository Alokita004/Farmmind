from __future__ import annotations

from typing import TypedDict

from typing_extensions import NotRequired


class FarmMindState(TypedDict):
    user_query: str
    farmer_profile: dict
    crop_data: dict
    crop_health_result: NotRequired[dict]
    advisory_result: NotRequired[dict]
    market_result: NotRequired[dict]
    profit_result: NotRequired[dict]
    sustainability_result: NotRequired[dict]
    required_agents: list[str]
    pending_agents: NotRequired[list[str]]
    recommendation_result: NotRequired[dict]
    final_response: str
