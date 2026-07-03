# runtime/MCP_SPEC.md

Model Context Protocol — OpenPS3 Runtime Specification

**Version:** 1.0

---

# 1. Purpose

This document defines the Model Context Protocol (MCP) used by the OpenPS3 runtime system.

MCP is the **strict execution boundary** between:

* AI Agents
* External Tools
* Execution Sandboxes
* Policy Enforcement Layer

Its role is to ensure that all tool interactions are:

* schema-validated
* policy-approved
* sandbox-executed
* fully traceable

---

# 2. Core Principle

> No external capability is accessible without explicit MCP mediation.

MCP is the only valid execution channel for tools.

No exceptions exist.

---

# 3. System Architecture

MCP consists of four core components:

## 3.1 Tool Registry

Central repository of all available tools.

Each tool is:

* versioned
* schema-defined
* permission-scoped
* risk-classified

No tool exists outside the registry.

---

## 3.2 MCP Router

Responsible for routing tool execution requests.

Functions:

* tool resolution
* version selection
* capability matching
* request normalization

---

## 3.3 Execution Sandbox

Isolated environment where tools execute.

Constraints:

* no persistent state unless explicitly defined
* no cross-tool memory sharing
* restricted I/O access
* no host system visibility

---

## 3.4 Policy Engine

Evaluates whether execution is allowed.

It enforces:

* agent permissions
* tool risk level
* system safety mode
* contextual constraints
* runtime restrictions

---

# 4. Tool Definition Model

Every MCP tool must strictly conform to this schema:

```json id="mcp_tool_schema"
{
  "name": "string",
  "version": "semver",
  "description": "string",
  "input_schema": {
    "type": "object",
    "properties": {},
    "required": []
  },
  "output_schema": {
    "type": "object"
  },
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

No dynamic or implicit registration is allowed.

---

## 5.2 Validation

Before activation, tools must pass:

* schema validation
* security inspection
* sandbox compatibility check
* policy compliance check

---

## 5.3 Activation

A tool becomes active only after:

* registry approval
* policy engine validation
* version lock confirmation

---

## 5.4 Deprecation

Deprecated tools:

* remain callable during transition period
* emit structured warnings
* are removed after defined grace period

---

# 6. Execution Model

## 6.1 Execution Flow

```id="mcp_flow_001"
Agent → MCP Router → Policy Engine → Sandbox → Tool → Sandbox → Response → Agent
```

---

## 6.2 Execution Stages

### Stage 1 — Request Formation

Agent generates structured tool invocation request.

---

### Stage 2 — Validation

MCP validates:

* schema correctness
* tool existence
* parameter integrity

---

### Stage 3 — Policy Evaluation

Policy engine checks:

* agent permissions
* tool risk level
* system safety mode
* contextual restrictions

---

### Stage 4 — Sandbox Execution

Tool runs in isolated environment.

Constraints:

* no external system access unless explicitly allowed
* no shared memory
* controlled runtime environment

---

### Stage 5 — Output Validation

Tool output is validated against schema before returning.

---

# 7. Permission Model

## 7.1 Hierarchical Access Control

Permissions are evaluated across:

* system level
* agent level
* tool level
* execution context

---

## 7.2 Execution Rules

A tool executes only if:

* agent is authorized
* tool is enabled in current safety mode
* policy engine approves execution
* no contextual violations exist

---

# 8. Risk Classification

Each tool is assigned a risk level:

## LOW

* pure computation
* no external I/O
* deterministic execution

## MEDIUM

* controlled external API usage
* limited I/O

## HIGH

* external systems interaction
* network or filesystem access

## CRITICAL

* privileged system operations
* infrastructure-level impact

---

# 9. Side Effect Model

Tools must declare side effect behavior:

* NONE → pure functions
* LIMITED → constrained internal effects
* EXTERNAL → interacts with external systems

External side effects require elevated policy checks.

---

# 10. Security Model

## 10.1 Isolation Guarantees

MCP enforces:

* no cross-tool contamination
* no state leakage
* no privilege escalation
* no sandbox escape paths

---

## 10.2 Injection Resistance

MCP must prevent:

* prompt injection via tool outputs
* parameter tampering
* context poisoning
* chained tool abuse

---

## 10.3 Execution Integrity

All executions must be:

* logged
* traceable
* reproducible
* auditable

---

# 11. Tool Composition Rules

Tools must NOT:

* invoke other tools implicitly
* modify registry state at runtime
* bypass policy engine
* execute uncontrolled recursive chains

Composition is only allowed via MCP Router orchestration.

---

# 12. Versioning Strategy

MCP tools follow semantic versioning:

* MAJOR → breaking changes
* MINOR → backward-compatible features
* PATCH → fixes

Production agents must pin tool versions.

---

# 13. Failure Model

MCP must handle:

* tool failure
* timeout
* schema mismatch
* policy rejection
* sandbox error

All failures must:

* be structured
* be logged
* never propagate raw to agent output

---

# 14. Observability

Each execution emits:

* tool_id
* version
* input hash
* output hash
* policy decision
* execution time
* sandbox trace ID

---

# 15. Non-Goals

MCP is NOT:

* a reasoning framework
* a prompt system
* a memory system
* an LLM orchestration layer

It is strictly a **tool execution protocol**.

---

# 16. System Invariants

The system must guarantee:

* no execution outside registry
* no tool call without policy approval
* no output bypassing validation
* no sandbox escape possible by design
* full traceability of execution chain

---

# 17. Final Principle

MCP enforces a strict separation:

> Agents decide *what to do*. MCP defines *what is possible to execute*.

This boundary is fundamental to system safety, determinism, and scalability.
