import abc
from collections.abc import AsyncGenerator
from typing import Any
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from src.models.users import User
from src.schemas.users import CreateBodyUserSchema


class DatabaseInterface(abc.ABC):
    @abc.abstractmethod
    async def get_async_session(self) -> AsyncGenerator[AsyncSession, Any]:
        pass


class UserCrudServiceInterface(abc.ABC):
    @abc.abstractmethod
    async def create_user(self, user: CreateBodyUserSchema) -> User | None:
        pass

    @abc.abstractmethod
    async def authenticate(self, email: str, password: str) -> User | None:
        pass

    @abc.abstractmethod
    async def refresh_token(self, refresh_token: str) -> User | None:
        pass


class UserTokenServiceInterface(abc.ABC):
    @abc.abstractmethod
    async def create_access_token(self, user_id: UUID, email: str) -> str:
        pass

    @abc.abstractmethod
    async def create_refresh_token(self, user_id: UUID, email: str) -> str:
        pass
