# ruff: noqa: F821

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.db import DBBaseModel


class Lead(DBBaseModel):
    """
    Модель лида(клиента):
        email - идентификатором, по которому определяем пользователя
    """
    email: Mapped[str] = mapped_column(String(200))
    
    contracts: Mapped[list["Contract"]] = relationship(back_populates="lead")
