from app.services.rag_service import (
    retrieve_relevant_chunks
)

from app.services.llm_service import (
    generate_rag_response
)

from app.core.logger import logger

def contract_review_agent(
    contract_id,
    user_query
):

    logger.info(
        f"Agent started for contract "
        f"{contract_id}"
    )

    # STEP 1
    # Retrieve relevant chunks
    retrieved_chunks = (
        retrieve_relevant_chunks(
            contract_id,
            user_query
        )
    )

    logger.info(
        "Relevant chunks retrieved"
    )

    # STEP 2
    # Build agent prompt
    agent_prompt = f"""
You are an AI Contract Risk Review Agent.

Your responsibilities:

1. Analyze contract clauses
2. Identify risks
3. Explain why they are risky
4. Suggest safer alternatives
5. Recommend improvements

User Query:
{user_query}

Provide professional analysis.
"""

    # STEP 3
    # Generate AI response
    response = generate_rag_response(
        query=agent_prompt,
        context_chunks=retrieved_chunks
    )

    logger.info(
        "Agent analysis completed"
    )

    return {
        "contract_id": contract_id,
        "query": user_query,
        "retrieved_chunks": retrieved_chunks,
        "agent_response": response
    }

