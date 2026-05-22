import ollama

MODEL_NAME = "gemma:2b"

def generate_rag_response(
    query,
    context_chunks
):

    context = "\n\n".join(context_chunks)

    prompt = f"""
You are an AI Contract Risk Intelligence Assistant.

Use ONLY the provided contract context to answer the user question.

If the answer is not found in the context, say:
"I could not find relevant information in the contract."

CONTRACT CONTEXT:
{context}

USER QUESTION:
{query}

ANSWER:
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
