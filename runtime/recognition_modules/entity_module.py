

"""Entity Recognition Module

Creates entity and structure candidates from organized surface chunks.
This module only produces recognition candidates. It does not assign final meaning.
"""


def apply_entity_module(organized_chunks):
    candidates = []

    entity_words = {
        "Leiss": "character",
        "リース": "character",
        "神社": "place",
        "谷": "place",
    }

    structure_words = {
        "山頂": "location_context",
    }

    for index, chunk in enumerate(organized_chunks):
        text = chunk.get("text")

        if text in entity_words:
            candidates.append({
                "candidate": {
                    "text": text,
                    "type": "entity",
                    "entity_hint": entity_words[text],
                },
                "source_chunks": [index],
                "status": "candidate",
                "confidence": "medium",
                "next_index": index + 1,
            })

        elif text in structure_words:
            candidates.append({
                "candidate": {
                    "text": text,
                    "type": "structure",
                    "structure_hint": structure_words[text],
                },
                "source_chunks": [index],
                "status": "candidate",
                "confidence": "medium",
                "next_index": index + 1,
            })

    return candidates