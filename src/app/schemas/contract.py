from uuid import UUID

from pydantic import BaseModel, Field, EmailStr



class ContractSchema(BaseModel):
    ''' Схема обращения/контракта '''
    
    lead_id: EmailStr = Field(100)
    source_id: UUID = Field(100)
    
    
class CreateContractSchema(BaseModel):
    ''' Схема для создания контракта '''
    
    lead_id: UUID
    source_id: UUID
    operator_id: UUID