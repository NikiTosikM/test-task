import sys
from pathlib import Path

from fastapi import FastAPI
import uvicorn

from src.app.api import main_router
from src.core.config import settings


sys.path.append(str(Path(__file__).parent))


app = FastAPI()

app.include_router(main_router)


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.app.host,
        port=settings.app.port,
        reload=settings.app.reload,
    )
