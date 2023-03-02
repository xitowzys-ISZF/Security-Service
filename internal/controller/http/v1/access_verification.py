from fastapi import APIRouter, Depends, status

from internal.dto.AccessVerificationDto import AccessVerificationDto
from internal.dto.application import BaseApplication
from internal.service.SigninService import SigninService
from internal.service.application import ApplicationService
from internal.usecase.utils import SucessfulResponse as Response

router = APIRouter()
responses = Response.schema(status.HTTP_201_CREATED)


@router.post(
    path='/',
    responses=responses,
    status_code=status.HTTP_201_CREATED,
    summary="Checking access to microservice"
)
async def access_verification(
        dto: AccessVerificationDto,
        signin_service: SigninService = Depends()
) -> Response:
    return False