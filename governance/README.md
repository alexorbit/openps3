# GOVERNANCE.md

# OpenPS3 Governance

**Version:** Draft 1.0

---

# 1. Preamble

OpenPS3 is established as an independent, community-driven, open-source initiative dedicated to researching, documenting, preserving, and reimplementing the software ecosystem of the PlayStation®3 through clean-room engineering practices.

This document defines the constitutional framework governing the OpenPS3 project.

Its purpose is to ensure that the project remains transparent, technically rigorous, legally responsible, vendor-neutral, and sustainable regardless of future contributors, maintainers, sponsors, or organizations involved in its development.

Unlike traditional software projects centered around a single company or individual, OpenPS3 is intended to become a long-lived public infrastructure project whose governance prioritizes continuity over personalities.

No contributor—including founders, maintainers, sponsors, or future organizations—owns the project itself.

Every participant serves the project rather than controls it.

The governance described here exists to preserve that principle.

---

# 2. Mission and Purpose

OpenPS3 exists to build a fully open implementation of the PlayStation®3 firmware stack while respecting intellectual property law and software preservation principles.

The project seeks to:

* develop an original firmware implementation through clean-room engineering;
* document undocumented hardware and system behavior;
* preserve technical knowledge that would otherwise disappear;
* enable research, education, interoperability, and experimentation;
* provide a sustainable foundation for future development;
* encourage collaboration between reverse engineers, systems programmers, emulator developers, hardware researchers, and security researchers;
* promote transparency in all technical decisions.

The project does **not** exist to facilitate software piracy, copyright infringement, circumvention of digital rights management for unlawful purposes, or unauthorized distribution of proprietary software.

OpenPS3 shall always distinguish legitimate interoperability research from activities that violate applicable laws.

---

# 3. Guiding Principles

Every decision made within OpenPS3 should align with the following principles.

## 3.1 Legality

The project shall operate under applicable intellectual property laws.

All code contributed to OpenPS3 must be original work or legally compatible open-source software.

No proprietary Sony source code may ever enter the repository.

No confidential documentation may be committed.

No contributor may intentionally contaminate the project with copyrighted implementation code.

---

## 3.2 Clean-Room Engineering

Whenever proprietary behavior must be reproduced, OpenPS3 shall follow clean-room engineering principles.

Whenever practical:

* specification authors should be separated from implementers;
* documentation should describe observable behavior rather than copied implementation;
* implementations should be based on independently produced specifications.

The integrity of the clean-room process takes precedence over development speed.

---

## 3.3 Transparency

Project governance shall be conducted in public whenever legally possible.

This includes:

* architectural discussions;
* RFC reviews;
* roadmap planning;
* governance changes;
* technical decisions;
* release planning.

Private discussions should only occur when necessary for:

* responsible security disclosure;
* legal matters;
* personal privacy;
* confidential vulnerability coordination.

---

## 3.4 Technical Excellence

OpenPS3 values correctness over velocity.

Every subsystem should favor:

* deterministic behavior;
* reproducibility;
* maintainability;
* comprehensive documentation;
* long-term stability.

Engineering shortcuts that introduce technical debt without compelling justification should be avoided.

---

## 3.5 Meritocracy with Accountability

Influence within the project is earned through sustained, high-quality contributions.

However, increased authority also carries increased responsibility.

Maintainers and committee members are expected to:

* review objectively;
* mentor contributors;
* document decisions;
* communicate respectfully;
* place project interests above personal preferences.

Authority exists to serve the community—not the reverse.

---

## 3.6 Vendor Neutrality

OpenPS3 shall remain independent from any commercial entity.

Organizations may contribute resources, funding, infrastructure, or engineering effort.

No organization shall obtain privileged control over:

* governance;
* technical direction;
* release schedules;
* project ownership.

Commercial participation is welcome.

Commercial control is not.

---

## 3.7 Long-Term Preservation

OpenPS3 recognizes software preservation as a public good.

Every design decision should consider whether future developers—possibly decades from now—will be able to understand, reproduce, and extend the project.

Documentation is therefore considered a first-class engineering artifact.

---

# 4. Governance Philosophy

OpenPS3 follows a governance model built upon five foundational concepts.

## 4.1 Community First

The community is the primary stakeholder.

Infrastructure, repositories, documentation, and decision-making processes exist for the benefit of the project rather than individual contributors.

---

## 4.2 Consensus Whenever Possible

Consensus produces better long-term decisions than authority alone.

Discussion should continue until technical concerns have been adequately explored.

Voting should be considered a mechanism of last resort rather than the default process.

---

## 4.3 Explicit Decision Records

Significant technical decisions shall be documented.

Whenever architectural choices materially affect the project, corresponding Architecture Decision Records (ADRs) should be created.

Historical context is considered valuable engineering documentation.

---

## 4.4 Stable Institutions over Individuals

No single contributor should become indispensable.

Project responsibilities should always be transferable.

Institutional knowledge must reside in documentation rather than personal memory.

Succession planning is considered an essential governance responsibility.

---

## 4.5 Evolution Without Instability

Governance must evolve alongside the project.

However, governance changes should occur deliberately, transparently, and conservatively.

Frequent structural changes create unnecessary uncertainty.

Stability is preferred unless clear improvements justify modification.

---

# 5. Scope of This Document

This governance document defines:

* project institutions;
* decision-making authority;
* contributor roles;
* technical governance;
* release governance;
* security governance;
* conflict resolution;
* amendment procedures;
* long-term project continuity.

Individual technical repositories may define additional operating procedures.

However, no repository-specific policy may conflict with this governance document.

In the event of conflict, this document takes precedence.

---

# 6. Governance Hierarchy

Governance within OpenPS3 is organized in descending order of authority:

1. Governance Charter (this document)
2. Project Policies
3. Technical Steering Committee decisions
4. Approved RFCs
5. Architecture Decision Records
6. Repository-level contribution guides
7. Maintainer operational practices

Lower-level documents must never contradict higher-level governance.

Whenever inconsistencies arise, higher-order governance prevails until formally amended.
