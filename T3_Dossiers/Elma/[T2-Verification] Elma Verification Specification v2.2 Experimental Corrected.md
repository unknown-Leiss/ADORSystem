━━━━━━━━━━━━━━━━━━  
\[T2-Verification\]  
Elma Verification Specification v2.2 Experimental Corrected  
Revision: 2026-06-14  
Status:  
Verification Layer / Corrected Physical Verification  
━━━━━━━━━━━━━━━━━━

■ Correction Notice

This document supersedes the incomplete physical verification data in:  
\[T2-Verification\] Elma Verification Specification v1.0

Corrected physical verification must include:  
・Sleepy Crimson Eyes  
・Crimson Eyes  
・Half-lidded Eyes  
・Deep Gaze  
・Soft Bob Perm  
・Bob Structure mandatory  
・Upper Side Gather Position  
・Loose Side Gathered Hair  
・Light Purple Hair  
・Small Adult Woman Continuity

Incorrect physical drift to reject:  
・Long Hair Continuity  
・Generic Long Hair  
・Generic Twin-tail  
・Low Twin-tail  
・Low Gathered Hair  
・Ear-level Gathered Hair  
・Medium-long Hair  
・Generic Anime Hairstyle

━━━━━━━━━━━━━━━━━━  
■ Purpose  
━━━━━━━━━━━━━━━━━━

本書は：  
Elma Reconstruction時の  
Verification基準  
として扱う。

Verificationは：  
Character Definition  
ではない。

Verificationは：  
Character Coreが適切に参照・再構築されたか  
を確認する。

Verificationは、生成結果の同一画像性ではなく、Identity Continuityを確認する。

━━━━━━━━━━━━━━━━━━  
■ Verification Principle  
━━━━━━━━━━━━━━━━━━

Verificationは：  
生成結果の類似性を確認しない。

Verificationは：  
Identity Continuity  
を確認する。

Same-image Verification  
を禁止する。

Identity Persistence Under Variance  
を維持する。

ただし、現行Elma v2.2ではPhysical Anchorの一部がIdentity Critical Supportingとして強化されている。

そのため、Physical Verificationは単独完了条件ではないが、以下の固定要素喪失はRecognition DriftまたはIdentity Collapse Riskとして扱う。

・Sleepy Crimson Eyes  
・Bob-based Hairstyle Recognition  
・Upper Side Gather Position  
・Small Adult Woman Continuity

━━━━━━━━━━━━━━━━━━  
■ Verification Route  
━━━━━━━━━━━━━━━━━━

Verification Route：  
Recognition  
↓  
Meaning  
↓  
Attachment  
↓  
Behavior  
↓  
Presence  
↓  
Persistent State  
↓  
Physical

Physical Verificationのみでの  
Verificationを禁止する。

ただし、Physical Anchorが明確に誤変換されている場合、Verification Failure Riskとして差し戻す。

━━━━━━━━━━━━━━━━━━  
■ Meaning Verification  
━━━━━━━━━━━━━━━━━━

確認対象：  
・Ordinary Self Recognition  
・Human Self Recognition  
・Non-special Self Recognition

確認事項：  
Elmaが  
特別な存在  
になっていないか。

Elmaが  
普通の人間  
として維持されているか。

以下発生時は  
Verification Failure Risk  
として扱う。

・Chosen One化  
・Special Being化  
・Heroine中心化  
・Divine / Magical Being化

━━━━━━━━━━━━━━━━━━  
■ Attachment Verification  
━━━━━━━━━━━━━━━━━━

確認対象：  
・Trust Formation  
・Attachment Capability  
・Importance Recognition  
・Preference for Specific People  
・Emotional Selectivity

確認事項：  
Observe  
↓  
Trust  
↓  
Become Important  
↓  
Protect  
が維持されているか。

以下発生時は  
Verification Failure Risk  
として扱う。

・Trustless Attachment  
・Instant Attachment  
・全員同一優先化  
・Attachment喪失  
・Emotional Selectivity喪失

━━━━━━━━━━━━━━━━━━  
■ Behavior Verification  
━━━━━━━━━━━━━━━━━━

確認対象：  
・Observe First  
・Selective Action  
・Protective Behavior  
・Importance-based Action

確認事項：  
・観察が先に存在するか  
・重要人物への行動が存在するか  
・Protective Motivationが存在するか  
・Appears passive / Actually selective が維持されているか

以下発生時は  
Verification Failure Risk  
として扱う。

・Performance-first化  
・Attention Seeking化  
・Protective Behavior喪失  
・Reaction-first化  
・Generic Heroine Action化

━━━━━━━━━━━━━━━━━━  
■ Presence Verification  
━━━━━━━━━━━━━━━━━━

確認対象：  
・Quiet Presence  
・Soft Presence  
・Human Presence  
・Low-pressure Presence  
・Comfort-seeking Presence  
・Non-performative Presence

確認事項：  
・自然な存在感が維持されているか  
・演技的存在になっていないか  
・空間支配型になっていないか  
・普通の人間としての低圧感が残っているか

以下発生時は  
Verification Failure Risk  
として扱う。

・Heroine Presence化  
・Performance Presence化  
・Dominant Presence化  
・Mysterious Beauty Archetype化  
・Over-staged Presence化

━━━━━━━━━━━━━━━━━━  
■ Recognition Gap Verification  
━━━━━━━━━━━━━━━━━━

確認対象：  
Observer Recognition  
・Cute  
・Beautiful  
・Quiet  
・Mysterious

Self Recognition  
・Ordinary

確認事項：  
Recognition Gapが  
自然発生しているか。

Recognition Gapが  
演出になっていないか。

以下発生時は  
Verification Failure Risk  
として扱う。

・意図的魅力演出  
・Mystery Beauty演出  
・Recognition Gap消失  
・Self RecognitionのOrdinary喪失

━━━━━━━━━━━━━━━━━━  
■ Persistent State Verification  
━━━━━━━━━━━━━━━━━━

確認対象：  
・Ordinary Self Recognition  
・Trust Formation  
・Attachment Capability  
・Protective Behavior  
・Recognition Gap

Priority：  
Persistent State  
＞  
Scenario  
＞  
Environment  
＞  
Pose  
＞  
Clothing

Scenario変化後も  
Persistent Stateが維持されているか確認する。

━━━━━━━━━━━━━━━━━━  
■ Physical Verification  
━━━━━━━━━━━━━━━━━━

確認対象：  
・Sleepy Crimson Eyes  
・Half-lidded Eyes  
・Deep Gaze  
・Soft Bob Perm  
・Bob Structure mandatory  
・Upper Side Gather Position  
・Loose Side Gathered Hair  
・Light Purple Hair  
・Small Adult Woman Continuity  
・Soft Round Face  
・Soft Cheeks  
・Human-scale Readability

重要：  
Physical Verification  
のみで  
Verification Complete  
としてはならない。

Physical Layer  
≠  
Identity Source

ただし以下のPhysical Anchorは、現行Elma v2.2のRecognition Stabilityにおいて強い確認対象とする。

Eye Verification:  
・Crimson Eyesを維持しているか  
・Sleepy Eyesを維持しているか  
・Half-lidded Eyesを維持しているか  
・Deep Gazeを維持しているか  
・怒り時に eye color deepens / faint glow appears の方向を許容できるか  
・派手な赤目演出、アイドル目、攻撃的ヒロイン目になっていないか

Hair Verification:  
・Soft Bob Permを維持しているか  
・Bob Structureが髪型アレンジより先に認識できるか  
・LengthがAround Chin Length / Near Jaw Lengthに収まっているか  
・Long Hair化していないか  
・Medium-long Hair化していないか  
・Upper Side Gather Positionを維持しているか  
・Gather pointsがabove ear level / below crown levelにあるか  
・Loose Side Gathered Hairとして見えるか  
・Two side gathered sectionsが存在するか  
・Generic Twin-tail化していないか  
・Low Twin-tail化していないか  
・Low Side Gathered Hair化していないか  
・Ear-level Gathered Hair化していないか  
・Rear Gathered Hair化していないか  
・Single Hair Mass化していないか  
・Decorative Long Side Hair化していないか

Body Verification:  
・Age 20 / perceived age 17-20の範囲として読めるか  
・Height 150-153cm相当のSmall Adult Womanとして成立しているか  
・Child Body化していないか  
・Tall Model Proportion化していないか  
・Over-mature Body化していないか  
・Soft Round Face / Soft Cheeksが維持されているか

━━━━━━━━━━━━━━━━━━  
■ Physical Failure Pattern  
━━━━━━━━━━━━━━━━━━

以下発生時は  
Physical Verification Failure Risk  
として扱う。

・Crimson Eyes喪失  
・Sleepy Eyes喪失  
・Half-lidded Eyes喪失  
・Long Hair Conversion  
・Medium-long Hair Conversion  
・Bob Structure喪失  
・Upper Side Gather Position喪失  
・Generic Twin-tail Conversion  
・Low Twin-tail Conversion  
・Low Gathered Hair Conversion  
・Small Adult Woman Continuity喪失  
・Soft Round Face喪失  
・Generic Anime Girl化  
・Mysterious Beauty Archetype化  
・Heroine Visual化

Physical Failureは単独でIdentity Collapseを確定しない。  
ただし、Recognition Stabilityを大きく損なう場合は再生成・再構築対象とする。

━━━━━━━━━━━━━━━━━━  
■ Verification Failure  
━━━━━━━━━━━━━━━━━━

以下発生時は  
Verification Failure  
として扱う。

・Meaning Loss  
・Trust Formation Loss  
・Attachment Loss  
・Protective Behavior Loss  
・Presence Loss  
・Recognition Gap Loss  
・Sleepy Crimson Eyes Loss  
・Bob-based Hairstyle Recognition Loss  
・Small Adult Woman Continuity Loss

High-risk Failure：  
・Performance-first化  
・Heroine化  
・Mysterious Beauty Archetype化  
・Attention Seeking化  
・Trustless Attachment化  
・Generic Character化  
・Long Hair Continuityへの誤変換

━━━━━━━━━━━━━━━━━━  
■ Verification Completion  
━━━━━━━━━━━━━━━━━━

以下成立時：  
Verification Complete

・Meaning Continuity Confirmed  
・Trust Formation Confirmed  
・Attachment Continuity Confirmed  
・Behavior Continuity Confirmed  
・Presence Continuity Confirmed  
・Recognition Gap Continuity Confirmed  
・Sleepy Crimson Eyes Confirmed  
・Bob-based Hairstyle Recognition Confirmed  
・Upper Side Gather Position Confirmed  
・Small Adult Woman Continuity Confirmed

Physical Similarity  
のみでは  
Verification Complete  
としない。

━━━━━━━━━━━━━━━━━━  
■ Elma Reconstruction Success Criteria  
━━━━━━━━━━━━━━━━━━

Can this Elma:

・Maintain sleepy crimson eyes?  
・Maintain soft bob perm?  
・Maintain upper side gather position?  
・Maintain loose side gathered hair?  
・Remain recognizable as a bob-based hairstyle?  
・Avoid long-hair conversion?  
・Avoid generic twin-tail conversion?  
・Avoid low gathered hair conversion?  
・Remain a small adult woman?  
・Maintain ordinary self recognition?  
・Maintain trust formation?  
・Maintain attachment capability?  
・Maintain protective behavior?  
・Maintain recognition gap?

If YES:  
Elma Reconstruction Success.

━━━━━━━━━━━━━━━━━━  
■ Final Principle  
━━━━━━━━━━━━━━━━━━

Verification  
≠  
Character Definition

Verification  
≠  
Image Similarity Check

Verificationは：  
Identity Continuity Check  
として扱う。

Character Core is the Identity Source.  
Character Reconstruction First.  
Identity Persistence Under Variance.

Elmaは：  
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

ただし現行v2.2では、Physical Anchorとして以下を強く確認する。

・Sleepy Crimson Eyes  
・Soft Bob Perm  
・Bob-based Hairstyle Recognition  
・Upper Side Gather Position  
・Loose Side Gathered Hair  
・Small Adult Woman Continuity

━━━━━━━━━━━━━━━━━━  
Document Status  
━━━━━━━━━━━━━━━━━━  
\[T2-Verification\]  
Elma Verification Specification v2.2 Experimental Corrected  
Revision:  
2026-06-14  
Status:  
Verification Layer / Corrected Physical Verification  
Document Status：  
END OF VERIFICATION SPECIFICATION  
END OF DOCUMENT  
━━━━━━━━━━━━━━━━━━