from sqlalchemy import Column, Integer, String

from app.database.database import Base

class HealthLog(Base):
    __tablename__ = "health_logs"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String(50))
    message = Column(String(255))

