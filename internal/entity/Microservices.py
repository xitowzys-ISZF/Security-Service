from sqlalchemy import Column, INTEGER, TEXT, Table, ForeignKey

from internal.entity.Base import Base

class Microservices(Base):
    __tablename__: str = "microservices"

    id: Column = Column(INTEGER, primary_key=True, autoincrement=True)
    name: Column = Column(TEXT, nullable=False, unique=True)
