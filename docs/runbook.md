# Runbook

## Local Setup
1. Activate the local virtual environment if present
2. Install dependencies from `requirements.txt`
3. Start the application from the project root

## Operational Checks
- `app.py` exists
- `pipeline/` exists
- `data/` exists
- `requirements.txt` exists

## Recovery Notes
- if retrieval fails, review ingestion, embeddings, and retrieval pipeline modules
- never commit secrets or runtime-only artifacts
