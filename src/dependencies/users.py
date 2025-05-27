from src.crud.users import UserCrudService
from src.interfaces.users import UserCrudServiceInterface


def get_user_crud() -> UserCrudServiceInterface:
    return UserCrudService()
