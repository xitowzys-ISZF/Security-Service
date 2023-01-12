from fastapi import FastAPI

def create_app() -> FastAPI:
    app: FastAPI = FastAPI()

    return app