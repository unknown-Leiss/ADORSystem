

def apply_action_module(organized_chunks):
    candidates = []

    action_keywords = [
        "歩く",
        "走る",
        "立つ",
        "座る",
        "待つ",
        "見る",
        "見上げる",
        "見下ろす",
        "振り返る",
        "微笑む",
        "笑う",
        "眠る",
        "浮かぶ",
        "進む",
        "止まる",
    ]

    for index, chunk in enumerate(organized_chunks):
        text = chunk.get("text", "")

        for keyword in action_keywords:
            if keyword in text:
                candidates.append({
                    "candidate": {
                        "text": text,
                        "type": "action",
                        "action_hint": keyword,
                    },
                    "source_chunks": [index],
                    "status": "candidate",
                    "confidence": "medium",
                    "next_index": index + 1,
                })
                break

    return candidates