\[T2-Runtime\]  
Recognition Decision Pipeline  
Revision: 2026-06-28  
Status: Draft

Purpose  
\- Make explicit the recognition decisions previously performed implicitly during \#ADOR.  
\- Separate recognition responsibilities into independent runtime stages.  
\- Prepare AI for Prompt Reconstruction without allowing the Runtime to choose Rails.

Runtime Flow  
Character Context  
↓  
Meaning Extraction  
↓  
Character Understanding  
↓  
Scenario Interpretation  
↓  
Intent Resolution  
↓  
Source Routing  
↓  
AI Rail Selection  
↓  
Prompt Reconstruction  
↓  
\#Exe Handoff

Responsibility Principles  
\- Character Understanding: Understand the Character only.  
\- Meaning Extraction: Build meaning from loaded sources.  
\- Scenario Interpretation: Understand the scenario.  
\- Intent Resolution: Determine what should be expressed.  
\- Source Routing: Present relevant source candidates only.  
\- AI Rail Selection: AI chooses the required Rail.  
\- Prompt Reconstruction: Build the Prompt Artifact.

Must Not  
\- Runtime must not choose Rails.  
\- Source Routing must not rewrite Character identity.  
\- Prompt Reconstruction must not reinterpret the Character.  
\- Execution Session must not read Character sources.  
