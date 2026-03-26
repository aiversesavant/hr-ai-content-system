import faiss
import numpy as np

def build_faiss_index(embeddings):
    embeddings = np.array(embeddings).astype("float32")
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

def search_index(query_embedding, index, top_k=3):
    query_embedding = np.array([query_embedding]).astype("float32")
    distances, indices = index.search(query_embedding, top_k)
    return distances[0], indices[0]