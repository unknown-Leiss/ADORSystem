def apply_compound_module(organized_chunks):
    candidates = []
    index = 0

    while index < len(organized_chunks):
        current = organized_chunks[index]

        if index + 1 < len(organized_chunks):
            nxt = organized_chunks[index + 1]

            # 「山頂 神社」「厚底 下駄」など、
            # 2つの単語を複合候補として扱う
            merged_text = (
                current.get("text", "")
                + nxt.get("text", "")
            )

            candidates.append({
                "candidate": {
                    "text": merged_text,
                    "type": "compound",
                },
                "source_chunks": [index, index + 1],
                "status": "candidate",
                "confidence": "low",
                "next_index": index + 2,
            })

        index += 1

    return candidates