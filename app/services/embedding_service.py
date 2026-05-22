from sentence_transformers import (
    SentenceTransformer
)

from app.core.logger import logger

# Load model ONLY ONCE
logger.info(
    "Loading embedding model..."
)

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

logger.info(
    "Embedding model loaded successfully"
)

def generate_embeddings(chunks):

    embeddings = embedding_model.encode(
        chunks
    )

    return embeddings.tolist()
