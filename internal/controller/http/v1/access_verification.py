from typing import Dict, Any

from fastapi import APIRouter, Depends, status, HTTPException

from internal.dto.AccessVerificationDto import AccessVerificationDto
from internal.dto.VerifyJwtDto import VerifyJwtDto
from internal.dto.application import BaseApplication
from internal.service.SigninService import SigninService
from internal.service.AccessVerificationService import AccessVerificationService
from internal.usecase.utils import SucessfulResponse as Response

router = APIRouter()
responses = Response.schema(status.HTTP_201_CREATED)


@router.post(
    path='/',
    responses=responses,
    status_code=status.HTTP_200_OK,
    summary="Checking access to microservice"
)
async def access_verification(
        dto: AccessVerificationDto,
        access_verification_service: AccessVerificationService = Depends()
) -> Response:
    result, err = await access_verification_service.verify_jwt_token(dto)

    if err is not None:
        raise HTTPException(status_code=404, detail=err)

    result, err = await access_verification_service.check_access(dto)

    if err is not None:
        raise HTTPException(status_code=403, detail=err)

    print(result)

    return {
        "access": result
    }
