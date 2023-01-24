from typing import Any, Callable, Generic, Type, TypeVar

import sqlalchemy as sa
from fastapi import Depends, params
from sqlalchemy import orm
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from internal.entity.Base import Base
from internal.usecase.utils import get_session

Model = TypeVar('Model', bound=Base)


class Repository(Generic[Model]):

    model: Type[Model]

    def __init__(
        self, session: AsyncSession = Depends(get_session),
    ) -> None:
        self.session = session

    def create(self, **fields) -> Type[Model]:
        return self.model(**fields)

    async def find(self, *options, **fields) -> Result:
        statement = sa.select(self.model).filter_by(**fields).options(
            *(orm.joinedload(option) for option in options),
        )
        return await self.session.execute(statement)

    async def save(self, instance: Type[Model]) -> Type[Model]:
        if instance.id is None:
            self.session.add(instance)
        else:
            instance = await self.session.merge(instance)
        await self.session.commit()
        return instance


def Inject(  # noqa: N802
    model: Callable[..., Any], *, use_cache: bool = True,
) -> Any:
    class_name = '{0.__name__}{1.__name__}'.format(model, Repository)
    class_bases = (Repository,)
    class_namespace = {'model': model}
    dependency = type(class_name, class_bases, class_namespace)
    return params.Depends(dependency=dependency, use_cache=use_cache)