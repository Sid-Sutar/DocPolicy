# AI Contract & Policy Risk Intelligence Agent

An enterprise-style AI-powered document intelligence platform for analyzing contracts, policies, and legal documents using Retrieval-Augmented Generation (RAG), vector search, conversational AI, and multi-agent orchestration.

---

# Features

- Upload and analyze PDF contracts/documents
- AI-powered semantic search using FAISS
- Retrieval-Augmented Generation (RAG)
- Conversational AI memory
- Citation-aware AI responses
- Multi-document querying
- AI-powered risk analysis
- Multi-agent orchestration system
- Dockerized deployment
- FastAPI backend architecture
- MySQL database integration
- Local LLM inference using Ollama

---

# Tech Stack

## Backend
- FastAPI
- Python

## AI / ML
- LangChain
- FAISS
- Sentence Transformers
- Ollama
- Phi3 Mini LLM

## Database
- MySQL

## Deployment
- Docker

## Other Tools
- Swagger UI
- Uvicorn
- PyMuPDF

---

# System Architecture

```text
User Upload
     ↓
PDF Extraction
     ↓
Text Chunking
     ↓
Embedding Generation
     ↓
FAISS Vector Search
     ↓
RAG Pipeline
     ↓
LLM Response Generation
     ↓
Conversational Memory
     ↓
Multi-Agent AI Analysis