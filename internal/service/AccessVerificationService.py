import jwt
import time

from sqlalchemy.exc import NoResultFound

from internal.config.Errors import Errors
from internal.config.settings import settings
from internal.config.database import current_session
from internal.dto.AccessVerificationDto import AccessVerificationDto
from internal.entity import Users


class AccessVerificationService:
    def __init__(self) -> None:
        self.session = current_session

    async def verify_jwt_token(self, dto: AccessVerificationDto):
        try:
            decode_token = jwt.decode(dto.access_token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])

            if decode_token['exp'] >= time.time():
                return True, None
            else:
                return False, Errors.access_token_invalid()
        except:
            return False, Errors.access_token_invalid()

    async def check_access(self, dto: AccessVerificationDto):

        self.session.begin()

        decode_token = jwt.decode(dto.access_token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])

        user = self.session.query(Users).filter_by(id=decode_token['user_id']).one()

        if dto.action_url == "all":
            for action in user.role.permissions_actions:
                if action.permissions_subject.microservice.name.lower() == dto.microservice_name.lower():
                    if action.action_url.lower() == dto.action_url.lower():
                        if action.has_permission == 1:
                            self.session.close()
                            return True, None
                        else:
                            self.session.close()
                            return False, Errors.access_restricted()

            self.session.close()
            return False, Errors.record_not_found()
        else:
            for action in user.role.permissions_actions:
                if action.permissions_subject.microservice.name.lower() == dto.microservice_name.lower():
                    if action.method.lower() == dto.method.lower():
                        if action.action_url.lower() == dto.action_url.lower():
                            if action.has_permission == 1:
                                self.session.close()
                                return True, None
                            else:
                                self.session.close()
                                return False, Errors.access_restricted()

            else:
                self.session.close()
                return False, Errors.record_not_found()

