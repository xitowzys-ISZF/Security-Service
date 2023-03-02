from fastapi import APIRouter

from . import applications, signin, signup, verify_jwt, access_verification
router = APIRouter()
router.include_router(
    applications.router,
    prefix='/applications',
    tags=['applications'],
)
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
    verify_jwt.router,
    prefix='/verify-jwt',
    tags=['Authentication'],
)
router.include_router(
    access_verification.router,
    prefix='/access-verification',
    tags=['Base']
)