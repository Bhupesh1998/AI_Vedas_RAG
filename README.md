# Offline RAG Chatbot for Hindi / Sanskrit Books

An offline Retrieval-Augmented Generation (RAG) system built using:

- Python
- BGE-M3 Embeddings
- ChromaDB
- Qwen3 8B (Ollama)
- FastAPI
- React (Frontend - WIP)

## Features

- PDF OCR Processing
- Text Cleaning Pipeline
- Text Chunking
- Vector Embeddings using BGE-M3
- ChromaDB Vector Search
- Offline LLM Inference using Qwen3 8B
- Hallucination Guard using Distance Threshold
- Works completely offline after setup

## Architecture

User Question

↓

BGE-M3 Embedding

↓

ChromaDB Similarity Search

↓

Top Relevant Chunks

↓

Qwen3 8B

↓

Answer

## Tech Stack

### Backend

- Python
- FastAPI
- ChromaDB
- Sentence Transformers
- Ollama

### Embedding Model

- BAAI/bge-m3

### LLM

- Qwen3 8B

## Installation

### Clone Repository

```bash
git clone <your-repo-url>
cd <repo-name>
```

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Ollama

```bash
ollama serve
```

### Download Model

```bash
ollama pull qwen3:8b
```

### Run Application

```bash
python rag.py
```

## Example Question

```text
माँ कौन थीं?
```

## Future Improvements

- FastAPI API Layer
- React Chat Interface
- Multi-PDF Support
- Source Citations
- Reranking
- Agentic RAG

## Author

Bhupesh
