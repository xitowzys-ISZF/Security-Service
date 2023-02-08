from internal.config.database import current_session
from internal.dto.SigninDto import SigninDto
from internal.config.settings import settings
from internal.entity import Users
from internal.usecase.AccessTokenGenerateUsecase import AccessTokenGenerateUsecase
from pyargon2 import hash
from internal.usecase.RefreshTokenGenerateUsecase import RefreshTokenGenerateUsecase


class SigninService:

    def __init__(self) -> None:
        self.session = current_session

    async def registration(self, dto: SigninDto):
        try:
            user: Users = Users(
                username=dto.username,
                email=dto.email,
                password=hash(password=dto.password.get_secret_value(), salt=settings.ARGON2_SALT)
            )

            self.session.add(user)
            self.session.commit()

            refresh_token: str = RefreshTokenGenerateUsecase.execute(user_id=user.id)
            user.refresh_token = hash(password=refresh_token, salt=settings.ARGON2_SALT)

            self.session.commit()

            return {
                "AccessToken": AccessTokenGenerateUsecase.execute(user_id=user.id),
                "RefreshToken": refresh_token
            }
        except:
            current_session.rollback()
            raise