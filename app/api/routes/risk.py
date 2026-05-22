from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.contract import Contract

from app.services.pdf_service import extract_text_from_pdf
from app.services.chunking_service import chunk_text

from app.services.faiss_service import (
    load_faiss_index
)

from app.services.search_service import (
    search_similar_chunks
)

from app.services.risk_service import (
    analyze_contract_risks
)

router = APIRouter()

@router.get("/analyze-risks/{contract_id}")
def analyze_risks(
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

    # Extract text
    extracted_text = extract_text_from_pdf(
        contract.file_path
    )

    # Chunk text
    chunks = chunk_text(extracted_text)

    # Load FAISS index
    index = load_faiss_index(contract.id)

    if not index:
        return {
            "error": "FAISS index not found"
        }

    # Retrieve risk-related chunks
    retrieved_chunks = search_similar_chunks(
        query="liability termination payment confidentiality compliance risks",
        index=index,
        chunks=chunks,
        top_k=5
    )

    # AI risk analysis
    risk_analysis = analyze_contract_risks(
        retrieved_chunks
    )

    return {
        "contract_id": contract.id,
        "filename": contract.filename,
        "retrieved_chunks": retrieved_chunks,
        "risk_analysis": risk_analysis
    }
