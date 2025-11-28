from uuid import UUID

from src.app.repositories.mappers.base_datamapper import BaseDataMapper
from src.app.models import Contract, Operator, Source, OperatorSource, Lead
from src.app.schemas import (
    ContractSchema,
    OperatorSchema,
    SourceSchema,
    LeadDBResponceSchema,
    LeadsContractSchema,
    ContratInfoSchema,
)


class ContractMapper(BaseDataMapper):
    model = Contract
    schema = ContractSchema


class LeadMapper(BaseDataMapper):
    model = Lead
    schema = LeadDBResponceSchema

    @classmethod
    def contract_conversion(cls, lead_id: UUID, contracts: list[tuple]) -> list[LeadsContractSchema]:
        contracts = [
            ContratInfoSchema(
                source_id=contract[0],  # извлекаем id источника
                operator_id=contract[1],  # извлекаем id оператора
            )
            for contract in contracts
        ]
        
        return LeadsContractSchema(
            lead_id=lead_id,
            contracts=contracts
        )


class OperatorMapper(BaseDataMapper):
    model = Operator
    schema = OperatorSchema


class SourceMapper(BaseDataMapper):
    model = Source
    schema = SourceSchema


class OperatorSourceMapper(BaseDataMapper):
    model = OperatorSource
    schema = OperatorSchema
