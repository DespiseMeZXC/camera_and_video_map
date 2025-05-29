import uuid
from datetime import datetime

from sqlalchemy import UUID, Boolean, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db_base import Base
from src.models.video import Video


class User(Base):
    """Модель пользователя"""

    __tablename__ = "user"

    id: Mapped[UUID] = mapped_column(
        UUID,
        primary_key=True,
        comment="Идентификатор пользователя",
        default=uuid.uuid4,
    )
    full_name: Mapped[str] = mapped_column(String, comment="ФИО")
    email: Mapped[str] = mapped_column(String, comment="Email", unique=True)
    password: Mapped[str] = mapped_column(String, comment="Пароль")
    is_active: Mapped[bool] = mapped_column(Boolean, comment="Активен", default=True)
    date_created: Mapped[DateTime] = mapped_column(
        DateTime,
        comment="Дата и время добавления записи в таблицу (техн.)",
        default=datetime.now,
    )
    date_updated: Mapped[DateTime] = mapped_column(
        DateTime,
        comment="Дата и время обновления записи в таблицу (техн.)",
        default=datetime.now,
    )
    organization: Mapped[UUID] = mapped_column(
        UUID, comment="Идентификатор организации", nullable=True
    )
    videos: Mapped[list[Video]] = relationship(back_populates="author")
