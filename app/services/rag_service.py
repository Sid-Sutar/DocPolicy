from app.models.contract import Contract

from app.services.pdf_service import (
    extract_text_from_pdf
)

from app.services.chunking_service import (
    chunk_text
)

from app.services.faiss_service import (
    load_faiss_index
)

from app.services.search_service import (
    search_similar_chunks
)

from app.database.database import SessionLocal

def retrieve_relevant_chunks(
    contract_id,
    query,
    top_k=5
):

    db = SessionLocal()

    try:

        # Find contract
        contract = db.query(Contract).filter(
            Contract.id == contract_id
        ).first()

        if not contract:

            return []

        # Extract text
        extracted_text = extract_text_from_pdf(
            contract.file_path
        )

        # Chunk text
        chunks = chunk_text(extracted_text)

        # Load FAISS index
        index = load_faiss_index(
            contract.id
        )

        if not index:

            return []

        # Semantic retrieval
        retrieved_chunks = (
            search_similar_chunks(
                query=query,
                index=index,
                chunks=chunks,
                top_k=top_k
            )
        )

        return retrieved_chunks

    finally:

        db.close()

