from sqlalchemy import Column, Integer, String

from app.database.database import Base

class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String(255))
    stored_filename = Column(String(255))
    file_path = Column(String(500))

