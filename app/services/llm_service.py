import ollama

from app.core.logger import logger

def generate_rag_response(
    query,
    context_chunks
):

    logger.info(
        "Generating LLM response"
    )

    combined_context = "\n\n".join(
        context_chunks
    )

    prompt = f"""
You are an AI Contract Intelligence Assistant.

RULES:
- Answer briefly and clearly
- Do NOT repeat information
- Keep answers under 200 words
- Use only relevant context
- Be professional and concise

Context:
{combined_context}

Question:
{query}

Answer:
"""

    response = ollama.chat(
        model="phi3:mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response["message"]["content"]

    logger.info(
        "LLM response generated"
    )

    return answer

