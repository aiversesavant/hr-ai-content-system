from pipeline.ingestion import load_documents
from pipeline.chunking import chunk_text
from pipeline.metadata import add_metadata

def run_pipeline():
    text = load_documents("data/sample_hr_docs.txt")
    chunks = chunk_text(text)
    enriched = add_metadata(chunks)

    for item in enriched:
        print(item)

if __name__ == "__main__":
    run_pipeline()