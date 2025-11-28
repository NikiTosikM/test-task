import random
from uuid import UUID
from src.app.models.operator import Operator
from src.app.service.base_service import BaseService

from src.app.schemas import (
    OperatorSchema,
    OperatorPartialUpdateSchema,
    OperatorFullUpdateSchema,
)
from src.app.repositories.repositories import OperatorRepository, OperatorSourceRepository


class OperatorService(BaseService[OperatorRepository]):
    repository_class = OperatorRepository

    def create_operator(self, data: OperatorSchema) -> None:
        self._repository.add(data)

    def update(
        self,
        data: OperatorFullUpdateSchema | OperatorPartialUpdateSchema,
        exclude_unset: bool = False,
        **filters
    ):
        self._repository.update(
           data, exclude_unset, **filters
        )
        
    def _get_available_operators_for_source(self, source_id: UUID) -> list[Operator]:
        """
        Получить доступных операторов для источника
        """
        operator_source_repository = OperatorSourceRepository(self._repository._session)
        
        # Получаем операторов с их весами для данного источника
        operator_sources = operator_source_repository.get_operators_for_source(source_id)
        
        available_operators = []
        for op_source in operator_sources:
            operator = op_source.operator
            # Проверяем условия доступности
            if operator.is_active and operator.current_load < operator.max_load:
                available_operators.append(operator)
        
        return available_operators
    
    def _select_operator_by_weight(self, operators: list[Operator], source_id: UUID) -> Operator | None:
        """
        Случайный выбор оператора с учетом весов
        """
        weights = []
        valid_operators = []
        
        for operator in operators:
            weight = self._get_operator_weight(operator, source_id)
            if weight > 0:
                weights.append(weight)
                valid_operators.append(operator)
        
        if not valid_operators:
            return random.choice(operators) if operators else None
        
        # Взвешенная случайная выборка
        total_weight = sum(weights)
        if total_weight == 0:
            return random.choice(valid_operators)
        
        rand_val = random.uniform(0, total_weight)
        cumulative = 0
        
        for i, weight in enumerate(weights):
            cumulative += weight
            if rand_val <= cumulative:
                return valid_operators[i]
        
        return valid_operators[-1]
    
    def _get_operator_weight(self, operator: Operator, source_id: UUID) -> int:
        """
        Получить вес оператора для конкретного источника
        """
        for operator_source in operator.sources:
            if operator_source.source_id == source_id:
                return operator_source.weight
            
        return 0
        
    def select_available_operator(self, source_id: UUID) -> Operator | None:
        """
        выбора оператора для источника
        """
        # получаем операторов для источника
        available_operators = self._get_available_operators_for_source(source_id)
        
        if not available_operators:
            return None
        
        if len(available_operators) == 1:
            return available_operators[0]
        
        # выбираем оператора по алгоритму распределения
        return self._select_operator_by_weight(available_operators, source_id)
    
    
