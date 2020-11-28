from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    APP_NAME = 'My App'
    REGISTRATION_TOKEN_LIFETIME = 60 * 60
    TOKEN_ALGORITHM = 'HS256'
    SMTP_SERVER: str
    MAIL_SENDER = 'noreply@example.com'
    API_PREFIX = '/api'
    MODELS = [
        'models.users',
    ]

    class Config:
        case_sensitive: bool = True


@lru_cache()
def get_settings():
    return Settings()
