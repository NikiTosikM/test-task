from typing import TypeVar, Generic, TYPE_CHECKING
from uuid import UUID

from sqlalchemy.orm import Session
from sqlalchemy import select, insert, Result, update, delete
from pydantic import BaseModel

from src.core.db import DBBaseModel


if TYPE_CHECKING:
    from src.app.repositories.mappers.base_datamapper import BaseDataMapper
    

Model = TypeVar("Model", bound=DBBaseModel)
Schema = TypeVar("Schema", bound=BaseModel)
DataMapper = TypeVar("DataMapper", bound="BaseDataMapper")


class BaseRepository(Generic[Model, DataMapper]):
    model: type[Model]
    data_mapper: type[DataMapper]

    def __init__(self, db_session: Session):
        self._session: Session = db_session

    def add(self, data: Schema) -> Model:
        """Добавить запись"""

        serialized_data: dict = self.data_mapper.map_to_persistence_entity(
            data
        )  # преобразовали схему в словарь

        stmt = insert(self.model).values(**serialized_data).returning(self.model)

        result = self._session.execute(stmt)
        
        return result.scalar_one()
        
    def add_bulk(self, datas: list[Schema]):
        ''' Добавить несколько записей сразу '''
        
        serialized_datas: list[dict] = [
            self.data_mapper.map_to_persistence_entity(data) for data in datas 
        ]
        
        stmt = insert(self.model).values(serialized_datas)
        
        self._session.execute(stmt)
        

    def get_filtered(self, **filters) -> list[Schema]:
        """Поиск записей по фильтру"""

        query = select(self.model).filter_by(**filters)
        result: Result = self._session.execute(query)
        models: list[Model] = result.scalars().all()

        return [self.data_mapper.map_to_domain_entity(model) for model in models]
    
    def get_object(self, **filters) -> Schema | None:
        ''' Поиск записи по фильтру '''
        
        query = select(self.model).filter_by(**filters)
        result: Result = self._session.execute(query)
        model: Model = result.scalar_one_or_none()
        
        if not model:
            return None
        
        return self.data_mapper.map_to_domain_entity(model)

    def get_all(self) -> list[Schema]:
        """Получить все записи"""

        return self.get_filtered()

    def update(self, data: Schema, exclude_unset: bool = False, **filters) -> None:
        """Обновить запись"""

        serialized_data: dict = self.data_mapper.map_to_persistence_entity(
            data=data, exclude_unset=exclude_unset
        )

        stmt = update(self.model).filter_by(**filters).values(**serialized_data)

        self._session.execute(stmt)

    def delete(self, **filters) -> None:
        """Удалить запись"""

        stmt = delete(self.model).filter_by(**filters)

        self._session.execute(stmt)
