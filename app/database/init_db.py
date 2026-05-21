from app.database.database import engine, Base

# Import models
from app.models.health_log import HealthLog
from app.models.contract import Contract

def create_tables():
    Base.metadata.create_all(bind=engine)

