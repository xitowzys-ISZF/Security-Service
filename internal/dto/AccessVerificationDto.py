from typing import Optional

from pydantic import BaseModel, EmailStr, SecretStr


class AccessVerificationDto(BaseModel):
    access_token: str
    microservice_name: str
    action_url: str
    method: Optional[str]