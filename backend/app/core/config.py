from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


# Project root: insuremind-ai/
PROJECT_ROOT = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    app_name: str = "InsureMind AI"
    app_version: str = "0.1.0"
    app_env: str = "development"
    debug: bool = True
    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
