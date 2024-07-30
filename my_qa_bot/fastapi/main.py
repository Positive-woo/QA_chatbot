import uvicorn
from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from apis import api_router
from cores.config import settings
from cores.logger import RichLogger, CatchExceptionMiddleware

# from databases.base import create_db_and_tables, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger = RichLogger.get_logger()
    logger.info(f"SERVER STARTING::{datetime.now()}")
    try:
        # create_db_and_tables(engine)
        yield
    finally:
        logger.info(f"::SERVER SHUTTING DOWN::{datetime.now()}")


app = FastAPI(
    lifespan=lifespan,
    title="Some FastAPI",
    version="0.0.3",
)

app.include_router(api_router)
app.add_middleware(CatchExceptionMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_credentials=settings.get("server.cors_allow_credentials", False),
    allow_methods=settings.get("server.cors_allow_methods", ["GET"]),
    allow_headers=settings.get("server.cors_allow_headers", []),
    allow_origins=settings.get("server.cors_allow_origins", []),
)


@app.get("/")
def root():
    now = datetime.now()
    return {
        "code": 200,
        "time": f"{now.strftime('%Y-%m-%d %H:%M:%S')}",
        "msg": "FASTAPI SERVICE",
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8989,
        log_config=None,
    )
