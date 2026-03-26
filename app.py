import gradio as gr

from pipeline.ingestion import load_documents
from pipeline.chunking import chunk_text
from pipeline.metadata import add_metadata
from pipeline.embeddings import generate_embeddings, model
from pipeline.retrieval import build_faiss_index, search_index
from pipeline.governance import apply_rbac
from pipeline.evaluation import evaluate_system


def retrieve_results(query, role="employee"):
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

    results = apply_rbac(results, role=role)
    return results


def format_results(results):
    output = ""
    for r in results:
        output += (
            f"Score: {r['score']:.4f}\n"
            f"Metadata: {r['metadata']}\n"
            f"Text: {r['text']}\n"
            f"{'-'*50}\n"
        )
    return output


def process_and_query(query, role):
    results = retrieve_results(query, role=role)
    return format_results(results)


def run_evaluation():
    eval_results, accuracy = evaluate_system(
        lambda q: retrieve_results(q, role="employee")
    )

    output = ""
    for r in eval_results:
        output += (
            f"Question: {r['question']}\n"
            f"Expected: {r['expected']}\n"
            f"Correct: {r['correct']}\n"
            f"{'-'*50}\n"
        )

    output += f"\nOverall Accuracy: {accuracy * 100:.2f}%"
    return output


with gr.Blocks() as demo:
    gr.Markdown("# HR AI Content Optimization System")
    gr.Markdown(
        "AI-ready HR knowledge pipeline with retrieval, governance, and evaluation."
    )

    with gr.Tab("Query System"):
        query_input = gr.Textbox(label="Ask an HR Question")
        role_input = gr.Radio(
            choices=["employee", "hr"],
            value="employee",
            label="User Role"
        )
        query_output = gr.Textbox(label="Retrieved Results", lines=20)
        query_btn = gr.Button("Search")

        query_btn.click(
            process_and_query,
            inputs=[query_input, role_input],
            outputs=query_output
        )

    with gr.Tab("Evaluation"):
        eval_btn = gr.Button("Run Evaluation")
        eval_output = gr.Textbox(label="Evaluation Results", lines=20)

        eval_btn.click(run_evaluation, outputs=eval_output)

demo.launch()