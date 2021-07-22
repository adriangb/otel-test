from fastapi import FastAPI

from app.api import api
from app.config import AppConfig
from app.telemetry import configure_otel



def create_app() -> FastAPI:
    config = AppConfig()
    app = FastAPI()
    app.include_router(api)
    configure_otel(config, app)
    return app


app = create_app()
