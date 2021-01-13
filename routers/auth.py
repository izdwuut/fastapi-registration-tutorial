from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from services.auth import Auth
from services.mailer import Mailer
from config.settings import get_settings
from models import users
from jose import jwt

settings = get_settings()
auth_router = APIRouter()


@auth_router.post("/register")
async def register(form_data: users.CreateUser = Depends()):
    if await users.UserModel.get_or_none(email=form_data.email) is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )
    user = await users.UserModel.create(
        email=form_data.email,
        hashed_password=Auth.get_password_hash(
            form_data.password.get_secret_value()
        )
    )
    confirmation = Auth.get_confirmation_token(user.id)
    user.confirmation = confirmation["jti"]
    await user.save()
    Mailer.send_confirmation_message(confirmation["token"], form_data.email)


@auth_router.get("/verify/{token}")
async def verify(token: str):
    invalid_token_error = HTTPException(status_code=400, detail="Invalid token")
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.TOKEN_ALGORITHM)
    except jwt.JWTError:
        raise HTTPException(status_code=403, detail="Token has expired")
    if payload['scope'] != 'registration':
        raise invalid_token_error
    user = await users.UserModel.get_or_none(id=payload['sub'])
    if not user or str(user.confirmation) != payload['jti']:
        raise invalid_token_error
    if user.is_active:
        raise HTTPException(status_code=403, detail="User already activated")
    user.confirmation = None
    user.is_active = True
    await user.save()
    return await users.User_Pydantic.from_tortoise_orm(user)

