from fastapi import APIRouter, Depends, HTTPException

from src.dependencies.videos import get_videos_crud
from src.interfaces.videos import VideosCrudServiceInterface
from src.schemas.videos import VideosSchema
from src.utils.jwt import JWTService

router = APIRouter(prefix="/videos", tags=["videos"])


@router.get(
    "/",
    response_model=list[VideosSchema],
    dependencies=[Depends(JWTService.get_current_user)],
)
async def get_videos(
    crud: VideosCrudServiceInterface = Depends(get_videos_crud),  # noqa: B008
):
    videos = await crud.get_videos()
    if videos is None:
        raise HTTPException(status_code=404, detail="Videos not found")
    return [VideosSchema.model_validate(video) for video in videos]
