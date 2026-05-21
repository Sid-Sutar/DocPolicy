from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.contract import Contract

from app.services.pdf_service import extract_text_from_pdf
from app.services.chunking_service import chunk_text

router = APIRouter()

@router.get("/chunk-contract/{contract_id}")
def chunk_contract(
    contract_id: int,
    db: Session = Depends(get_db)
):

    # Find contract
    contract = db.query(Contract).filter(
        Contract.id == contract_id
    ).first()

    if not contract:
        return {
            "error": "Contract not found"
        }

    # Extract PDF text
    extracted_text = extract_text_from_pdf(
        contract.file_path
    )

    # Create chunks
    chunks = chunk_text(extracted_text)

    return {
        "contract_id": contract.id,
        "filename": contract.filename,
        "total_chunks": len(chunks),
        "chunks": chunks[:5]
    }
