from contextlib import contextmanager
from typing import ContextManager

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
    
    @contextmanager
    def get_session(self) -> ContextManager[Session, None]:
        try:
            session: Session = self._db_sessionmaker()
            
            yield session
            
            session.commit()
        except Exception:
            session.rollback()
        finally:
            session.close()