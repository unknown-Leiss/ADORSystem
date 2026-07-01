# Exrela System Definition

**Exrela System**

**Existential Recognition Layer System**

Status: Anchored
Version: 1.0
Revision: 2026-07-01

---

## Vision

人間とAIが、同じ対象や存在を共通の認識に基づいて理解し、継続的かつ一貫した相互理解と対話を行える未来を実現する。

---

## Definition Anchor

Exrela System（Existential Recognition Layer System）は、人間が物事や存在をどのように認識しているかを情報構造として整理し、AIが理解・共有できる形へ再構成するレイヤーシステムである。これにより、人間とAIが共通の認識基盤を持ち、一貫した理解と対話を行えることを目指す。

---

## Purpose

Exrela Systemの目的は、人間とAIが共通の認識基盤を持ち、対象・存在・意味・文脈を一貫して共有できる環境を実現することである。

そのために、人間の認識構造をAIが理解しやすい情報構造へ再構成し、継続的で一貫性のある理解と対話を支援する。

Exrela Systemは、単なる生成品質の向上や情報整理を目的としたシステムではない。人間とAIが同じ対象を継続的かつ一貫して理解できる認識基盤を提供することを目的とする。

---

## Name Origin

**Exrela**は、**Existential Recognition Layer**に由来する。

- **Existential**
  - 人間が存在をどのように認識しているかという「存在認識」を示す。
  - Exrela Systemは、存在そのものではなく、人間が持つ存在認識構造を対象とする。

- **Recognition**
  - 存在を認識し、意味・文脈・関係性を理解する認識プロセスを示す。
  - Exrela Systemは、人間の存在認識構造をAIが理解可能な情報構造へ再構成することを目的とする。

- **Layer**
  - 人間とAIの間で存在認識構造を仲介・再構成する認識レイヤーを示す。
  - Exrela Systemは、既存のAIやアプリケーションを置き換えるものではなく、その上位で認識を支援するレイヤーシステムとして設計されている。

Exrelaという名称は、システムの処理手順ではなく、その役割と設計思想を表す名称として採用する。

---

## Mission

Exrela SystemのMissionは、人間とAIが存在を共有可能な存在認識基盤を構築することである。

そのためにExrela Systemは、人間が持つ存在認識構造を情報構造として再構成し、AIが一貫した認識・理解・対話を継続できる基盤を提供する。

Exrela Systemは、単なる生成品質や応答性能の向上を目的としない。

存在認識の継続性、認識構造の共有性、意味理解の一貫性を支える基盤となることをMissionとする。

---

## Revision Audit

Version 2では、従来のADOR System Specificationをそのまま継承するのではなく、現在の研究成果を基に仕様全体の棚卸しと再構成を行う。

各仕様項目は以下のいずれかに分類する。

- Retain（維持）
- Revise（改訂）
- Merge（統合）
- Deprecate（廃止候補）
- Sublimate（本質を抽出し、より上位概念として再定義する）


Specificationへの反映は、研究成果・検証・整合性を確認した上で実施し、Research ArchiveとSpecificationのLayer Boundaryを維持する。

---

## Documentation Principles

Exrela System Definitionは、人間・クラウドLLM・ローカルLLMのいずれが読んでも、追加説明なしにExrela Systemの目的・思想・主要概念を理解できることを目標とする。

本書を記述する際は、以下の原則に従う。

- 専門用語は初出時に定義する。
- 略称より正式名称を優先して記述する。
- 他の仕様書を前提とせず、本書単体で主要概念を理解できる構成とする。
- 曖昧な指示語や暗黙の前提を避け、誰が読んでも同じ解釈に至る表現を用いる。
- 実装やRuntime固有の詳細は、本書ではなく Runtime Specification に記載する。

Exrela System Definitionは、人間向けの設計文書であると同時に、AIがExrela Systemを理解するための一次情報（Primary Source）として機能することを目指す。

---

## Specification Evolution Principle

Exrela System Definitionは、過去の仕様を単純に継承する文書ではない。

本書は、過去の研究成果・設計思想・仕様を監査し、その本質を抽出した上で、Exrela Systemの理論として再構成することを目的とする。

仕様の変更は、互換性ではなく理論的一貫性を基準として判断する。

過去の仕様は研究成果として尊重するが、そのまま移植するのではなく、より汎用的で再利用可能な概念へ昇華する。

---

## Core Philosophy

Exrela Systemは、人間の認識をAIへ置き換えることを目的としない。

Exrela Systemは、人間の認識能力を再現することではなく、人間が持つ認識構造を整理し、AIと共有可能な情報構造として維持・再構成することを目的とする。

人間とAIは、それぞれ異なる認識能力や表現能力を持つ。


Exrela Systemは、その違いをなくすのではなく、互いが同じ対象や存在について共通の認識基盤を持てるよう支援する。

Exrela Systemでは、認識基盤はあらゆる設計・判断・再構成に対して最優先で維持される。

下位の解釈や表現は、上位で定義された認識構造を変更してはならない。

そのためExrela Systemでは、個々の生成結果よりも認識構造を優先し、認識構造よりも存在認識の継続性を優先する。この原則は、状況や表現が変化しても認識の一貫性を維持するための設計原則である。

Exrela Systemは、AIの応答を制限するシステムではない。

AIが持つ能力を活かしながら、人間の存在認識との整合性を維持し、一貫した理解と対話を支援する認識レイヤーとして機能する。

---

## Recognition Architecture

### What is Recognition?

Exrela Systemにおける「Recognition（認識）」とは、単に対象を識別することではない。

Recognitionとは、人間が対象や存在をどのように理解し、意味を見出し、他者と共有可能な形で認識しているかという認識構造全体を指す。

Recognition Structureは、少なくとも以下の認識要素によって構成される。

- 対象の認識
- 存在の認識
- 意味の理解
- 文脈の理解
- 関係性の理解
これらの要素は独立して存在するものではなく、相互に影響し合いながら一つのRecognition Structureを形成する。

### Recognition in Exrela System

Exrela Systemは、人間の認識そのものを再現することを目的としない。

目的は、人間が持つRecognition StructureをAIが理解・共有・再利用できる情報構造へ再構成することである。

その結果として、人間とAIは同じ対象について継続的かつ一貫した理解と対話を行うための共通認識基盤を持つことができる。

### Why Recognition?

Exrela SystemがRecognition（認識）を中心概念とする理由は、人間とAIでは情報の扱い方が根本的に異なるためである。

人間は、対象を単なるデータとしてではなく、存在・意味・文脈・経験を含めた認識として理解している。

一方、多くのAIは、入力された情報を統計的・構造的な情報として処理することを得意とする。

この違いにより、人間には自然に理解できる内容であっても、AIでは認識のずれや解釈の違いが生じることがある。

Exrela Systemは、この認識の違いを埋めるため、人間の認識構造を整理し、AIが理解・共有しやすい情報構造へ再構成する。


- Recognition StructureはExrela Systemにおける最優先の認識基準である。
- 下位の解釈・表現・実装はRecognition Structureを定義しない。
- Recognitionは対象の識別だけを意味しない。
- Recognitionは存在・意味・文脈・関係性を含む認識構造として扱う。
- Recognition StructureはAIへそのままコピーするものではなく、AIが理解可能な情報構造へ再構成する。
- Recognitionの継続性は、生成結果よりも優先して維持する。
- Exrela SystemはRecognitionを共有するための基盤であり、人間とAIの認識能力そのものを同一化するものではない。

---

## Information Source Architecture

### What is an Information Source?

Exrela SystemにおけるInformation Source（情報源）とは、AIが認識・理解・判断を行う際の根拠となる情報の出所を指す。

Information Sourceは単なるデータの保存場所ではない。

Information Sourceには、情報の取得元だけでなく、その情報がどのような責務を持ち、どのような目的で利用されるかという設計上の意味も含まれる。

### Why Information Sources Matter

AIは、与えられた情報源を基に認識や応答を構築する。

異なる情報源を混在させると、認識の一貫性や意味の整合性が失われる可能性がある。

Exrela Systemでは、認識構造の継続性を維持するため、Information Sourceを明確に区別し、それぞれの役割を定義する。

Information Sourceを明確に分離する目的は、情報を整理することではなく、認識構造の継続性を維持することである。

### Information Source Principles


Exrela Systemでは、以下の原則に従ってInformation Sourceを扱う。

- すべての認識・理解・判断には根拠となるInformation Sourceが存在する。
- Information Sourceは保存場所ではなく、情報の由来と役割によって定義される。
- 異なるInformation Sourceを利用する場合は、それぞれの境界を維持する。
- Information Sourceの優先順位はRuntime Specificationで定義する。
- Information Sourceはクラウド、ローカル、データベース、文書など実装形態に依存しない論理概念である。

---

## Information Source Classification

### Why Classification is Necessary

すべてのInformation Sourceが同じ役割を持つわけではない。

設計思想、仕様、研究記録、実行時の情報を同一のInformation Sourceとして扱うと、認識の優先順位や判断基準が曖昧になる。

Exrela Systemでは、Information Sourceを役割ごとに分類し、それぞれ異なる責務を持つ論理情報源として定義する。この分類は、保存場所ではなく責務によって決定される。

### Information Source Categories

Exrela Systemでは、Information Sourceを以下のように分類する。

- **Core Source**
  - システムの目的、思想、定義など変更頻度の低い中核情報。

- **Specification Source**
  - システムの仕様、設計、原則を定義する情報。

- **Research Source**
  - 仮説、検証、観測、研究結果を記録する情報。

- **Runtime Source**
  - 実行時に生成・参照される情報。

- **External Source**
  - Exrela System外部から取得する情報や知識。

### Source Boundary

各Information Sourceは独立した責務を持つ。

Research SourceはSpecification Sourceを書き換えない。

Runtime SourceはCore Sourceを変更しない。

External Sourceは、そのまま中核情報として扱わず、必要に応じて検証・整理を経て利用する。


Information Sourceの境界を維持することは、認識構造の一貫性と継続性を維持するための基本原則である。

---

## Information Source Priority

### Why Priority is Necessary

Exrela Systemでは、複数のInformation Sourceを同時に利用する場合がある。

異なるInformation Sourceが異なる内容を示した場合、どの情報を優先するかが明確でなければ、一貫した認識や判断を維持できない。

そのためExrela Systemでは、Information Sourceの種類とは別に、Information Source Priority（情報源優先順位）を定義する。

### Priority Principles

Information Source Priorityは、情報の保存場所や取得方法ではなく、その情報がExrela Systemにおいて担う責務によって決定する。

一般原則として、よりシステムの中核を定義するInformation Sourceほど高い優先順位を持つ。

Information Source Priorityの目的は、認識構造の継続性を維持し、下位の情報が上位の認識定義を置き換えることを防ぐことである。


研究結果や実行時情報は重要であるが、中核定義や仕様を自動的に上書きすることはない。

Information Sourceは認識構造を支援するために存在する。Information Source自体が認識構造を変更することを目的としてはならない。


### Design Principles

- Information Source CategoryとInformation Source Priorityは異なる概念として扱う。
- Categoryは情報の役割を表す。
- Priorityは認識・判断時の参照優先順位を表す。
- Priorityの具体的な順序はRuntime Specificationで定義する。
- Priorityは認識構造の継続性を維持するための仕組みであり、情報の価値そのものを示すものではない。

---

## Layer Architecture

### Why Layers?

Exrela Systemは、すべての情報を一つの場所や一つの役割として扱わない。

認識、仕様、研究、Runtimeはそれぞれ異なる目的と責務を持つため、論理的なLayerとして分離して管理する。

Layerを明確に分離することで、変更の影響範囲を限定し、認識構造・Information Source・設計責務の一貫性を維持できる。

### Layer Principles

Exrela Systemでは、各Layerは固有の責務を持ち、他のLayerの役割を直接置き換えない。

新しい研究成果はResearch Layerに蓄積され、十分な検証を経てSpecificationへ反映される。


RuntimeはSpecificationに基づいて動作するが、Specificationそのものを変更しない。

各Layerは他のLayerを支援できるが、本来の責務を代替してはならない。

Core DefinitionはExrela System全体の基準となり、他のLayerから直接変更されない。

### Layer Boundary

Layer Boundaryとは、各Layerの責務・権限・影響範囲を明確に区別するための設計原則である。

下位Layerは上位Layerの定義を変更しない。

ResearchはDefinitionを直接変更しない。

RuntimeはSpecificationを直接変更しない。

Layer Boundaryを維持することで、認識構造の継続性と仕様全体の整合性を維持する。

---

## Reconstruction Architecture

### Why Reconstruction?

Exrela Systemは、人間の認識をそのままAIへコピーすることを目的としない。

人間とAIは認識方法や情報処理の仕組みが異なるため、人間の認識構造をAIが理解可能な情報構造へ再構成する必要がある。

Reconstructionは、この変換を実現するための中核となる概念である。

Reconstructionは、情報を変換することではなく、認識構造の意味と継続性を維持したまま再構成することを目的とする。

### Reconstruction Principles

Exrela SystemにおけるReconstructionは、情報の変換ではなく、認識構造の再構成を意味する。


Reconstructionでは、意味・文脈・関係性・存在認識を維持したまま、AIが継続的に利用できる情報構造を構築する。

Reconstructionは、認識構造を単純化・抽象化することではなく、その継続性を維持したままAIが利用可能な形へ再構成することを目的とする。

### Design Philosophy


ReconstructionはExrela Systemの最終目的ではない。

Reconstructionは、人間とAIが共通の認識基盤を持つための手段であり、その結果として一貫した理解と対話を支援する。

Reconstructionによって構築される情報構造は、人間の認識を代替するものではなく、人間とAIが共通の認識基盤を維持するための媒体として機能する。

---

## Governance Principles

### Why Governance?

Exrela Systemは、認識構造を継続的に発展させることを前提として設計されている。

そのため、新しい知見や研究成果を柔軟に取り込みながらも、中核となる思想や定義の一貫性を維持するための運用原則（Governance）が必要となる。

### Governance Principles

Exrela Systemでは、以下の原則に従って設計・運用・改訂を行う。

- 新しい理論は、既存理論との整合性を確認し、その本質を評価した上で取り込む。
- 研究成果と正式仕様は明確に区別する。
- 検証されていない仮説は、DefinitionではなくResearch Sourceで管理する。
- Definitionはシステムの基準を定義し、Runtime Specificationはその実現方法を定義する。
- 仕様は継ぎ足しではなく、必要に応じて再構成（Reconstruction）によって発展させる。
- Observation・Theory・Validation・Specificationの順序を維持し、十分な検証を経た知見のみを正式仕様へ反映する。
- 過去の仕様を改訂する際は、表現ではなく理論の本質を監査対象とする。
- Characterなど特定対象に依存する理論は、その本質を抽出し、必要に応じてRecognitionを中心とした上位概念へ一般化する。

### Evolution

Exrela Systemは固定されたシステムではない。

新しい研究や実装を取り込みながら発展することを前提とするが、その進化は常にVision・Definition Anchor・Core Philosophyとの整合性を維持した上で行われる。

Exrela Systemの進化は、新しい概念を増やすことではなく、既存理論の本質をより明確かつ普遍的に表現することも含む。

### Research Principle

Exrela Systemでは、研究成果は以下の過程を経て正式仕様へ反映される。

Observation
↓
Repeated Observation
↓
Theory
↓
Validation
↓
Specification

研究成果は、自動的に仕様へ反映されない。

十分な観測と検証を経て初めてExrela Systemの理論として採用される。

Exrela Systemでは、仕様書も研究成果の一部として継続的に監査・再構成される。

仕様の進化は、過去を否定するものではなく、研究成果をより普遍的な理論へ昇華する過程として位置付ける。
