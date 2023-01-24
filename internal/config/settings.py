from typing import Any, Dict, List
from .envirous import env

from pydantic import (
    AmqpDsn,
    AnyHttpUrl,
    BaseSettings,
    PostgresDsn,
    validator,
)


class Settings(BaseSettings):
    API: str = '/api'
    RPC: str = '/rpc'
    DOCS: str = '/docs'
    ADMIN: str = '/admin'
    STARTUP: str = 'startup'
    SHUTDOWN: str = 'shutdown'
    # SECRET_KEY: str
    FLASK_ADMIN_SWATCH: str = 'cerulean'

    NAME: str = 'FastAPI Clean API'
    VERSION: str = '1.0'
    DESCRIPTION: str = 'FastAPI Clean REST API'

    SWAGGER_UI_PARAMETERS: Dict[str, Any] = {
        'displayRequestDuration': True,
        'filter': True,
    }

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator('BACKEND_CORS_ORIGINS', pre=True)
    def assemble_cors_origins(
            cls, value: str | List[str],  # noqa: N805, WPS110
    ) -> str | List[str]:
        if isinstance(value, str) and not value.startswith('['):
            return [i.strip() for i in value.split(',')]
        elif isinstance(value, (list, str)):
            return value

        raise ValueError(value)

    DB_HOST: str = env.str("DB_HOST", "127.0.0.1")
    DB_PORT: str = env.str("DB_PORT", "3306")
    DB_USER: str = env.str("DB_USER")
    DB_PASSWORD: str = env.str("DB_PASS")
    DB_NAME: str = env.str("DB_NAME")
    DATABASE_URI: str = f'mariadb+mariadbconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    # @validator('DATABASE_URI', pre=True)
    # def assemble_db_connection(
    #         cls, value: str | None, values: Dict[str, Any],  # noqa: N805, WPS110
    # ) -> str:
    #     if isinstance(value, str):
    #         return value
    #
    #     return PostgresDsn.build(
    #         scheme='postgresql+asyncpg',
    #         user=values.get('DB_USER'),
    #         password=values.get('DB_PASSWORD'),
    #         host=values.get('DB_HOST'),
    #         port=values.get('DB_PORT'),
    #         path='/{0}'.format(values.get('DB_NAME')),
    #     )

    class Config(object):
        case_sensitive = True


settings = Settings()
