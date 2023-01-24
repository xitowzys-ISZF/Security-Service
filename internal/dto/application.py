from pydantic import BaseModel, EmailStr

# from internal.usecase.pydantic import PhoneStr


class BaseApplication(BaseModel):

    email: EmailStr
    text: str


class ApplicationRead(BaseApplication):

    id: int

    class Config(object):
        orm_mode = True