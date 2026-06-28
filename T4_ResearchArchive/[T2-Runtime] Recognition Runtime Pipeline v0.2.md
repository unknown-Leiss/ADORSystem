\[T2-Runtime\]  
Recognition Runtime Pipeline  
Revision: 2026-06-28  
Version: v0.2  
Status: Draft

Purpose  
Define the recognition-side runtime pipeline that makes explicit the recognition process previously handled implicitly inside \#ADOR.  
This pipeline exists before Prompt Reconstruction.  
It does not execute image generation.  
It does not replace Character Source.  
It prepares AI and Human to observe the same structure before Runtime judgment.

Core Principle  
Scenario must not jump directly to Meaning.  
Scenario must pass through observation, disassembly, organization, and reassembly.

Runtime Flow  
Scenario  
↓  
Token Observation Runtime  
↓  
Structural Observation Runtime  
↓  
Structural Organization Runtime  
↓  
Meaning Reconstruction Runtime  
↓  
Scenario Interpretation Runtime  
↓  
Source Routing Runtime  
↓  
AI Rail Selection  
↓  
Prompt Reconstruction Runtime  
↓  
\#Exe Handoff

Runtime Responsibilities

1\. Token Observation Runtime  
Input:  
\- Raw Scenario text

Responsibility:  
\- Observe the scenario as tokens and surface fragments.  
\- Preserve wording without assigning meaning.

Output:  
\- Token Observation Artifact

Must Not:  
\- Interpret meaning.  
\- Select Rails.  
\- Rewrite scenario intent.

2\. Structural Observation Runtime  
Input:  
\- Token Observation Artifact  
\- Character Understanding

Responsibility:  
\- Disassemble scenario into observable structures.  
\- Extract entities, relations, actions, attributes, observation order, and raw structure.

Output:  
\- Structural Observation Artifact

Must Not:  
\- Decide scene priority.  
\- Convert structure into prompt terms.  
\- Decide required Rails.

3\. Structural Organization Runtime  
Input:  
\- Structural Observation Artifact

Responsibility:  
\- Organize observed fragments into stable structural groups.  
\- Separate spatial structure, observation structure, behavior structure, existence structure, and context structure.

Output:  
\- Structural Organization Artifact

Must Not:  
\- Collapse structure into generic scene labels.  
\- Replace structure with atmosphere.  
\- Assign final meaning.

4\. Meaning Reconstruction Runtime  
Input:  
\- Structural Organization Artifact  
\- Character Understanding

Responsibility:  
\- Reassemble meaning from organized structure.  
\- Produce scenario-level meaning without losing structural origin.

Output:  
\- Scenario Meaning Artifact

Must Not:  
\- Treat meaning as a generic category.  
\- Ignore Character Understanding.  
\- Select final Rails.

5\. Scenario Interpretation Runtime  
Input:  
\- Scenario Meaning Artifact  
\- Character Understanding

Responsibility:  
\- Interpret scenario intent and operational need.  
\- Determine what must be considered before Source Routing.

Output:  
\- Scenario Interpretation Artifact

Must Not:  
\- Execute Prompt Reconstruction.  
\- Overwrite Character Identity.  
\- Bypass Source Routing.

6\. Source Routing Runtime  
Input:  
\- Scenario Interpretation Artifact  
\- Character Understanding  
\- Available Character Package sources

Responsibility:  
\- Present relevant source candidates.  
\- Preserve AI decision space.

Output:  
\- Source Candidate Set

Must Not:  
\- Force final Rail selection.  
\- Treat source candidates as prompt output.

7\. AI Rail Selection  
Input:  
\- Source Candidate Set  
\- Scenario Interpretation Artifact  
\- Character Understanding

Responsibility:  
\- AI chooses the required Rail for this specific scenario.

Output:  
\- Selected Rail Intent

Must Not:  
\- Treat Rail as Identity Source.  
\- Ignore Character Core priority.

8\. Prompt Reconstruction Runtime  
Input:  
\- Selected Rail Intent  
\- Character Understanding  
\- Scenario Interpretation Artifact

Responsibility:  
\- Build Prompt Artifact after Recognition Decision Pipeline is complete.

Output:  
\- Prompt Artifact

Must Not:  
\- Reinterpret Character from scratch.  
\- Read Drive sources directly.  
\- Execute image generation.

Session Boundary  
Source Session:  
\- Token Observation  
\- Structural Observation  
\- Structural Organization  
\- Meaning Reconstruction  
\- Scenario Interpretation  
\- Source Routing  
\- Prompt Reconstruction

Execution Session:  
\- \#Exe  
\- Image generation execution  
\- Output monitoring

Execution Session must not perform Source Read or Character Reconstruction.

Design Note  
This pipeline follows the ADOR movement:  
Assembly  
↓  
Disassembly  
↓  
Organization  
↓  
Reassembly

The pipeline exists to prevent Scenario from collapsing into generic prompt categories.  
ADOR preserves structure before meaning.

Implementation Mapping  
Current implemented files:  
\- runtime/meaning\_extraction.py  
\- runtime/character\_understanding.py  
\- runtime/structural\_observation.py  
\- runtime/scenario\_interpretation.py

Next implementation candidates:  
\- runtime/token\_observation.py  
\- runtime/structural\_organization.py  
\- runtime/meaning\_reconstruction.py  
\- runtime/source\_routing.py  
\- runtime/prompt\_reconstruction.py  
