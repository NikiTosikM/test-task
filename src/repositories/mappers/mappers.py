from src.repositories.mappers.base_datamapper import BaseDataMapper
from src.app.models import Contract, Operator, Source, OperatorSource, Lead


class ContractMapper(BaseDataMapper):
    model: type[Contract]
    schema: None
    

class LeadMapper(BaseDataMapper):
    model: type[Lead]
    schema: None
    
    
class OperatorMapper(BaseDataMapper):
    model: type[Operator]
    schema: None
    

class SourceMapper(BaseDataMapper):
    model: type[Source]
    schema: None
    
    
class OperatorSourceMapper(BaseDataMapper):
    model: type[OperatorSource]
    schema: None
    