from config.settings import get_settings

settings = get_settings()

DB_CONFIG = {
    "connections": {
        "default": settings.DATABASE_URL.split('?')[0]
    },
    "apps": {
        "models": {
            "models": settings.MODELS
        }
    }
}
