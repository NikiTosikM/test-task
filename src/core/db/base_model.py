from datetime import UTC, datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class DBBaseModel(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(UUID(), primary_key=True, default=uuid4)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, default=lambda: datetime.now(UTC).replace(tzinfo=None)
    )

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + "s"