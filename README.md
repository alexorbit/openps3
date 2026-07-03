# OpenPS3

> **An open platform for the PlayStation®3.**
>
> Preserving hardware. Advancing knowledge. Building the future.

---

## Overview

OpenPS3 is an open-source initiative to transform the PlayStation 3 into a fully documented, community-driven computing platform.

Rather than extending the life of proprietary firmware, OpenPS3 seeks to establish an independent ecosystem for software development, hardware preservation, research, and education.

The project is built on open specifications, modular architecture, and long-term maintainability.

Our objective is simple:

**Ensure that one of the most ambitious computing platforms ever created remains useful for decades to come.**

---

## Why OpenPS3?

Commercial support for the PlayStation 3 is gradually coming to an end.

Online services evolve.

Digital storefronts close.

Infrastructure disappears.

Hardware, however, continues to function.

OpenPS3 exists to preserve that hardware by creating an open software platform that is independent of proprietary services while remaining focused on legitimate software development, research, and preservation.

---

## Vision

OpenPS3 aims to become for the PlayStation 3 what projects such as Coreboot, OpenWrt, ReactOS and Haiku became for their respective ecosystems:

* A long-term engineering project
* A fully documented platform
* A community-driven ecosystem
* A reference implementation built on open specifications

---

## Project Principles

OpenPS3 is built upon seven principles:

* **Freedom** — Users should control the hardware they own.
* **Preservation** — Digital preservation is cultural preservation.
* **Transparency** — Every subsystem should be documented.
* **Engineering Excellence** — Architecture before implementation.
* **Modularity** — Components should evolve independently.
* **Community** — Knowledge belongs to everyone.
* **Longevity** — Build software that survives decades.

---

## Project Structure

```text
openps3/

├── openps3-foundation/
├── governance/
├── pps/
├── aps/
├── adr/
├── rfc/
├── boot/
├── kernel/
├── hal/
├── drivers/
├── runtime/
├── shell/
├── sdk/
├── toolchain/
├── pkg/
├── registry/
├── apps/
├── examples/
├── tests/
└── branding/
```

Each repository or module has a clearly defined purpose and an independent lifecycle.

---

## Documentation

The project documentation is divided into four primary collections.

### PPS — PlayStation Platform Specification

Documents describing the PlayStation 3 hardware.

Examples:

* Boot architecture
* Cell processor
* RSX graphics processor
* Hypervisor
* Memory map
* Storage
* Networking

The PPS documents describe the hardware.

---

### APS — Architecture Specifications

Documents describing OpenPS3 itself.

Examples:

* Kernel architecture
* Driver model
* Runtime
* Filesystem
* Package manager
* Security model

The APS documents describe the software architecture.

---

### ADR — Architecture Decision Records

Permanent records explaining major engineering decisions.

Every important design choice is documented.

---

### RFC — Requests for Comments

Large engineering proposals are discussed publicly before implementation.

Architecture evolves through technical consensus.

---

## Development Status

Current phase:

**Research & Platform Specification**

The project is currently focused on:

* hardware documentation
* reverse engineering
* architecture design
* specification writing
* repository organization

Implementation follows only after the architecture reaches sufficient maturity.

---

## Repository Roadmap

```
Research
    ↓
Specifications
    ↓
Architecture
    ↓
Boot Prototype
    ↓
Kernel
    ↓
Drivers
    ↓
Runtime
    ↓
Shell
    ↓
SDK
    ↓
Package Ecosystem
    ↓
Version 1.0
```

---

## Licensing

OpenPS3 uses multiple licenses according to component responsibilities.

| Component      | License          |
| -------------- | ---------------- |
| Specifications | CC BY 4.0        |
| Documentation  | CC BY 4.0        |
| Boot           | MPL 2.0          |
| Kernel         | MPL 2.0          |
| HAL            | MPL 2.0          |
| Drivers        | MPL 2.0          |
| Runtime        | Apache 2.0       |
| SDK            | Apache 2.0       |
| Toolchain      | Apache 2.0       |
| Applications   | MIT              |
| Branding       | Trademark Policy |

See each repository for its specific license.

---

## Contributing

OpenPS3 welcomes engineers, researchers, reverse engineers, technical writers, designers, testers, and educators.

Before contributing, please read:

* CONTRIBUTING.md
* CODE_OF_CONDUCT.md
* SECURITY.md

Architecture discussions should begin as RFCs whenever they affect public interfaces or system design.

---

## Project Philosophy

OpenPS3 follows one simple rule:

> **Specifications before implementation.**

Code can always be rewritten.

Knowledge cannot.

Our first objective is to preserve knowledge.

Software follows.

---

## Community

We believe the future of legacy hardware depends on open collaboration.

Every verified experiment.

Every documented interface.

Every recovered register.

Every architectural insight.

Each contribution becomes part of a permanent public knowledge base.

---

## Disclaimer

OpenPS3 is an independent open-source project.

It is not affiliated with, endorsed by, sponsored by, or associated with Sony Group Corporation or Sony Interactive Entertainment.

"PlayStation" and "PS3" are trademarks of their respective owners and are referenced solely for compatibility and identification purposes.

---

## Building the Future

OpenPS3 is more than a firmware project.

It is an engineering effort to preserve one of the most remarkable computing platforms ever built.

If you believe hardware should outlive corporate support,

**welcome to OpenPS3.**
