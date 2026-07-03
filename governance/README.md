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

# 6. OpenPS3 Foundation

The OpenPS3 Foundation is the legal and organizational anchor of the project.

It exists to provide continuity, infrastructure stewardship, and legal protection for the OpenPS3 ecosystem without exerting unilateral technical control over the project.

## 6.1 Role and Scope

The Foundation is responsible for:

* holding project trademarks (if registered);
* maintaining legal ownership of core infrastructure assets (domains, CI systems, build infrastructure);
* coordinating funding and grants when applicable;
* ensuring compliance with applicable laws and regulations;
* providing neutral infrastructure hosting for repositories and services;
* supporting long-term continuity in case of leadership turnover.

The Foundation does **not** control technical direction.

It has no authority over:

* architectural decisions;
* code acceptance/rejection;
* roadmap definition;
* release approval;
* RFC approval.

Technical authority is explicitly delegated to the Technical Steering Committee.

---

## 6.2 Neutrality Constraint

The Foundation must remain structurally neutral.

It may not privilege any company, individual, or subgroup within the project.

Any attempt by external organizations to capture or dominate the Foundation must be considered a governance failure and addressed through the conflict resolution process defined later in this document.

---

## 6.3 Governance Interface

The Foundation interacts with the technical project only through formal interfaces:

* Technical Steering Committee reports
* Public RFC outcomes
* Release reports
* Security advisories

Informal or private technical influence is not permitted.

---

## 6.4 Financial Stewardship

If the project receives funding, the Foundation acts as custodian of resources.

Funds may only be allocated to:

* infrastructure costs (CI, hosting, storage);
* security audits;
* documentation initiatives;
* community grants;
* operational continuity.

Financial transparency is required on a periodic basis.

---

# 7. Technical Steering Committee (TSC)

The Technical Steering Committee is the highest technical authority in OpenPS3.

It governs architectural direction, release approvals, and resolution of technical disputes.

---

## 7.1 Mandate

The TSC is responsible for:

* approving or rejecting RFCs;
* defining project-wide technical architecture;
* resolving cross-repository conflicts;
* setting release criteria and schedules;
* ensuring consistency across subsystems;
* appointing and removing maintainers (via documented process);
* overseeing technical health of the project.

---

## 7.2 Composition

The TSC is composed of senior contributors with sustained, high-impact contributions across multiple subsystems.

Membership is:

* merit-based;
* time-bound or periodically reviewed;
* subject to renewal based on contribution quality and activity.

No single organization may hold majority control of the TSC.

---

## 7.3 Decision-Making

The TSC prefers consensus.

When consensus cannot be reached:

* formal voting is used;
* simple majority is sufficient unless otherwise defined by policy;
* dissenting opinions must be documented.

Decisions must always be recorded in public logs.

---

## 7.4 Accountability

TSC members are accountable to:

* the governance document;
* public technical review;
* maintainers and contributors;
* project principles defined in Section 3.

TSC members may be removed for:

* prolonged inactivity;
* repeated disregard of governance;
* conflict of interest violations;
* abusive behavior;
* failure to fulfill responsibilities.

---

# 8. Working Groups

Working Groups (WGs) are semi-autonomous technical units focused on specific domains of the OpenPS3 ecosystem.

---

## 8.1 Purpose

Working Groups exist to:

* divide complex system domains into manageable units;
* increase specialization;
* improve engineering efficiency;
* distribute decision-making responsibility.

---

## 8.2 Examples of Working Groups

Typical WGs may include:

* Kernel / System Core WG
* Hypervisor Emulation WG
* Filesystem & Storage WG
* Graphics Pipeline WG
* Networking WG
* Toolchain & Build Systems WG
* Documentation & Specification WG
* Security & Audit WG

---

## 8.3 Authority

Working Groups:

* propose RFCs;
* implement approved designs;
* maintain subsystem codebases;
* manage internal technical discussions.

However, they do not override:

* TSC decisions;
* governance document;
* project-wide architecture constraints.

---

## 8.4 Leadership

Each Working Group has one or more maintainers responsible for:

* coordinating contributors;
* ensuring quality of changes;
* representing WG concerns in TSC discussions;
* maintaining documentation accuracy.

WG leads are appointed by the TSC and may be replaced through formal review.

---

# 9. Maintainers

Maintainers are responsible for the long-term health of specific repositories or subsystems.

---

## 9.1 Responsibilities

Maintainers:

* review and merge contributions;
* enforce coding standards;
* ensure tests and CI integrity;
* maintain repository documentation;
* participate in RFC evaluation;
* guide contributors.

---

## 9.2 Authority Boundaries

Maintainers may:

* approve changes within their scope;
* reject contributions that violate technical or governance rules;
* request modifications for quality or consistency.

Maintainers may NOT:

* override governance decisions;
* introduce breaking architectural changes without RFC approval;
* act outside their assigned scope.

---

## 9.3 Appointment

Maintainers are appointed based on:

* sustained contribution quality;
* domain expertise;
* demonstrated judgment in reviews;
* community trust.

Appointment is confirmed by the TSC.

---

## 9.4 Removal

Maintainers may be removed for:

* inactivity;
* repeated poor review quality;
* violation of governance principles;
* abuse of authority;
* loss of trust.

Removal requires documented rationale.

---

# 10. Committers

Committers are contributors with write access to one or more repositories.

---

## 10.1 Scope

Commit access is:

* scoped per repository;
* not global by default;
* revocable.

---

## 10.2 Responsibilities

Committers must:

* adhere to contribution guidelines;
* ensure correctness of committed code;
* respect maintainer review processes;
* avoid bypassing CI or review systems.

---

## 10.3 Safety Requirements

Direct commits must not:

* bypass required reviews;
* introduce unreviewed architectural changes;
* violate security constraints.

---

# 11. Contributors

Contributors are any individuals participating in the project without elevated privileges.

---

## 11.1 Rights

Contributors may:

* submit pull requests;
* open issues;
* propose RFCs;
* participate in discussions;
* review public changes.

---

## 11.2 Responsibilities

Contributors are expected to:

* follow contribution guidelines;
* respect clean-room constraints;
* maintain professional conduct;
* ensure originality of contributions.

---

## 11.3 Contribution Merit

Contributor reputation is established through:

* code quality;
* consistency;
* review participation;
* technical depth;
* adherence to governance principles.

---

# 12. Role Lifecycle

All roles within OpenPS3 follow a lifecycle model.

---

## 12.1 Promotion

Advancement (Contributor → Committer → Maintainer → TSC) is based on:

* sustained contribution history;
* technical expertise;
* trust and review reliability;
* community impact.

---

## 12.2 Suspension

Roles may be temporarily suspended due to:

* security concerns;
* investigation of governance violations;
* inactivity.

---

## 12.3 Removal

Permanent removal may occur for:

* repeated governance violations;
* malicious behavior;
* abandonment;
* conflict of interest abuse.

All removals must be documented.

---

## 12.4 Succession

No role is permanent.

All responsibilities must be transferable.

Succession planning is mandatory for maintainers and TSC members.

---

# 13. Structural Integrity Rule

No individual, organization, or subgroup may accumulate irreversible control over the project.

Any structural drift toward centralized control must trigger governance review.

The long-term integrity of the governance model takes precedence over short-term efficiency gains.

# 14. Decision-Making Process

OpenPS3 adopts a hybrid decision-making model combining consensus-driven discussion with structured escalation mechanisms.

The objective is to maximize technical correctness while preserving decision velocity.

---

## 14.1 Default Model: Consensus

All non-trivial decisions should begin with consensus-seeking discussion.

Consensus is defined as:

> a state in which no qualified participant maintains a sustained, technically justified objection.

Consensus does not require unanimity of preference, but it requires absence of unresolved technical blocking concerns.

---

## 14.2 Scope of Consensus

Consensus is required for:

* architectural changes;
* cross-subsystem interfaces;
* kernel or hypervisor modifications;
* changes to governance rules;
* release criteria modifications;
* security model changes.

Operational or localized changes may bypass consensus if they remain within maintainer authority.

---

## 14.3 Escalation to Voting

If consensus cannot be reached within a reasonable timeframe, the issue escalates to formal voting.

Voting is used only when:

* discussion has stabilized without resolution;
* technical positions are well-documented;
* further debate is unlikely to change outcomes.

---

## 14.4 Voting Mechanics

Unless otherwise specified:

* each eligible TSC member has one vote;
* majority rule applies (>50%);
* abstentions do not count toward the total.

In case of tie:

* the proposal is rejected unless a designated tie-breaking mechanism is defined for that domain.

---

## 14.5 Blocking vs Non-Blocking Objections

Objections are categorized as:

### Blocking Objection

A blocking objection must be:

* technically substantiated;
* relevant to system correctness, security, or architecture;
* within scope of governance authority.

Blocking objections prevent adoption until resolved or overridden by vote.

### Non-Blocking Objection

Non-blocking objections may include:

* stylistic concerns;
* performance optimizations without correctness impact;
* subjective preferences.

Non-blocking objections do not prevent progress.

---

## 14.6 Documentation Requirement

All final decisions must be documented in at least one of:

* RFC record;
* ADR record;
* release notes (for operational decisions).

Undocumented decisions are considered invalid within governance scope.

---

# 15. RFC Process (Request for Comments)

The RFC process is the primary mechanism for introducing significant changes into OpenPS3.

---

## 15.1 Purpose

RFCs exist to:

* formalize technical proposals;
* enable structured review;
* preserve architectural history;
* ensure cross-team alignment.

---

## 15.2 When RFCs Are Required

An RFC is required when a proposal:

* modifies system architecture;
* introduces new subsystems;
* changes public APIs or interfaces;
* alters security model;
* impacts multiple working groups;
* affects release strategy or compatibility guarantees.

---

## 15.3 RFC Lifecycle

Each RFC follows a defined lifecycle:

### 1. Draft

Initial proposal written by contributor or working group.

### 2. Discussion

Public review phase with technical feedback.

### 3. Revision

RFC updated based on feedback.

### 4. Review

TSC and maintainers perform formal evaluation.

### 5. Decision

Approved, rejected, or deferred.

### 6. Implementation

If approved, implementation proceeds under tracked issue.

### 7. Finalization

RFC is marked as active specification or archived.

---

## 15.4 RFC Structure

Every RFC must include:

* Summary
* Motivation
* Technical Design
* Alternatives Considered
* Backward Compatibility Impact
* Security Considerations
* Implementation Plan
* Open Questions

---

## 15.5 RFC Authority

RFCs are not binding until approved.

Approval requires:

* TSC consensus or vote;
* confirmation of feasibility;
* alignment with governance principles.

---

## 15.6 RFC Rejection

RFCs may be rejected due to:

* architectural inconsistency;
* insufficient justification;
* security risks;
* redundancy;
* maintenance burden.

Rejected RFCs must include rationale.

---

# 16. ADR Policy (Architecture Decision Records)

ADR documents capture irreversible or semi-permanent technical decisions.

---

## 16.1 Purpose

ADRs serve to:

* document architectural reasoning;
* provide historical context;
* prevent repeated debates;
* guide future implementations.

---

## 16.2 Scope

ADRs are required for decisions that:

* cannot be trivially reversed;
* define system structure;
* introduce core abstractions;
* impact long-term maintenance.

---

## 16.3 ADR Format

Each ADR must include:

* Title
* Status (Proposed / Accepted / Deprecated / Superseded)
* Context
* Decision
* Consequences
* Rationale
* References

---

## 16.4 ADR Immutability

Once accepted, ADRs are immutable records.

If a decision changes:

* a new ADR must be created;
* the previous ADR is marked "Superseded";
* linkage between versions must be preserved.

---

## 16.5 Relationship with RFCs

* RFCs propose changes.
* ADRs record accepted outcomes.

Not all RFCs result in ADRs, but all ADR-level decisions must originate from RFC or equivalent formal review.

---

# 17. Release Governance

Release governance defines how OpenPS3 produces stable and versioned outputs.

---

## 17.1 Release Philosophy

Releases prioritize:

* stability over frequency;
* reproducibility over experimentation;
* correctness over feature completeness.

---

## 17.2 Release Types

### Major Release

* architectural changes
* potential incompatibilities
* RFC-driven

### Minor Release

* backward-compatible features
* subsystem improvements

### Patch Release

* bug fixes
* security patches
* minimal risk changes

---

## 17.3 Release Criteria

A release may only proceed when:

* CI is green across all core subsystems;
* no unresolved blocking security issues exist;
* documentation is updated for public interfaces;
* maintainers approve subsystem readiness;
* TSC confirms release integrity.

---

## 17.4 Release Ownership

Each release has a designated Release Maintainer responsible for:

* coordinating release timeline;
* ensuring readiness of components;
* signing off on release candidate builds;
* publishing release artifacts.

---

## 17.5 Release Candidate Process

Before final release:

1. Release Candidate (RC) is generated
2. Testing phase begins (internal + community)
3. Issues are triaged and fixed
4. RC iterations continue until stable
5. Final release is signed off

---

## 17.6 Rollback Policy

If a release introduces critical regressions:

* immediate patch release is prioritized;
* rollback builds may be issued;
* affected components may be temporarily disabled.

---

## 17.7 Versioning Scheme

OpenPS3 uses semantic versioning:

* MAJOR.MINOR.PATCH

Additional suffixes may include:

* -rc (release candidate)
* -beta (pre-release testing)
* -alpha (experimental builds)

---

# 18. Security Governance

Security governance ensures that OpenPS3 maintains a defensible security posture.

---

## 18.1 Security Principles

* security is a first-class design constraint;
* vulnerabilities are treated as systemic issues;
* disclosure is handled responsibly;
* fixes take priority over feature work.

---

## 18.2 Security Working Group

A dedicated Security WG is responsible for:

* vulnerability assessment;
* threat modeling;
* audit coordination;
* security RFC review;
* incident response.

---

## 18.3 Vulnerability Handling

When a vulnerability is identified:

1. Private report is submitted
2. Security WG validates issue
3. Fix is developed in private branch if necessary
4. Patch is prepared
5. Coordinated disclosure occurs
6. Public advisory is published

---

## 18.4 Disclosure Policy

Disclosure must balance:

* user protection;
* system stability;
* responsible publication of security information.

Immediate disclosure is required for actively exploited vulnerabilities.

---

## 18.5 Security Boundaries

OpenPS3 explicitly does not guarantee:

* protection against malicious host systems;
* protection against hardware-level attacks;
* protection outside defined threat model.

Security guarantees apply only within defined system scope.

---

## 18.6 Security Review Requirement

All changes affecting:

* kernel;
* hypervisor;
* networking stack;
* privilege boundaries;

must undergo mandatory security review.

# 19. Documentation Governance

Documentation in OpenPS3 is treated as a core engineering artifact, equivalent in importance to source code.

---

## 19.1 Scope

Documentation includes:

* architecture specifications;
* API references;
* subsystem design documents;
* RFCs and ADRs;
* developer guides;
* build and tooling instructions;
* security advisories.

---

## 19.2 Principles

All documentation must adhere to:

* accuracy over completeness;
* clarity over stylistic preference;
* traceability to implementation;
* version alignment with codebase;
* minimal ambiguity.

---

## 19.3 Source of Truth

The canonical source of truth is:

1. Source code behavior
2. RFCs and ADRs
3. Maintained documentation

When conflicts arise, documentation must be updated to match implementation or corrected via governance process.

---

## 19.4 Ownership

Each subsystem must have designated documentation maintainers responsible for:

* keeping documentation synchronized with code;
* reviewing documentation changes alongside code changes;
* ensuring consistency across repositories.

---

## 19.5 Documentation Changes

Any change affecting:

* public APIs;
* system behavior;
* architecture;

must include corresponding documentation updates.

---

## 19.6 Documentation Drift

Documentation drift is treated as a technical defect.

Recurring drift may result in:

* maintainer review;
* mandatory documentation refactoring;
* temporary freeze on feature merges in affected areas.

---

# 20. Financial and Trademark Governance

This section defines stewardship of financial resources and intellectual property identifiers.

---

## 20.1 Financial Governance Scope

Financial governance applies to:

* donations;
* grants;
* sponsorships;
* infrastructure funding;
* service credits or in-kind contributions.

---

## 20.2 Financial Principles

All financial activity must follow:

* transparency;
* traceability;
* public reporting (when legally permitted);
* strict separation from technical authority.

---

## 20.3 Spending Categories

Funds may only be allocated to:

* infrastructure operations (CI, hosting, storage);
* security audits and penetration testing;
* documentation and preservation efforts;
* community development grants;
* operational continuity.

---

## 20.4 Financial Oversight

The OpenPS3 Foundation acts as custodian of financial resources and must:

* maintain accounting records;
* publish periodic financial summaries;
* ensure separation of duties;
* prevent unilateral fund usage without oversight.

---

## 20.5 Trademark Governance

All project-related trademarks (e.g., OpenPS3 name, logos) are managed to:

* prevent misuse or misrepresentation;
* preserve project identity;
* ensure consistent branding.

---

## 20.6 Trademark Usage

Permitted usage includes:

* non-commercial community projects;
* documentation and research references;
* approved derivative tooling.

Prohibited usage includes:

* implying official endorsement without approval;
* commercial exploitation that misrepresents affiliation;
* forks attempting brand impersonation.

---

## 20.7 Enforcement

Trademark misuse is handled through:

* public notice;
* request for correction;
* escalation to Foundation oversight if needed.

---

# 21. Conflict Resolution

This section defines structured mechanisms for resolving disputes within OpenPS3.

---

## 21.1 Guiding Principle

Conflict resolution prioritizes:

* technical correctness;
* project stability;
* fairness in process;
* preservation of contributor trust.

---

## 21.2 Types of Conflicts

### Technical Conflicts

Disagreements about implementation, architecture, or design.

### Governance Conflicts

Disputes over authority, process, or decision legitimacy.

### Interpersonal Conflicts

Behavioral or communication issues between contributors.

---

## 21.3 Resolution Hierarchy

Conflicts are resolved in ascending order:

1. Direct discussion between parties
2. Working Group mediation
3. Maintainer mediation
4. TSC review
5. Formal governance vote (if necessary)

---

## 21.4 Mediation Principles

Mediators must:

* remain neutral;
* base decisions on governance rules;
* document outcomes;
* avoid informal or opaque rulings.

---

## 21.5 Escalation Threshold

Escalation occurs when:

* technical disagreement blocks progress;
* mediation fails to produce resolution;
* governance violation is suspected.

---

## 21.6 Binding Decisions

Final decisions made by the TSC under governance scope are binding unless overturned through formal amendment.

---

## 21.7 Behavioral Standards

Repeated violations of conduct expectations may result in:

* temporary suspension;
* role downgrade;
* permanent removal from roles.

---

# 22. Amendment Process

This section defines how governance itself can evolve.

---

## 22.1 Amendment Requirement

Any modification to this governance document requires:

* formal proposal;
* documented rationale;
* review period;
* approval by TSC.

---

## 22.2 Amendment Threshold

Unless otherwise specified:

* amendments require supermajority approval (>2/3 of TSC).

---

## 22.3 Review Period

Proposed amendments must remain open for review for a minimum period before final decision, allowing:

* community feedback;
* technical evaluation;
* impact assessment.

---

## 22.4 Emergency Amendments

Emergency amendments are permitted only when:

* there is a critical legal risk;
* security concerns require immediate governance change;
* project integrity is at risk.

Emergency changes must be:

* documented immediately;
* reviewed retroactively;
* subject to ratification.

---

## 22.5 Versioning

Each governance revision must increment version:

* ensuring traceability of structural evolution;
* preserving historical governance states.

---

# 23. Dissolution and Project Continuity

This section defines continuity guarantees for long-term preservation of OpenPS3.

---

## 23.1 Continuity Objective

OpenPS3 is designed to survive:

* loss of key contributors;
* organizational changes;
* funding disruptions;
* infrastructure migration.

---

## 23.2 Dissolution Conditions

Dissolution of the Foundation or governance structure may occur only when:

* no viable contributor base remains;
* legal or regulatory constraints force termination;
* unanimous or legally mandated decision is reached.

---

## 23.3 Asset Preservation

In case of dissolution:

* source code remains under open-source license;
* repositories are archived publicly;
* documentation is preserved in read-only form;
* trademarks are released or reassigned according to legal constraints.

---

## 23.4 Continuity Transfer

If governance collapses, responsibility may transition to:

* successor open-source foundations;
* distributed community governance models;
* independent maintainers maintaining fork continuity.

---

## 23.5 Non-Abandonment Principle

The project shall not be silently abandoned.

Any discontinuation must be:

* publicly declared;
* fully documented;
* structurally preserved for future recovery.

---

## 23.6 Final Principle

OpenPS3 is designed as infrastructure, not a temporary software project.

Its governance must therefore prioritize survivability under adverse conditions over organizational convenience.

# Appendix A — Definitions

This appendix defines formal terminology used throughout the OpenPS3 governance framework. These definitions are binding for interpretation of all governance documents.

---

## A.1 Core Entities

### Project

The OpenPS3 project refers to the collective set of repositories, specifications, documentation, tooling, and community processes governed under this document.

---

### Foundation

The OpenPS3 Foundation is the legal and operational entity responsible for infrastructure stewardship, financial custody, and trademark management.

It does not control technical decisions.

---

### Technical Steering Committee (TSC)

The highest technical authority in OpenPS3 responsible for architecture, RFC approval, and release governance.

---

### Working Group (WG)

A domain-specific technical unit responsible for implementing and maintaining subsystems within a defined scope.

---

### Maintainer

A contributor with delegated authority to review, approve, and manage changes within a specific subsystem or repository.

---

### Committer

A contributor with write access to one or more repositories, operating under maintainer oversight.

---

### Contributor

Any individual participating in the project without elevated privileges.

---

## A.2 Governance Artifacts

### RFC (Request for Comments)

A formal proposal document used to introduce or modify significant technical or architectural changes.

---

### ADR (Architecture Decision Record)

A permanent record of an accepted architectural decision and its rationale.

---

### Release

A versioned and published snapshot of the OpenPS3 system or its components.

---

### PR (Pull Request)

A proposed code change submitted for review and potential integration.

---

## A.3 Decision Terminology

### Consensus

A state in which no qualified participant maintains a sustained, technically grounded objection.

---

### Blocking Objection

A formally justified objection preventing progress until resolution or escalation.

---

### Non-Blocking Objection

A subjective or non-critical concern that does not prevent decision finalization.

---

### Vote

A formal decision mechanism used when consensus cannot be reached.

---

## A.4 Governance States

### Draft

Initial state of an RFC or ADR under development.

### Active

A formally accepted and operational document or decision.

### Superseded

A document replaced by a newer version.

### Rejected

A proposal that has been formally declined.

### Deprecated

A previously active decision that is no longer recommended for use but retained for historical context.

---

## A.5 Technical Scope Definitions

### System Core

The foundational layer of OpenPS3 including kernel, hypervisor, and runtime primitives.

---

### Subsystem

A logically isolated functional component such as networking, graphics, or storage.

---

### Interface Contract

A formally defined interaction boundary between subsystems.

---

### Clean-Room Implementation

An implementation produced without direct reference to proprietary source code, based solely on documented behavior.

---

# Appendix B — Governance Lifecycle

This appendix describes the lifecycle of governance entities and artifacts across the OpenPS3 system.

---

## B.1 Lifecycle Overview

OpenPS3 governance operates as a state-transition system where entities evolve through defined stages:

* Contributors evolve into Committers, Maintainers, and potentially TSC members.
* RFCs evolve from Draft → Active → Superseded or Rejected.
* ADRs evolve from Proposed → Accepted → Superseded.
* Releases evolve from Development → RC → Stable → Patched.

---

## B.2 Contributor Lifecycle

### Stage 1 — Contributor

Initial participation through issues, pull requests, and discussions.

---

### Stage 2 — Committer

Granted repository write access under maintainer supervision.

Requirements:

* sustained contribution quality;
* adherence to governance rules;
* demonstrated reliability.

---

### Stage 3 — Maintainer

Responsible for subsystem stewardship.

Requirements:

* deep domain expertise;
* review competence;
* architectural understanding.

---

### Stage 4 — TSC Member

Highest technical governance role.

Requirements:

* cross-subsystem expertise;
* long-term project impact;
* proven governance judgment.

---

## B.3 RFC Lifecycle Diagram (Logical Flow)

RFC progression follows this abstract state machine:

1. Draft created
2. Public discussion initiated
3. Revision cycles occur
4. Review by maintainers and TSC
5. Decision phase:

   * Approved → Implementation
   * Rejected → Archived
   * Deferred → Backlog
6. Finalization and archival

---

## B.4 ADR Lifecycle

ADR flow:

1. Proposed
2. Reviewed alongside RFC or decision context
3. Accepted and frozen as immutable record
4. Superseded when replaced
5. Archived for historical traceability

---

## B.5 Release Lifecycle

### Phase 1 — Development

Active integration of features and fixes.

---

### Phase 2 — Feature Freeze

Only bug fixes and stabilization changes allowed.

---

### Phase 3 — Release Candidate (RC)

Pre-release builds distributed for validation.

---

### Phase 4 — Stable Release

Official release published under version tag.

---

### Phase 5 — Patch Cycle

Post-release maintenance and security fixes.

---

## B.6 Governance Evolution Constraints

Governance evolution is constrained by the following rules:

* No entity may bypass lifecycle stages.
* Role elevation requires documented justification.
* Artifact state changes must be traceable.
* Historical states must remain accessible.

---

## B.7 Structural Invariants

The governance system must always preserve:

* separation of technical and financial authority;
* non-centralization of power;
* reproducibility of decision history;
* auditability of all major changes;
* survivability of the project beyond individual contributors.

---

## B.8 Final Note

This governance framework is intentionally designed as a living system.

However, its structural invariants are not optional and must not be compromised for short-term efficiency gains.


