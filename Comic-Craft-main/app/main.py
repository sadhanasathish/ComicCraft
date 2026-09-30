from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config import settings
from app.routes import router
from app.utils.files import ensure_directories

BASE_DIR = Path(__file__).resolve().parent.parent

ensure_directories()

app = FastAPI(
    title="ComicCraft API",
    description="AI-powered five-panel comic generator",
    version="1.0.0",
)

app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static",
)

app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=settings.app_host,
        port=settings.app_port,
        reload=settings.debug,
    )