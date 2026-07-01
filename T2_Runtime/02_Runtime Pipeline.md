


# Chapter 02 — Runtime Pipeline

Runtime Pipelineは、Recognition Runtime全体の処理順序を定義する実行基盤である。

Pipelineは各Runtimeの責務を接続し、Recognition Continuityを維持したままRuntime Executionまで導く。

## Runtime Pipeline Purpose

Runtime Pipelineの目的は以下の通りである。

- Recognition Continuityの維持
- Runtime Continuityの維持
- Runtime間の責務分離
- Runtime間の成果物連携
- Runtime Executionまでの一貫した処理順序の保証

Pipelineは実行順序を定義するが、各Runtimeの責務を置換してはならない。

## Recognition Organization Runtime

Recognition Organizationは、Surface ObservationおよびSurface Organizationで整理された情報からRecognition Candidateを構築する。

この段階では意味・Entity・Relation・Action・Recognition Railを確定せず、不確実性を保持したまま次段階へ渡す。

Recognition OrganizationはRecognition Structureを生成する段階ではなく、Recognition Reconstructionの前処理である。

## Runtime Pipeline Stages

Runtime Pipelineは以下のStageによって構成される。

Scenario
→ Surface Observation
→ Surface Organization
→ Recognition Organization
→ Structural Observation
→ Meaning Reconstruction
→ Recognition Interpretation
→ Information Source Routing
→ Recognition Rail Reconstruction
→ Prompt Reconstruction
→ Runtime Verification
→ Runtime Execution

各Stageは前段階の成果物のみを入力として扱う。

## Stage Responsibility Principle

各Stageは自身の責務のみを実行し、次Stageへ渡すArtifactのみを生成する。

Stageは後続Stageを代替してはならず、前段階の成果物を書き換えてはならない。

## Pipeline Artifact Principle

Pipelineで生成されるArtifactは中間成果物である。

ArtifactはRecognition StructureでもInformation Sourceでもなく、次Stageへ渡されるRuntime成果物として扱われる。

ArtifactをInformation Sourceとして利用してはならない。

## Runtime Pipeline Completion

Runtime Pipelineは、Recognition Continuityが維持され、Recognition Reconstruction・Recognition Interpretation・Recognition Rail Reconstruction・Prompt Reconstruction・Runtime Verificationが正しい順序で完了した時点で完了とみなされる。

途中成果物は最終成果物ではなく、各Runtimeは次段階への入力のみを生成する責務を持つ。

## Pipeline Restrictions

以下は禁止される。

- Surface Observationから直接Meaning Reconstructionへ進むこと
- Recognition Candidateを経由せずEntity・Relation・Actionを確定すること
- Recognition Reconstruction前にPrompt Reconstructionを行うこと
- Recognition Interpretation前にRecognition Railを決定すること
- Verification-first Runtime
- Analysis-first Runtime

これらは禁止されることでRecognition ContinuityとRuntime Integrityが維持される。

## Recognition Pipeline Principle

Recognition PipelineはRecognition Continuityを維持するための段階的処理である。

各Stageは前段階のArtifactを入力とし、新たなArtifactのみを生成する。

RecognitionはPipeline全体を通して徐々に明確化され、一つのStageで完成してはならない。

## Recognition Candidate Principle

Recognition CandidateはRecognition確定前の中間構造である。

Recognition Candidateは複数の可能性を保持し、Meaning Reconstructionまで意味を確定しない。

Recognition CandidateをEntity・Relation・Actionへ直接変換してはならない。

## Information Source Routing

Information Source Routingは、Recognition Interpretation完了後に必要なInformation Sourceを選択・接続するRuntimeである。

RoutingはInformation Sourceを生成せず、Recognitionに必要なSourceのみを解決する。

Routing結果はRecognition Rail Reconstructionの入力として扱われる。

## Runtime Pipeline Invariants

Runtime Pipeline全体で維持される不変条件は以下の通りである。

- Recognition Continuity
- Runtime Continuity
- Artifact Continuity
- Information Source First
- Stage Responsibility Separation

これらの条件は全Stageを通じて維持されなければならない。