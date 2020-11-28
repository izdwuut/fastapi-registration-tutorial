from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from config.db import DB_CONFIG
from config.settings import Settings
import uvicorn

settings = Settings()
app = FastAPI(title=settings.APP_NAME)

register_tortoise(
    app,
    config=DB_CONFIG,
    generate_schemas=False,
)


if __name__ == '__main__':
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
