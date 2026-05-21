from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.contract import Contract
from app.services.pdf_service import extract_text_from_pdf

router = APIRouter()

@router.get("/extract-text/{contract_id}")
def extract_text(
    contract_id: int,
    db: Session = Depends(get_db)
):

    # Find contract in DB
    contract = db.query(Contract).filter(
        Contract.id == contract_id
    ).first()

    if not contract:
        return {
            "error": "Contract not found"
        }

    # Extract text
    extracted_text = extract_text_from_pdf(
        contract.file_path
    )

    return {
        "contract_id": contract.id,
        "filename": contract.filename,
        "extracted_text": extracted_text[:3000]
    }

