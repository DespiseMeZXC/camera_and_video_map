import abc

from src.models.users import User
from src.schemas.users import CreateBodyUserSchema


class UserCrudServiceInterface(abc.ABC):
    @abc.abstractmethod
    async def create_user(self, user: CreateBodyUserSchema) -> User | None:
        pass
