from fastapi import APIRouter

from src.app.api.operator import router as operator_router
from src.app.api.source import router as source_router


main_router = APIRouter()


main_router.include_router(operator_router)
main_router.include_router(source_router)