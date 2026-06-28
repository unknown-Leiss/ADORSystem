def build_token_observation(scenario):
    print()
    print("=== Surface Observation Runtime ===")

    surface_chunks = build_surface_chunks(scenario)

    surface_observation = {
        "scenario": scenario,
        "surface_chunks": surface_chunks,
        "surface_order": list(range(len(surface_chunks))),
        "surface_status": "provisional",
        "purpose": "Observe surface fragments before structural observation"
    }

    print("Surface Observation Ready")

    return surface_observation


def build_surface_chunks(text):
    cleaned_text = text.strip()

    if not cleaned_text:
        return []

    separators = ["。", "、", "から", "へ", "に", "で", "を", "が", "は", "と", "の"]

    chunks = []
    current = cleaned_text

    for separator in separators:
        if separator in current:
            parts = current.split(separator)
            rebuilt = []

            for index, part in enumerate(parts):
                if part:
                    rebuilt.append(part)

                if index < len(parts) - 1 and separator not in ["。", "、"]:
                    rebuilt.append(separator)

            current = "|".join(rebuilt)

    for chunk in current.split("|"):
        chunk = chunk.strip()
        if chunk:
            chunks.append(chunk)

    return chunks