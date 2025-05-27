from src.crud.cameras import CamerasCrudService
from src.interfaces.cameras import CamerasCrudServiceInterface


def get_cameras_crud() -> CamerasCrudServiceInterface:
    return CamerasCrudService()
