from jose import jwt
from datetime import datetime, timedelta
from config.settings import get_settings
from pydantic import UUID4
import uuid
from passlib.context import CryptContext

settings = get_settings()


class Auth:
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def get_password_hash(cls, password: str) -> str:
        return cls.password_context.hash(password)

    @staticmethod
    def get_token(data: dict, expires_delta: int):
        pass
        to_encode = data.copy()
        to_encode.update({
            "exp": datetime.utcnow() + timedelta(seconds=expires_delta),
            "iss": settings.APP_NAME
        })
        return jwt.encode(
            to_encode,
            settings.SECRET_KEY,
            algorithm=settings.TOKEN_ALGORITHM
        )

    @staticmethod
    def get_confirmation_token(user_id: UUID4):
        jti = uuid.uuid4()
        claims = {
            "sub": str(user_id),
            "scope": "registration",
            "jti": str(jti)
        }
        return {
            "jti": jti,
            "token": Auth.get_token(
                claims,
                settings.REGISTRATION_TOKEN_LIFETIME
            )
        }

