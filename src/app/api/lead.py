from uuid import UUID

from fastapi import APIRouter, status
from fastapi.responses import ORJSONResponse

from src.app.api.dependencies import GetSessionDep
from src.app.service.bussines.lead_service import LeadService


router = APIRouter(
    prefix="/lead", tags=["Клиент"], default_response_class=ORJSONResponse
)


@router.get(path="/{lead_id}", summary="Получение списка всех обращение оератора", status_code=status.HTTP_200_OK)
def get_contract_for_lead(
    session: GetSessionDep,
    lead_id: str
):
    lead_service = LeadService(session=session)
    
    contracts = lead_service.get_contracts(
        UUID(lead_id)
    )
    
    return contracts

