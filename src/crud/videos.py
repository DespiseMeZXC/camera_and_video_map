from sqlalchemy import select

from src.database import Database
from src.interfaces.videos import VideosCrudServiceInterface
from src.models import Video


class VideosCrudService(VideosCrudServiceInterface):
    def __init__(self):
        self.db: Database = Database()

    async def get_videos(self) -> list[Video]:
        async for session in self.db.get_async_session():
            query = select(Video)
            result = await session.execute(query)
            return result.scalars().all()
        return None

    async def create_video(self, video) -> Video:
        pass
