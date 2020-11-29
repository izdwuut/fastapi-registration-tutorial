from jose import jwt
from datetime import datetime, timedelta
from config.settings import Settings
from pydantic import UUID4
import uuid
from passlib.context import CryptContext

settings = Settings()


class Auth:
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def get_password_hash(cls, password: str) -> str:
        return cls.password_context.hash(password)

    @staticmethod
    def create_token(data: dict, expires_delta: int):
        pass
        to_encode = data.copy()
        to_encode.update({
            "exp": datetime.utcnow() + timedelta(seconds=expires_delta),
            "iss": settings.APP_NAME,
            "aud": settings.HOST
        })
        return jwt.encode(
            to_encode,
            settings.SECRET_KEY,
            algorithm=settings.TOKEN_ALGORITHM
        )

    @staticmethod
    def create_confirmation_token(user_id: UUID4):
        claims = {
            "sub": user_id,
            "scope": "registration",
            "jti": uuid.uuid4()
        }
        return Auth.create_token(
            claims,
            settings.REGISTRATION_TOKEN_LIFETIME
        )
