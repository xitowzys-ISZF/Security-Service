from fastapi import APIRouter, Depends, status

from internal.dto.SigninDto import SigninDto
from internal.dto.application import BaseApplication
from internal.service.SigninService import SigninService
from internal.usecase.utils import SucessfulResponse as Response

router = APIRouter()
responses = Response.schema(status.HTTP_201_CREATED)


@router.post(
    path='/',
    responses=responses,
    status_code=status.HTTP_201_CREATED,
    summary="Registration of users"
)
async def signin(
        dto: SigninDto,
        signin_service: SigninService = Depends()
) -> Response:
    return await signin_service.registration(dto)
