from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from config.db import DB_CONFIG
from config.settings import get_settings
import uvicorn
from routers.auth import auth_router
settings = get_settings()
app = FastAPI(title=settings.APP_NAME)

register_tortoise(
    app,
    config=DB_CONFIG,
    generate_schemas=False,
)

app.include_router(
    auth_router,
    prefix=settings.API_PREFIX + '/auth',
    tags=['Authentication'],
)

if __name__ == '__main__':
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
