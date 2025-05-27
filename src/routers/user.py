from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["user"])


@router.post("/auth")
def auth():
    pass


@router.post("/register")
def register():
    pass
