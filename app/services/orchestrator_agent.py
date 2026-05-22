from app.services.compliance_agent import (
    compliance_review_agent
)

from app.services.rewrite_agent import (
    rewrite_agent
)

from app.core.logger import logger

def orchestrator_agent(
    contract_id,
    user_query
):

    logger.info(
        "Starting orchestrator agent"
    )

    # Run compliance analysis
    compliance_result = (
        compliance_review_agent(
            contract_id,
            user_query
        )
    )

    # Run rewrite analysis
    rewrite_result = (
        rewrite_agent(
            contract_id,
            user_query
        )
    )

    logger.info(
        "All agents completed"
    )

    return {
        "contract_id": contract_id,
        "query": user_query,
        "compliance_agent":
        compliance_result,
        "rewrite_agent":
        rewrite_result
    }

