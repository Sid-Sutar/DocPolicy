import faiss
import numpy as np
import pickle
import os

FAISS_FOLDER = "data/embeddings"

def create_faiss_index(embeddings, contract_id):

    vectors = np.array(
        embeddings,
        dtype="float32"
    )

    dimension = vectors.shape[1]

    # Create FAISS index
    index = faiss.IndexFlatL2(dimension)

    # Add vectors
    index.add(vectors)

    # Save index
    faiss_path = os.path.join(
        FAISS_FOLDER,
        f"contract_{contract_id}.index"
    )

    faiss.write_index(index, faiss_path)

    return faiss_path


def load_faiss_index(contract_id):

    faiss_path = os.path.join(
        FAISS_FOLDER,
        f"contract_{contract_id}.index"
    )

    if not os.path.exists(faiss_path):
        return None

    index = faiss.read_index(faiss_path)

    return index
