from sqlalchemy import Column, INTEGER, TEXT, Table, ForeignKey
from sqlalchemy.orm import relationship

from internal.entity.Base import Base


association_table = Table(
    "roles_permissions_action",
    Base.metadata,
    Column("roles_id", ForeignKey("roles.id")),
    Column("permissions_action_id", ForeignKey("permissions_action.id")),
)


class Roles(Base):
    __tablename__: str = "roles"

    id: Column = Column(INTEGER, primary_key=True, autoincrement=True)
    name: Column = Column(TEXT, nullable=False, unique=True)

    permissions_actions = relationship(
        "PermissionsAction",
        secondary=association_table,
        back_populates="roles"
    )

    # users = relationship("Users", backref="roles_list")