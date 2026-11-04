# InsureMind AI — System Architecture

**Project:** InsureMind AI — Agentic Enterprise Knowledge Intelligence Platform  
**Architecture status:** Proposed — implementation pending  
**Architecture style:** Modular monolith  
**Primary objective:** Build an enterprise document intelligence platform using advanced RAG and controlled agentic workflows.

---

## 1. System Overview

InsureMind AI is an enterprise knowledge intelligence platform that enables employees to upload organizational documents, retrieve relevant information, ask complex questions, compare policies and receive evidence-grounded answers with source citations.

The application combines document processing, advanced retrieval, hierarchical RAG, agentic orchestration, answer verification and evaluation in a modular full-stack application.

The initial use case is a fictional insurance organization with a curated knowledge base containing insurance policies, compliance documents, employee handbooks and operational documentation.

## 2. Technology Stack

| Layer | Technology | Responsibility |
|---|---|---|
| Frontend | React | User interface |
| Language | TypeScript | Frontend type safety |
| Build tool | Vite | Frontend development |
| Styling | Tailwind CSS | UI styling |
| Backend | FastAPI | REST API |
| Backend language | Python | Application logic |
| Validation | Pydantic | Request and response validation |
| Agent orchestration | LangGraph | Controlled agent workflows |
| LLM inference | Ollama | Local model inference |
| Embeddings | BGE family | Vector representations |
| Vector database | Qdrant | Dense vector storage and search |
| Keyword retrieval | BM25 | Lexical retrieval |
| Reranking | BGE cross-encoder | Relevance reranking |
| Application database | PostgreSQL | Users, documents and metadata |
| Cache / coordination | Redis | Optional caching and background coordination |
| Document extraction | PyMuPDF | PDF extraction |
| Document processing | Docling | Advanced document parsing where appropriate |
| Evaluation | Custom framework, pytest, optional RAGAS | RAG quality measurement |
| Observability | Self-hosted Langfuse | Tracing and monitoring |
| Infrastructure | Docker Compose | Local service orchestration |
| CI/CD | GitHub Actions | Automated checks |

All development and deployment choices must respect the free-only constraint. Local and open-source components are preferred. Hosted free tiers must be verified before use.

## 3. High-Level Architecture

The system follows a modular monolith architecture.

### 3.1 Frontend Layer

The React application provides:

- Dashboard
- AI Chat
- Knowledge Base
- Evaluation
- Agent Traces
- Settings

The frontend communicates with FastAPI through REST APIs and streaming endpoints where appropriate.

### 3.2 Backend Layer

FastAPI handles:

- API routing
- Authentication and authorization
- Input validation
- Document management
- Retrieval requests
- Agent execution
- Answer generation
- Evaluation requests

Business logic is separated into independent application modules.

### 3.3 AI and RAG Layer

This layer contains:

- Document ingestion
- Chunking
- Embedding generation
- Vector indexing
- Dense retrieval
- BM25 retrieval
- Hybrid retrieval
- Reciprocal Rank Fusion
- Cross-encoder reranking
- Hierarchical retrieval
- Agent orchestration
- Answer generation
- Citation verification

### 3.4 Data Layer

PostgreSQL stores application metadata and relational records.

Qdrant stores vector representations and searchable chunk metadata.

Original uploaded files are stored separately from their extracted text and vector representations.

Redis may be introduced when caching or background-job coordination becomes necessary.

## 4. Document Ingestion Pipeline

The ingestion pipeline processes documents before they become searchable.

**Processing sequence:**

1. Receive document upload.
2. Validate file type and size.
3. Calculate document hash for deduplication.
4. Extract text and metadata.
5. Identify pages and document sections.
6. Apply the selected chunking strategy.
7. Generate parent-child relationships.
8. Generate embeddings.
9. Store vectors in Qdrant.
10. Store document metadata and processing status in PostgreSQL.

Supported initial file formats:

- PDF
- TXT
- Markdown
- DOCX

Original text and source metadata must be preserved to support traceable citations.

## 5. Chunking and Embedding Architecture

The application will support multiple chunking strategies:

- Fixed-size chunking
- Recursive character chunking
- Semantic chunking
- LLM-assisted chunk enrichment
- Hierarchical chunking
- Parent-child chunking

Each chunk should maintain:

- Document ID
- Chunk ID
- Parent chunk ID where applicable
- Page number
- Section identifier
- Original text
- Chunking strategy
- Embedding model identifier

Embedding generation must support batching and consistent model configuration.

Re-indexing must be possible when the embedding model changes.

## 6. Retrieval Architecture

The retrieval system supports multiple strategies.

### Dense Retrieval

Uses embedding similarity to identify semantically relevant passages.

### Keyword Retrieval

Uses BM25 to identify passages matching important terms and phrases.

### Hybrid Retrieval

Combines dense and lexical retrieval results.

### Reciprocal Rank Fusion

RRF combines ranked result lists using:

`RRF_score(d) = Σ 1 / (k + rank_i(d))`

The implementation will use a configurable smoothing constant and retrieval weights only where justified by experiments.

### Reranking

A cross-encoder evaluates query-passage relevance and reranks the retrieved candidates.

### Hierarchical Retrieval

The document hierarchy is:

Document → Document Summary → Sections → Parent Chunks → Child Chunks.

The system can retrieve a relevant child chunk and expand its parent context.

## 7. Agentic RAG Architecture

LangGraph will coordinate a bounded agent workflow.

Planned graph nodes:

1. Query classifier
2. Query router
3. Retrieval planner
4. Tool executor
5. Retrieval grader
6. Query rewriter
7. Context aggregator
8. Answer generator
9. Answer verifier
10. Final response

Planned tools:

- vector_search
- keyword_search
- hybrid_search
- hierarchical_search
- document_lookup
- calculator
- policy_comparator

The agent must use validated tool schemas and enforce:

- Maximum iteration limits
- Tool timeouts
- Error handling
- Retry limits
- Tool-call logging
- Evidence-based abstention

Retrieved document content is untrusted data. It must never override system instructions or independently authorize tool execution.

Unrestricted code execution is prohibited.

## 8. Answer Generation and Verification

Answers must be grounded in retrieved evidence.

The generation layer will support:

- Context-grounded generation
- Source citations
- Page and section references
- Conversation history
- Follow-up questions
- Evidence indicators
- Insufficient-information responses

The answer verifier will check whether generated claims are supported by the available evidence.

The application must not invent source references or claim certainty when evidence is insufficient.

## 9. Evaluation Architecture

The evaluation framework compares multiple retrieval and generation strategies.

### Retrieval Metrics

- Precision@K
- Recall@K
- Mean Reciprocal Rank
- Normalized Discounted Cumulative Gain

### Answer Metrics

- Faithfulness
- Answer relevance
- Completeness
- Context precision
- Context recall

### Operational Metrics

- End-to-end latency
- Retrieval latency
- Generation latency
- Token usage where available
- Inference cost
- Number of retrieval attempts

The benchmark will compare:

1. Naive vector RAG
2. Hybrid RAG
3. Hybrid RAG with reranking
4. Hierarchical RAG
5. Agentic RAG

Evaluation datasets must contain questions, reference answers, relevant document IDs, relevant chunk IDs and expected keywords.

Only measured results will be presented as actual benchmark results.

## 10. Security and Reliability

The application will implement:

- Authentication
- User-level document access
- Document-level authorization
- Input validation
- File upload validation
- Rate limiting
- Secure secret management
- Error handling
- Structured logging
- Database migrations
- Automated tests

Users must never retrieve documents they are not authorized to access.

Uploaded documents must be treated as untrusted input.

## 11. Deployment Architecture

The initial development environment will use local services.

Planned infrastructure:

- React frontend
- FastAPI backend
- Ollama for local inference
- Qdrant for vector storage
- PostgreSQL for application data
- Optional Redis
- Docker Compose for reproducible infrastructure
- GitHub Actions for automated testing

Deployment will use free hosting or self-hosted infrastructure where practical.

Persistent storage, resource limits, availability and free-tier restrictions must be verified before selecting a deployment provider.

## 12. Architectural Principles

1. Modular separation of concerns.
2. Reuse existing working RAG implementations where appropriate.
3. Prefer explicit and testable workflows over uncontrolled agent behavior.
4. Keep retrieval strategies independently measurable.
5. Preserve source traceability.
6. Use typed interfaces and validated data models.
7. Avoid unnecessary dependencies and premature microservices.
8. Keep inference local wherever feasible.
9. Make performance claims only from measured results.
10. Document architectural decisions and trade-offs.

## 13. Implementation Status

This document describes the intended architecture.

A component must not be marked as implemented until its code, tests and acceptance criteria have been completed.

Architecture changes must be documented with their reasons and trade-offs.

**Current status:** Architecture specification in progress.