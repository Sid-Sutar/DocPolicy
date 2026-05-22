from app.services.rag_service import (
    retrieve_relevant_chunks
)

from app.services.llm_service import (
    generate_rag_response
)

from app.core.logger import logger

def generate_contract_summary(
    contract_id
):

    logger.info(
        f"Generating summary for "
        f"contract {contract_id}"
    )

    # Retrieve broad document context
    retrieved_chunks = (
        retrieve_relevant_chunks(
            contract_id=contract_id,
            query="""
            contract overview,
            responsibilities,
            risks,
            obligations,
            technical details,
            compliance,
            agreements
            """,
            top_k=8
        )
    )

    summary_prompt = """
You are an AI Contract Intelligence Assistant.

Generate a professional contract summary.

Include:
1. Main purpose
2. Key responsibilities
3. Important technical details
4. Risks or concerns
5. Overall assessment

Be concise and professional.
"""

    summary = generate_rag_response(
        query=summary_prompt,
        context_chunks=retrieved_chunks
    )

    logger.info(
        "Summary generation completed"
    )

    return {
        "contract_id": contract_id,
        "retrieved_chunks": retrieved_chunks,
        "summary": summary
    }
