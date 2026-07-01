# ADORSystem Workspace Architecture
# ADORSystem ワークスペース設計

## Document Status
## 文書状態

- Version: v0.1
- Status: Draft / Workspace Skeleton
- Scope: Workspace architecture only

- バージョン: v0.1
- 状態: 草案 / ワークスペース骨組み
- 範囲: ワークスペース設計のみ

This document does not define the ADOR Runtime specification.

このドキュメントは、ADOR Runtimeそのものの仕様を定義しない。

---

## Purpose
## 目的

This document defines the workspace architecture of ADORSystem.

このドキュメントは、ADORSystemのワークスペース構造を定義する。

The workspace separates research, development, and deployment in order to preserve source integrity and maintain a stable development process.

ワークスペースは、情報源の完全性を保ち、安定した開発プロセスを維持するために、研究・開発・配布の役割を分離する。

The workspace exists to transform conversational knowledge into maintainable specifications so that development can continue without reconstructing previous conversations.

ワークスペースは、対話によって得られた知見を保守可能な仕様へ変換し、過去チャットを再構築しなくても開発を継続できる状態を実現するために存在する。

---

## Workspace Layers
## ワークスペース階層

ADORSystem workspace is organized into three layers.

ADORSystemのワークスペースは、三つの階層に分けて扱う。

1. Research Layer
2. Development Layer
3. Deployment Layer

1. 研究層
2. 開発層
3. 配布層

---

## Workspace Philosophy
## ワークスペース思想

ADORSystem Workspace is not a storage layout.

ADORSystem Workspaceは単なるフォルダ構成ではない。

It is the operational architecture that separates research, development, and deployment while preserving source integrity.

情報源の完全性を維持しながら、研究・開発・配布を分離する運用アーキテクチャである。

The workspace exists so that each layer has a single primary responsibility.

各Layerは一つの主要責務だけを持つことを目的とする。

Workspace specifications serve as the development gate.

Runtime implementation should begin only after the required specifications have been reviewed.

ワークスペース仕様書は開発ゲートとして機能する。

必要な仕様がレビューされた後にのみ、Runtime実装を開始する。

The following promotion path is the standard development path.

以下の昇格経路を標準開発経路とする。

Research
↓
Specification
↓
Implementation
↓
Verification
↓
Deployment

研究
↓
仕様
↓
実装
↓
検証
↓
配布

---

## AI Independence
## AI非依存方針

ADORSystem is AI-agnostic.

ADORSystemは特定のAIに依存しない。

The workspace architecture shall remain valid regardless of the inference engine used.

ワークスペース設計は利用する推論エンジンに依存しない。

The same Research Layer, Development Layer, and Deployment Layer shall support cloud AI, local AI, and future AI implementations.

Research Layer・Development Layer・Deployment Layerは、クラウドAI・ローカルAI・将来のAI実装を共通して支援する。

AI is treated as a Runtime consumer rather than the owner of the knowledge assets.

AIは知識資産の所有者ではなく、Runtimeを利用する実行主体として扱う。

---

## 1. Research Layer
## 1. 研究層

### Workspace Position
### ワークスペース上の位置付け

The Research Layer is the authoritative source layer of ADORSystem.

研究層はADORSystemの正規情報源層である。

It preserves knowledge before implementation and supplies validated sources to the Development Layer.

実装前の知識を保持し、検証済み情報源をDevelopment Layerへ供給する。

### Purpose
### 目的

The Research Layer is the information source layer.

研究層は、情報源として扱う層である。

It stores official sources, research archives, character packages, runtime sources, and historical records.

研究層は、正本となる情報源、研究アーカイブ、キャラクターパッケージ、Runtime Source、履歴資料を保管する。

### Current Location
### 現在の配置

- Global ADORLibrary (Google Drive)

- Global ADORLibrary（Google Drive）

### Contains
### 含むもの

- T0_Index
- T1_Core
- T2_Runtime
- T3_Dossiers
- T4_ResearchArchive

The current canonical Research Layer structure is:

現在のResearch Layerの正規構成は以下とする。

```text
Research Layer
├── T0_Index
├── T1_Core
├── T2_Runtime
├── T3_Dossiers
└── T4_ResearchArchive
```

### Must
### やること

- Preserve source documents.
- Preserve research history.
- Preserve official and candidate runtime sources.

- 情報源を保持する。
- 研究履歴を保持する。
- 正式または候補段階のRuntime Sourceを保持する。

- Preserve research artifacts before specification review.
- Promote only reviewed and approved content into the Development Layer.

- 研究成果は仕様レビュー前の状態で保持する。
- レビュー・承認された内容のみをDevelopment Layer（開発層）へ昇格させる。

### Must Not
### やらないこと

- Do not treat implementation files as official sources by default.
- Do not mix temporary development notes with official source documents without classification.

- 実装ファイルを自動的に正本として扱わない。
- 一時的な開発メモを分類なしに正式情報源へ混在させない。

### Boundary
### 境界

Research Layer stores information sources.

研究層は情報源を保管する。

It does not function as the implementation workspace.

実装ワークスペースとして利用しない。

Research Layer
≠
Development Layer

Information Source
≠
Implementation

Research archives must remain distinguishable from runtime implementations.

研究資料とRuntime実装は常に区別可能な状態を維持する。

---

## 2. Development Layer
## 2. 開発層

### Purpose
### 目的

The Development Layer is the workspace for designing and implementing ADORSystem.

開発層は、ADORSystemを設計し実装するための作業領域である。

It connects source documents to local specifications and implementation.

開発層は、情報源をローカル仕様書と実装へ接続する。

### Current Location
### 現在の配置

- Local ADORSystem (Mac)
- Development workspace built on top of the Local ADORLibrary.

- Local ADORSystem（Mac）
- Local ADORLibrary上に構築される開発ワークスペース。

### Contains
### 含むもの

- docs
- runtime
- Git repository
- tests / future
- logs / future

- docs
- runtime
- Gitリポジトリ
- tests / 将来
- logs / 将来

### Internal Structure
### 内部構造

The Development Layer is organized as follows.

開発層は以下の構造で構成される。

```text
Development Layer
├── 00_Workspace_Architecture
├── 01_Recognition_Runtime
├── 90_Development_Guide
├── 91_Runtime_Implementation_Map
├── 92_Runtime_Module_Specification
├── 93_Runtime_Development_Log
├── runtime/
├── tests/
└── Git Repository
```

Development documents define the architecture before runtime implementation.

開発文書はRuntime実装より先に設計を定義する。

### Must
### やること

- Define local specifications before implementation.
- Review source documents before changing runtime behavior.
- Keep implementation aligned with documented architecture.

- 実装前にローカル仕様を定義する。
- Runtime挙動を変更する前に情報源を確認する。
- 実装を文書化された設計と一致させる。

- Convert important design decisions into specifications before implementation.
- Use docs as the primary implementation review reference.

- 重要な設計判断は実装前に仕様へ昇格させる。
- docsを実装レビューの第一基準として利用する。

### Must Not
### やらないこと

- Do not implement from memory alone.
- Do not promote proposals to specification without review.
- Do not treat generated output as a source document.

- 記憶だけで実装しない。
- レビュー前の提案を仕様として扱わない。
- 生成結果を情報源として扱わない。

### Boundary
### 境界

Development Layer is the implementation workspace.

開発層は実装作業領域である。

It receives reviewed source understanding from the Research Layer and converts it into local specifications, runtime code, tests, and development logs.

研究層からレビュー済みの情報源理解を受け取り、ローカル仕様・Runtimeコード・テスト・開発ログへ変換する。

Development Layer
≠
Research Layer

Development Specification
≠
Information Source

Implementation
≠
Specification

docs are local development specifications.

docsはローカル開発仕様である。

docs are not the ADORLibrary itself.

docsはADORLibraryそのものではない。

runtime/ implements specifications.

runtime/ は仕様を実装する。

runtime/ is not the source specification itself.

runtime/ は仕様そのものではない。

---

## 3. Deployment Layer
## 3. 配布層

### Purpose
### 目的

The Deployment Layer is the future portable runtime environment.

配布層は、将来的な可搬Runtime環境である。

It is intended to allow ADOR Runtime to be carried on USB or SSD and used outside the development machine.

USBまたはSSDでADOR Runtimeを持ち運び、開発母艦以外の環境でも利用できるようにすることを目的とする。

### Future Target
### 将来の配置

- Portable SSD
- USB storage
- Portable ADOR Runtime package

- 外付けSSD
- USBストレージ
- 可搬ADOR Runtimeパッケージ

### Must
### やること

- Contain only what is required to run the portable runtime.
- Preserve separation from research archives.

- 可搬Runtimeの実行に必要なものだけを含める。
- 研究アーカイブとは分離する。

### Must Not
### やらないこと

- Do not carry unnecessary research archives by default.
- Do not treat deployment output as the original source.

- 不要な研究アーカイブを標準で持ち運ばない。
- 配布物を元の情報源として扱わない。

### Boundary
### 境界

Deployment Layer is the operational runtime layer.

配布層は運用Runtime層である。

It packages verified implementations for execution outside the development environment.

検証済みの実装を、開発環境外で実行可能な形へまとめる。

Deployment Layer
≠
Development Layer

Deployment Package
≠
Development Workspace

Deployment Output
≠
Information Source

Portable packages must not become the authoritative source.

可搬パッケージを正規情報源として扱ってはならない。

Deployment packages should contain only the minimum components required for execution.

配布パッケージには実行に必要な最小構成のみを含める。

---

## Layer Relationship
## 階層関係

```mermaid
flowchart TD
    A[Research Layer<br/>Global ADORLibrary (Google Drive)] --> B[Development Layer<br/>Local ADORSystem (Mac)]
    B --> C[Deployment Layer<br/>Portable Runtime]
```

### Global and Local Architecture
### Global / Local アーキテクチャ

The Research Layer is represented by the Global ADORLibrary.

Research LayerはGlobal ADORLibraryとして実体化される。

The Development Layer is represented by the Local ADORSystem.

Development LayerはLocal ADORSystemとして実体化される。

The Local ADORSystem synchronizes required knowledge assets from the Global ADORLibrary and uses them for specification, implementation, verification, and runtime development.

Local ADORSystemはGlobal ADORLibraryから必要な知識資産を同期し、仕様・実装・検証・Runtime開発へ利用する。

Research Layer provides source documents.

研究層は情報源を提供する。

Development Layer converts source understanding into local specifications and implementation.

開発層は、情報源の理解をローカル仕様と実装へ変換する。

Deployment Layer packages the verified runtime for portable use.

配布層は、検証済みRuntimeを可搬利用できる形へまとめる。

Development Flow

Research Layer
↓
Development Documents (00–93)
↓
Runtime Implementation
↓
Verification
↓
Deployment Layer

研究層
↓
開発文書（00〜93）
↓
Runtime実装
↓
検証
↓
配布層

### AI Integration
### AI統合

Global ADORLibrary
        ↓
Local ADORSystem
        ↓
AI Adapter
        ↓
ChatGPT / Local LLM / Future AI

The architecture intentionally separates knowledge assets from AI implementations.

本アーキテクチャは知識資産とAI実装を意図的に分離する。

Changing the AI implementation must not require redesigning the workspace.

AIを変更してもWorkspace設計を変更してはならない。

---

## Documentation Rule
## 文書作成ルール

All workspace specifications should be written in both English and Japanese.

すべてのワークスペース仕様書は、英語と日本語を併記する。

English provides technical structure.

英語は技術構造を記述する。

Japanese provides operational clarification and human readability.

日本語は運用上の意味と人間が読める理解を補足する。

Chat conversations are discussion records.

Workspace specifications are the authoritative development reference.

チャットは議論の記録である。

ワークスペース仕様書を開発時の正規参照先とする。

---

## Open Questions
## 未確定事項

### Local ADORSystem Migration
### 開発環境移行条件

Define the conditions required before promoting the Mac local environment to the primary development workspace.

Macローカル環境を正式な開発母艦とするために満たすべき条件を定義する。

Migration Criteria

- Workspace Architecture v1.0 is completed.
- The fundamental structure of docs is established.
- Git workflow has been established.
- The role of Google Drive as the Research Layer has been organized.

移行条件

- Workspace Architecture v1.0 が完成していること。
- docs の基本構造が確立していること。
- Git運用が確立していること。
- Google Drive を Research Layer（情報源）として整理し終えていること。

- What exact files should remain in Research Layer?
- What exact files should be copied into Development Layer?
- What should be included in the first portable Deployment Layer package?

- 研究層に残すファイルは何か。
- 開発層へコピーするファイルは何か。
- 最初の可搬配布パッケージに何を含めるか。

---

## Revision History
## 改訂履歴

### v0.1

- Created initial workspace architecture skeleton.
- Defined Research Layer, Development Layer, and Deployment Layer.
- Added English / Japanese documentation rule.

- Defined layer boundaries for Research, Development, and Deployment.
- Established Workspace Philosophy and Development Gate.
- Formalized Research Layer as the authoritative source layer.

- ワークスペース設計の初期骨組みを作成。
- 研究層、開発層、配布層を定義。
- 英語・日本語併記ルールを追加。

- 研究層・開発層・配布層の境界を定義。
- Workspace Philosophy と Development Gate を追加。
- Research Layerを正規情報源層として正式化。