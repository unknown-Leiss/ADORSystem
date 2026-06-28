

def apply_attribute_module(organized_chunks):
    candidates = []

    attribute_keywords = [
        "白",
        "黒",
        "赤",
        "青",
        "緑",
        "金",
        "銀",
        "長い",
        "短い",
        "高い",
        "低い",
        "大きい",
        "小さい",
        "古い",
        "新しい",
        "静か",
        "明るい",
        "暗い",
        "柔らかい",
        "硬い",
    ]

    for index, chunk in enumerate(organized_chunks):
        text = chunk.get("text", "")

        for keyword in attribute_keywords:
            if keyword in text:
                candidates.append({
                    "candidate": {
                        "text": text,
                        "type": "attribute",
                        "attribute_hint": keyword,
                    },
                    "source_chunks": [index],
                    "status": "candidate",
                    "confidence": "medium",
                    "next_index": index + 1,
                })
                break

    return candidates