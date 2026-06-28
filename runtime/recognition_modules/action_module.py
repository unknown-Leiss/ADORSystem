def apply_action_module(organized_chunks):
    candidates = []

    action_keywords = [
        "見下ろしている",
        "見下ろして",
        "見下ろす",
        "見上げている",
        "見上げて",
        "見上げる",
        "振り返っている",
        "振り返って",
        "振り返る",
        "微笑んでいる",
        "微笑んで",
        "微笑む",
        "歩いている",
        "歩いて",
        "歩く",
        "走っている",
        "走って",
        "走る",
        "立っている",
        "立って",
        "立つ",
        "座っている",
        "座って",
        "座る",
        "待っている",
        "待って",
        "待つ",
        "見ている",
        "見て",
        "見る",
        "笑っている",
        "笑って",
        "笑う",
        "眠っている",
        "眠って",
        "眠る",
        "浮かんでいる",
        "浮かんで",
        "浮かぶ",
        "進んでいる",
        "進んで",
        "進む",
        "止まっている",
        "止まって",
        "止まる",
        "履いている",
        "履いて",
        "履く",
        "舞っている",
        "舞って",
        "舞う",
        "差し込み",
        "差し込む",
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