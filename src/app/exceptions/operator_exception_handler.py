from fastapi import FastAPI, Request, status
from fastapi.responses import ORJSONResponse

from src.app.exceptions.exceptions import OperatorNotFound


def operator_error_handler(app: FastAPI):
    @app.exception_handler(OperatorNotFound)
    def operator_not_found(request: Request, exc: OperatorNotFound):
        return ORJSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": "На данный момент все операторы заняты. Попробуйте позже"}
        )