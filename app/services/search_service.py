import numpy as np

from app.services.embedding_service import (
    embedding_model
)

def search_similar_chunks(
    query,
    index,
    chunks,
    top_k=3
):

    # Convert query into embedding
    query_embedding = embedding_model.encode(
        [query]
    )

    query_vector = np.array(
        query_embedding,
        dtype="float32"
    )

    # Search similar vectors
    distances, indices = index.search(
        query_vector,
        top_k
    )

    results = []

    for idx in indices[0]:

        if idx < len(chunks):

            results.append(chunks[idx])

    return results
