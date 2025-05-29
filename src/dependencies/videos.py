from src.crud.videos import VideosCrudService
from src.interfaces.videos import VideosCrudServiceInterface


def get_videos_crud() -> VideosCrudServiceInterface:
    return VideosCrudService()
