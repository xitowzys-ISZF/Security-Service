from fastapi import APIRouter, Depends, status, HTTPException

from internal.dto.VerifyJwtDto import VerifyJwtDto
from internal.service.VerifyJwtService import VerifyJwtService
from internal.usecase.utils import SucessfulResponse as Response


router = APIRouter()
responses = Response.schema(status.HTTP_201_CREATED)

@router.post(
    path='/',
    responses=responses,
    status_code=status.HTTP_201_CREATED,
    summary="Log in to the system"
)
async def verify_jwt(
    dto: VerifyJwtDto,
    verify_jwt_service: VerifyJwtService = Depends()
) -> Response:
    print(dto)

    result, err = await verify_jwt_service.verify(dto)

    if (err is not None):
        return HTTPException(status_code=404, detail=err["msg"])

    return result
