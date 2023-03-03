from sqlalchemy import Column, INTEGER, VARCHAR, BOOLEAN
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from internal.entity.Base import Base


class Users(Base):
    __tablename__: str = "users"

    id: Column = Column(INTEGER, primary_key=True, autoincrement=True)
    username: Column = Column(VARCHAR(length=255))
    email: Column = Column(VARCHAR(length=255))
    password: Column = Column(VARCHAR(length=255))
    refresh_token: Column = Column(VARCHAR(length=255))
    is_deactivate: Column = Column(BOOLEAN, nullable=False, default=False)
    role_id: Column = Column(INTEGER, ForeignKey("roles.id"))

    role = relationship("Roles", backref="users_list")
