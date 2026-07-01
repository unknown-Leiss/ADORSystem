# Source Management
# 情報源管理

Status: Draft v0.1

---

## Purpose
## 目的

Define how information sources are created, preserved, transformed, and supplied to the Development Layer.

情報源の生成・保存・変換・開発層への供給方法を定義する。

This document defines the lifecycle of information sources.

本仕様は情報源のライフサイクルを定義する。

---

## Core Principle
## 基本原則

Human Source
≠
AI Source

AI Source
≠
Development Specification

Development Specification
≠
Implementation

Implementation
≠
Deployment

Each stage has a different responsibility.

各段階は異なる責務を持つ。

---

## Document State
## 文書状態

Exrela System manages documents by lifecycle state rather than file format.

Exrela Systemではファイル形式ではなく、文書状態によって管理する。

### Draft

Primary Format

- Google Docs

Purpose

- Research
- Brainstorming
- Human editing
- Collaborative review

Draft documents are expected to change frequently.

ドラフト文書は頻繁な変更を前提とする。

---

### Working

Primary Format

- Markdown

Purpose

- AI-readable source
- Development support
- Git tracking

Markdown is a working copy generated from the current draft.

Markdownは現在のドラフトから生成される作業用複写である。

It may be regenerated at any time.

必要に応じていつでも再生成してよい。

---

### Released

Primary Format

- PDF

Purpose

- Long-term preservation
- Snapshot archive
- Stable reference

Released documents are created only after their contents have been stabilized.

Released文書は内容が安定した後にのみ作成する。

---

## Source Lifecycle
## 情報源ライフサイクル

```text
Draft
(Google Docs)
        ↓
Working
(Markdown)
        ↓
Development Specification
(☆Docs)
        ↓
Runtime Implementation
        ↓
Verification
        ↓
Released
(PDF)
        ↓
Deployment
```

---

## Library Architecture
## ライブラリアーキテクチャ

Exrela Library exists as the canonical knowledge asset.

Exrela Libraryは知識資産として存在する。

Exrela System is the local environment that consumes those knowledge assets to design, implement, verify, and operate Runtime.

Exrela SystemはExrela Libraryを利用してRuntimeを設計・実装・検証・運用するローカル環境である。

### Global Exrela Library

Location

- Google Drive

Purpose

- Canonical research assets
- Human editing
- Cross-device access
- Long-term preservation

The Global Exrela Library is the authoritative research library.

Global Exrela Libraryは研究資産の正本である。

---

### Local Exrela System

Location

- Mac

Purpose

- Runtime development
- Development specifications
- Local LLM execution
- Git management
- PDF generation

The Local Exrela System consumes the Exrela Library and produces implementations.

Local Exrela SystemはExrela Libraryを利用して実装を構築する。

---

### Relationship

```text
Global Exrela Library
(Google Drive)
        ↓
Synchronization
        ↓
Local Source Library
        ↓
Development Specifications
        ↓
Runtime
```

The Global Exrela Library remains the canonical research source.

Global Exrela Libraryは常に研究資産の正本として扱う。

---

## Source Provider
## Source Provider

Exrela System does not depend on a single storage location.

Exrela Systemは単一の保存場所へ依存しない。

Knowledge assets are accessed through a Source Provider abstraction.

知識資産はSource Providerを通じて取得される。

### Supported Providers

- Google Drive Source Provider
- Local Source Provider
- Package Source Provider
- Future Providers

Each provider is responsible only for locating and reading sources.

各Providerは情報源の検索と読込のみを担当する。

They must not perform Runtime reconstruction.

Runtime再構築を担当してはならない。

---

## Source Discovery
## 情報源探索

Source Discovery determines which information sources are required before Runtime Bootstrap.

Source DiscoveryはRuntime Bootstrap前に必要な情報源を決定する。

Typical flow:

```text
Request
    ↓
Source Discovery
    ↓
Source Routing
    ↓
Source Validation
    ↓
Source Read
    ↓
Runtime Bootstrap
```

Source Discovery must complete before Runtime construction begins.

Runtime構築開始前にSource Discoveryを完了しなければならない。

---

## Source Formats
## 情報源フォーマット

### Google Docs

Purpose

Human editing.
Collaborative writing.
Research drafting.

人間による編集。
共同執筆。
研究ドラフト。

Google Docs is the editable master document.

Google Docsは編集可能な原本である。

### PDF

Purpose

Local preservation.
Snapshot archive.

ローカル保存。
スナップショット保管。

PDF is an immutable preservation copy.

PDFは変更しない保存用コピーである。

### Markdown

Purpose

AI-readable source.

AIが読み取る情報源。

Markdown is generated from the editable source.

Markdownは編集元から生成される複写である。

It may be regenerated when necessary.

必要に応じて再生成してよい。

### ☆Docs

Purpose

Development specifications.

開発仕様。

☆Docs define how Runtime should be implemented.

☆DocsはRuntime実装方法を定義する。

They are not the original information source.

情報源そのものではない。

---

## Boundary
## 境界

Google Docs
≠
Markdown

Markdown
≠
☆Docs

☆Docs
≠
Runtime

Runtime
≠
Deployment Package

Information should move through review before being promoted.

情報はレビューを経て昇格する。

Source Provider
≠
Exrela Runtime

Exrela Runtime
≠
AI Adapter

AI Adapter
≠
Executor

---

## Revision History

### v0.1

- Initial Source Management specification.
- Defined source lifecycle.
- Defined Google Docs, PDF, Markdown and ☆Docs responsibilities.
- Defined Global Exrela Library and Local Exrela System responsibilities.
- Added Library Architecture.

- Global Exrela LibraryとLocal Exrela Systemの役割を定義。
- Library Architectureを追加。

- Added Source Provider abstraction.
- Added Source Discovery flow.
- Defined Runtime boundary from Source Provider.

- Source Provider抽象化を追加。
- Source Discoveryフローを追加。
- Source ProviderとRuntimeの責務境界を定義。
