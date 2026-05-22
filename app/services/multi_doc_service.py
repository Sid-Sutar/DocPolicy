from app.database.database import (
    SessionLocal
)

from app.models.contract import Contract

from app.services.rag_service import (
    retrieve_relevant_chunks
)

from app.services.llm_service import (
    generate_rag_response
)

from app.core.logger import logger

def multi_document_query(
    user_query
):

    logger.info(
        "Starting multi-document query"
    )

    db = SessionLocal()

    try:

        contracts = db.query(
            Contract
        ).all()

        all_chunks = []

        for contract in contracts:

            logger.info(
                f"Searching contract "
                f"{contract.id}"
            )

            chunks = retrieve_relevant_chunks(
                contract_id=contract.id,
                query=user_query,
                top_k=3
            )

            for chunk in chunks:

                labeled_chunk = (
                    f"[Document: "
                    f"{contract.filename}]\n"
                    f"{chunk}"
                )

                all_chunks.append(
                    labeled_chunk
                )

        if not all_chunks:

            return {
                "message":
                "No relevant content found"
            }

        combined_prompt = f"""
You are an AI Contract Intelligence Assistant.

Analyze the retrieved information from
multiple documents.

User Query:
{user_query}

Requirements:
1. Compare relevant findings
2. Mention document names
3. Highlight similarities/differences
4. Provide professional analysis
"""

        response = generate_rag_response(
            query=combined_prompt,
            context_chunks=all_chunks
        )

        logger.info(
            "Multi-document analysis completed"
        )

        return {
            "query": user_query,
            "documents_analyzed":
            len(contracts),
            "retrieved_chunks":
            all_chunks,
            "analysis":
            response
        }

    finally:

        db.close()

