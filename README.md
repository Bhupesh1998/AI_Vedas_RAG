# Vyas AI 📚

An AI-powered Retrieval-Augmented Generation (RAG) application built using React, FastAPI, ChromaDB, BGE-M3 embeddings, Gemini, and Qwen.

## Features

- Ask questions from books and documents
- Retrieval-Augmented Generation (RAG)
- ChromaDB Vector Database
- BGE-M3 Embeddings
- Gemini Integration (Development)
- Qwen3:8B Integration (Production / Offline)
- FastAPI Backend
- React + Tailwind Frontend
- Mobile Responsive UI
- Environment-based LLM Switching

## Tech Stack

### Frontend

- React
- Vite
- Tailwind CSS

### Backend

- FastAPI
- ChromaDB
- Sentence Transformers (BGE-M3)

### LLMs

- Gemini 2.5 Flash (Development)
- Qwen3:8B via Ollama (Production)

## Architecture

User
↓
React Frontend
↓
FastAPI
↓
ChromaDB Retrieval
↓
Gemini / Qwen
↓
Answer

## Installation

### Backend

```bash
git clone <repository-url>
cd backend

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

### Run Backend

```bash
uvicorn api:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

## Environment Variables

```env
APP_ENV=development

GEMINI_API_KEY=YOUR_API_KEY
```

Production:

```env
APP_ENV=production
```

## API Example

POST `/chat`

Request:

```json
{
  "question": "माँ कौन थीं?"
}
```

Response:

```json
{
  "answer": "..."
}
```

## Future Improvements

- Streaming Responses
- Chat History
- Markdown Rendering
- User Authentication
- Multi-book Support
- Source Citations
- LangGraph Integration

## Author

Bhupesh Mali
