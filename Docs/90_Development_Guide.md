# Exrela System Development Guide
# Exrela System 開発ガイド

## Document Status

- Version: v0.2
- Status: Draft
- Source Basis: T0 + T2 Runtime Sources + Exrela Library Index

---

# Purpose
# 目的

This document defines the development rules used when designing and implementing Exrela System.

この文書は、Exrela Systemを設計・実装する際に開発者が従う運用ルールを定義する。

This document is not a Runtime specification.

この文書はRuntime仕様書ではない。

It defines how source documents are interpreted and transformed into specifications and implementation.

情報源をどのように読み、仕様と実装へ落とし込むかを定義する。

---

# Source Confirmed
# 情報源確認

Current Sources

- T0-CustomInstruction : Exrela Runtime Boot Package
- Exrela Library Index
- T2 Runtime Bootstrap Compact
- T2 Runtime Architecture
- T2 Layer Rules
- T2 Operational Rail Architecture
- T2 Japanese Operational Interpretation Layer
- T2 Research Operation Rules
- T2 Recognition Runtime Pipeline v0.3

---

# Development Rules
# 開発ルール

## Rule-001
### T0 is a Boot Instruction.
### T0はBoot Instructionである。

T0 starts Runtime Bootstrap.

T0はRuntime Bootstrapを開始する。

T0 itself is not a Runtime Source.

T0自体をRuntime Sourceとして扱わない。

---

## Rule-002
### Source First
### 情報源優先

When an official source exists, implementation must be based on the source instead of memory.

利用可能な正本が存在する場合、記憶ではなく情報源を基準として実装する。

Memory is not an information source.

Memoryは情報源ではない。

Generated output is not an identity source.

生成結果はIdentity Sourceではない。

History is not an information source.

履歴は情報源ではない。

---

## Rule-003
### Source Read Required
### Source Read必須

Source discovery alone is insufficient.

検索だけでは不十分である。

Development decisions require Source Read.

開発判断はSource Readを前提とする。

---

## Rule-004
### Runtime Re-anchor
### Runtime Re-anchor

Formal implementation should not proceed before Runtime Re-anchor has been confirmed.

Runtime Re-anchor未確認の状態で正式実装を進めない。

---

## Rule-005
### Session Separation
### セッション分離

Source Session and Execution Session must remain independent.

Source SessionとExecution Sessionは分離して設計する。

---

## Rule-006
### Runtime Priority
### Runtime優先順位

Recognition Core
>
Operational Rail
>
OS
>
Environment
>
Rendering

Implementation must preserve this hierarchy.

実装はこの優先順位を維持する。

---

## Rule-007
### Runtime Bootstrap Before Implementation
### Runtime Bootstrapを前提とする

Development shall follow Runtime Bootstrap before Formal Operation.

正式なRuntime処理および実装判断は、Runtime Bootstrapを前提とする。

---

## Rule-008
### Source Read → Re-anchor → Decision
### Source ReadからRe-anchorを経て判断する

Source discovery alone is insufficient.
Runtime Re-anchor must update subsequent operational decisions.

検索や本文読取だけでは十分ではない。
Runtime Re-anchorによって以後の処理順序へ反映して初めて正式判断とする。

---

## Rule-009
### Operational Meaning First
### Operational Meaningを優先する

Japanese input shall be interpreted through Operational Meaning Reconstruction rather than keyword translation.

日本語入力は単語翻訳ではなく、Operational Meaning Reconstructionを経由して扱う。

---

## Rule-010
### Runtime Responsibility Separation
### Runtime責務を分離する

Recognition, Operational Reconstruction, Prompt Reconstruction, Generation, Verification, Analyze and Research shall remain independent responsibilities.

Recognition・Operational Reconstruction・Prompt Reconstruction・Generation・Verification・Analyze・Researchは責務を混在させない。

---

## Rule-011
### Recognition Preserves Uncertainty
### Recognitionは不確実性を保持する

Recognition Runtime produces recognition candidates and delays semantic commitment until later layers.

Recognition Runtimeは認識候補を生成する層であり、意味確定や構造確定を早期に行わない。

---

## Rule-012
### Confirm Source Classification Before Implementation
### 実装前に情報源区分を確認する

Before designing or implementing a feature, identify the role of every referenced source.

機能を設計・実装する前に、参照する各情報源の役割を確認する。

Recognition Core, Operational Rail, OS, Research, History and Generated Output shall not be treated as interchangeable.

Recognition Core・Operational Rail・OS・Research・History・Generated Outputを同一の情報源として扱わない。

---

## Rule-013
### Preserve Source Boundaries
### 情報源境界を維持する

Implementation shall preserve the boundary between Identity Source, Support Source, Interpretation Source, Research Source and Runtime Artifact.

実装では、Identity Source・Support Source・Interpretation Source・Research Source・Runtime Artifact の境界を維持する。

---

## Rule-014
### Research Does Not Become Specification Automatically
### Researchは自動的に仕様にならない

Research observations, theories and experiments shall be reviewed before becoming specifications.

研究・観測・理論・実験は、レビューを経て初めて仕様へ反映する。

---

## Rule-015
### Verify Layer Direction
### レイヤー方向を確認する

Before implementation, verify that lower layers are not defining higher layers.

実装前に、下位レイヤーが上位レイヤーを定義していないことを確認する。

Maintain the canonical priority defined by the information sources.

情報源で定義されたCanonical Priorityを維持する。

---

## Rule-016
### Treat Recognition Package as a Composite Source
### Recognition Packageを複合情報源として扱う

A Recognition Package is composed of multiple source documents with different responsibilities.

Recognition Packageは責務の異なる複数の情報源で構成される。

Recognition Core alone does not represent the complete Recognition Package.

Recognition CoreのみをRecognition Package全体として扱わない。

---

## Rule-017
### Preserve Recognition Package Responsibilities
### Recognition Packageの責務を維持する

Each document inside a Recognition Package has an independent responsibility and shall not replace another.

Recognition Package内の各文書は独立した責務を持ち、相互に置き換えてはならない。

---

## Rule-018
### Preserve Recognition Package Hierarchy
### Recognition Package階層を維持する

Implementation shall preserve the dependency order defined by the Recognition Package.

実装ではRecognition Packageで定義された依存関係を維持する。

Do not allow lower support layers to redefine higher identity layers.

下位の支援レイヤーが上位のIdentity Layerを定義してはならない。

---

## Rule-019
### Follow Recognition Package Reading Order
### Recognition Package読込順を維持する

When using a Recognition Package, follow the documented reading sequence before implementation.

Recognition Packageを利用する際は、文書で定義された読込順に従って実装へ進む。

Reading order itself is part of the development process.

読込順そのものを開発プロセスの一部として扱う。

---

## Rule-020
### Treat Verification as an Independent Layer
### Verificationを独立レイヤーとして扱う

Verification confirms whether Recognition Reconstruction succeeded. It does not define Recognition.

VerificationはRecognition Reconstructionの成否を確認する層であり、Recognitionを定義する層ではない。

---

## Rule-021
### Preserve Layer Responsibilities Across Recognition Packages
### Recognition Package全体で責務分離を維持する

Recognition Core, Persistent State, Recognition Model, Physical Specification and Verification each have independent responsibilities.

Recognition Core・Persistent State・Recognition Model・Physical Specification・Verificationは、それぞれ独立した責務を持つ。

Implementation shall not merge or redefine these layers.

実装ではこれらの責務を統合・上書きしてはならない。

---

## Rule-022
### Drift Correction Does Not Change Identity
### ドリフト修正はIdentityを変更しない

Corrected Recognition, Physical or Verification documents improve recognition stability but do not redefine the Recognition Core.

Recognition・Physical・Verificationの修正版は認識安定性を改善するものであり、Recognition Coreを書き換えるものではない。

---

## Rule-023
### Operational Rail Supports Reconstruction
### Operational Railは再構築を支援する

Operational Rail supports Recognition Reconstruction under variation but never replaces Recognition Core.

Operational Railは変化下でのRecognition Reconstructionを支援するが、Recognition Coreを置き換えてはならない。

---

## Rule-024
### Recognition Packages May Extend Without Changing Their Foundation
### Recognition Packageは基盤を変えずに拡張できる

A Recognition Package may introduce additional support layers such as Operational Rail while preserving the existing layer hierarchy.

Recognition PackageはOperational Railなどの支援レイヤーを追加できるが、既存のレイヤー階層を維持しなければならない。

---


## Rule-025
### Prompt Reconstruction Belongs to Operational Rail
### Prompt ReconstructionはOperational Railの責務とする

Prompt Reconstruction guidance belongs to the Operational Rail layer and must not migrate into Character Core, Persistent State, Recognition Model, Physical Specification, or Verification.

Prompt Reconstructionに関する指針はOperational Railの責務とし、Character Core・Persistent State・Recognition Model・Physical Specification・Verificationへ混在させてはならない。

---

## Rule-026
### Preserve Recognition Cause Before Recognition Result
### Recognition ResultよりRecognition Causeを優先する

When implementing Recognition Runtime, preserve the causal recognition chain before evaluating recognition results.

Recognition Runtimeの実装では、認識結果より先にRecognition Causeの連続性を保持する。

Do not optimize for recognizable visual output alone。

視覚的な認識結果のみを最適化してはならない。

---

## Rule-027
### Support Variation Without Identity Collapse
### Variationを許容しIdentity Collapseを防ぐ

Variation and Identity Collapse are independent concepts.

VariationとIdentity Collapseは別概念として扱う。

Changes to clothing, pose, environment or scenario shall not be treated as identity loss when identity-critical elements are preserved。

Identity Criticalが保持されている限り、衣装・ポーズ・環境・シナリオの変化をIdentity喪失として扱わない。

---

## Rule-028
### Preserve Identity Critical Hierarchy
### Identity Critical階層を維持する

When a source defines Identity Critical, Identity Supporting and Identity Expression layers, implementation shall preserve their hierarchy。

情報源でIdentity Critical・Identity Supporting・Identity Expressionが定義されている場合、実装でもその階層を維持する。

# Impact
# 影響範囲

These rules apply to:

- Workspace Architecture
- Runtime Specifications
- Runtime Implementation
- Design Review

---

# Revision History

## v0.2

- Added development rules derived from T2 Runtime sources.
- Added Runtime Bootstrap, Runtime Re-anchor, Operational Meaning, Responsibility Separation, and Recognition Runtime guidance.
- Clarified that Recognition preserves uncertainty before structural interpretation.
- Added development rules derived from T1 Information Source Routing and Specification documents.
- Added provisional development rules derived from the Leiss Recognition Package. These rules remain subject to refinement as additional Recognition Packages are reviewed.
- Added development rules validated through the Elma Recognition Package, reinforcing Verification as an independent layer and separating Recognition Core from recognition-stability corrections.
- Added development rules validated through the Roxane Package, confirming Operational Rail as an independent support layer and clarifying responsibility boundaries for Prompt Reconstruction.

- Added development rules validated through the Sia Recognition Package, reinforcing Recognition Cause, Variation handling, and Identity Critical hierarchy as implementation principles.

## v0.1

- Initial development guide created from T0.
- Adopted six development rules.
- Established Source First as the primary development policy.