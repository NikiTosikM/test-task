from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.db import DBBaseModel


class Lead(DBBaseModel):
    """
    Модель лида(клиента):
        email - идентификатором, по которому определяем пользователя
    """
    email: Mapped[str] = mapped_column(String(200))
