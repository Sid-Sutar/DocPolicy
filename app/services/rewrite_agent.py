from app.services.rag_service import (
    retrieve_relevant_chunks
)

from app.services.llm_service import (
    generate_rag_response
)

from app.core.logger import logger

def rewrite_agent(
    contract_id,
    user_query
):

    logger.info(
        f"Running rewrite agent "
        f"for contract {contract_id}"
    )

    retrieved_chunks = (
        retrieve_relevant_chunks(
            contract_id=contract_id,
            query=user_query,
            top_k=2
        )
    )

    rewrite_prompt = f"""
You are a Contract Rewrite AI Agent.

Your responsibilities:
1. Rewrite risky clauses
2. Improve clarity
3. Suggest safer alternatives
4. Improve professionalism
5. Simplify legal language

User Query:
{user_query}

Provide concise rewritten suggestions.
"""

    response = generate_rag_response(
        query=rewrite_prompt,
        context_chunks=retrieved_chunks
    )

    logger.info(
        "Rewrite agent completed"
    )

    return {
        "agent": "rewrite_agent",
        "analysis": response,
        "retrieved_chunks": retrieved_chunks
    }

