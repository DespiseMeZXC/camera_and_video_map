from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class VideosSchema(BaseModel):
    """Схема видео"""

    id: UUID
    name: str
    duration: int
    video_resolution: str
    fps: int
    time_of_day: str
    tracing: bool
    counter: int
    date_created: datetime
    data_updated: datetime
    author_name: str

    model_config = {"from_attributes": True}
