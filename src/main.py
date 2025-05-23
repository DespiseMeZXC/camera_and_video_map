import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="Карта с камерами и видео",
    description="Карта с камерами и видео",
    version="0.1.0",
)


@app.get("/health_check")
def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
