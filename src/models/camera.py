from sqlalchemy import UUID, DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Camera(Base):
    """Модель камер"""

    __tablename__ = "d_camera"

    id: Mapped[UUID] = mapped_column(
        UUID, primary_key=True, comment="Идентификатор камеры"
    )
    camera_id: Mapped[str] = mapped_column(String, comment="Номер камеры")
    camera_class_cd: Mapped[int] = mapped_column(
        Integer, comment="Идентификатор класса камеры"
    )
    camera_class: Mapped[str] = mapped_column(String, comment="Класс камеры")
    model: Mapped[str] = mapped_column(String, comment="Модель")
    camera_name: Mapped[str] = mapped_column(String, comment="Название камеры")
    camera_place: Mapped[str] = mapped_column(String, comment="Адрес")
    camera_place_cd: Mapped[int] = mapped_column(
        Integer, comment="Идентификатор адреса"
    )
    serial_number: Mapped[str] = mapped_column(String, comment="Серийный номер")
    camera_type_cd: Mapped[int] = mapped_column(
        Integer, comment="Идентификатор типа камеры"
    )
    camera_type: Mapped[str] = mapped_column(String, comment="Тип камеры")
    camera_latitude: Mapped[float] = mapped_column(Float, comment="Широта")
    camera_longitude: Mapped[float] = mapped_column(Float, comment="Долгота")
    archive: Mapped[int] = mapped_column(Integer, comment="Признак архивной записи")
    azimuth: Mapped[int] = mapped_column(Integer, comment="Азимут")
    date_created: Mapped[DateTime] = mapped_column(
        DateTime, comment="Дата и время добавления записи в таблицу (техн.)"
    )
