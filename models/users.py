from tortoise import fields, models
import pydantic
from tortoise.contrib.pydantic import pydantic_model_creator


class UserModel(models.Model):
    id = fields.UUIDField(pk=True)
    email = fields.CharField(null=False, max_length=255)
    hashed_password = fields.CharField(null=True, max_length=255)
    is_active = fields.BooleanField(null=False, default=False)
    confirmation = fields.UUIDField(null=True)

    class Meta:
        table: str = 'users'


class CreateUser(pydantic.BaseModel):
    email: pydantic.EmailStr
    password: pydantic.SecretStr


User_Pydantic = pydantic_model_creator(
    UserModel,
    name='User',
    exclude=('hashed_password', 'confirmation')
)


