from src.crud.users import UsersCrudService
from src.interfaces.users import UsersCrudServiceInterface


def get_users_crud() -> UsersCrudServiceInterface:
    return UsersCrudService()
