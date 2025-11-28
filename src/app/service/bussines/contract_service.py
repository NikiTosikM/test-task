from src.app.models.lead import Lead
from src.app.service.bussines.operator_service import OperatorService
from src.app.service.bussines.lead_service import LeadService
from src.app.service.base_service import BaseService
from src.app.repositories.repositories import ContractRepository
from src.app.schemas.contract import CreateContractSchema, ContractSchema


class ContractService(BaseService[ContractRepository]):
    repository_class = ContractRepository

    def create_contract(self, data: ContractSchema):
        ''' Создаем контракт с автоматическим подбором оператора '''
        
        # ищем оператора или создаем его
        lead_service = LeadService(session=self._repository._session) 
        lead: Lead = lead_service.get_or_create_lead(email=data.email)
        
        # выбираем оператора
        operator_service = OperatorService(session=self._repository._session)
        operator = operator_service.select_available_operator(data.source_id)
        
        if not operator:
            return None
        
        # создаем контракт
        data_contract = CreateContractSchema(
            lead_id=lead.id,
            source_id=data.source_id,
            operator_id=operator.id
        )
        
        self._repository.add(data_contract)