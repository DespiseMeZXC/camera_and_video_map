from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class CameraSchema(BaseModel):
    """Схема камеры."""

    id: UUID
    camera_id: int
    camera_class_cd: int
    camera_class: str
    model: str
    camera_name: str
    camera_place: str
    camera_place_cd: int
    serial_number: str
    camera_type_cd: int
    camera_type: str
    camera_latitude: float
    camera_longitude: float
    archive: int
    azimuth: int
    date_created: datetime

    model_config = {"from_attributes": True}
