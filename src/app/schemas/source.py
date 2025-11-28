from pydantic import BaseModel, Field

from src.app.schemas.operator import OperatorWeightSchema


class SourceSchema(BaseModel):
    """Cхема источника"""

    name: str = Field(max_length=100)


class SourceBind(BaseModel):
    ''' Схема хранит имена операторов и их вес '''
    
    operators:  list[OperatorWeightSchema ]