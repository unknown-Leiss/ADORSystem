# Exrela System Runtime Module Specification
# Exrela System Runtime モジュール仕様

## Document Status

- Version: v0.1
- Status: Draft
- Source Basis: 90_Development_Guide.md + 91_Runtime_Implementation_Map.md
- Scope: Runtime module responsibilities and boundaries

---

# Purpose
# 目的

This document defines the responsibility of each Runtime module.

この文書は、各Runtimeモジュールの責務を定義する。

This document does not define Recognition identity or development rules.

この文書はRecognition Identityや開発ルールを定義しない。

Those belong to:

- 90_Development_Guide (Development Rules)
- 91_Runtime_Implementation_Map (Rule → Implementation Mapping)

This document specifies the runtime modules that implement those rules.

---

# Responsibility Boundary
# 責務境界

90 → What developers must preserve.

91 → Where each rule affects implementation.

92 → What each Runtime module is responsible for.

Runtime source files implement the specifications defined here.

---

# Runtime Module Template
# Runtimeモジュール記述テンプレート

Each Runtime module should be documented using the following structure.

```text
Module Name:
Purpose:
Inputs:
Outputs:
Dependencies:
Must Preserve:
Must Not Do:
Related Rules:
Related Runtime Files:
Status:
Notes:
```

---

# Planned Runtime Modules
# 予定Runtimeモジュール

- Recognition Context Runtime
- Meaning Extraction Runtime
- Recognition Understanding Runtime
- Token Observation Runtime
- Surface Organization Runtime
- Recognition Runtime
- Recognition Resolution Runtime
- Structural Observation Runtime
- Structural Organization Runtime
- Meaning Reconstruction Runtime
- Meaning Verification Runtime
- Meaning Expansion Runtime
- Scenario Interpretation Runtime
- Operational Intent Runtime (Future)
- Artifact Writer Runtime (Future)

---

# Runtime Module Specification
# Runtimeモジュール仕様

## Recognition Runtime

### Module Name
Recognition Runtime

### Purpose
Generate recognition candidates from organized observations.

構造化された観測結果からRecognition Candidateを生成する。

### Inputs

- Surface Organization Runtime output

### Outputs

- Recognition Candidates

### Dependencies

- Surface Organization Runtime
- Recognition Resolution Runtime

### Must Preserve

- Recognition Cause
- Recognition uncertainty
- Source boundary
- Layer boundary

### Must Not Do

- Decide Meaning
- Define Recognition Identity
- Collapse uncertainty into a single interpretation

### Related Rules

- Rule-011
- Rule-026

### Related Runtime Files

- runtime/recognition_engine.py
- runtime/recognition_modules/

### Status

Draft

### Notes

Recognition Runtime generates candidate observations only.
Meaning determination belongs to later Runtime layers.

Recognition Runtimeは観測候補を生成する責務のみを持つ。
意味の決定は後続Runtimeで行う。

---

## Recognition Engine

### Module Name
Recognition Engine

### Purpose
Coordinate Recognition Modules and collect Recognition Candidates.

Recognition Module群を実行し、Recognition Candidateを収集する。

### Inputs

- Surface Organization Runtime output

### Outputs

- Recognition Candidates

### Dependencies

- Particle Module
- Compound Module
- Entity Module
- Action Module
- Attribute Module
- Relation Module

### Must Preserve

- Module independence
- Candidate ordering
- Recognition uncertainty
- Source boundary

### Must Not Do

- Decide Meaning
- Resolve candidate conflicts
- Perform structural organization
- Define Recognition Identity

### Related Rules

- Rule-011
- Rule-026

### Related Runtime Files

- runtime/recognition_engine.py

### Status

Draft

### Notes

Recognition Engine is an orchestrator.

Its responsibility is to execute Recognition Modules and aggregate their outputs.

Conflict resolution belongs to Recognition Resolution Runtime.

Meaning determination belongs to later Runtime layers.

Recognition Engineはオーケストレーターである。

Recognition Moduleを実行し、結果を集約することだけを責務とする。

競合解決はRecognition Resolution Runtimeが担当する。

意味決定は後続Runtimeで行う。

---

# Revision History

## v0.1

- Created Runtime Module Specification.
- Defined document responsibility.
- Established module specification template.
- Listed planned Runtime modules for future specification.