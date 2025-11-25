from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.models.operator import Operator
from src.app.models.source import Source
from src.core.db import DBBaseModel


class OperatorSource(DBBaseModel):
    operator_id: Mapped[int] = mapped_column(ForeignKey("operator.id"))
    source_id: Mapped[int] = mapped_column(ForeignKey("source.id"))
    weight: Mapped[int]

    source: Mapped["Source"] = relationship(
        back_populates="operators"
    )
    operator: Mapped["Operator"] = relationship(
        back_populates="sources"
    )
