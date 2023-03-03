from sqlalchemy import create_engine, orm

from internal.config.settings import settings
from sqlalchemy.orm import scoped_session

def sync_session(url: str):
    engine = create_engine(url)

    Session = orm.sessionmaker()
    Session.configure(bind=engine, expire_on_commit=True)
    return scoped_session(Session)


current_session = sync_session(settings.DATABASE_URI)
