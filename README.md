# Hello World API

Simple REST API built with Python and FastAPI.

## Features

- FastAPI REST API
- POST endpoint for text processing
- Docker support
- GitHub Actions CI pipeline
- Deployment on Render

---

# Run locally

## Create virtual environment

```bash
py -m venv .venv
```

## Activate virtual environment

```bash
.venv\Scripts\Activate.ps1
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run application

```bash
py -m uvicorn main:app --reload
```

Application will be available at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

# Run with Docker

## Build image

```bash
docker build -t hello-world-api .
```

## Run container

```bash
docker run -p 8000:8000 hello-world-api
```

---

# API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Hello world endpoint |
| GET | /health | Health check |
| POST | /process-text | Process input text |
| POST | /classify-text | Classify text as invoice-related |

---

# POST /process-text Example

## Request

```json
{
  "text": "Hello FastAPI"
}
```

## Response

```json
{
  "message": "Přijal jsem text: Hello FastAPI",
  "length": 13
}
```

## POST /classify-text Example

### Request

```json
{
  "text": "Dobrý den, v příloze zasíláme fakturu."
}
```

### Response

```json
{
  "text": "Dobrý den, v příloze zasíláme fakturu.",
  "is_invoice": true,
  "reason": "Text contains invoice-related keyword."
}
```

---

# Technologies

- Python
- FastAPI
- Docker
- GitHub Actions
- Render