from fastapi import APIRouter, Depends, HTTPException, status

from src.dependencies.users import get_users_crud
from src.interfaces.users import UsersCrudServiceInterface
from src.schemas.users import (
    AuthBodySchema,
    BaseUserSchema,
    CreateBodyUserSchema,
    TokenSchema,
)

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/auth", response_model=TokenSchema)
async def auth(
    user: AuthBodySchema,
    crud: UsersCrudServiceInterface = Depends(get_users_crud),  # noqa: B008
) -> TokenSchema:
    token = await crud.authenticate(user.email, user.password)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    return token


@router.post("/register", response_model=BaseUserSchema)
async def register(
    user: CreateBodyUserSchema,
    crud: UsersCrudServiceInterface = Depends(get_users_crud),  # noqa: B008
):
    db_user = await crud.create_user(user)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists",
        )
    return BaseUserSchema.model_validate(db_user)


@router.post("/refresh", response_model=TokenSchema)
async def refresh(
    refresh_token: str,
    crud: UsersCrudServiceInterface = Depends(get_users_crud),  # noqa: B008
):
    token = await crud.refresh_token(refresh_token)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
        )
    return token
