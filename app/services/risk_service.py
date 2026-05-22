from app.services.llm_service import (
    generate_rag_response
)

def analyze_contract_risks(
    retrieved_chunks
):

    risk_prompt = """
Analyze the provided contract clauses and identify risks.

Return analysis in this format:

1. Risk Type
2. Risk Level (LOW/MEDIUM/HIGH)
3. Explanation
4. Recommendation

Focus on:
- liability risks
- termination risks
- payment issues
- confidentiality concerns
- compliance problems
"""

    response = generate_rag_response(
        query=risk_prompt,
        context_chunks=retrieved_chunks
    )

    return response
