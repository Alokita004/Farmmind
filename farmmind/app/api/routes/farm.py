from __future__ import annotations

import uuid

from fastapi import APIRouter

from farmmind.app.graph.workflow import build_workflow
from farmmind.app.schemas.requests import AnalysisRequest

router = APIRouter(prefix="/api/v1", tags=["farm"])


@router.post("/farm/analyze", summary="Run a complete farm analysis")
async def analyze_farm(request: AnalysisRequest):
    workflow = build_workflow()
    state = {
        "user_query": request.query,
        "farmer_profile": request.farmer.model_dump(),
        "crop_data": request.crop.model_dump(),
        "required_agents": ["crop_health", "advisory", "market", "profit", "sustainability"],
        "final_response": "",
    }
    result = workflow.invoke(state)
    return {
        "request_id": str(uuid.uuid4()),
        "query": request.query,
        "agents_used": result.get("required_agents", []),
        "analysis": {
            "crop_health": result.get("crop_health_result", {}),
            "advisory": result.get("advisory_result", {}),
            "market": result.get("market_result", {}),
            "profit": result.get("profit_result", {}),
            "sustainability": result.get("sustainability_result", {}),
        },
        "recommendation": result.get("recommendation_result", {}),
        "final_answer": result.get("final_response", "Recommendation generated.")
    }
