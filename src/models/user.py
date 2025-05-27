from sqlalchemy import UUID, Boolean, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class User(Base):
    """Модель пользователя"""

    __tablename__ = "d_user"

    id: Mapped[UUID] = mapped_column(
        UUID, primary_key=True, comment="Идентификатор пользователя"
    )
    full_name: Mapped[str] = mapped_column(String, comment="ФИО")
    email: Mapped[str] = mapped_column(String, comment="Email")
    password: Mapped[str] = mapped_column(String, comment="Пароль")
    is_active: Mapped[bool] = mapped_column(Boolean, comment="Активен")
    date_created: Mapped[DateTime] = mapped_column(
        DateTime, comment="Дата и время добавления записи в таблицу (техн.)"
    )
    date_updated: Mapped[DateTime] = mapped_column(
        DateTime, comment="Дата и время обновления записи в таблицу (техн.)"
    )
