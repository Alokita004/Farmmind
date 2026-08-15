import logging
import sys

from farmmind.app.core.config import settings


logger = logging.getLogger("farmmind")
logger.setLevel(getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO))

if not logger.handlers:
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(
        "%(asctime)s %(levelname)s agent=%(agent)s tool=%(tool)s duration=%(duration)s %(message)s"
    ))
    logger.addHandler(handler)


def get_logger(name: str | None = None) -> logging.Logger:
    return logging.getLogger(f"farmmind.{name}" if name else "farmmind")
