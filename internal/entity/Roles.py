from sqlalchemy import Column, INTEGER, TEXT

from internal.entity.Base import Base


class Roles(Base):
    __tablename__: str = "roles"

    id: Column = Column(INTEGER, primary_key=True, autoincrement=True)
    name: Column = Column(TEXT, nullable=False, unique=True)