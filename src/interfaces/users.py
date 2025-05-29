import abc
from collections.abc import AsyncGenerator
from typing import Any
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from src.models.users import User
from src.schemas.users import CreateBodyUserSchema, TokenSchema


class DatabaseInterface(abc.ABC):
    @abc.abstractmethod
    async def get_async_session(self) -> AsyncGenerator[AsyncSession, Any]:
        pass


class UsersCrudServiceInterface(abc.ABC):
    @abc.abstractmethod
    async def create_user(self, user: CreateBodyUserSchema) -> User | None:
        pass

    @abc.abstractmethod
    async def authenticate(self, email: str, password: str) -> TokenSchema | None:
        pass

    @abc.abstractmethod
    async def refresh_token(self, refresh_token: str) -> TokenSchema | None:
        pass


class JWTServiceInterface(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def create_access_token(user_id: UUID, email: str) -> str:
        pass

    @staticmethod
    @abc.abstractmethod
    def create_refresh_token(user_id: UUID, email: str) -> str:
        pass

    @staticmethod
    @abc.abstractmethod
    def get_current_user(token: str) -> UUID:
        pass
