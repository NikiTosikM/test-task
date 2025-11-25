from pathlib import Path
from typing import Literal

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).resolve().parent.parent.parent


class AppConfig(BaseModel):
    host: str
    port: int = 8000
    reload: bool = False


class DBConfig(BaseModel):
    db_name: str = "appeal-handler"
    echo: bool = False

    @property
    def get_db_url(self):
        return f"sqlite:///{ROOT_DIR}/{self.db_name}.sqlite3"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        env_nested_delimiter="__",
    )
    mode: Literal["PROD", "TEST", "LOCAL", "DEV"]
    app: AppConfig
    db: DBConfig


settings = Settings()
