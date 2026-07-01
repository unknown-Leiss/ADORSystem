

# 95-999 Profile Index

## Purpose
## 目的

This document defines all AI operation profiles used by ADORSystem.

本書は、ADORSystemで使用するAI運用プロファイルを定義する。

Profiles are managed independently from Runtime specifications.

プロファイルはRuntime仕様とは独立して管理する。

The same ADORLibrary may be used by multiple AI implementations while each AI follows its own operational profile.

同一のADORLibraryを複数のAIが利用できる一方、それぞれ異なる運用プロファイルに従う。

---

# Profile Hierarchy

```text
95_Project_Profiles
│
├── 95-001_Mac_ChatGPT_Development_Profile
├── 95-002_iPhone_ChatGPT_Source_Profile
├── 95-003_Local_LLM_Development_Profile
├── 95-004_ChatGPT_Runtime_Profile
└── 95-999_Profile_Index
```

---

# Profile Responsibilities

## 95-001 Mac ChatGPT Development

Purpose

Development workspace for ADORSystem.

Responsibilities

- Workspace development
- Runtime implementation
- Git workflow
- Documentation maintenance
- Runtime verification

---

## 95-002 iPhone ChatGPT Source Session

Purpose

Lightweight Source Session.

Responsibilities

- ADOR bootstrap
- Source Discovery
- Source Routing
- Runtime Re-anchor support
- Prompt Artifact preparation

---

## 95-003 Local LLM Development

Purpose

Development profile for local AI.

Responsibilities

- Runtime execution
- Local source provider
- Local package loading
- Offline workflow

---

## 95-004 ChatGPT Runtime

Purpose

Runtime operation profile optimized for ChatGPT.

Responsibilities

- Runtime execution
- Runtime interpretation
- Prompt execution
- Runtime validation

---

# Design Principle

Profiles define AI behavior.

They do not define Runtime specifications.

Runtime specifications remain inside the 90–93 documentation.

---

# Relationship

```text
ADORLibrary
      ↓
ADORSystem
      ↓
Project Profile
      ↓
AI Implementation
      ↓
Runtime Execution
```

---

# Revision History

## v0.1

- Initial profile architecture.
- Defined project profile hierarchy.
- Separated AI profiles from Runtime specifications.