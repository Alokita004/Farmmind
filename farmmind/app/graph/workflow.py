from __future__ import annotations

from langgraph.graph import END, START, StateGraph

from farmmind.app.graph.nodes import (
    advisory_node,
    consume_next_agent,
    crop_health_node,
    market_node,
    profit_node,
    recommendation_node,
    response_node,
    router_node,
    sustainability_node,
)
from farmmind.app.graph.state import FarmMindState


def build_workflow():
    workflow = StateGraph(FarmMindState)
    workflow.add_node("router_node", router_node)
    workflow.add_node("crop_health_node", crop_health_node)
    workflow.add_node("advisory_node", advisory_node)
    workflow.add_node("market_node", market_node)
    workflow.add_node("profit_node", profit_node)
    workflow.add_node("sustainability_node", sustainability_node)
    workflow.add_node("recommendation_node", recommendation_node)
    workflow.add_node("response_node", response_node)

    workflow.add_edge(START, "router_node")
    workflow.add_conditional_edges(
        "router_node",
        consume_next_agent,
        {
            "crop_health_node": "crop_health_node",
            "advisory_node": "advisory_node",
            "market_node": "market_node",
            "profit_node": "profit_node",
            "sustainability_node": "sustainability_node",
            "recommendation_node": "recommendation_node",
        },
    )

    workflow.add_conditional_edges(
        "crop_health_node",
        consume_next_agent,
        {
            "crop_health_node": "crop_health_node",
            "advisory_node": "advisory_node",
            "market_node": "market_node",
            "profit_node": "profit_node",
            "sustainability_node": "sustainability_node",
            "recommendation_node": "recommendation_node",
        },
    )
    workflow.add_conditional_edges(
        "advisory_node",
        consume_next_agent,
        {
            "crop_health_node": "crop_health_node",
            "advisory_node": "advisory_node",
            "market_node": "market_node",
            "profit_node": "profit_node",
            "sustainability_node": "sustainability_node",
            "recommendation_node": "recommendation_node",
        },
    )
    workflow.add_conditional_edges(
        "market_node",
        consume_next_agent,
        {
            "crop_health_node": "crop_health_node",
            "advisory_node": "advisory_node",
            "market_node": "market_node",
            "profit_node": "profit_node",
            "sustainability_node": "sustainability_node",
            "recommendation_node": "recommendation_node",
        },
    )
    workflow.add_conditional_edges(
        "profit_node",
        consume_next_agent,
        {
            "crop_health_node": "crop_health_node",
            "advisory_node": "advisory_node",
            "market_node": "market_node",
            "profit_node": "profit_node",
            "sustainability_node": "sustainability_node",
            "recommendation_node": "recommendation_node",
        },
    )
    workflow.add_conditional_edges(
        "sustainability_node",
        consume_next_agent,
        {
            "crop_health_node": "crop_health_node",
            "advisory_node": "advisory_node",
            "market_node": "market_node",
            "profit_node": "profit_node",
            "sustainability_node": "sustainability_node",
            "recommendation_node": "recommendation_node",
        },
    )
    workflow.add_edge("recommendation_node", "response_node")
    workflow.add_edge("response_node", END)

    return workflow.compile()
