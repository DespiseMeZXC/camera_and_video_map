from fastapi import APIRouter, Depends, HTTPException, status

from src.dependencies.users import get_user_crud
from src.interfaces.users import UserCrudServiceInterface
from src.schemas.users import (
    AuthBodySchema,
    BaseUserSchema,
    CreateBodyUserSchema,
    TokenSchema,
)

router = APIRouter(prefix="/users", tags=["user"])


@router.post("/auth", response_model=TokenSchema)
async def auth(
    user: AuthBodySchema,
    crud: UserCrudServiceInterface = Depends(get_user_crud),  # noqa: B008
):
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
    crud: UserCrudServiceInterface = Depends(get_user_crud),  # noqa: B008
):
    db_user = await crud.create_user(user)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists",
        )
    return BaseUserSchema.model_validate(db_user)
