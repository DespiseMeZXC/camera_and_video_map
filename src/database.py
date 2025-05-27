from collections.abc import AsyncGenerator
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from src.config import settings


class Base(DeclarativeBase):
    """Базовый класс для всех моделей."""


class Database:
    """Класс для работы с базой данных."""

    def __init__(self) -> None:
        """Инициализация подключения к базе данных."""
        self.engine = create_async_engine(
            settings.db.database_url,
            echo=settings.app.debug,
            future=True,
        )
        self.session = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )

    async def get_session(self) -> AsyncGenerator[AsyncSession, Any]:
        """Получить сессию для работы с базой данных."""
        async with self.session() as session:
            yield session


# Создаем экземпляр базы данных
db = Database()
