from fastapi import FastAPI

from app.core.config import settings
from app.api.routes.health import router as health_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

# Include routes
app.include_router(health_router)

@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} is running"
    }

