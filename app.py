import gradio as gr

from pipeline.ingestion import load_documents
from pipeline.chunking import chunk_text
from pipeline.metadata import add_metadata
from pipeline.embeddings import generate_embeddings, model
from pipeline.retrieval import build_faiss_index, search_index
from pipeline.governance import apply_rbac
from pipeline.evaluation import evaluate_system

def process_and_query(query):
    text = load_documents("data/sample_hr_docs.txt")
    chunks = chunk_text(text, chunk_size=50)
    enriched = add_metadata(chunks)

    embeddings = generate_embeddings(enriched)
    index = build_faiss_index(embeddings)

    query_embedding = model.encode(query)
    distances, indices = search_index(query_embedding, index)

    results = []
    for dist, idx in zip(distances, indices):
        results.append({
            "score": float(dist),
            "text": enriched[idx]["text"]
        })

    results = apply_rbac(results, role="employee")

    output = ""
    for r in results:
        output += f"\nScore: {r['score']}\nText: {r['text']}\n---\n"

    return output


def run_evaluation():
    results, accuracy = evaluate_system(process_and_query)

    output = ""
    for r in results:
        output += f"\nQ: {r['question']}\nCorrect: {r['correct']}\n"

    output += f"\nAccuracy: {accuracy*100:.2f}%"
    return output


with gr.Blocks() as demo:
    gr.Markdown("# HR AI Content Optimization System")

    with gr.Tab("Query System"):
        query_input = gr.Textbox(label="Ask HR Question")
        query_output = gr.Textbox(label="Results")
        query_btn = gr.Button("Search")

        query_btn.click(process_and_query, inputs=query_input, outputs=query_output)

    with gr.Tab("Evaluation"):
        eval_btn = gr.Button("Run Evaluation")
        eval_output = gr.Textbox(label="Evaluation Results")

        eval_btn.click(run_evaluation, outputs=eval_output)

demo.launch()