from uuid import UUID
from fastapi import APIRouter, status
from fastapi.responses import ORJSONResponse

from src.app.schemas import (
    OperatorSchema,
    OperatorPartialUpdateSchema,
    OperatorFullUpdateSchema,
)
from src.app.service.bussines.operator_service import OperatorService
from src.app.api.dependencies import GetSessionDep


router = APIRouter(
    prefix="/operator", tags=["Оператор"], default_response_class=ORJSONResponse
)


@router.get(
    path="/", summary="Получение всех операторов", status_code=status.HTTP_200_OK
)
def get_all_operators(session: GetSessionDep):
    operator_service = OperatorService(session=session)
    
    operators = operator_service.get_all()
    
    return operators


@router.post(
    path="/", summary="Создание оператора", status_code=status.HTTP_201_CREATED
)
def create_operator(operator_data: OperatorSchema, session: GetSessionDep):
    operator_service = OperatorService(session=session)

    operator: UUID = operator_service.create_operator(data=operator_data)

    return {"status": "ok", "operator": operator}


@router.put(
    path="/{operator_id}",
    summary="Обновление лимита нагрузки и активности оператора",
    status_code=status.HTTP_200_OK,
)
def full_update_operator(
    operator_id: str, operator_data: OperatorFullUpdateSchema, session: GetSessionDep
):
    operator_service = OperatorService(session=session)

    operator_service.update(data=operator_data, id=UUID(operator_id))

    return {"status": "ok"}


@router.patch(
    path="/{operator_id}",
    summary="Обновление лимита нагрузки и активности оператора",
    status_code=status.HTTP_200_OK,
)
def partial_update_operator(
    operator_id: str, operator_data: OperatorPartialUpdateSchema, session: GetSessionDep
):
    operator_service = OperatorService(session=session)

    operator_service.update(
        data=operator_data, exclude_unset=True, id=UUID(operator_id)
    )

    return {"status": "ok"}
