from typing import TypeVar, Generic

from sqlalchemy.orm import Session

from src.app.repositories.base_repository import BaseRepository


Repository = TypeVar("Repository", bound=BaseRepository)


class BaseService(Generic[Repository]):   
    repository_class: type[Repository]
     
    def __init__(self, session: Session):
        self._repository = self.repository_class(session)