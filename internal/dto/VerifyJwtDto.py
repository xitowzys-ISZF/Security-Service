from pydantic import BaseModel, EmailStr, SecretStr


class VerifyJwtDto(BaseModel):
    jwt: str