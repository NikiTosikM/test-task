from uuid import UUID

from pydantic import BaseModel, Field


class OperatorSourceSchema(BaseModel):
    operator_id: UUID
    source_id: UUID
    weight: int = Field(le=100)