import abc
from uuid import UUID

from src.models.users import User
from src.schemas.users import CreateBodyUserSchema


class UserCrudServiceInterface(abc.ABC):
    @abc.abstractmethod
    async def create_user(self, user: CreateBodyUserSchema) -> User | None:
        pass

    @abc.abstractmethod
    async def authenticate(self, email: str, password: str) -> User | None:
        pass


class UserTokenServiceInterface(abc.ABC):
    @abc.abstractmethod
    async def create_access_token(self, user_id: UUID, email: str) -> str:
        pass

    @abc.abstractmethod
    async def create_refresh_token(self, user_id: UUID, email: str) -> str:
        pass
