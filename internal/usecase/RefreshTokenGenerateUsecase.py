import jwt
import time
from internal.config.settings import settings


class RefreshTokenGenerateUsecase:
    @staticmethod
    def execute(user_id: int):
        payload = {
            "user_id": user_id,
            "exp": time.time() + 604800
        }

        return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
