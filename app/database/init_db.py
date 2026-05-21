from app.database.database import engine, Base

# Import models here
from app.models.health_log import HealthLog

def create_tables():
    Base.metadata.create_all(bind=engine)
