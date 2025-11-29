import sys
from pathlib import Path

from fastapi import FastAPI
import uvicorn

sys.path.append(str(Path(__file__).parent.parent))

from src.app.api import main_router
from src.core.config import settings
from src.app.exceptions.operator_exception_handler import operator_error_handler



app = FastAPI()

app.include_router(main_router)

operator_error_handler(app)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.app.host,
        port=settings.app.port,
        reload=settings.app.reload,
    )
