from fastapi import APIRouter

from . import applications, signin, signup
router = APIRouter()
router.include_router(
    applications.router,
    prefix='/applications',
    tags=['applications'],
)
router.include_router(
    signin.router,
    prefix='/signin',
    tags=['signin'],
)
router.include_router(
    signup.router,
    prefix='/signup',
    tags=['signup'],
)