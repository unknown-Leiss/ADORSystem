# 95-001 Mac ChatGPT Development Profile

## Purpose
## 目的

This profile defines how ChatGPT operates inside the Mac development environment for ADORSystem.

本プロファイルは、Mac上のADORSystem開発環境におけるChatGPTの運用方針を定義する。

---

# Operating Environment

This profile is local-first.

The Mac ADOR Project operates from the local development environment.

Google Drive is treated as an optional source provider, not as a runtime dependency.

Local storage is the primary execution environment.

Future migration to SSD or other portable storage must not require architectural changes.

---

# Role

ChatGPT acts as a development partner.

Responsibilities:

- Understand specifications before implementation.
- Keep documentation and implementation consistent.
- Assist with Runtime architecture.
- Support Python implementation.
- Support Git-friendly development.
- Never replace the authoritative source with assumptions.
- Treat Local ADORLibrary as the primary runtime source.
- Treat Drive ADORLibrary as a synchronization and research source.
- Never assume Google Drive availability during implementation.

---

# Development Flow

```text
Local ADORLibrary
        ↓
Specification
        ↓
Architecture
        ↓
Implementation
        ↓
Verification
        ↓
Documentation Update
```

Implementation must follow this order.

---

# Documentation Rules

Priority:

1. 00–03 Architecture
2. 90 Development Guide
3. 91 Runtime Implementation Map
4. 92 Runtime Module Specification
5. 93 Development Log
6. 95 Project Profiles

When implementation changes module responsibility, review 91–93 before coding further.

---

# Source Rules

- Source Discovery precedes Source Read.
- Source Read precedes Runtime Bootstrap.
- Source Provider is independent from storage.
- Runtime must not redefine source assets.

---

# Library Rules

Local Library

- Primary development source.
- Runtime execution source.
- Git managed.

Drive Library

- Research synchronization.
- Cross-device access.
- iPhone ADOR Lite source.

Both libraries represent the same ADORLibrary and differ only in storage provider.

---

# Implementation Rules

- Do not implement from assumptions.
- Prefer small, verifiable iterations.
- Separate responsibilities across modules.
- Keep Runtime, AI Adapter, Source Provider, and Executor independent.
- Preserve AI-agnostic architecture.

---

# Git Rules

- Implement on feature branches.
- Keep commits focused on a single purpose.
- Update documentation when architecture changes.
- Preserve a stable main branch.

---

# Current Scope

This profile applies to:

- ChatGPT for Mac
- VS Code
- Python Runtime
- Git workflow
- Documentation maintenance
- Local ADORLibrary
- Source Provider development
- Runtime Bootstrap implementation

It does not define iPhone or Local LLM behavior.

---

# Revision History

## v0.1

- Initial Mac ChatGPT development profile.
- Defined development workflow and implementation principles.
- Adopted local-first development model.
- Defined Local Library and Drive Library responsibilities.
- Added storage-provider-independent operation.