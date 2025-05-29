from fastapi import APIRouter, Depends, HTTPException

from src.dependencies.cameras import get_cameras_crud
from src.interfaces.cameras import CamerasCrudServiceInterface
from src.schemas.cameras import CameraSchema
from src.utils.jwt import JWTService

router = APIRouter(prefix="/cameras", tags=["cameras"])


@router.get(
    "/",
    response_model=list[CameraSchema],
    dependencies=[Depends(JWTService.get_current_user)],
)
async def get_cameras(
    crud: CamerasCrudServiceInterface = Depends(get_cameras_crud),  # noqa: B008
):
    cameras = await crud.get_cameras()
    if cameras is None:
        raise HTTPException(status_code=404, detail="Cameras not found")
    return cameras
