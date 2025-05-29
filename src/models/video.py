import uuid
from datetime import datetime
from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Integer, String

from src.db_base import Base

if TYPE_CHECKING:
    from src.models.camera import Camera
    from src.models.users import User


class Video(Base):
    """Модель видео."""

    __tablename__ = "video"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), comment="Идентификатор", primary_key=True, default=uuid4
    )
    name: Mapped[str] = mapped_column(String, comment="Название видео")
    duration: Mapped[int] = mapped_column(Integer, comment="Длительность")
    video_resolution: Mapped[str] = mapped_column(String, comment="Разрешение видео")
    fps: Mapped[int] = mapped_column(Integer, comment="Количество кадров в секунду")
    time_of_day: Mapped[str] = mapped_column(String, comment="Время суток")
    tracing: Mapped[bool] = mapped_column(Boolean, comment="Готовность рассчета")
    author_name: Mapped[str] = mapped_column(String, comment="Автор")
    counter: Mapped[int] = mapped_column(Integer, comment="Кол-во расчётов")
    date_created: Mapped[datetime] = mapped_column(
        DateTime, comment="Дата создания", default=datetime.now
    )
    camera_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("d_camera.id"), comment="Идентификатор камеры"
    )
    data_updated: Mapped[datetime] = mapped_column(
        DateTime, comment="Дата обновления", default=datetime.now
    )
    author_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("user.id"), comment="Идентификатор автора"
    )
    # Relationships
    author: Mapped["User"] = relationship("User", back_populates="videos")
    camera: Mapped["Camera"] = relationship("Camera", back_populates="videos")
