
def apply_recognition_rules(organized_chunks):
    recognition_candidates = []
    index = 0

    while index < len(organized_chunks):
        candidate = build_particle_connection_candidate(
            organized_chunks,
            index,
        )

        if candidate:
            recognition_candidates.append({
                "id": len(recognition_candidates),
                **candidate,
            })
            index = candidate["next_index"]
            continue

        chunk = organized_chunks[index]
        classified_chunk = classify_chunk(chunk)

        recognition_candidates.append({
            "id": len(recognition_candidates),
            "candidate": classified_chunk,
            "source_chunks": [index],
            "status": "candidate",
            "confidence": classified_chunk.get("confidence", "unknown")
        })

        index += 1

    return recognition_candidates


def classify_chunk(chunk):
    text = chunk.get("text", "")
    classified = dict(chunk)

    lexical_rules = [
        {
            "keywords": ["朝日", "夕日", "月光", "光", "雨", "雪", "風", "霧", "雲", "空"],
            "type": "environment",
            "semantic_role": "environment_context",
            "confidence": "medium",
        },
        {
            "keywords": ["山頂", "神社", "谷", "海", "森", "街", "部屋", "庭", "道", "橋", "駅", "学校", "城"],
            "type": "structure",
            "semantic_role": "location_context",
            "confidence": "medium",
        },
        {
            "keywords": ["旅", "終わり", "記憶", "約束", "別れ", "再会", "過去", "未来", "運命", "願い"],
            "type": "abstract_context",
            "semantic_role": "narrative_context",
            "confidence": "medium",
        },
        {
            "keywords": ["静か", "穏やか", "寂し", "優し", "柔らか", "冷た", "暖か", "儚", "淡", "深"],
            "type": "mood",
            "semantic_role": "behavior_modifier",
            "confidence": "medium",
        },
        {
            "keywords": ["受け入れ", "見つめ", "見下ろ", "祈", "待", "歩", "立", "座", "笑", "泣", "抱", "振り返"],
            "type": "action",
            "semantic_role": "character_action",
            "confidence": "medium",
        },
    ]

    for rule in lexical_rules:
        for keyword in rule["keywords"]:
            if keyword in text:
                classified.update({
                    "type": rule["type"],
                    "semantic_role": rule["semantic_role"],
                    "confidence": rule["confidence"],
                })
                return classified

    classified.setdefault("type", "unknown")
    classified.setdefault("confidence", "unknown")
    return classified


def build_particle_connection_candidate(organized_chunks, index):
    if index + 2 >= len(organized_chunks):
        return None

    left = organized_chunks[index]
    particle = organized_chunks[index + 1]
    right = organized_chunks[index + 2]

    particle_text = particle.get("text")

    particle_relation_map = {
        "の": "modifier",
        "から": "origin",
        "へ": "direction",
        "に": "location_or_target",
        "で": "place_or_means",
        "を": "object",
        "と": "with_or_relation",
    }

    if particle_text not in particle_relation_map:
        return None

    merged_text = (
        left.get("text", "")
        + particle.get("text", "")
        + right.get("text", "")
    )

    left_classified = classify_chunk(left)
    right_classified = classify_chunk(right)

    merged_candidate = {
        "text": merged_text,
        "type": "unknown",
        "relation_hint": particle_relation_map[particle_text],
    }

    merged_candidate = classify_particle_connection(
        merged_candidate,
        left_classified,
        particle_text,
        right_classified,
    )

    return {
        "candidate": merged_candidate,
        "source_chunks": [index, index + 1, index + 2],
        "status": "candidate",
        "confidence": merged_candidate.get("confidence", "low"),
        "next_index": index + 3,
    }


def classify_particle_connection(candidate, left, particle_text, right):
    text = candidate.get("text", "")
    classified = dict(candidate)


    if particle_text == "の":
        left_type = left.get("type")
        right_type = right.get("type")

        if left_type == "structure" and right_type == "structure":
            classified.update({
                "type": "structure",
                "semantic_role": "compound_location",
                "confidence": "medium",
            })
            return classified

        if left_type == "abstract_context" or right_type == "abstract_context":
            classified.update({
                "type": "abstract_context",
                "semantic_role": "narrative_context",
                "confidence": "medium",
            })
            return classified

    if particle_text == "から" and left.get("type") == "structure":
        classified.update({
            "type": "structure",
            "semantic_role": "view_origin",
            "confidence": "medium",
        })
        return classified

    if particle_text == "を" and right.get("type") == "action":
        classified.update({
            "type": "action",
            "semantic_role": "object_action",
            "confidence": "medium",
        })
        return classified

    classified.setdefault("confidence", "low")
    return classified