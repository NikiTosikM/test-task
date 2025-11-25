from enum import Enum

from sqlalchemy.orm import Mapped, mapped_column, relationship, validates
from sqlalchemy.dialects.postgresql import ENUM

from src.core.db import DBBaseModel
from src.app.models import OperatorSource, Contract


class OperatorActive(Enum):
    NOT_ACTIVE = "not_active"
    ACTIVE = "active"


class Operator(DBBaseModel):
    is_active: Mapped[bool] = mapped_column(ENUM(OperatorActive))
    max_load: Mapped[int]
    sources: Mapped[list["OperatorSource"]] = relationship(back_populates="operator")
    contracts: Mapped[list["Contract"]] = relationship(back_populates="operator")

    @validates("max_load")
    def validate_max_load(self, key, value):
        if value < 1:
            raise ValueError("Нагрузка должена быть больше 0")
        return value
    
    @property
    def current_load(self) -> int:
        '''
        Вычисляем нагрузку на оператора
        '''
        load: int = len([contr for contr in self.contracts])
        
        return load
    
    @property
    def accept_contract(self):
        return self.is_active and self.current_load < self.max_load