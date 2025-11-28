from typing import Annotated

from sqlalchemy.orm import Session
from fastapi import Depends

from src.core.db.config import DBCore




def get_db_session():
    with DBCore.get_session() as db_session:
        yield db_session
        
GetSessionDep = Annotated[Session, Depends(get_db_session)]