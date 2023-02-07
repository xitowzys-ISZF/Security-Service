from internal.entity.Base import Base
from sqlalchemy import Column, INTEGER, TEXT, VARCHAR


class PermissionsSubject(Base):
    __tablename__: str = "permissions_subject"

    id: Column = Column(INTEGER, primary_key=True, autoincrement=True)
    name: Column = Column(VARCHAR(length=255))