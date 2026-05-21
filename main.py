from fastapi import FastAPI

from app.core.config import settings

from app.api.routes.health import router as health_router
from app.api.routes.upload import router as upload_router
from app.api.routes.extract import router as extract_router
from app.api.routes.chunk import router as chunk_router
from app.api.routes.embed import router as embed_router
from app.api.routes.search import router as search_router




from app.database.init_db import create_tables

# Create database tables
create_tables()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

# Register routes
app.include_router(health_router)
app.include_router(upload_router)
app.include_router(extract_router)
app.include_router(chunk_router)
app.include_router(embed_router)
app.include_router(search_router)





@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} is running"
    }
