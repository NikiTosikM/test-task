from enum import Enum

from sqlalchemy.orm import Mapped, relationship, validates

from src.core.db import DBBaseModel


class OperatorActive(str, Enum):
    NOT_ACTIVE = "not active"
    ACTIVE = "active"


class Operator(DBBaseModel):
    name: Mapped[str]
    is_active: Mapped[str]
    max_load: Mapped[int]
    
    sources: Mapped[list["OperatorSource"]] = relationship(back_populates="operator") # noqa: F821
    contracts: Mapped[list["Contract"]] = relationship(back_populates="operator") # noqa: F821

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