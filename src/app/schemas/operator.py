from uuid import UUID

from pydantic import BaseModel, Field

from src.app.models.operator import OperatorActive


class OperatorSchema(BaseModel):
    """Cхема для создания"""

    name: str = Field(max_length=50)
    is_active: OperatorActive
    max_load: int = Field(gt=0)


class OperatorFullUpdateSchema(BaseModel):
    """Схема для обновления активности и нагрузки"""
    
    name: str
    is_active: OperatorActive
    max_load: int = Field(gt=0)


class OperatorPartialUpdateSchema(BaseModel):
    """Схема для частичного обновления данных (только активность или нагрузка)"""

    name: str | None = None
    is_active: OperatorActive | None = None
    max_load: int | None = Field(None, gt=0)
    

class OperatorWeightSchema(BaseModel):
    id: UUID = Field(description="id оператора, с которым хотим связать")
    weight: int = Field(le=100)
