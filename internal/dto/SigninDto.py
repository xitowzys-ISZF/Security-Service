from pydantic import BaseModel, EmailStr, SecretStr

class SigninDto(BaseModel):
    username: str
    email: EmailStr
    password: SecretStr
