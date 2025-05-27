from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base, declared_attr

from src.config import settings


class CustomBase:
    """Базовый класс для всех моделей."""

    metadata = MetaData(naming_convention=settings.db.naming_convention)

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


Base = declarative_base(cls=CustomBase)
