from sqlalchemy import UUID, DateTime, Float, Integer, String
from sqlalchemy.orm import mapped_column

from src.database import Base


class Camera(Base):
    """Модель камер"""

    __tablename__ = "d_camera"

    id = mapped_column(UUID, primary_key=True, comment="Идентификатор камеры")
    camera_id = mapped_column(String, comment="Номер камеры")
    camera_class_cd = mapped_column(Integer, comment="Идентификатор класса камеры")
    camera_class = mapped_column(String, comment="Класс камеры")
    model = mapped_column(String, comment="Модель")
    camera_name = mapped_column(String, comment="Название камеры")
    camera_place = mapped_column(String, comment="Адрес")
    camera_place_cd = mapped_column(Integer, comment="Идентификатор адреса")
    serial_number = mapped_column(String, comment="Серийный номер")
    camera_type_cd = mapped_column(Integer, comment="Идентификатор типа камеры")
    camera_type = mapped_column(String, comment="Тип камеры")
    camera_latitude = mapped_column(Float, comment="Широта")
    camera_longitude = mapped_column(Float, comment="Долгота")
    archive = mapped_column(Integer, comment="Признак архивной записи")
    azimuth = mapped_column(Integer, comment="Азимут")
    process_dttm = mapped_column(
        DateTime, comment="Дата и время добавления записи в таблицу (техн.)"
    )
