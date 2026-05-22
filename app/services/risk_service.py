from app.services.llm_service import (
    generate_rag_response
)

def analyze_contract_risks(
    retrieved_chunks
):

    risk_prompt = """
Analyze the provided contract clauses carefully.

Return ONLY structured analysis in this format:

[
    {
        "risk_type": "...",
        "risk_level": "...",
        "explanation": "...",
        "recommendation": "..."
    }
]

Focus on:
- liability risks
- termination risks
- payment risks
- confidentiality issues
- compliance concerns

Be concise and professional.
"""

    response = generate_rag_response(
        query=risk_prompt,
        context_chunks=retrieved_chunks
    )

    return response
