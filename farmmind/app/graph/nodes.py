from __future__ import annotations

import json

from farmmind.app.graph.state import FarmMindState
from farmmind.app.llm.provider import LLMProvider
from farmmind.app.llm.prompts import FINAL_RESPONSE_PROMPT, ROUTER_PROMPT
from farmmind.app.tools.crop_tools import analyze_crop_health
from farmmind.app.tools.market_tools import get_market_prices
from farmmind.app.tools.profit_tools import calculate_profit
from farmmind.app.tools.sustainability_tools import calculate_sustainability
from farmmind.app.decision.recommendation import make_recommendation
from farmmind.app.decision.scoring import score_health, score_market, score_profit, score_sustainability


llm_provider = LLMProvider()


def router_node(state: FarmMindState) -> FarmMindState:
    query = state["user_query"]
    prompt = ROUTER_PROMPT.format(query=query)
    response = llm_provider.invoke(prompt)
    try:
        payload = json.loads(response)
        intents = payload.get("intents") if isinstance(payload, dict) else ["market", "profit"]
    except Exception:
        intents = ["market", "profit"] if "sell" in query.lower() or "price" in query.lower() else ["crop_health", "advisory"]
    if "complete analysis" in query.lower() or ("farm" in query.lower() and "analysis" in query.lower()):
        intents = ["crop_health", "advisory", "market", "profit", "sustainability"]
    state["required_agents"] = list(dict.fromkeys(intents))
    state["pending_agents"] = list(state["required_agents"])
    return state


def consume_next_agent(state: FarmMindState) -> str:
    remaining = state.get("pending_agents", [])
    if not remaining:
        return "recommendation_node"
    next_agent = remaining[0]
    return {
        "crop_health": "crop_health_node",
        "advisory": "advisory_node",
        "market": "market_node",
        "profit": "profit_node",
        "sustainability": "sustainability_node",
    }.get(next_agent, "recommendation_node")


def crop_health_node(state: FarmMindState) -> FarmMindState:
    crop = state["crop_data"].get("name", "Rice")
    farmer = state["farmer_profile"]
    state["crop_health_result"] = analyze_crop_health(
        crop=crop,
        location=farmer.get("location", "Odisha"),
        symptoms="yellow leaves and slow growth",
        soil_moisture=42,
        temperature=31,
    )
    state["pending_agents"] = state.get("pending_agents", [])[1:]
    return state


def advisory_node(state: FarmMindState) -> FarmMindState:
    health = state.get("crop_health_result", {"possible_issues": ["Check soil and irrigation"], "recommended_actions": ["Monitor crop"]})
    state["advisory_result"] = {
        "priority": "High" if health.get("health_score", 0) < 70 else "Medium",
        "actions": health.get("recommended_actions", ["Monitor crop conditions"]),
        "reasoning": "The crop symptoms indicate possible nutrient or water stress requiring prompt attention.",
    }
    state["pending_agents"] = state.get("pending_agents", [])[1:]
    return state


def market_node(state: FarmMindState) -> FarmMindState:
    crop = state["crop_data"]["name"]
    state["market_result"] = get_market_prices(crop=crop, location=state["farmer_profile"].get("location", "Odisha"))
    state["pending_agents"] = state.get("pending_agents", [])[1:]
    return state


def profit_node(state: FarmMindState) -> FarmMindState:
    crop = state["crop_data"]["name"]
    farmer = state["farmer_profile"]
    state["profit_result"] = calculate_profit(
        crop=crop,
        farm_size_acres=farmer.get("farm_size_acres", 5),
        expected_yield=state["crop_data"].get("expected_yield_quintals", 50),
        selling_price=state.get("market_result", {}).get("current_price", 2450),
        seed_cost=5000,
        fertilizer_cost=3500,
        labor_cost=7000,
        irrigation_cost=3000,
        other_cost=2000,
    )
    state["pending_agents"] = state.get("pending_agents", [])[1:]
    return state


def sustainability_node(state: FarmMindState) -> FarmMindState:
    state["sustainability_result"] = calculate_sustainability(
        water_usage=60,
        fertilizer_usage=40,
        soil_health=70,
        crop_rotation=True,
        resource_efficiency=80,
        environmental_impact=25,
    )
    state["pending_agents"] = state.get("pending_agents", [])[1:]
    return state


def recommendation_node(state: FarmMindState) -> FarmMindState:
    health_score = score_health(state.get("crop_health_result", {}).get("health_score", 75))
    market_score = score_market(float(state.get("market_result", {}).get("price_change_percent", 2.5)))
    profit_result = state.get("profit_result", {"roi_percent": 25})
    profit_score = score_profit(float(profit_result.get("roi_percent", 25)))
    sustainability_score = score_sustainability(state.get("sustainability_result", {}).get("sustainability_score", 75))
    crop = state["crop_data"]["name"]
    state["recommendation_result"] = make_recommendation(
        health_score=health_score,
        market_score=market_score,
        profit_score=profit_score,
        sustainability_score=sustainability_score,
        crop=crop,
    )
    return state


def response_node(state: FarmMindState) -> FarmMindState:
    summary = {
        "query": state["user_query"],
        "crop_health": state.get("crop_health_result", {}),
        "advisory": state.get("advisory_result", {}),
        "market": state.get("market_result", {}),
        "profit": state.get("profit_result", {}),
        "sustainability": state.get("sustainability_result", {}),
        "recommendation": state.get("recommendation_result", {}),
    }
    final_prompt = FINAL_RESPONSE_PROMPT.format(analysis_summary=summary)
    state["final_response"] = llm_provider.invoke(final_prompt)
    return state
