import jwt
import time
from internal.config.settings import settings


class AccessTokenGenerateUsecase:
    @staticmethod
    def execute(user_id: int):
        payload = {
            "user_id": user_id,
            "exp": time.time() + 900
        }

        return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
