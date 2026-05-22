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

from app.services.llm_service import (
    generate_rag_response
)

router = APIRouter()

@router.get("/ask-contract")
def ask_contract(
    contract_id: int,
    question: str,
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

    # Semantic retrieval
    retrieved_chunks = search_similar_chunks(
        query=question,
        index=index,
        chunks=chunks
    )

    # Generate AI response
    answer = generate_rag_response(
        query=question,
        context_chunks=retrieved_chunks
    )

    return {
        "question": question,
        "retrieved_chunks": retrieved_chunks,
        "answer": answer
    }
