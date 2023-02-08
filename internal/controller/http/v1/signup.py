from fastapi import APIRouter, Depends, status, HTTPException

from internal.dto.SigninDto import SigninDto
from internal.dto.SignupDto import SignupDto
from internal.dto.application import BaseApplication
from internal.service.SignupService import SignupService
from internal.service.application import ApplicationService
from internal.usecase.utils import SucessfulResponse as Response


router = APIRouter()
responses = Response.schema(status.HTTP_201_CREATED)

@router.post(
    path='/',
    responses=responses,
    status_code=status.HTTP_201_CREATED,
    summary="Log in to the system"
)
async def signup(
    dto: SignupDto,
    signup_service: SignupService = Depends()
) -> Response:

    result, err = await signup_service.login(dto)

    if (err is not None):
        return HTTPException(status_code=404, detail=err["msg"])

    return result