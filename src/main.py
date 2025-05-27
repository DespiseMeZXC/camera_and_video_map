from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import settings
from src.routers.users import router as user_router

app = FastAPI(
    title=settings.app.name,
    description=settings.app.description,
    version=settings.app.version,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.middleware.origins_list,
    allow_credentials=settings.middleware.allow_credentials,
    allow_methods=settings.middleware.methods_list,
    allow_headers=settings.middleware.headers_list,
)

# Подключаем роутеры
app.include_router(user_router)


@app.get("/health_check")
async def health_check():
    """Проверка работоспособности сервера."""
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
