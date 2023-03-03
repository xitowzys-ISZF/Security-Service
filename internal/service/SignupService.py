from typing import Tuple, Dict, Any

from sqlalchemy.exc import NoResultFound

from internal.config.Errors import Errors
from internal.config.database import current_session
from internal.config.settings import settings
from internal.dto.SignupDto import SignupDto
from internal.entity import Users
from pyargon2 import hash

from internal.usecase.AccessTokenGenerateUsecase import AccessTokenGenerateUsecase
from internal.usecase.RefreshTokenGenerateUsecase import RefreshTokenGenerateUsecase


class SignupService:

    def __init__(self) -> None:
        self.session = current_session

    async def login(self, dto: SignupDto) -> tuple[dict[Any, Any], dict[str, int | str]] | tuple[
        dict[str, str | Any], None]:
        try:
            user: Users = self.session.query(Users).filter(Users.email == dto.email).one()
        except NoResultFound:
            return {}, Errors.no_user_found()

        password_hash = hash(dto.password.get_secret_value(), salt=settings.ARGON2_SALT)

        if password_hash != user.password:
            return {}, Errors.password_incorrect()

        access_token: str = AccessTokenGenerateUsecase.execute(user_id=user.id)
        refresh_token: str = RefreshTokenGenerateUsecase.execute(user_id=user.id)

        user.refresh_token = hash(password=refresh_token, salt=settings.ARGON2_SALT)

        self.session.commit()

        return {
                "AccessToken": access_token,
                "RefreshToken": refresh_token
            }, None
