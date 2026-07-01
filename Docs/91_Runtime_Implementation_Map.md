
# Exrela System Runtime Implementation Map
# Exrela System Runtime 実装対応表

## Document Status
## 文書状態

- Version: v0.1
- Status: Draft / Initial Mapping
- Source Basis: 90_Development_Guide.md
- Scope: Mapping development rules to runtime implementation areas

- バージョン: v0.1
- 状態: 草案 / 初期対応表
- 情報源基準: 90_Development_Guide.md
- 範囲: 開発ルールとRuntime実装領域の対応整理

This document maps development rules to implementation areas.

この文書は、開発ルールを実装領域へ対応付ける。

This document does not define Exrela philosophy, Recognition identity, or Runtime source rules.

この文書は、Exrela思想・Recognition Identity・Runtime Source Ruleを定義しない。

---

## Purpose
## 目的

This document connects 90_Development_Guide rules to concrete runtime modules and implementation checks.

この文書は、90_Development_Guide の開発ルールを、具体的なRuntimeモジュールおよび実装確認項目へ接続する。

90 defines what developers must preserve.

90は、開発者が何を守るべきかを定義する。

91 defines where those rules affect implementation.

91は、それらのルールが実装上どこへ影響するかを整理する。

---

## Responsibility Boundary
## 責務境界

### 90_Development_Guide
### 90_Development_Guide

Defines development rules.

開発ルールを定義する。

### 91_Runtime_Implementation_Map
### 91_Runtime_Implementation_Map

Maps development rules to implementation areas and files.

開発ルールを実装領域およびファイルへ対応付ける。

### Runtime Code
### Runtime Code

Implements runtime behavior.

Runtime挙動を実装する。

---

## Mapping Format
## 対応表フォーマット

Each mapping entry should use the following structure.

各対応項目は、以下の構造で記録する。

```text
Rule:
Affected Runtime Area:
Affected Files:
Implementation Check:
Status:
Notes:
```

---

## Initial Priority Mapping
## 初期優先対応表

### Rule-011 — Recognition Preserves Uncertainty
### Rule-011 — Recognitionは不確実性を保持する

Affected Runtime Area:

- Recognition Runtime
- Recognition Resolution
- Structural Observation

Affected Files:

- runtime/recognition_engine.py
- runtime/recognition_resolution.py
- runtime/structural_observation.py

Implementation Check:

- Recognition candidates are generated without premature semantic commitment.
- Structural classification is delayed until the appropriate layer.
- Accepted / held / rejected states preserve uncertainty where required.

実装確認:

- Recognition Candidateを早期に意味確定しない。
- 構造分類は適切なLayerまで遅延する。
- accepted / held / rejected によって必要な不確実性を保持する。

Status:

- Active

---

### Rule-026 — Preserve Recognition Cause Before Recognition Result
### Rule-026 — Recognition ResultよりRecognition Causeを優先する

Affected Runtime Area:

- Recognition Runtime
- Structural Observation Runtime
- Meaning Reconstruction Runtime

Affected Files:

- runtime/recognition_modules/
- runtime/recognition_engine.py
- runtime/structural_observation.py
- runtime/meaning_reconstruction.py

Implementation Check:

- Recognition should preserve causal chains rather than only surface results.
- Recognition modules should avoid visual-output-only optimization.
- Meaning Reconstruction should be able to recover why something is recognized, not only what was recognized.

実装確認:

- Recognitionは表面的な結果だけでなく、認識原因の連続性を保持する。
- Recognition Moduleは視覚的出力だけを最適化しない。
- Meaning Reconstructionは「何として認識されたか」だけでなく、「なぜそう認識されるか」を復元できるようにする。

Status:

- Active

---

### Rule-027 — Support Variation Without Recognition Collapse
### Rule-027 — Variationを許容しRecognition Collapseを防ぐ

Affected Runtime Area:

- Meaning Verification Runtime
- Scenario Interpretation Runtime
- Recognition Package Handling

Affected Files:

- runtime/meaning_verification.py
- runtime/scenario_interpretation.py
- runtime/recognition_understanding.py

Implementation Check:

- Scenario, clothing, pose, environment, and expression changes are not automatically treated as recognition loss.
- Recognition-critical elements must be checked before declaring collapse.
- Variation should be separated from Recognition Drift and Recognition Collapse.

実装確認:

- シナリオ・衣装・ポーズ・環境・表情変化を自動的にRecognition喪失として扱わない。
- Collapse判定前にRecognition Critical要素を確認する。
- VariationをRecognition DriftおよびRecognition Collapseから分離する。

Status:

- Active

---

### Rule-028 — Preserve Recognition Critical Hierarchy
### Rule-028 — Recognition Critical階層を維持する

Affected Runtime Area:

- Recognition Understanding Runtime
- Meaning Verification Runtime
- Scenario Interpretation Runtime

Affected Files:

- runtime/recognition_understanding.py
- runtime/meaning_verification.py
- runtime/scenario_interpretation.py

Implementation Check:

- Recognition Critical, Recognition Supporting, and Recognition Expression are preserved as separate layers.
- Runtime evaluation does not treat all extracted elements as equal priority.
- Tier changes are reflected in verification and interpretation.

実装確認:

- Recognition Critical・Recognition Supporting・Recognition Expressionを別Layerとして保持する。
- Runtime評価時に、抽出要素をすべて同じ優先度として扱わない。
- Tierの違いをVerificationおよびInterpretationに反映する。

Status:

- Active

---


---

## Source Management Mapping
## Source Management対応

### Source Provider
### Source Provider

Affected Runtime Area:

- Source Management Runtime

Affected Files:

- runtime/source_provider.py
- runtime/providers/drive_source_provider.py
- runtime/providers/local_source_provider.py
- runtime/providers/package_source_provider.py

Implementation Check:

- Source Provider is storage-independent.
- Providers only discover and read sources.
- Providers do not perform Runtime reconstruction.

実装確認:

- Source Providerは保存先へ依存しない。
- Providerは情報源探索と読込のみを担当する。
- Runtime再構築を担当しない。

Status:

- Planned

---

### Source Discovery
### Source Discovery

Affected Runtime Area:

- Source Discovery Runtime

Affected Files:

- runtime/source_discovery.py

Implementation Check:

- Required sources are identified before Runtime Bootstrap.
- Discovery completes before Source Routing begins.

実装確認:

- Runtime Bootstrap前に必要情報源を決定する。
- Source Routing開始前にDiscoveryを完了する。

Status:

- Planned

---

### Source Routing
### Source Routing

Affected Runtime Area:

- Source Routing Runtime

Affected Files:

- runtime/source_routing.py

Implementation Check:

- Source priority follows the Source Management specification.
- Routing determines which source should be read.

実装確認:

- Source Priorityに従ってRoutingを行う。
- 読み込む情報源を決定する。

Status:

- Active

---

### Source Validation
### Source Validation

Affected Runtime Area:

- Source Validation Runtime

Affected Files:

- runtime/source_validation.py

Implementation Check:

- Validate required sources before Runtime Bootstrap.
- Detect missing or invalid sources.

実装確認:

- Runtime Bootstrap前に情報源を検証する。
- 不足・破損した情報源を検出する。

Status:

- Planned

---

### Source Read
### Source Read

Affected Runtime Area:

- Package Reader Runtime

Affected Files:

- runtime/package_reader.py

Implementation Check:

- Read validated sources.
- Build Runtime input from source contents.

実装確認:

- 検証済み情報源を読み込む。
- Runtime入力を構築する。

Status:

- Active

---

### Runtime Bootstrap
### Runtime Bootstrap

Affected Runtime Area:

- Runtime Bootstrap

Affected Files:

- runtime/bootstrap/runtime_bootstrap.py

Implementation Check:

- Runtime starts only after Source Discovery, Routing, Validation, and Read are complete.

実装確認:

- Discovery・Routing・Validation・Read完了後にのみRuntimeを開始する。

Status:

- Planned

---

## Open Mapping Targets
## 未対応の対応対象

The following rules require mapping after current runtime files are reviewed.

以下のルールは、現在のRuntimeファイル確認後に対応表へ追加する。

- Rule-001 through Rule-010
- Rule-012 through Rule-025

---

## Revision History
## 改訂履歴

### v0.1

- Created initial implementation map.
- Added priority mappings for Recognition Runtime and Recognition Continuity related rules.
- Separated development rules from implementation mapping.

- 初期実装対応表を作成。
- Recognition RuntimeおよびRecognition Continuity関連ルールの優先対応を追加。
- 開発ルールと実装対応表を分離。