from sqlalchemy import select

from src.database import Database
from src.models.camera import Camera


class CamerasCrudService:
    def __init__(self):
        self.db: Database = Database()

    async def get_cameras(self) -> list[Camera] | None:
        async for session in self.db.get_async_session():
            query = select(Camera)
            result = await session.execute(query)
            return result.scalars().all()
