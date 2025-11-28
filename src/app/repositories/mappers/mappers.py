from src.app.repositories.mappers.base_datamapper import BaseDataMapper
from src.app.models import Contract, Operator, Source, OperatorSource, Lead
from src.app.schemas import ContractSchema, OperatorSchema, SourceSchema, LeadSchema


class ContractMapper(BaseDataMapper):
    model = Contract 
    schema = ContractSchema


class LeadMapper(BaseDataMapper):
    model = Lead
    schema = LeadSchema


class OperatorMapper(BaseDataMapper):
    model = Operator
    schema = OperatorSchema


class SourceMapper(BaseDataMapper):
    model = Source
    schema = SourceSchema


class OperatorSourceMapper(BaseDataMapper):
    model = OperatorSource
    schema = OperatorSchema
