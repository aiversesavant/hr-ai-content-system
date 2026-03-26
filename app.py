from pipeline.evaluation import evaluate_system
from pipeline.governance import apply_rbac
from pipeline.ingestion import load_documents
from pipeline.chunking import chunk_text
from pipeline.metadata import add_metadata
from pipeline.embeddings import generate_embeddings, model
from pipeline.retrieval import build_faiss_index, search_index

def run_pipeline_and_query(query):
    text = load_documents("data/sample_hr_docs.txt")
    chunks = chunk_text(text, chunk_size=50)
    enriched = add_metadata(chunks)

    embeddings = generate_embeddings(enriched)
    index = build_faiss_index(embeddings)

    query_embedding = model.encode(query)
    distances, indices = search_index(query_embedding, index, top_k=3)

    results = []
    for dist, idx in zip(distances, indices):
        results.append({
            "score": float(dist),
            "text": enriched[idx]["text"],
            "metadata": enriched[idx]["metadata"]
        })

    return results

if __name__ == "__main__":
    print("=== RUNNING SAMPLE QUERY ===")
    query = "What is the parental leave policy?"
    results = run_pipeline_and_query(query)
    results = apply_rbac(results, role="employee")

    for r in results:
        print("\n--- RESULT ---")
        print("Score:", r["score"])
        print("Metadata:", r["metadata"])
        print("Text:", r["text"])

    print("\n=== RUNNING EVALUATION ===")
    eval_results, accuracy = evaluate_system(run_pipeline_and_query)

    for e in eval_results:
        print("\nQuestion:", e["question"])
        print("Expected:", e["expected"])
        print("Correct:", e["correct"])

    print(f"\nOverall Accuracy: {accuracy * 100:.2f}%")