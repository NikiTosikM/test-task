from fastapi import APIRouter, status
from fastapi.responses import ORJSONResponse

from src.app.schemas.contract import ContractSchema
from src.app.api.dependencies import GetSessionDep
from src.app.service.bussines.contract_service import ContractService


router = APIRouter(prefix="/contract", tags=["Контракт/обращение"], default_response_class=ORJSONResponse)


@router.post(
    path="/",
    summary="Создание контракта",
    status_code=status.HTTP_201_CREATED
)
def create_contract(
    session: GetSessionDep,
    data_contract: ContractSchema
):
    contract_service = ContractService(session=session)
    
    contract_service.create_contract(data=data_contract)
    
    return {"status": "ok"}