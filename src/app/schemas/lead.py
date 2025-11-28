from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr

from src.app.schemas.contract import ContratInfoSchema


class LeadSchema(BaseModel):
    """Схема для создания клиента/лида"""

    email: EmailStr


class LeadDBResponceSchema(BaseModel):
    """Схема хранит данные от бд о клиенте"""

    id: UUID
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


class LeadsContractSchema(BaseModel):
    """
    Схема хранит id источника, оператора И клиента.
    Используется когда клиент хочет получить информацию по его контрактам
    """
    lead_id: UUID
    contracts: list[ContratInfoSchema]
    
