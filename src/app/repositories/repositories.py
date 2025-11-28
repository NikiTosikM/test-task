import datetime
from uuid import UUID
from sqlalchemy import and_, func, select
from sqlalchemy.orm import joinedload

from src.app.repositories.base_repository import BaseRepository
from src.app.repositories.mappers import ContractMapper, LeadMapper, OperatorMapper, OperatorSourceMapper, SourceMapper
from src.app.models import Contract, Lead, Operator, OperatorSource, Source


class ContractRepository(BaseRepository, ContractMapper):
    model = Contract
    data_mapper = ContractMapper
    
    def get_distribution_stats(self, source_id: UUID, hours_back: int = 24) -> dict[UUID, float]:
        """
        Получаем историю контрактов по операторам
        за период времени
        
        Args:
            hours_back: период в часах (по умолчанию 24 часа)
        
        """
        # Вычисляем временную границу
        time_threshold = datetime.utcnow() - datetime.timedelta(hours=hours_back)
        
        # Запрос для получения количества контрактов по операторам
        query = (
            select(
                self.model.operator_id,
                func.count(Contract.id).label('contract_count')
            )
        ).filter(
            and_(
                Contract.source_id == source_id,
                Contract.created_at >= time_threshold
            )
        ).group_by(Contract.operator_id)
        
        result = self._session.execute(query)
        rows = result.all()
        
        if not rows:
            return {}
        
        # Вычисляем общее количество контрактов
        total_contracts = sum(row.contract_count for row in rows)
        
        if total_contracts == 0:
            return {}
        
        # Вычисляем доли в процентах для каждого оператора
        distribution = {}
        for row in rows:
            percentage = (row.contract_count / total_contracts) * 100
            distribution[row.operator_id] = round(percentage, 2)
        
        return distribution
    
    
class LeadRepository(BaseRepository, LeadMapper):
    model = Lead
    data_mapper = LeadMapper
    
    
class SourceRepository(BaseRepository, SourceMapper):
    model = Source
    data_mapper = SourceMapper
    
    
class OperatorRepository(BaseRepository, OperatorMapper):
    model = Operator
    data_mapper = OperatorMapper
    
    
class OperatorSourceRepository(BaseRepository, OperatorSourceMapper):
    model = OperatorSource
    data_mapper = OperatorSourceMapper
    
    def get_operators_for_source(self, source_id: UUID) -> list[OperatorSource]:
        """
        Получить всех операторов для источника с их весами
        """
        
        query = (
            select(self.model)
            .options(joinedload(OperatorSource.operator))
            .filter(OperatorSource.source_id == source_id)
        )
        
        result = self._session.execute(query)
        
        return result.scalars().all()
    
    
    