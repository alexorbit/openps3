# AI_SYSTEM.md

OpenPS3 Runtime — Agent, RAG & MCP System Specification

**Version:** 1.0

---

# 1. System Overview

The OpenPS3 AI Runtime defines a controlled execution environment for LLM-based agents.

It is not a chatbot framework.

It is a **deterministic orchestration layer for AI execution units**.

The system integrates three core subsystems:

* Agent Runtime Engine
* RAG Context System
* MCP Tool Execution Layer

---

# 2. Core Architecture

The runtime is composed of four layers:

## 2.1 Agent Runtime Layer

Responsible for execution lifecycle:

* request parsing
* orchestration loop
* state transitions
* tool invocation
* response synthesis

---

## 2.2 LLM Interface Layer

Abstracts model execution:

* prompt assembly
* context injection
* token management
* structured output enforcement

No direct model calls outside this layer are allowed.

---

## 2.3 RAG System Layer

Provides external knowledge injection:

* document indexing
* embedding generation
* retrieval pipeline
* ranking and filtering
* context compression

---

## 2.4 MCP Tool Layer

Handles external tool execution:

* tool registry
* schema validation
* execution sandboxing
* policy enforcement

---

# 3. Entry Point

All agent execution flows begin from a single controlled entry point:

```
POST /runtime/agent/execute
```

---

## 3.1 Request Schema

```json id="entry_schema_001"
{
  "agent_id": "string",
  "input": "string",
  "context": {
    "session_id": "string",
    "user_id": "string",
    "metadata": {}
  },
  "tools": [],
  "mode": "strict | balanced | experimental"
}
```

---

## 3.2 Execution Flow

1. Input validation
2. Policy evaluation (guardrails)
3. RAG context assembly
4. MCP tool resolution
5. Prompt construction
6. LLM execution
7. Output validation
8. Tool execution (if required)
9. Final response normalization

---

# 4. Agent Model

Agents are defined as execution configurations:

* system prompt (policy-bound)
* tool permissions
* memory scope
* RAG scope
* safety mode

---

## 4.1 Agent Categories

### System Agents

* infrastructure control
* no external tool execution unless explicitly enabled

### Domain Agents

* specialized reasoning (security, architecture, etc.)

### User Agents

* interactive assistants
* strict guardrails enabled

### Autonomous Agents

* background execution
* scheduled tasks
* sandboxed environment

---

# 5. RAG Architecture

## 5.1 Pipeline

```
Ingestion → Chunking → Embedding → Index → Retrieval → Rerank → Context Assembly
```

---

## 5.2 Retrieval Rules

* semantic similarity primary signal
* recency weighting secondary signal
* trust score filtering mandatory
* deduplication required

---

## 5.3 Context Construction

Final context is constructed using:

* top-k retrieval
* diversity sampling
* compression layer
* policy filtering layer

---

# 6. MCP Integration

MCP is the execution boundary between agents and external systems.

It enforces:

* schema validation
* permission checks
* sandbox execution
* output normalization

No tool executes outside MCP.

---

# 7. Guardrails System

Guardrails operate in four phases:

## 7.1 Input Layer

* schema validation
* injection filtering

## 7.2 Context Layer

* RAG sanitization
* source validation

## 7.3 Execution Layer

* tool permission enforcement
* model instruction hierarchy enforcement

## 7.4 Output Layer

* structured output validation
* policy compliance check

---

# 8. Memory System

Memory is strictly scoped:

* session memory (ephemeral)
* agent memory (persistent scoped)
* system memory (restricted global state)

Memory is not raw storage — it is filtered abstraction.

---

# 9. Observability

Every execution must emit:

* trace_id
* tool calls
* RAG sources
* policy decisions
* token usage
* execution timeline

---

# 10. System Invariants

The runtime must guarantee:

* no tool execution outside MCP
* no unvalidated LLM output execution
* no memory leakage across scopes
* no bypass of guardrails layer
* full traceability of all decisions

---

# 11. Design Principle

Agents are not autonomous entities.

They are **controlled execution units inside a constrained system governed by policy, tools, and context**.
