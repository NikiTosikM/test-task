# ruff: noqa: F821
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import ForeignKey

from src.core.db import DBBaseModel


class Contract(DBBaseModel):
    lead_id: Mapped[UUID] = mapped_column(ForeignKey("leads.id"))
    source_id: Mapped[UUID] = mapped_column(ForeignKey("sources.id"))
    operator_id: Mapped[UUID] = mapped_column(ForeignKey("operators.id"))

    source: Mapped["Source"] = relationship(back_populates="contracts")
    operator: Mapped["Operator"] = relationship(back_populates="contracts")
    lead: Mapped["Lead"] = relationship(back_populates="contracts")