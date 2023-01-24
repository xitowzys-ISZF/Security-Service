from fastapi import FastAPI

from internal.config.settings import settings
from internal.controller.http.router import api_router


def create_app() -> FastAPI:
    app: FastAPI = FastAPI()
    app.include_router(api_router, prefix=settings.API)
    return app
