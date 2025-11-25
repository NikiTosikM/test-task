from src.repositories.base_repository import BaseRepository
from src.repositories.mappers import ContractMapper, LeadMapper, OperatorMapper, OperatorSourceMapper, SourceMapper
from src.app.models import Contract, Lead, Operator, OperatorSource, Source


class ContractRepository(BaseRepository[Contract, ContractMapper]):
    model: type[Contract]
    mapper: type[ContractMapper]
    
    
class LeadRepository(BaseRepository[Lead, LeadMapper]):
    model: type[Lead]
    mapper: type[LeadMapper]
    
    
class SourceRepository(BaseRepository[Source, SourceMapper]):
    model: type[Source]
    mapper: type[SourceMapper]
    
    
class OperatorRepository(BaseRepository[Operator, OperatorMapper]):
    model: type[Operator]
    mapper: type[OperatorMapper]
    
    
class OperatorSourceRepository(BaseRepository[OperatorSource, OperatorSourceMapper]):
    model: type[Operator]
    mapper: type[OperatorMapper]