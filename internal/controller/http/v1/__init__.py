from fastapi import APIRouter

from . import signin, signup, access_verification
router = APIRouter()
router.include_router(
    signin.router,
    prefix='/signin',
    tags=['Authentication'],
)
router.include_router(
    signup.router,
    prefix='/signup',
    tags=['Authentication'],
)
router.include_router(
    access_verification.router,
    prefix='/access-verification',
    tags=['Base']
)