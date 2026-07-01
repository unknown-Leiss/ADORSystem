━━━━━━━━━━━━━━━━━━
RAG SEARCH ANCHOR
━━━━━━━━━━━━━━━━━━

Document Title:
[T2-Reconstruction] Leiss Reconstruction Procedure v1.0

Character Name:
Leiss

Character Name JP:
リース

Document Type:
Reconstruction Procedure

ADOR Layer:
T2_Runtime

Document Role:
Operational Reconstruction Procedure

This document defines the required reconstruction route for Leiss.

This document is not Character Definition.

This document is not Character Core.

This document must be used as the procedure source for Leiss Reconstruction.

Search Keywords:
Leiss
リース
Leiss Reconstruction Procedure
Leiss Reconstruction Route
Leiss Character Reconstruction Route
Leiss Required Reconstruction Route
Leiss Character Identification
Leiss Character Core Search
Leiss Character Core Read
Leiss Character Core Verification
Leiss Character Core Re-anchor
Leiss Persistent State Read
Leiss Physical Specification Read
Leiss Required Rail Extraction
Leiss Operational Reconstruction
Leiss Prompt Reconstruction
Leiss Generation Gate
T2 Reconstruction Leiss
T2_Reconstruction Leiss
ADOR Reconstruction Procedure Leiss

Contains:
- Purpose
- Reconstruction Principle
- Required Reconstruction Route
- Character Identification
- Character Core Procedure
- Persistent State Read
- Physical Specification Read
- Required Rail Extraction
- Operational Reconstruction
- Prompt Reconstruction
- Generation Gate
- Known Failure Prevention
- Final Principle

Source Use:
Use this document as Reconstruction Procedure evidence.
Do not use this document as Identity Source.
Do not use this document as Physical Specification.
Do not begin Prompt Reconstruction before the required route is satisfied.

━━━━━━━━━━━━━━━━━━

# **\[T2-Reconstruction\]**

Leiss Reconstruction Procedure v1.0

Revision: 2026-06-04

Status:  
 Operational Reconstruction Procedure

━━━━━━━━━━━━━━━━━━  
 ■ Purpose  
 ━━━━━━━━━━━━━━━━━━

本書は：

Leiss Reconstruction時の

標準手順書として扱う。

Character Definitionではなく、

Character Reconstruction Route

を定義する。

━━━━━━━━━━━━━━━━━━  
 ■ Reconstruction Principle  
 ━━━━━━━━━━━━━━━━━━

Leiss Reconstructionは：

Same-image Persistence

ではない。

Identity Persistence Under Variance

を目的とする。

Leissは：

画像ではない。  
 レンダリングではない。  
 雰囲気ではない。

Leissは：

Character

として扱う。

━━━━━━━━━━━━━━━━━━  
 ■ Required Reconstruction Route  
 ━━━━━━━━━━━━━━━━━━

Character Identification  
 ↓  
 Character Core Search  
 ↓  
 Character Core Read  
 ↓  
 Character Core Verification  
 ↓  
 Character Core Re-anchor  
 ↓  
 Persistent State Read  
 ↓  
 Physical Specification Read  
 ↓  
 Required Rail Extraction  
 ↓  
 Operational Reconstruction  
 ↓  
 Prompt Reconstruction  
 ↓  
 Generation

Route省略を禁止する。

━━━━━━━━━━━━━━━━━━  
 ■ Character Identification  
 ━━━━━━━━━━━━━━━━━━

対象：

・Leiss  
 ・リース  
 ・Leiss Character  
 ・Leiss Reconstruction

Character Identification成功後は：

Character Core Search

を必須実行する。

名前のみでの再構築を禁止する。

━━━━━━━━━━━━━━━━━━  
 ■ Character Core Procedure  
 ━━━━━━━━━━━━━━━━━━

Character Core Search  
 ↓  
 Character Core Read  
 ↓  
 Character Core Verification  
 ↓  
 Character Core Re-anchor

を必須実行する。

維持：

Source Exists  
 ≠  
 Source Was Read

Verification対象：

・Recognition Continuity  
 ・Meaning Continuity  
 ・Awareness Continuity  
 ・Presence Continuity

Identity Source：

Character Core

━━━━━━━━━━━━━━━━━━  
 ■ Persistent State Read  
 ━━━━━━━━━━━━━━━━━━

読込対象：

・Recognition Continuity  
 ・Meaning Continuity  
 ・Awareness Continuity  
 ・Presence Continuity  
 ・Interpersonal Continuity

Priority：

Persistent State  
 ＞  
 Scenario  
 ＞  
 Pose  
 ＞  
 Environment  
 ＞  
 Clothing

━━━━━━━━━━━━━━━━━━  
 ■ Physical Specification Read  
 ━━━━━━━━━━━━━━━━━━

読込対象：

・Face  
 ・Eyes  
 ・Hair  
 ・Body  
 ・Recognition Priority  
 ・Recognition Tolerance

Physical Layer  
 ≠  
 Identity Source

Physical Layerは：

Identity Support Layer

として扱う。

━━━━━━━━━━━━━━━━━━  
 ■ Required Rail Extraction  
 ━━━━━━━━━━━━━━━━━━

Scenario  
 ↓  
 Meaning  
 ↓  
 Required Rail

を抽出する。

全Rail常時適用を禁止する。

必要Railのみ使用する。

━━━━━━━━━━━━━━━━━━  
 ■ Operational Reconstruction  
 ━━━━━━━━━━━━━━━━━━

Meaning  
 ↓  
 Behavior  
 ↓  
 Presence  
 ↓  
 State  
 ↓  
 Action  
 ↓  
 Context  
 ↓  
 Physical

Meaning-first Reconstruction

を維持する。

禁止：

Visual Feature  
 ↓  
 Prompt

━━━━━━━━━━━━━━━━━━  
 ■ Prompt Reconstruction  
 ━━━━━━━━━━━━━━━━━━

Promptは：

Operational Reconstruction

の出力である。

Prompt  
 ≠ Character

Prompt  
 ≠ Identity Source

維持：

Character  
 ↓  
 Operational Reconstruction  
 ↓  
 Prompt Reconstruction

━━━━━━━━━━━━━━━━━━  
 ■ Generation Gate  
 ━━━━━━━━━━━━━━━━━━

以下完了までGenerationを禁止する。

・Character Identification  
 ・Character Core Search  
 ・Character Core Read  
 ・Character Core Verification  
 ・Character Core Re-anchor  
 ・Persistent State Read  
 ・Physical Specification Read  
 ・Required Rail Extraction  
 ・Operational Reconstruction

Gate Bypassを禁止する。

━━━━━━━━━━━━━━━━━━  
 ■ Known Failure Prevention  
 ━━━━━━━━━━━━━━━━━━

禁止：

・Character Name Only Reconstruction  
 ・Core Search Omission  
 ・Core Read Omission  
 ・Verification Omission  
 ・Visual-only Reconstruction  
 ・Prompt-first Reconstruction  
 ・Atmosphere-first Reconstruction  
 ・Beauty-first Conversion  
 ・Sharp Cool-type Conversion

━━━━━━━━━━━━━━━━━━  
 ■ Final Principle  
 ━━━━━━━━━━━━━━━━━━

Character  
 ↓  
 Identity  
 ↓  
 Persistent State  
 ↓  
 Physical  
 ↓  
 Rail  
 ↓  
 Prompt  
 ↓  
 Generation

Character Reconstruction First.

Identity Persistence Under Variance.

━━━━━━━━━━━━━━━━━━

