from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    AES_KEY: str
    EMAIL: str
    PRODUCTION: bool
    DEBUG: bool


SETTINGS = Settings()
