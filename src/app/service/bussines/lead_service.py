from uuid import UUID

from src.app.schemas.lead import LeadsContractSchema
from src.app.repositories.repositories import LeadRepository
from src.app.schemas import LeadSchema
from src.app.service.base_service import BaseService
from src.app.models import Lead


class LeadService(BaseService[LeadRepository]):
    repository_class = LeadRepository

    def create_lead(self, data: LeadSchema) -> UUID:
        lead_id: UUID = self._repository.add(data)
        
        return lead_id

    def search_lead(self, email: str) -> Lead | None:
        """Поиск оператора по email"""

        lead: Lead | None = self._repository.get_object(email=email)

        return lead

    def get_or_create_lead(self, email: str) -> Lead:
        lead: Lead | None = self.search_lead(email)

        if not lead:
            data_lead = LeadSchema(email=email)
            created_lead = self._repository.add(data=data_lead)
            
            return created_lead

        return lead

    def get_contracts(self, lead_id: UUID) -> list[LeadsContractSchema]:
        contracts = self._repository.load_contracts(lead_id)

        return contracts
