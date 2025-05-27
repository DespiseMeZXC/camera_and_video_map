from collections.abc import AsyncGenerator
from typing import Any

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, declared_attr, sessionmaker

from src.config import settings


class Base(DeclarativeBase):
    """Базовый класс для всех моделей."""

    metadata = MetaData(naming_convention=settings.db.naming_convention)

    @declared_attr
    @classmethod
    def __tablename__(cls) -> str:
        """Получить имя таблицы."""
        return cls.__name__.lower()


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
