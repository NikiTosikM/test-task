from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.core.config import settings


class DBCore:
    _async_engine = create_engine(
        url=settings.db.get_db_url,
        echo=settings.db.echo
    )
    _db_sessionmaker: sessionmaker = sessionmaker(
        autoflush=False,
        bind=_async_engine
    )
    
    @classmethod
    @contextmanager
    def get_session(cls) -> Generator[Session, None, None]:
        try:
            session: Session = cls._db_sessionmaker()
            
            yield session
            
            session.commit()
        except Exception as error:
            session.rollback()
            raise error
        finally:
            session.close()