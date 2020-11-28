from jose import jwt
from datetime import datetime, timedelta
from config.settings import Settings
from pydantic import UUID4

settings = Settings()


class Auth:
    @staticmethod
    def create_token(data: dict, expires_delta: int):
        pass
        to_encode = data.copy()
        to_encode.update({
            "exp": datetime.utcnow() + timedelta(seconds=expires_delta)
        })
        return jwt.encode(
            to_encode,
            settings.SECRET_KEY,
            algorithm=settings.TOKEN_ALGORITHM
        )

    @staticmethod
    def create_confirmation_token(user_id: UUID4):
        return Auth.create_token(
            {"sub": user_id},
            settings.REGISTRATION_TOKEN_LIFETIME
        )
