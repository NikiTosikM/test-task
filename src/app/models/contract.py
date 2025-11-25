from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import ForeignKey

from src.core.db import DBBaseModel
from src.app.models import Lead, Operator, Source


class Contract(DBBaseModel):
    lead_id: Mapped["Lead"] = mapped_column(ForeignKey("leads.id"))
    source_id: Mapped["Source"] = mapped_column(ForeignKey("source.id"))
    operator_id: Mapped["Operator"] = mapped_column(ForeignKey("operator.id"))

    source: Mapped["Source"] = relationship(back_populates="contracts")
    operator: Mapped["Operator"] = relationship(back_populates="contracts")