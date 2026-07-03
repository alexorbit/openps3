# runtime/TOOLING.md

Tooling & MCP Registry Specification — OpenPS3 Runtime

**Version:** 1.0

---

# 1. Purpose

This document defines the **Tooling System** of the OpenPS3 runtime.

It specifies how tools are:

* defined
* registered
* versioned
* exposed to agents
* executed via MCP
* governed across lifecycle stages

The Tooling System is the **authoritative registry layer for all executable capabilities**.

---

# 2. Core Principle

> No tool exists unless it is explicitly registered, versioned, and policy-approved.

There is no dynamic or implicit tool execution in OpenPS3.

---

# 3. System Architecture

The Tooling System is composed of four subsystems:

## 3.1 Tool Registry

Central catalog of all tools in the system.

Responsibilities:

* tool registration
* version tracking
* metadata storage
* capability indexing

---

## 3.2 Tool Schema Validator

Ensures all tools conform to MCP specification.

Validates:

* input schema
* output schema
* side-effect declarations
* risk classification
* determinism guarantees

---

## 3.3 Tool Execution Adapter

Bridges MCP execution requests to actual runtime execution.

Responsibilities:

* request normalization
* sandbox routing
* execution isolation
* result formatting

---

## 3.4 Tool Governance Layer

Enforces lifecycle policies:

* approval
* deprecation
* removal
* version upgrades

---

# 4. Tool Definition Model

Every tool must conform to the MCP schema:

```json id="tool_schema_001"
{
  "name": "string",
  "version": "semver",
  "description": "string",
  "input_schema": {},
  "output_schema": {},
  "auth_scope": "public | internal | restricted",
  "risk_level": "low | medium | high | critical",
  "side_effects": "none | limited | external",
  "determinism": "deterministic | non_deterministic"
}
```

---

# 5. Tool Lifecycle

## 5.1 Registration

Tools must be explicitly registered in the Tool Registry.

No exceptions.

---

## 5.2 Validation

Each tool must pass:

* schema validation
* security inspection
* sandbox compatibility check
* policy compliance validation

---

## 5.3 Activation

A tool becomes active only when:

* approved by governance layer
* validated by MCP policy engine
* version locked

---

## 5.4 Update

Tool updates follow strict versioning rules:

* backward-compatible changes → MINOR
* bug fixes → PATCH
* breaking changes → MAJOR

---

## 5.5 Deprecation

Deprecated tools:

* remain callable during transition period
* emit warnings in logs
* are removed after grace period expires

---

# 6. Execution Model

## 6.1 Execution Flow

```id="tool_flow_001"
Agent → MCP Router → Tool Registry → Policy Engine → Sandbox → Tool Execution → Response → Agent
```

---

## 6.2 Execution Constraints

Tools must execute under:

* isolated sandbox environment
* restricted system access
* no cross-tool memory sharing
* controlled I/O boundaries

---

## 6.3 Determinism Requirement

Tools must declare determinism:

* deterministic → same input = same output
* non_deterministic → external dependencies allowed

Non-deterministic tools require stricter policy enforcement.

---

# 7. Risk Model

Each tool must be classified:

## LOW

* pure computation
* no external I/O
* fully deterministic

---

## MEDIUM

* limited external API calls
* controlled data access

---

## HIGH

* network or filesystem access
* external system interaction

---

## CRITICAL

* system-level operations
* infrastructure modifications

---

# 8. Side Effect Model

Tools must declare side effects explicitly:

* NONE → no state change
* LIMITED → constrained internal change
* EXTERNAL → interacts with external systems

External side effects require elevated policy approval.

---

# 9. Security Model

## 9.1 Isolation Guarantees

Tool execution must guarantee:

* no cross-tool state leakage
* no sandbox escape paths
* no host system visibility
* no unauthorized persistence

---

## 9.2 Injection Resistance

Tooling system must defend against:

* parameter injection
* tool chaining abuse
* output-based prompt injection
* registry manipulation attempts

---

## 9.3 Execution Integrity

All tool executions must be:

* logged
* traceable
* reproducible
* auditable

---

# 10. Tool Composition Rules

Tools may NOT:

* invoke other tools implicitly
* modify registry at runtime
* bypass MCP policy engine
* execute uncontrolled recursion

Composition only occurs via MCP Router orchestration.

---

# 11. Versioning Strategy

All tools follow semantic versioning:

* MAJOR → breaking changes
* MINOR → backward-compatible features
* PATCH → fixes and patches

Production systems must pin tool versions explicitly.

---

# 12. Failure Model

Tooling system must handle:

* execution failure
* timeout
* schema mismatch
* sandbox crash
* policy rejection

Failures must:

* be structured
* be logged
* never propagate raw errors to agents

---

# 13. Observability

Each tool execution emits:

* tool_id
* version
* input hash
* output hash
* execution time
* policy decision
* sandbox trace ID

---

# 14. Registry Invariants

The Tool Registry must always guarantee:

* no unregistered tool execution
* no unvalidated schema execution
* no bypass of policy engine
* full version traceability
* deterministic registry state

---

# 15. Non-Goals

Tooling system is NOT:

* a reasoning engine
* a memory system
* a prompt system
* an orchestration layer

It is strictly a **controlled execution registry for external capabilities**.

---

# 16. Final Principle

The tooling layer ensures:

> No capability exists in the system unless it is explicitly defined, constrained, and governed.
