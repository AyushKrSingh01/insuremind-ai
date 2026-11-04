# InsureMind AI

### Agentic Enterprise Knowledge Intelligence Platform

InsureMind AI is an enterprise knowledge intelligence platform designed to help organizations retrieve, understand, compare and reason over internal documents using advanced Retrieval-Augmented Generation (RAG) and controlled agentic workflows.

The initial implementation focuses on a fictional insurance organization with a curated knowledge base of insurance policies, compliance documents, employee handbooks and operational documentation.

**Project status:** Architecture and initial repository setup completed. Implementation in progress.

---

## Key Features (Planned)

- Multi-format document ingestion (PDF, DOCX, TXT and Markdown).
- Multiple chunking strategies, including recursive and semantic chunking.
- Local embedding generation using BGE models.
- Dense vector and BM25 keyword retrieval.
- Hybrid retrieval with Reciprocal Rank Fusion (RRF).
- Cross-encoder reranking.
- Hierarchical and parent-child RAG.
- Agentic RAG using LangGraph and controlled tools.
- Context-grounded answers with source citations.
- Answer verification and evidence-based abstention.
- Retrieval and answer evaluation.
- Enterprise dashboard with document management and agent traces.

---

## Technology Stack

| Component | Technology |
|---|---|
| Frontend | React, TypeScript, Vite |
| Styling | Tailwind CSS |
| Backend | Python, FastAPI |
| Validation | Pydantic |
| Agent orchestration | LangGraph |
| Local LLM inference | Ollama |
| Embeddings | BGE |
| Vector database | Qdrant |
| Keyword retrieval | BM25 |
| Application database | PostgreSQL |
| Document processing | PyMuPDF, Docling |
| Evaluation | Custom evaluation, pytest |
| Observability | Self-hosted Langfuse |
| Infrastructure | Docker Compose |

The project prioritizes open-source software, local inference and free infrastructure options.

---

## System Architecture

The application follows a modular monolith architecture.

Major modules:

1. Document ingestion
2. Chunking and preprocessing
3. Embedding generation
4. Vector indexing
5. Hybrid retrieval
6. Reranking
7. Hierarchical retrieval
8. Agent orchestration
9. Answer generation and verification
10. Evaluation and observability

See [`docs/architecture.md`](docs/architecture.md) for the detailed architecture specification.

---

## Project Structure

```text
insuremind-ai/
├── frontend/
├── backend/
├── docs/
│   └── architecture.md
├── data/
├── scripts/
├── .github/
│   └── workflows/
├── README.md
├── .gitignore
└── .env.example
```

The structure will expand as individual modules are implemented.

---

## Development Roadmap

| Phase | Focus |
|---|---|
| 1 | Architecture and repository setup |
| 2 | Backend, database and ingestion |
| 3 | Chunking, embeddings and vector indexing |
| 4 | Hybrid retrieval and reranking |
| 5 | Hierarchical RAG |
| 6 | Agentic RAG with LangGraph |
| 7 | Answer generation and conversational memory |
| 8 | Retrieval and answer evaluation |
| 9 | Frontend and dashboard |
| 10 | Security and automated testing |
| 11 | Deployment and monitoring |
| 12 | Documentation and demonstration |

---

## Evaluation

The planned evaluation framework will measure:

**Retrieval**
- Precision@K
- Recall@K
- MRR
- NDCG@K

**Answer quality**
- Faithfulness
- Answer relevance
- Completeness
- Context precision
- Context recall

**Performance**
- Retrieval latency
- Generation latency
- End-to-end latency
- Inference cost

Benchmark results will be reported only after actual experiments.

---

## Running the Project

Setup and execution instructions will be added as the frontend, backend and infrastructure become operational.

---

## Security

- User-level document authorization.
- File validation.
- Secure configuration and secret management.
- Input validation.
- Controlled agent tool execution.
- Protection against prompt injection through retrieved documents.

---

## License

License to be determined.

---

**Built as an engineering project to explore advanced RAG, agentic AI and production-oriented software development.**