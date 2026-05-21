from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.contract import Contract

from app.services.pdf_service import extract_text_from_pdf
from app.services.chunking_service import chunk_text
from app.services.embedding_service import generate_embeddings

from app.services.faiss_service import (
    create_faiss_index,
    load_faiss_index
)

from app.services.search_service import (
    search_similar_chunks
)

router = APIRouter()

@router.get("/build-index/{contract_id}")
def build_index(
    contract_id: int,
    db: Session = Depends(get_db)
):

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

    # Create FAISS index
    faiss_path = create_faiss_index(
        embeddings,
        contract.id
    )

    return {
        "message": "FAISS index created",
        "faiss_path": faiss_path,
        "total_chunks": len(chunks)
    }


@router.get("/semantic-search/{contract_id}")
def semantic_search(
    contract_id: int,
    query: str,
    db: Session = Depends(get_db)
):

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

    # Search similar chunks
    results = search_similar_chunks(
        query=query,
        index=index,
        chunks=chunks
    )

    return {
        "query": query,
        "matching_chunks": results
    }
