# runtime/RAG_PIPELINE.md

Retrieval-Augmented Generation Pipeline — OpenPS3 Specification

**Version:** 1.0

---

# 1. Purpose

This document defines the RAG (Retrieval-Augmented Generation) subsystem used by the OpenPS3 Agent Runtime.

The RAG pipeline is responsible for:

* external knowledge ingestion
* semantic indexing
* context retrieval
* ranking and filtering
* context assembly for LLM consumption

It operates as a **deterministic information retrieval layer** feeding the Agent Runtime.

---

# 2. Core Principle

> The model does not “know” external information. It is provided structured, filtered context via RAG.

RAG is the only mechanism for external knowledge injection.

No direct document access is allowed from agents or models.

---

# 3. System Architecture

The RAG system is composed of five stages:

## 3.1 Ingestion Layer

Responsible for ingesting raw documents.

Sources may include:

* repository documentation
* RFCs and ADRs
* code comments (structured extraction only)
* external approved datasets

---

## 3.2 Chunking Engine

Transforms documents into retrievable units.

Constraints:

* semantic boundaries preferred over fixed size
* structural integrity preserved (headings, code blocks, sections)
* overlap allowed but controlled

---

## 3.3 Embedding Layer

Converts chunks into vector representations.

Requirements:

* consistent embedding model per index
* versioned embeddings
* reproducible generation pipeline

---

## 3.4 Vector Index

Stores embeddings for retrieval.

Characteristics:

* partitioned by domain
* version-aware
* supports metadata filtering
* supports hybrid search (vector + keyword)

---

## 3.5 Retrieval Engine

Executes query-time search operations.

Responsible for:

* similarity search
* metadata filtering
* ranking
* deduplication

---

## 3.6 Reranking Layer

Applies secondary ranking signals:

* relevance scoring
* recency weighting
* trust scoring
* source authority weighting

---

## 3.7 Context Assembly Layer

Final stage before LLM consumption.

Produces a structured context bundle:

* ranked chunks
* source metadata
* compression output
* policy-filtered content

---

# 4. Pipeline Flow

```id="rag_flow_001"
Document → Ingestion → Chunking → Embedding → Indexing → Query → Retrieval → Rerank → Context Assembly → LLM
```

---

# 5. Chunking Rules

## 5.1 Semantic Integrity

Chunks must preserve:

* logical section boundaries
* code block integrity
* RFC/ADR structure

---

## 5.2 Chunk Size Constraints

* minimum size: context-aware (no fixed minimum)
* maximum size: bounded by embedding model limits
* overlapping chunks allowed for continuity

---

## 5.3 Metadata Attachment

Each chunk must include:

* source document ID
* section path
* version hash
* creation timestamp

---

# 6. Embedding Model Governance

## 6.1 Model Consistency

All embeddings in a single index must be generated using:

* the same model version
* the same preprocessing pipeline

---

## 6.2 Versioning Requirement

Embedding models must be versioned explicitly.

Any change requires:

* full re-indexing
* version migration tracking
* backward compatibility mapping

---

# 7. Index Design

## 7.1 Partitioning Strategy

Indexes are partitioned by:

* domain (architecture, security, runtime, etc.)
* document type (RFC, code, docs)
* sensitivity level

---

## 7.2 Hybrid Search Model

RAG supports:

* vector similarity search
* keyword search
* metadata filtering

Final ranking is a weighted combination.

---

# 8. Retrieval Model

## 8.1 Query Processing

Incoming query is transformed into:

* embedding vector
* keyword expansion set
* metadata filters

---

## 8.2 Candidate Selection

System retrieves top-k candidates from:

* vector index
* keyword index

---

## 8.3 Filtering Stage

Candidates are filtered based on:

* relevance threshold
* policy constraints
* domain restrictions
* trust scoring

---

## 8.4 Deduplication

Near-duplicate chunks are removed using:

* embedding similarity threshold
* structural hash comparison

---

# 9. Reranking Model

Reranking applies secondary scoring signals:

## 9.1 Signals

* semantic relevance score
* recency score
* source trust score
* structural importance score

---

## 9.2 Final Score

Final ranking is computed as:

```
Score = (Relevance × α) + (Recency × β) + (Trust × γ) + (Structure × δ)
```

Weights are system-defined per domain.

---

# 10. Context Assembly

## 10.1 Construction Rules

Final context must:

* respect token budget
* preserve highest-ranked sources
* maintain diversity of sources
* avoid redundancy

---

## 10.2 Compression Layer

When token limits are reached:

* lower-ranked chunks are summarized
* redundant sections are merged
* high-signal content is preserved verbatim where possible

---

## 10.3 Output Format

RAG output is structured as:

* ranked context blocks
* metadata headers
* source trace identifiers

---

# 11. Policy Integration

RAG output must pass through policy filtering:

* sensitive data filtering
* injection resistance filtering
* source trust validation
* domain restriction enforcement

---

# 12. Security Model

## 12.1 Injection Resistance

RAG must prevent:

* malicious document injection
* prompt injection embedded in documents
* context poisoning attacks

---

## 12.2 Trust Scoring

Each document source is assigned:

* trust score
* domain reliability rating
* verification status

Low-trust sources are deprioritized or excluded.

---

# 13. Failure Model

RAG system must handle:

* empty retrieval results
* embedding mismatch
* index corruption
* retrieval timeout
* ranking failure

Fallback behavior:

* degrade gracefully to partial context
* never inject unvalidated raw data

---

# 14. Observability

Every RAG operation must log:

* query vector hash
* retrieved chunk IDs
* ranking scores
* filtering decisions
* final context size
* token usage impact

---

# 15. Non-Goals

RAG is NOT:

* a reasoning engine
* a memory system
* a generative model
* a tool execution system

It is strictly a **retrieval and context assembly layer**.

---

# 16. System Invariants

RAG must always guarantee:

* no raw document injection without processing
* no unfiltered external data exposure
* no bypass of ranking/filtering stages
* full traceability of retrieved content
* versioned and reproducible retrieval outputs

---

# 17. Final Principle

RAG exists to ensure:

> The model never relies on internal memory for external truth. It always reasons over curated, traceable context.
