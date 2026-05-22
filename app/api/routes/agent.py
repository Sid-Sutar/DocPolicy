from fastapi import APIRouter

from app.services.agent_service import (
    contract_review_agent
)

router = APIRouter()

@router.get("/agent-review/{contract_id}")
def run_agent_review(
    contract_id: int,
    query: str
):

    result = contract_review_agent(
        contract_id,
        query
    )

    return result
