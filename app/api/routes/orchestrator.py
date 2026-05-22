from fastapi import APIRouter

from app.services.orchestrator_agent import (
    orchestrator_agent
)

router = APIRouter()

@router.get("/orchestrator-review/{contract_id}")
def run_orchestrator(
    contract_id: int,
    query: str
):

    result = orchestrator_agent(
        contract_id,
        query
    )

    return result

