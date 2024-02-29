from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    """
    Class for storing app settings.
    """

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)

    SECRET_KEY: str

    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    DEBUG: bool = True

    ALLOWED_HOSTS: str = "127.0.0.1"
    ALLOWED_ORIGINS: str = "http://localhost:8000"


settings = Settings()
