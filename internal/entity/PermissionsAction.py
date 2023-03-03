from sqlalchemy.dialects.mssql import TINYINT

from internal.entity.Base import Base
from sqlalchemy import Column, INTEGER, TEXT, VARCHAR, ForeignKey, Boolean, text
from sqlalchemy.orm import relationship


class PermissionsAction(Base):
    __tablename__: str = "permissions_action"

    id: Column = Column(INTEGER, primary_key=True, autoincrement=True)
    action_url: Column = Column(VARCHAR(length=255))
    method: Column = Column(VARCHAR(length=255))
    subject_id: Column = Column(INTEGER, ForeignKey("permissions_subject.id"))
    has_permission: Column = Column(Boolean, default=True, nullable=False, server_default=text("1"))


    permissions_subject = relationship("PermissionsSubject", backref="permission_action")

    roles = relationship(
        "Roles",
        secondary="roles_permissions_action",
        back_populates="permissions_actions"
    )
