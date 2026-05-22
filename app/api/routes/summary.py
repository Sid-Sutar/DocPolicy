from fastapi import APIRouter

from app.services.summary_service import (
    generate_contract_summary
)

router = APIRouter()

@router.get("/summarize-contract/{contract_id}")
def summarize_contract(
    contract_id: int
):

    result = generate_contract_summary(
        contract_id
    )

    return result

