from sqlalchemy import UUID, Boolean, DateTime, String
from sqlalchemy.orm import mapped_column

from src.database import Base


class User(Base):
    """Модель пользователя"""

    __tablename__ = "d_user"

    id = mapped_column(UUID, primary_key=True, comment="Идентификатор пользователя")
    full_name = mapped_column(String, comment="ФИО")
    email = mapped_column(String, comment="Email")
    password = mapped_column(String, comment="Пароль")
    is_active = mapped_column(Boolean, comment="Активен")
    date_created = mapped_column(
        DateTime, comment="Дата и время добавления записи в таблицу (техн.)"
    )
    date_updated = mapped_column(
        DateTime, comment="Дата и время обновления записи в таблицу (техн.)"
    )
