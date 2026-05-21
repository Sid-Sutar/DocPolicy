from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.contract import Contract

from app.services.pdf_service import extract_text_from_pdf
from app.services.chunking_service import chunk_text
from app.services.embedding_service import generate_embeddings

router = APIRouter()

@router.get("/embed-contract/{contract_id}")
def embed_contract(
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

    # Generate embeddings
    embeddings = generate_embeddings(chunks)

    return {
        "contract_id": contract.id,
        "filename": contract.filename,
        "total_chunks": len(chunks),
        "embedding_dimension": len(embeddings[0]),
        "sample_embedding": embeddings[0][:10]
    }

