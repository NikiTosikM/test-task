from uuid import UUID

from fastapi import APIRouter, status
from fastapi.responses import ORJSONResponse

from src.app.api.dependencies import GetSessionDep
from src.app.schemas.source import SourceSchema
from src.app.schemas.operator import OperatorWeightSchema
from src.app.service.bussines.source_service import SourceService


router = APIRouter(
    prefix="/source", tags=["Источник"], default_response_class=ORJSONResponse
)


@router.post(
    path="/", summary="Создание источника", status_code=status.HTTP_201_CREATED
)
def create_source(source_data: SourceSchema, session: GetSessionDep):
    source_repository = SourceService(session)

    source_repository.create_source(data=source_data)

    return {"status": "ok"}


@router.post(
    path="/bind/{source_id}",
    summary="Привязывает оператора и его вес к источнику",
    status_code=status.HTTP_201_CREATED,
)
def bind_source(
    source_id: str,
    name_and_weight_operators: list[OperatorWeightSchema],
    session: GetSessionDep,
):
    source_repository = SourceService(session)

    source_repository.bind_operator_to_source(
        source_id=UUID(source_id), operators=name_and_weight_operators
    )

    return {"status": "ok"}
