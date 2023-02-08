from pydantic import BaseModel, EmailStr, SecretStr

class SignupDto(BaseModel):
    email: EmailStr
    password: SecretStr