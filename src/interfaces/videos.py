from abc import ABC, abstractmethod

from src.models.video import Video


class VideosCrudServiceInterface(ABC):
    @abstractmethod
    async def get_videos(self) -> list[Video]:
        pass

    @abstractmethod
    async def create_video(self, video) -> Video:
        pass
