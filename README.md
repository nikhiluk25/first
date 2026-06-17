# Garbage File Generator API

## Run locally
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000
uvicorn app.main:app --host 0.0.0.0 --port 8000

## Endpoint
GET /generate → creates 1GB file
curl http://localhost:8000/generate