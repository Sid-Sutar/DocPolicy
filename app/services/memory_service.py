from collections import defaultdict

from app.core.logger import logger

# In-memory chat storage
conversation_memory = defaultdict(list)

def save_message(
    session_id,
    role,
    message
):

    conversation_memory[
        session_id
    ].append({
        "role": role,
        "message": message
    })

    logger.info(
        f"Message saved for session "
        f"{session_id}"
    )

def get_conversation_history(
    session_id
):

    return conversation_memory.get(
        session_id,
        []
    )

def format_conversation_history(
    history
):

    formatted_history = ""

    for item in history:

        formatted_history += (
            f"{item['role']}: "
            f"{item['message']}\n"
        )

    return formatted_history

