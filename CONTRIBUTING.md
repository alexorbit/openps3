# Contributing to OpenPS3

First, thank you for your interest in contributing to OpenPS3.

This project exists because of people who believe that great engineering should remain accessible long after commercial support ends.

Whether you are a reverse engineer, kernel developer, hardware researcher, technical writer, designer, tester, or student, your contributions are welcome.

---

# Before You Start

OpenPS3 is **not** a typical software project.

It is a long-term engineering initiative built around specifications, documentation, and implementation.

Please take some time to understand the project before contributing.

Recommended reading order:

1. README.md
2. Manifesto
3. Technical Charter
4. Architecture Specifications (APS)
5. Platform Specifications (PPS)
6. Architecture Decision Records (ADR)
7. Open RFCs

Understanding the architecture before writing code is strongly encouraged.

---

# Core Engineering Principles

Every contribution should respect the following principles.

## Documentation Before Code

Documentation is a deliverable.

Every new subsystem must include documentation.

Undocumented code will not be considered complete.

---

## Architecture Before Implementation

Large implementations require architectural discussion first.

Do not implement major features without an approved RFC.

---

## Engineering Over Opinion

Technical decisions are based on:

* measurements
* benchmarks
* experiments
* documentation
* reproducible evidence

Not personal preference.

---

## Simplicity

Choose the simplest architecture capable of solving the problem.

Complexity requires justification.

---

## Long-Term Maintainability

Every line of code becomes future maintenance.

Optimize for clarity rather than cleverness.

---

# Ways to Contribute

There are many ways to contribute.

## Documentation

Improve specifications.

Correct inaccuracies.

Add diagrams.

Write tutorials.

Expand hardware documentation.

---

## Reverse Engineering

Document hardware behavior.

Map registers.

Study firmware.

Analyze protocols.

Validate assumptions.

---

## Software Development

Kernel

Drivers

Runtime

Shell

SDK

Toolchain

Developer tools

Applications

---

## Testing

Hardware validation.

Regression testing.

Performance benchmarking.

Compatibility verification.

Long-duration stability testing.

---

## Design

User interface.

Icons.

Developer experience.

Documentation diagrams.

Website.

---

# Contribution Workflow

Every significant contribution follows the same lifecycle.

```text
Issue
    ↓
Discussion
    ↓
RFC (if required)
    ↓
Implementation
    ↓
Review
    ↓
Merge
```

Skipping architectural discussion usually results in unnecessary rework.

---

# Issues

Please search existing issues before opening a new one.

When creating a new issue, include:

* objective
* motivation
* affected subsystem
* expected behavior
* current behavior
* supporting information

Reproducible examples are preferred.

---

# Feature Requests

Large features require an RFC.

Small improvements may begin directly as issues.

Examples requiring RFCs:

* kernel scheduler changes
* new graphics API
* package format modifications
* filesystem architecture
* driver framework
* public API changes

---

# RFC Process

RFCs exist to improve engineering quality.

An RFC should answer:

* What problem is being solved?
* Why is the change necessary?
* What alternatives were considered?
* What are the compatibility implications?
* What are the performance implications?
* What are the security implications?
* How will this be documented?

Implementation begins only after technical consensus.

---

# Architecture Decision Records

Major engineering decisions are recorded permanently.

Every ADR includes:

* context
* decision
* alternatives
* consequences

ADRs explain *why* the project evolved in a particular direction.

---

# Coding Standards

General principles:

* Write readable code.
* Prefer explicit behavior.
* Avoid hidden side effects.
* Minimize global state.
* Fail predictably.
* Keep functions focused.
* Keep interfaces stable.

Readability is more important than cleverness.

---

# Documentation Standards

Every public interface must include:

Purpose

Parameters

Return values

Error conditions

Examples

Thread safety

Performance notes

Compatibility notes

Documentation should be understandable without reading the implementation.

---

# Commit Messages

Follow a simple conventional style.

Examples:

```text
kernel: implement priority scheduler

drivers: add USB initialization

runtime: improve package validation

docs: expand memory specification

pps: document RSX interrupt registers
```

Keep commits focused.

Avoid mixing unrelated changes.

---

# Pull Requests

A pull request should solve one problem.

Please include:

* summary
* motivation
* implementation notes
* testing performed
* documentation updates

Small pull requests are easier to review.

---

# Code Review

Reviews focus on engineering quality.

Reviewers evaluate:

Correctness.

Architecture.

Maintainability.

Documentation.

Testing.

Performance.

Security.

Feedback should remain constructive and technical.

---

# Testing Requirements

Every contribution should include appropriate validation whenever applicable.

Possible validation includes:

* unit tests
* integration tests
* hardware testing
* performance benchmarks
* regression testing

Untested changes should clearly explain why testing was not possible.

---

# Documentation Requirements

New public functionality should include updates to:

* specifications
* examples
* tutorials
* API reference
* diagrams (when appropriate)

Documentation is not optional.

---

# Licensing

By contributing, you agree that your work will be distributed under the license of the repository to which you contribute.

Please verify the repository license before submitting contributions.

---

# Developer Certificate of Origin (DCO)

OpenPS3 uses the Developer Certificate of Origin.

Instead of signing a Contributor License Agreement (CLA), contributors certify that they have the right to submit their work.

Every commit should include:

```text
Signed-off-by: Your Name <email@example.com>
```

---

# Communication

Technical discussions should remain respectful, evidence-based, and focused on solving engineering problems.

Disagreement is expected.

Personal attacks are not.

---

# What We Value

We value contributors who:

* document discoveries;
* improve existing work;
* ask thoughtful questions;
* verify assumptions;
* simplify complex systems;
* help others understand the platform.

Great engineering is collaborative.

---

# Our Philosophy

OpenPS3 is not built by writing the most code.

It is built by creating the clearest architecture, the best documentation, and the highest-quality engineering possible.

Every contribution should move the project toward that goal.

Thank you for helping build the future of OpenPS3.
