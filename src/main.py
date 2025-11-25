import sys
from pathlib import Path

from fastapi import FastAPI
import uvicorn




sys.path.append(str(Path(__file__).parent))

app = FastAPI

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="localhost", port=8000)