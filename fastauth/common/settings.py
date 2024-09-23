from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    AES_KEY: bytes
    ALGORITHM: str
    SECRET_KEY: str
    EMAIL: str
    PRODUCTION: bool
    DEBUG: bool

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


SETTINGS = Settings()
