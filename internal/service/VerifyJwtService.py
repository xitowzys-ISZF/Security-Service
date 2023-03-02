import jwt
import time
from internal.config.settings import settings
from internal.config.database import current_session
from internal.dto.VerifyJwtDto import VerifyJwtDto


class VerifyJwtService:
    def __init__(self) -> None:
        self.session = current_session

    async def verify(self, dto: VerifyJwtDto):
        try:
            decode_token = jwt.decode(dto.jwt, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
            if decode_token['exp'] >= time.time():
                return True, None
            else:
                return False, None
        except:
            return False, None
