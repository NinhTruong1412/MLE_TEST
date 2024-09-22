import logging
import sys
from types import FrameType
from typing import List, cast
from loguru import logger
from pydantic import AnyHttpUrl
from app.helpers import Constant as Const
import app.config as config

DATA_FILE_NAME = "test_34_dataset.parquet"
MODEL_FILE_NAME = "model.joblib"


class LoggingSettings():
    LOGGING_LEVEL: int = logging.INFO  # logging levels are type int

class Settings():
    API_V1_STR: str = "/api/v1"

    # Meta
    logging: LoggingSettings = LoggingSettings()


    PROJECT_NAME: str = "sale-prediction"

    class Config:
        case_sensitive = True

class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:  # pragma: no cover
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:  # noqa: WPS609
            frame = cast(FrameType, frame.f_back)
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level,
            record.getMessage(),
        )
    
def setup_app_logging(config: Settings) -> None:
    """Prepare custom logging for our application."""

    LOGGERS = ("uvicorn.asgi", "uvicorn.access")
    logging.getLogger().handlers = [InterceptHandler()]
    for logger_name in LOGGERS:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = [InterceptHandler(level=config.logging.LOGGING_LEVEL)]

    logger.configure(
        handlers=[{"sink": sys.stderr, "level": config.logging.LOGGING_LEVEL, "serialize": True}]
    )

settings = Settings()