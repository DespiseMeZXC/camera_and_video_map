import abc

from src.models.camera import Camera


class CamerasCrudServiceInterface(abc.ABC):
    @abc.abstractmethod
    async def get_cameras(self) -> list[Camera] | None:
        pass
