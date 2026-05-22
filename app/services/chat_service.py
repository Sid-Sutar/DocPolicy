from app.services.rag_service import (
    retrieve_relevant_chunks
)

from app.services.llm_service import (
    generate_rag_response
)

from app.services.memory_service import (
    save_message,
    get_conversation_history,
    format_conversation_history
)

from app.core.logger import logger

def conversational_rag_chat(
    contract_id,
    session_id,
    user_query
):

    logger.info(
        f"Starting conversation for "
        f"session {session_id}"
    )

    # Retrieve memory
    history = get_conversation_history(
        session_id
    )

    formatted_history = (
        format_conversation_history(
            history
        )
    )

    # Retrieve relevant chunks
    retrieved_chunks = (
        retrieve_relevant_chunks(
            contract_id=contract_id,
            query=user_query,
            top_k=5
        )
    )

    conversational_prompt = f"""
You are an AI Contract Intelligence Assistant.

Conversation History:
{formatted_history}

Current User Question:
{user_query}

Instructions:
1. Use conversation history
2. Understand follow-up questions
3. Use retrieved context
4. Provide professional answers
5. Maintain conversational continuity
"""

    # Generate response
    answer = generate_rag_response(
        query=conversational_prompt,
        context_chunks=retrieved_chunks
    )

    # Save messages
    save_message(
        session_id,
        "user",
        user_query
    )

    save_message(
        session_id,
        "assistant",
        answer
    )

    logger.info(
        "Conversational response generated"
    )

    return {
        "contract_id": contract_id,
        "session_id": session_id,
        "conversation_history": history,
        "retrieved_chunks": retrieved_chunks,
        "answer": answer
    }

