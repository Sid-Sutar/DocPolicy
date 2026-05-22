from fastapi import APIRouter

from app.services.citation_service import (
    generate_cited_response
)

router = APIRouter()

@router.get("/ask-with-citations/{contract_id}")
def ask_with_citations(
    contract_id: int,
    question: str
):

    result = generate_cited_response(
        contract_id,
        question
    )

    return result

