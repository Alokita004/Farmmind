from __future__ import annotations

from typing import Any

from farmmind.app.core.config import settings


class MockLLM:
    def __init__(self, model: str = "mock-model"):
        self.model = model

    def invoke(self, prompt: str, **kwargs: Any) -> str:
        if "classify" in prompt.lower() or "intent" in prompt.lower():
            return '{"intents": ["market", "profit", "sustainability"]}'
        return (
            "Here is the recommendation: maintain balanced irrigation, monitor crop health, "
            "and consider market timing to improve profitability while protecting sustainability."
        )


class LLMProvider:
    def __init__(self):
        self.provider = settings.LLM_PROVIDER.lower()
        self.mock = MockLLM(settings.OPENAI_MODEL)

    def get_client(self):
        if self.provider in {"openai", "azure"} and settings.OPENAI_API_KEY:
            return self.mock
        return self.mock

    def invoke(self, prompt: str, **kwargs: Any) -> str:
        return self.mock.invoke(prompt, **kwargs)
