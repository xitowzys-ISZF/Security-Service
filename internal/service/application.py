from internal.config.database import current_session
from internal.dto.application import BaseApplication
from internal.entity.Roles import Roles
from internal.usecase.repository import Inject, Repository


class ApplicationService(object):

    def __init__(
        self,
    ) -> None:
        self.session = current_session
        pass

    async def create(self, dto: BaseApplication):
        # application = self.application_repository.create(**dto.dict())
        # return await self.application_repository.save(application)
        # application = self.application_repository.create(name="hello")
        # await self.application_repository.save(application)


        try:
            self.session.add(Roles(name="test"))
            self.session.commit()
        except:
            current_session.rollback()
            raise

        return {}
