from uuid import UUID

from src.app.service.base_service import BaseService
from src.app.repositories.repositories import SourceRepository
from src.app.repositories.repositories import OperatorSourceRepository


from src.app.schemas.source import SourceSchema
from src.app.schemas.operator import OperatorWeightSchema
from src.app.schemas.operator_source import OperatorSourceSchema


class SourceService(BaseService[SourceRepository]):
    repository_class = SourceRepository
    
    def create_source(self, data: SourceSchema) -> UUID:
        ''' Создать оператора '''
        source_id: UUID = self._repository.add(data)
        
        return source_id
        
    def bind_operator_to_source(self, source_id: UUID, operators: list[OperatorWeightSchema]):
        ''' Привязать оператора к источнику и назначить ему вес '''
        
        operator_source_service = OperatorSourceRepository(self._repository._session)
        
        operator_source_datas = [
            OperatorSourceSchema(
                source_id=source_id,
                operator_id=operator.lead_id,
                weight=operator.weight
            ) for operator in operators
        ]
        operator_source_service.add_bulk(operator_source_datas)
        
        