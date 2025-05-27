from fastapi import APIRouter, Depends

from src.dependencies.users import get_user_crud
from src.interfaces.users import UserCrudServiceInterface
from src.schemas.users import BaseUserSchema, CreateBodyUserSchema

router = APIRouter(prefix="/users", tags=["user"])


@router.post("/auth")
def auth():
    pass


@router.post("/register", response_model=BaseUserSchema)
async def register(
    user: CreateBodyUserSchema,
    crud: UserCrudServiceInterface = Depends(get_user_crud),  # noqa: B008
):
    db_user = await crud.create_user(user)
    return BaseUserSchema.model_validate(db_user)
