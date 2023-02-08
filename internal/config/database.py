from sqlalchemy import create_engine, orm

from internal.config.settings import settings
from sqlalchemy.orm import scoped_session

class Errors:
    @staticmethod
    def any_error(msg: str) -> dict[str, int | str]:
        return {
            "code": -1,
            "msg": msg
        }

    @staticmethod
    def no_user_found() -> dict[str, int | str]:
        return {
            "code": 1,
            "msg": f"Email or password is incorrect"
        }

    @staticmethod
    def password_incorrect() -> dict[str, int | str]:
        return {
            "code": 2,
            "msg": f"Email or password is incorrect"
        }

def sync_session(url: str):
    engine = create_engine(url)

    Session = orm.sessionmaker()
    Session.configure(bind=engine)
    return scoped_session(Session)


current_session = sync_session(settings.DATABASE_URI)
