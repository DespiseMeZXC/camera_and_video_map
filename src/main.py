import uvicorn
from config import settings
from fastapi import FastAPI

app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
)


@app.get("/health_check")
def health_check():
    """Проверка работоспособности сервера."""
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
