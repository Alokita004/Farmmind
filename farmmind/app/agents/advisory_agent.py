from __future__ import annotations


class AdvisoryAgent:
    def run(self, crop_health_result: dict) -> dict:
        actions = crop_health_result.get("recommended_actions", ["Monitor crop conditions"])
        priority = "High" if crop_health_result.get("health_score", 100) < 70 else "Medium"
        return {
            "priority": priority,
            "actions": actions,
            "reasoning": "The symptoms indicate possible nutrient or water stress, so timely field monitoring is recommended.",
        }
