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

    @staticmethod
    def access_token_invalid() -> dict[str, int | str]:
        return {
            "code": 3,
            "msg": f"Invalid or expired AccessToken"
        }

    @staticmethod
    def access_restricted() -> dict[str, int | str]:
        return {
            "code": 4,
            "msg": f"Access to the requested resource is restricted"
        }

    @staticmethod
    def record_not_found() -> dict[str, int | str]:
        return {
            "code": 5,
            "msg": f"The requested record was not found"
        }
