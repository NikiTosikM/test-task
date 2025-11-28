from uuid import UUID

from pydantic import BaseModel, Field, EmailStr



class ContractSchema(BaseModel):
    ''' Схема обращения/контракта '''
    
    email: EmailStr = Field(..., description="Указываем email клиента")
    source_id: UUID
    
class CreateContractSchema(BaseModel):
    ''' Схема для создания контракта '''
    
    lead_id: UUID
    source_id: UUID
    operator_id: UUID
    
class ContratInfoSchema(BaseModel):
    source_id: UUID
    operator_id: UUID
