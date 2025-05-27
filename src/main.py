import uvicorn
from fastapi import FastAPI

from src.config import settings

app = FastAPI(
    title=settings.app.name,
    description=settings.app.description,
    version=settings.app.version,
)


@app.get("/health_check")
def health_check():
    """Проверка работоспособности сервера."""
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
