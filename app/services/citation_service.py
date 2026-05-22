from app.services.rag_service import (
    retrieve_relevant_chunks
)

from app.services.llm_service import (
    generate_rag_response
)

from app.core.logger import logger

def generate_cited_response(
    contract_id,
    user_query
):

    logger.info(
        f"Generating cited response "
        f"for contract {contract_id}"
    )

    # Retrieve chunks
    retrieved_chunks = (
        retrieve_relevant_chunks(
            contract_id=contract_id,
            query=user_query,
            top_k=5
        )
    )

    if not retrieved_chunks:

        return {
            "message":
            "No relevant chunks found"
        }

    # Create numbered citations
    cited_chunks = []

    for idx, chunk in enumerate(
        retrieved_chunks,
        start=1
    ):

        cited_chunk = (
            f"[SOURCE {idx}]\n"
            f"{chunk}"
        )

        cited_chunks.append(
            cited_chunk
        )

    citation_prompt = f"""
You are an AI Contract Intelligence Assistant.

Answer the user's question
using the provided sources.

IMPORTANT:
- Use information from the sources
- Mention technologies, skills, tools,
  or clauses clearly if present
- Cite sources like [SOURCE 1]
- Be concise and professional

User Question:
{user_query}

Answer with citations.
"""

    answer = generate_rag_response(
        query=citation_prompt,
        context_chunks=cited_chunks
    )

    logger.info(
        "Citation-aware response generated"
    )

    return {
        "contract_id": contract_id,
        "question": user_query,
        "sources": cited_chunks,
        "answer": answer
    }

