from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


class CropHealthResult(BaseModel):
    crop: str
    health_score: int = Field(..., ge=0, le=100)
    status: str
    possible_issues: list[str] = Field(default_factory=list)
    recommended_actions: list[str] = Field(default_factory=list)


class AdvisoryResult(BaseModel):
    priority: Literal["High", "Medium", "Low"]
    actions: list[str] = Field(default_factory=list)
    reasoning: str


class MarketResult(BaseModel):
    crop: str
    current_price: float
    trend: str
    price_change_percent: float
    selling_recommendation: str
    source: str = "mock market data"


class ProfitResult(BaseModel):
    revenue: float
    total_cost: float
    estimated_profit: float
    roi_percent: float


class SustainabilityResult(BaseModel):
    sustainability_score: int = Field(..., ge=0, le=100)
    water_efficiency: str
    soil_health: str
    resource_efficiency: str
    recommendations: list[str] = Field(default_factory=list)


class RecommendationResult(BaseModel):
    overall_score: float
    risk_level: str
    recommendation: str
    key_factors: list[str] = Field(default_factory=list)


class ChatResponse(BaseModel):
    request_id: str
    query: str
    agents_used: list[str]
    analysis: dict[str, Any]
    recommendation: dict[str, Any]
    final_answer: str


class HealthResponse(BaseModel):
    status: str = "healthy"
