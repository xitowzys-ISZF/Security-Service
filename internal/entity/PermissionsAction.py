from internal.entity.Base import Base
from sqlalchemy import Column, INTEGER, TEXT, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship


class PermissionsAction(Base):
    __tablename__: str = "permissions_action"

    id: Column = Column(INTEGER, primary_key=True, autoincrement=True)
    action: Column = Column(VARCHAR(length=255))
    subject_id: Column = Column(INTEGER, ForeignKey("permissions_subject.id"))

    permissions_subject = relationship("PermissionsSubject", backref="permission_action")
