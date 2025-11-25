from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.db import DBBaseModel


class Lead(DBBaseModel):
    """
    Модель лида(клиента):
        name - имя клиента
        email - идентификатором, по которому определяем пользователя
    """

    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(200))
