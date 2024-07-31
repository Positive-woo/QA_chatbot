import os
import sys
import logging
import warnings
from rich.logging import RichHandler
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from cores.config import settings
from cores.commons import create_folder


RICH_FORMAT = "[%(filename)s:%(lineno)s] >> %(message)s"
FILE_HANDLER_FORMAT = "[%(asctime)s]\\t%(levelname)s\\t[%(filename)s:%(funcName)s:%(lineno)s]\\t>> %(message)s"


class RichLogger:
    _logger = None

    @classmethod
    def get_logger(cls):
        if cls._logger is None:
            cls._initialize_logger()
        return cls._logger

    @classmethod
    def _initialize_logger(cls):
        cls._logger = logging.getLogger()
        cls._logger.setLevel(settings.server.log_level)
        cls._add_handlers()
        cls._redirect_warnings()

    @classmethod
    def _add_handlers(cls):
        # Rich log handler
        rich_handler = RichHandler(rich_tracebacks=True)
        rich_handler.setFormatter(logging.Formatter(RICH_FORMAT))
        cls._logger.addHandler(rich_handler)

        # File log handler
        log_dir = os.path.join(
            os.getcwd(), settings.server.volume_dir, settings.server.log_dir
        )
        create_folder(log_dir)
        file_handler = logging.handlers.TimedRotatingFileHandler(
            filename=log_dir + "/logfile.log",
            when="midnight",
            interval=1,
            encoding="utf-8",
        )
        file_handler.setFormatter(logging.Formatter(FILE_HANDLER_FORMAT))
        file_handler.suffix = "%Y%m%d"
        cls._logger.addHandler(file_handler)

    @classmethod
    def _redirect_warnings(cls):
        def send_warnings_to_logging(
            message, category, filename, lineno, file=None, line=None
        ):
            cls._logger.warning(f"{filename}:{lineno}: {category.__name__}: {message}")

        warnings.showwarning = send_warnings_to_logging
        warnings.simplefilter("default")


class CatchExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
        except Exception as e:
            request_info = f"Path: {request.url.path}, Method: {request.method}"
            exc_type = e.__class__.__name__
            logger = RichLogger.get_logger()
            logger.exception(
                f"Unhandled exception during API request\n{request_info}\{exc_type}: {str(e)}"
            )
            return JSONResponse(
                status_code=500, content={"detail": "Internal Server Error"}
            )
        return response


def handle_exception(exc_type, exc_value, exc_traceback):
    logger = RichLogger.get_logger()
    logger.exception(
        f"System-level unexpected exception\n{exc_type.__name__}: {str(exc_value)}",
        exc_info=(exc_type, exc_value, exc_traceback),
    )


sys.excepthook = handle_exception
