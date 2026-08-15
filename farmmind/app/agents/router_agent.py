from __future__ import annotations

import json

from farmmind.app.llm.provider import LLMProvider


class RouterAgent:
    def __init__(self):
        self.llm = LLMProvider()

    def classify(self, query: str) -> list[str]:
        prompt = (
            "Classify the user request into one or more intents among: "
            "crop_health, advisory, market, profit, sustainability, complete_analysis. "
            "Return JSON: {\"intents\": [...]}\n"
            f"Query: {query}"
        )
        try:
            response = self.llm.invoke(prompt)
            payload = json.loads(response)
            if isinstance(payload, dict):
                return payload.get("intents", ["market", "profit"])
        except Exception:
            pass
        if "complete" in query.lower() and "farm" in query.lower():
            return ["crop_health", "advisory", "market", "profit", "sustainability"]
        if "sell" in query.lower() or "price" in query.lower() or "market" in query.lower():
            return ["market", "profit"]
        if "yellow" in query.lower() or "health" in query.lower() or "disease" in query.lower():
            return ["crop_health", "advisory"]
        return ["market", "profit", "sustainability"]
