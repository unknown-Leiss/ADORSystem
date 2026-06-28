

def apply_relation_module(organized_chunks):
    candidates = []

    relation_keywords = {
        "右": "right",
        "左": "left",
        "上": "above",
        "下": "below",
        "前": "front",
        "後ろ": "behind",
        "隣": "beside",
        "近く": "near",
        "遠く": "far",
        "奥": "depth",
        "手前": "foreground",
        "中央": "center",
        "端": "edge",
        "から": "origin",
        "へ": "direction",
        "に": "location_or_target",
        "で": "place_or_means",
        "を": "object",
        "と": "with_or_relation",
        "の": "modifier",
    }

    for index, chunk in enumerate(organized_chunks):
        text = chunk.get("text", "")

        for keyword, relation_hint in relation_keywords.items():
            if keyword in text:
                candidates.append({
                    "candidate": {
                        "text": text,
                        "type": "relation",
                        "relation_hint": relation_hint,
                    },
                    "source_chunks": [index],
                    "status": "candidate",
                    "confidence": "medium",
                    "next_index": index + 1,
                })
                break

    return candidates