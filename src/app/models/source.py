from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from src.core.db import DBBaseModel


class Source(DBBaseModel):
    name: Mapped[str] = mapped_column(String(100))
    operators: Mapped[list["OperatorSource"]] = relationship(back_populates="source")  # noqa: F821
    contracts: Mapped[list["Contract"]] = relationship(back_populates="source")  # noqa: F821