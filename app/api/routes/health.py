from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.health_log import HealthLog

router = APIRouter()

@router.get("/health")
def health_check(db: Session = Depends(get_db)):

    log = HealthLog(
        status="healthy",
        message="Backend running successfully"
    )

    db.add(log)
    db.commit()

    return {
        "status": "healthy",
        "message": "Backend running successfully"
    }

