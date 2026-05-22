from fastapi import APIRouter

from app.services.chat_service import (
    conversational_rag_chat
)

router = APIRouter()

@router.get("/chat/{contract_id}")
def chat_with_memory(
    contract_id: int,
    session_id: str,
    question: str
):

    result = conversational_rag_chat(
        contract_id=contract_id,
        session_id=session_id,
        user_query=question
    )

    return result
