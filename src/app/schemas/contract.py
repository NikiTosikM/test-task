from uuid import UUID

from pydantic import BaseModel, Field, EmailStr



class ContractSchema(BaseModel):
    ''' Схема обращения/контракта '''
    
    email: EmailStr
    source_id: UUID
    
class CreateContractSchema(BaseModel):
    ''' Схема для создания контракта '''
    
    lead_id: UUID
    source_id: UUID
    operator_id: UUID