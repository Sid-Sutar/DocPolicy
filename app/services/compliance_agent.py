from app.services.rag_service import (
    retrieve_relevant_chunks
)

from app.services.llm_service import (
    generate_rag_response
)

from app.core.logger import logger

def compliance_review_agent(
    contract_id,
    user_query
):

    logger.info(
        f"Running compliance agent "
        f"for contract {contract_id}"
    )

    retrieved_chunks = (
        retrieve_relevant_chunks(
            contract_id=contract_id,
            query=user_query,
            top_k=2
        )
    )

    compliance_prompt = f"""
You are a Compliance Review AI Agent.

Your responsibilities:
1. Identify compliance concerns
2. Detect policy risks
3. Find missing protections
4. Highlight legal concerns
5. Suggest improvements

User Query:
{user_query}

Provide concise compliance analysis.
"""

    response = generate_rag_response(
        query=compliance_prompt,
        context_chunks=retrieved_chunks
    )

    logger.info(
        "Compliance agent completed"
    )

    return {
        "agent": "compliance_agent",
        "analysis": response,
        "retrieved_chunks": retrieved_chunks
    }

