# Exrela System Runtime Development Log
# Exrela System Runtime 開発ログ

## Document Status

- Version: v0.1
- Status: Active
- Scope: Development history and implementation decisions

---

# Purpose
# 目的

This document records the history of runtime development.

この文書は、Runtime開発の履歴と設計判断を記録する。

It is not a specification document.

この文書は仕様書ではない。

It records why a decision was made, what changed, and what remains.

何を変更したか、なぜ変更したか、何が未完了かを記録する。

---

# Responsibility Boundary
# 責務境界

90 : Development Rules（何を守るか）

91 : Implementation Mapping（どこへ反映するか）

92 : Runtime Module Specification（各Runtimeの責務）

93 : Development History（開発履歴・設計判断・保留事項）

---

# Log Entry Template

```text
Date:
Topic:
Reason:
Decision:
Affected Documents:
Affected Runtime:
Status:
Next Action:
Notes:
```

---

# Initial Development Record

## Runtime Documentation Foundation

Reason:

Established the foundational documentation structure before continuing Runtime implementation.

Decision:

Separated documentation into four independent responsibilities:

- 90 Development Guide
- 91 Runtime Implementation Map
- 92 Runtime Module Specification
- 93 Runtime Development Log

Status:

Active

Next Action:

Continue Runtime implementation based on the documentation workflow.

---

# Documentation Runtime PoC

Date:

2026-06-28

Topic:

Documentation Runtime / Docs and Code Synchronization PoC

Reason:

Exrela System development now requires Docs and runtime code to evolve together.

Docs should not remain separate from implementation decisions.

Decision:

Begin a PoC for a Exrela Documentation Runtime that can inspect code changes and generate update candidates for:

- 91_Runtime_Implementation_Map
- 92_Runtime_Module_Specification
- 93_Runtime_Development_Log

Initial Scope:

- Detect changed runtime files.
- Identify affected Runtime area.
- Suggest whether 91, 92, or 93 should be updated.
- Keep all generated updates as review candidates until approved.

Affected Documents:

- 91_Runtime_Implementation_Map.md
- 92_Runtime_Module_Specification.md
- 93_Runtime_Development_Log.md

Affected Runtime:

- Future Exrela Documentation Runtime

Alternatives Considered:

- Manual Docs update only
- Writing all implementation notes directly into 90_Development_Guide

Rejected:

Manual-only updates risk documentation drift.

Writing all implementation notes into 90 would mix development rules with implementation history.

Status:

Adopted as PoC direction.

Next Action:

Inspect current runtime files and decide where the first Exrela Documentation Runtime implementation should live.

Notes:

90 remains the development rule source.
91 maps rules to implementation areas.
92 defines module responsibilities.
93 records development decisions and implementation history.

---

# Exrela System Version 1.0 Release

Date:

2026-07-01

Topic:

Exrela System Version 1.0 Freeze

Reason:

The initial design objectives for the Exrela System Definition, Runtime Suite, library architecture, and documentation framework were completed and verified.

Decision:

Freeze Exrela System Version 1.0 as the first stable specification baseline.

Completed Scope:

- Exrela System Definition (T1)
- Exrela Runtime Suite (T2)
- Exrela Library architecture (T0–T6)
- Documentation set (90–93)
- Library reorganization from ADOR to Exrela
- Version 1.0 Git baseline

Affected Documents:

- T1 Definition
- T2 Runtime Suite
- T0 Index
- Documentation (90–93)

Affected Runtime:

- Exrela Runtime Suite Version 1.0

Status:

Released

Next Action:

Begin Version 1.1 development and continue expansion of Recognition, Runtime, and implementation support.

Notes:

This release establishes the first official Exrela System baseline. Future development should extend Version 1.0 while preserving its architectural principles and responsibility boundaries.

# Revision History

## v0.1

- Created Runtime Development Log.
- Defined document responsibility.
- Established development log template.
- Recorded initial documentation milestone.


-- Rebranded Runtime Development Log for Exrela System.
-- Updated Documentation Runtime terminology to Exrela Documentation Runtime.

---

# Runtime Pre-Release — LLM Distortion Mode v0.1

Date:

2026-07-02

Topic:

LLM Distortion Runtime Pre-Release

Reason:

The Runtime was reorganized to establish a dedicated LLM Distortion mode before Character Reconstruction. This separates Runtime operational guidance from Character Package reconstruction and aligns Runtime responsibilities with the Exrela Information Source architecture.

Decision:

- Replaced the previous multi-mode controller with a two-mode structure.
- Established Mode 1: LLM Distortion.
- Established Mode 2: Reconstruction.
- Runtime now reads Exrela Information Sources before formal reconstruction.
- T1 Definition and T2 Runtime Suite are loaded as Runtime Information Sources during LLM Distortion.
- Runtime does not perform source selection; Exrela-guided LLM is responsible for Information Source selection, Required Rail Extraction, and Prompt Artifact generation after Scenario understanding.

Affected Documents:

- T1 Exrela System Definition
- T2 Runtime Suite
- Runtime controller
- distortion_brief
- reconstruction_brief

Affected Runtime:

- Controller
- Bootstrap
- LLM Distortion
- Reconstruction

Status:

Pre-Release v0.1 Completed

Next Action:

Extend Runtime State to retain and expose the complete text of each Character Package layer as Information Sources for Reconstruction.

Notes:

This milestone establishes the Runtime foundation where Information Sources are loaded before Character Reconstruction, while preserving Runtime responsibility separation and Information Source First.