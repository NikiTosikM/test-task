from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


from src.core.db import DBBaseModel


class OperatorSource(DBBaseModel):
    operator_id: Mapped[int] = mapped_column(ForeignKey("operators.id"))
    source_id: Mapped[int] = mapped_column(ForeignKey("sources.id"))
    weight: Mapped[int]

    source: Mapped["Source"] = relationship( # noqa: F821
        back_populates="operators"
    ) # noqa: F821
    operator: Mapped["Operator"] = relationship( # noqa: F821
        back_populates="sources"
    ) 
