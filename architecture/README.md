# OpenPS3 System Architecture

**Version:** Draft 1.0
**Scope:** System-wide architecture specification

---

# 1. Architectural Overview

OpenPS3 is a modular system designed to reimplement the PlayStation®3 software stack using clean-room principles, focusing on correctness, reproducibility, and long-term maintainability.

The architecture is organized into layered subsystems that mirror the functional decomposition of a modern console operating system:

* Hardware Abstraction Layer (HAL)
* Kernel Core
* Hypervisor Layer (LV2 emulation boundary)
* System Services Layer
* Runtime & Application Layer
* Tooling & Development Layer

Each layer enforces strict dependency directionality.

---

# 2. Core Design Principles

## 2.1 Clean Layer Separation

No subsystem may bypass its architectural boundary.

* Upper layers may depend on lower layers
* Lower layers must not depend on upper layers

This constraint is non-negotiable.

---

## 2.2 Deterministic Behavior

All system components must aim for deterministic execution where hardware variability is abstracted away.

This includes:

* scheduling behavior
* memory allocation patterns (where possible)
* I/O sequencing
* system call semantics

---

## 2.3 Hardware Abstraction First

All hardware interaction must pass through HAL boundaries.

Direct hardware access from higher layers is forbidden.

---

## 2.4 Observable Behavior Matching

The system is defined by observable behavior, not internal implementation similarity.

Correctness is measured by:

* external API behavior
* system call semantics
* timing constraints (within defined tolerances)

---

## 2.5 Isolation by Design

Subsystems must be isolated such that:

* failure in one subsystem does not cascade unpredictably
* memory boundaries are strictly enforced
* privilege boundaries are explicit

---

# 3. System Layers

## 3.1 Hardware Layer (External)

The hardware layer includes:

* Cell Broadband Engine (PPE + SPEs)
* RSX GPU
* Memory architecture (XDR RAM + VRAM)
* I/O controllers

OpenPS3 does not reimplement hardware; it abstracts it.

---

## 3.2 Hardware Abstraction Layer (HAL)

### Responsibility

The HAL provides a normalized interface to hardware capabilities.

### Responsibilities include:

* CPU scheduling primitives
* memory mapping abstraction
* interrupt handling abstraction
* GPU command translation layer
* I/O device abstraction

### Constraints:

* HAL must not implement system policy
* HAL must remain stateless where possible

---

## 3.3 Kernel Core

The kernel is the central execution manager.

### Responsibilities:

* process scheduling
* memory management
* syscall dispatch
* permission enforcement
* inter-process communication (IPC)

### Constraints:

* must not depend on userland services
* must remain minimal and stable
* must not embed hardware-specific logic (delegated to HAL)

---

## 3.4 Hypervisor Layer (LV2 Boundary)

This layer models PS3 hypervisor behavior.

### Responsibilities:

* isolation of guest execution contexts
* privilege level enforcement
* system resource arbitration
* controlled access to privileged instructions

### Design Note:

This layer is critical for compatibility fidelity and must preserve strict behavioral equivalence with observed system behavior.

---

## 3.5 System Services Layer

System services provide OS-level functionality.

Examples:

* filesystem service
* networking stack
* package management system
* security services
* configuration management

### Constraints:

* must be replaceable without modifying kernel
* must communicate via defined IPC mechanisms

---

## 3.6 Runtime Layer

The runtime layer executes user applications.

### Responsibilities:

* application lifecycle management
* module loading
* memory sandboxing
* API exposure to applications

### Constraints:

* no privileged access to kernel or hypervisor
* all operations mediated by system services or syscalls

---

## 3.7 Tooling & Development Layer

This layer includes:

* SDK tooling
* debugging infrastructure
* emulation test harnesses
* build systems

It is not part of runtime execution but is essential for ecosystem development.

---

# 4. Subsystem Boundaries

Subsystems must conform to strict boundary rules:

## 4.1 Allowed Communication

* syscall interface (user → kernel)
* hypervisor calls (kernel → hypervisor)
* IPC channels (service ↔ service)
* HAL interfaces (kernel → hardware abstraction)

---

## 4.2 Forbidden Communication

* userland → hardware direct access
* service → kernel internal state access
* cross-layer circular dependencies

---

## 4.3 Interface Contracts

All cross-subsystem interactions must be defined via:

* explicit interface definitions
* versioned contracts
* documented invariants

---

# 5. Memory Architecture

## 5.1 Memory Model

OpenPS3 defines a unified logical memory model over:

* system RAM (XDR)
* video memory (VRAM)
* DMA-accessible regions

---

## 5.2 Memory Domains

Memory is partitioned into:

* Kernel space
* User space
* Hypervisor space
* Device-mapped regions

---

## 5.3 Isolation Rules

* user space cannot access kernel memory
* kernel may access user memory under controlled rules
* hypervisor has privileged access with strict auditing constraints

---

# 6. Execution Model

## 6.1 Process Model

The system uses a process abstraction with:

* isolated address spaces
* scheduled execution units
* explicit lifecycle states

---

## 6.2 Threading Model

Threads are managed by kernel scheduler and may map to:

* PPE threads
* SPE execution contexts
* virtualized execution units

---

## 6.3 Scheduling Policy

Scheduling is:

* preemptive
* priority-aware
* deterministic within defined constraints

---

# 7. I/O Architecture

## 7.1 Device Model

All devices are abstracted through HAL.

---

## 7.2 I/O Flow

Standard flow:

Application → System Service → Kernel → HAL → Hardware

Reverse flow applies for interrupts and responses.

---

## 7.3 Interrupt Handling

Interrupts are:

* normalized in HAL
* dispatched to kernel
* optionally routed to system services

---

# 8. Graphics Architecture

## 8.1 GPU Model

The RSX GPU is abstracted as a command-based rendering pipeline.

---

## 8.2 Command Flow

Application → Graphics API → Driver Layer → HAL → GPU

---

## 8.3 Constraints

* GPU state must be validated at boundaries
* no direct GPU memory manipulation from userland
* command buffers must be sanitized

---

# 9. Security Architecture

## 9.1 Privilege Levels

The system defines multiple privilege levels:

* User mode
* Kernel mode
* Hypervisor mode

---

## 9.2 Enforcement Model

Security enforcement is centralized in:

* kernel (policy enforcement)
* hypervisor (privilege isolation)

---

## 9.3 Threat Model

OpenPS3 assumes:

* untrusted userland code
* potentially malicious applications
* trusted kernel and hypervisor layers

---

# 10. Build and Deployment Architecture

## 10.1 Build System

The system must support:

* reproducible builds
* cross-compilation
* deterministic artifact generation

---

## 10.2 Artifact Types

* kernel images
* system services binaries
* runtime packages
* tooling SDKs

---

## 10.3 Version Alignment

All artifacts must align with:

* semantic versioning rules
* dependency compatibility constraints

---

# 11. System Invariants

The following invariants must always hold:

* no circular dependency between layers
* kernel remains minimal and stable
* hypervisor boundary remains strict
* HAL remains hardware-only abstraction
* userland remains unprivileged
* all cross-layer communication is explicit

---

# 12. Architectural Evolution

Architecture evolves exclusively through:

* RFC process (primary mechanism)
* ADR records (final state documentation)

No implicit architectural changes are permitted.

---

# 13. Final Principle

OpenPS3 architecture is designed for:

* correctness over emulation shortcuts
* clarity over performance hacks
* long-term maintainability over short-term completeness

The system must remain structurally understandable to future engineers without reliance on undocumented behavior.
