from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import ForeignKey

from src.core.db import DBBaseModel


class Contract(DBBaseModel):
    lead_id: Mapped[int] = mapped_column(ForeignKey("leads.id")) # noqa: F821
    source_id: Mapped[int] = mapped_column(ForeignKey("sources.id")) # noqa: F821
    operator_id: Mapped[int] = mapped_column(ForeignKey("operators.id")) # noqa: F821

    source: Mapped["Source"] = relationship(back_populates="contracts") # noqa: F821
    operator: Mapped["Operator"] = relationship(back_populates="contracts") # noqa: F821