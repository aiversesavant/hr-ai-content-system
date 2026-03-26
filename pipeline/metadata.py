def add_metadata(chunks):
    enriched = []

    for i, chunk in enumerate(chunks):
        metadata = {
            "chunk_id": i,
            "length": len(chunk),
            "source": "HR_DOC"
        }

        enriched.append({
            "text": chunk,
            "metadata": metadata
        })

    return enriched