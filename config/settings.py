from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    APP_NAME: str = 'My App'
    API_PREFIX: str = '/api'
    MODELS = [
        'models.users',
    ]

    class Config:
        case_sensitive: bool = True


@lru_cache()
def get_settings():
    return Settings()
