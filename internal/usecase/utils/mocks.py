from internal.config.database import current_session


def get_session():
    return current_session
