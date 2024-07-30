from fastapi import APIRouter

from .v1 import (
    some_api,
)

api_router = APIRouter()

api_router.include_router(some_api.router, prefix="/some", tags=["some"])
