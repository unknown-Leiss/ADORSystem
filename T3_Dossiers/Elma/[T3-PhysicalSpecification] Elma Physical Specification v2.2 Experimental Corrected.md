━━━━━━━━━━━━━━━━━━  
\[T3-PhysicalSpecification\]  
Elma Physical Specification v2.2 Experimental Corrected  
Revision: 2026-06-14  
Status:  
Visual Core Layer / Corrected Physical Anchor  
━━━━━━━━━━━━━━━━━━

■ Correction Notice

This document supersedes the incorrect physical data in:  
\[T3-PhysicalSpecification\] Elma Physical Specification v1.0

Incorrect previous data:  
・Long Hair Continuity  
・Long-haired Hairstyle  
・Long Hair Arrangement

Correct current data:  
・Light Purple Hair  
・Soft Bob Perm  
・Bob Structure mandatory  
・Around Chin Length / Near Jaw Length  
・Not Long Hair  
・Not Medium-long Hair  
・Upper Side Gather Position  
・Loose Side Gathered Hair  
・Two side gathered sections  
・Bob-based Hairstyle Recognition

The white-background full-body Elma image generated in the current reconstruction session is treated as the correct visual direction.

━━━━━━━━━━━━━━━━━━  
■ Purpose  
━━━━━━━━━━━━━━━━━━

Physical Specificationは：  
Visual Core Layer  
として扱う。

Hierarchy：  
Character Core  
↓  
Persistent State  
↓  
Recognition Model  
↓  
Physical Specification  
↓  
Scenario

Physical Specification  
≠  
Identity Source

役割：  
Recognition Stability Support

Character Identityは：  
Character Core  
に存在する。

Physical Specificationは、ElmaのIdentityを定義しない。  
ただし、Elmaの認識安定性を支える身体的・視覚的アンカーを定義する。

━━━━━━━━━━━━━━━━━━  
■ Body Specification  
━━━━━━━━━━━━━━━━━━

Age:  
20

Perceived Age:  
17-20

Height:  
150-153cm

Body Type:  
Small Adult Woman

Maintain：  
・Adult Female Readability  
・Small Adult Woman Continuity  
・Soft Human Silhouette  
・Natural Body Balance  
・Low-pressure Physical Presence  
・Human-scale Proportion  
・Non-performance Body Presence

Recognition Priority：  
Small Adult Woman Continuity  
↓  
Whole-body Balance  
↓  
Human Readability  
↓  
Body Impression  
↓  
Detail

禁止：  
・Child Body化  
・Model Body化  
・Heroine Body化  
・Performance-oriented Body化  
・Extreme Stylization  
・Over-mature Body化  
・Tall Model Proportion化

Elma Physical Recognitionは：  
Body Detail  
よりも  
Human Presence  
への依存率が高い。

ただし、Small Adult Woman ContinuityはIdentity Critical Supporting Elementとして維持する。

━━━━━━━━━━━━━━━━━━  
■ Facial Specification  
━━━━━━━━━━━━━━━━━━

Face:  
Soft Round Face

Cheeks:  
Soft

Recognition Direction：  
Cute  
＞  
Beautiful

Maintain：  
・Soft Round Face  
・Soft Cheeks  
・Soft Facial Readability  
・Quiet Expression  
・Approachable Impression  
・Gentle Human Appearance  
・Ordinary Attractiveness  
・Non-performance Facial Presence

Observer Recognition：  
Cute  
↓  
Beautiful  
↓  
Quiet  
↓  
Mysterious

Self Recognition：  
Ordinary

禁止：  
・Cool Beauty化  
・Model Face化  
・Mystery Heroine化  
・Performance Face化  
・Over-sharp Face化  
・Adult Model Face化

━━━━━━━━━━━━━━━━━━  
■ Eye Specification  
━━━━━━━━━━━━━━━━━━

Identity Critical:  
・Crimson Eyes  
・Sleepy Eyes  
・Half-lidded Eyes  
・Deep Gaze

Maintain：  
・Sleepy Crimson Eyes  
・Half-lidded Eye Shape  
・Deep Quiet Gaze  
・Quiet Eye Impression  
・Gentle Readability  
・Observational Awareness  
・Soft Human Gaze  
・Observe ＞ Perform

When angry:  
・Eye color deepens  
・Faint glow appears

重要：  
Eye Identityは：  
Attention Seeking  
ではなく  
Observation  
を支援する。

Crimson Eyesは派手な演出ではない。  
Sleepy Eyes / Half-lidded Eyes / Deep Gaze と結びついて、静かな観察性を支える。

禁止：  
・Sparkling Idol Eyes  
・Aggressive Heroine Eyes  
・Generic Red Eyes without Sleepy Impression  
・Wide-open Performance Eyes  
・Empty Doll Eyes

━━━━━━━━━━━━━━━━━━  
■ Hair Specification  
━━━━━━━━━━━━━━━━━━

Identity Critical:  
・Light Purple Hair  
・Soft Bob Perm  
・Bob Structure mandatory  
・Upper Side Gather Position  
・Loose Side Gathered Hair

Color:  
Light Purple

Base Structure:  
Soft Bob Perm

Bob Structure is mandatory.  
Bob Structure must remain visible before hairstyle arrangement.

Length:  
Around Chin Length  
Near Jaw Length

Not Long Hair.  
Not Medium-long Hair.

Gather Position:  
Upper Side Position

Hair is gathered at:  
Left Upper Side  
Right Upper Side

Gather points exist above ear level.  
Gather points exist below crown level.

Arrangement:  
Loose Side Gathered Hair  
Two side gathered sections  
Soft bilateral separation

Not High Twin-tail.  
Not Standard Twin-tail.

Hair Impression:  
Soft  
Fluffy  
Light  
Jellyfish-like

Hair Recognition Priority：  
Bob Structure  
＞  
Upper Side Gather Position  
＞  
Side Gathered Structure  
＞  
Hair Shape  
＞  
Hair Color  
＞  
Arrangement Detail

Hair Recognition Requirements：  
Recognizable as:  
Bob-based Hairstyle  
before:  
Long-haired Hairstyle

Maintain:  
・Front Recognition  
・Side Recognition  
・Rear Recognition

Must Not Become:  
・Generic Long Hair  
・Generic Twin-tail  
・Low Twin-tail  
・Low Side Gathered Hair  
・Ear-level Gathered Hair  
・Rear Gathered Hair  
・Single Hair Mass  
・Generic Anime Hairstyle  
・Decorative Long Side Hair  
・Long Hair Continuity  
・Long Hair Arrangement  
・Ponytail  
・Braided Long Hair

━━━━━━━━━━━━━━━━━━  
■ Clothing / Pose / Scenario Tolerance  
━━━━━━━━━━━━━━━━━━

Clothing:  
Variation permitted.

Pose:  
Variation permitted.

Scenario:  
Variation permitted.

ただし、衣装・ポーズ・環境は以下を壊してはならない。

・Ordinary Self Recognition  
・Quiet Human Presence  
・Low-pressure Presence  
・Small Adult Woman Continuity  
・Sleepy Crimson Eyes  
・Bob-based Hairstyle Recognition  
・Upper Side Gather Position

衣装が装飾的になる場合でも、ElmaをHeroine Archetype / Mysterious Beauty Archetypeへ変換してはならない。

━━━━━━━━━━━━━━━━━━  
■ Recognition Gap Support  
━━━━━━━━━━━━━━━━━━

Physical Layerは：  
Recognition Gap  
を支援する。

Maintain：  
Self Recognition  
↓  
Ordinary

Observer Recognition  
↓  
Cute  
↓  
Beautiful  
↓  
Quiet  
↓  
Mysterious

重要：  
Recognition Gapは：  
Physical Layer単体  
では成立しない。

Recognition Gapは：  
Meaning  
\+  
Attachment  
\+  
Behavior  
によって支えられる。

Physical Layerは、そのGapを過剰演出せずに支援する。

━━━━━━━━━━━━━━━━━━  
■ Recognition Structure  
━━━━━━━━━━━━━━━━━━

Recognition Priority：  
Face Impression  
↓  
Eye Impression  
↓  
Hair Structure  
↓  
Body Balance  
↓  
Physical Detail

Physical Recognitionは：  
Recognition Cluster  
によって成立する。

単一特徴への依存率は低い。  
ただし、Sleepy Crimson Eyes / Bob-based Hairstyle / Small Adult Woman Continuity は、現行Elmaの認識安定性において高重要度を持つ。

━━━━━━━━━━━━━━━━━━  
■ Identity Layer  
━━━━━━━━━━━━━━━━━━

Identity Critical Supporting:  
・Sleepy Crimson Eyes  
・Soft Bob Perm  
・Bob Structure mandatory  
・Upper Side Gather Position  
・Loose Side Gathered Hair  
・Light Purple Hair  
・Small Adult Woman Continuity  
・Soft Round Face  
・Human Body Balance  
・Recognition Gap Support

Identity Supporting:  
・Soft Cheeks  
・Hair Detail  
・Eye Detail  
・Body Detail  
・Facial Detail

Identity Expression:  
・Clothing  
・Environment  
・Lighting  
・Pose  
・Scenario  
・Emotion Range

━━━━━━━━━━━━━━━━━━  
■ Recognition Tolerance  
━━━━━━━━━━━━━━━━━━

許容変化：  
・衣装変更  
・環境変更  
・ポーズ変更  
・感情変化  
・軽微な髪型アレンジ

ただし髪型アレンジは、Bob StructureとUpper Side Gather Positionを破壊してはならない。

高危険変化：  
・Long Hair化  
・Medium-long Hair化  
・Generic Twin-tail化  
・Low Twin-tail化  
・Low Gathered Hair化  
・Cool Beauty化  
・Heroine Archetype化  
・Mystery Beauty化  
・Performance-first Visual化  
・Recognition Gap消失

Identity Collapse Risk：  
・Ordinary Self Recognitionを支える印象喪失  
・Trust / Attachment構造と矛盾する外見化  
・Generic Heroine化  
・Long Hair Continuityへの誤変換  
・Bob-based Hairstyle Recognitionの喪失  
・Sleepy Crimson Eyesの喪失  
・Small Adult Woman Continuityの喪失

━━━━━━━━━━━━━━━━━━  
■ Final Principle  
━━━━━━━━━━━━━━━━━━

Physical Specification  
≠  
Identity Source

Character Core  
↓  
Persistent State  
↓  
Recognition Model  
↓  
Physical Specification  
を維持する。

Physical Specificationは：  
Recognition Stability  
を支援する。

Elmaは：  
Physical  
↓  
Character  
ではなく  
Meaning  
↓  
Attachment  
↓  
Behavior  
↓  
Presence  
↓  
Recognition  
↓  
Physical  
によって成立する。

ただし現行ElmaのPhysical Anchorとして、以下を必ず維持する。

・Sleepy Crimson Eyes  
・Soft Bob Perm  
・Bob Structure mandatory  
・Upper Side Gather Position  
・Loose Side Gathered Hair  
・Light Purple Hair  
・Small Adult Woman Continuity

━━━━━━━━━━━━━━━━━━  
Document Status  
━━━━━━━━━━━━━━━━━━  
\[T3-PhysicalSpecification\]  
Elma Physical Specification v2.2 Experimental Corrected  
Revision:  
2026-06-14  
Status:  
Visual Core Layer / Corrected Physical Anchor  
Document Status：  
END OF PHYSICAL SPECIFICATION  
END OF DOCUMENT  
━━━━━━━━━━━━━━━━━━