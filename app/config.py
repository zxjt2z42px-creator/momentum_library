import sys

from pydantic_settings import BaseSettings, SettingsConfigDict


def get_env_file():
    if "pytest" in sys.modules:
        return ".env.test"

    return ".env"


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=get_env_file(), env_file_encoding="utf-8"
    )


settings = Settings()
