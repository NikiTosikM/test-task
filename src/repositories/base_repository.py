from typing import TypeVar, Generic

from sqlalchemy.orm import Session
from sqlalchemy import select, insert, Result, update, delete
from pydantic import BaseModel

from src.core.db import DBBaseModel
from src.repositories.mappers.base_datamapper import BaseDataMapper


Model = TypeVar("Model", bound=DBBaseModel)
DataMapper = TypeVar("DataMapper", bound=BaseDataMapper)
Schema = TypeVar("Schema", bound=BaseModel)


class BaseRepository(Generic[Model, DataMapper]):
    model: type[Model]
    data_mapper: type[BaseDataMapper]

    def __init__(self, db_session: Session):
        self._session: Session = db_session

    def add(self, data: dict) -> None:
        ''' Добавить запись '''
        
        stmt = insert(self.model).values(**data)

        self._session.execute(stmt)

    def get_filtered(self, **filters) -> list[Schema]:
        ''' Поиск записей по фильтру '''
        
        query = select(self.model).filter_by(**filters)
        result: Result = self._session.execute(query)
        models: list[Model] = result.scalars().all()

        return self.data_mapper.map_to_domain_entity(**[obj for obj in models])

    def get_all(self) -> list[Schema]:
        ''' Получить все записи '''
        
        return self.get_filtered()

    def update(self, data: dict, **filters) -> None:
        ''' Обновить запись '''
        
        stmt = update(self.model).filter_by(**filters).values(**data)

        self._session.execute(stmt)
        
    def delete(self, **filters) -> None:
        ''' Удалить запись '''
        
        stmt = delete(self.model).filter_by(**filters)
        
        self._session.execute(stmt)