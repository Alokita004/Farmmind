class FarmMindError(Exception):
    """Base exception for FarmMind."""


class LLMServiceError(FarmMindError):
    pass


class AgentExecutionError(FarmMindError):
    pass


class ToolExecutionError(FarmMindError):
    pass


class DatabaseError(FarmMindError):
    pass


class RedisUnavailableError(FarmMindError):
    pass


class VectorDBError(FarmMindError):
    pass
