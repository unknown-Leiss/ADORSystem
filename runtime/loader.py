from pathlib import Path


def count_files(path):
    md_files = list(path.rglob("*.md"))
    gdoc_files = list(path.rglob("*.gdoc"))
    return len(md_files), len(gdoc_files)


def list_md_files(path):
    return sorted([f.name for f in path.rglob("*.md")])


def bootstrap():
    root = Path.cwd()

    targets = {
        "T0_Index": root / "T0_Index",
        "T1_Core": root / "T1_Core",
        "T2_Runtime": root / "T2_Runtime",
        "T3_Dossiers": root / "T3_Dossiers",
    }

    print("\n=== ADOR Bootstrap Status ===")

    for name, path in targets.items():
        if path.exists():
            md_count, gdoc_count = count_files(path)

            print(f"{name}: FOUND")
            print(f"  .md files: {md_count}")
            print(f"  .gdoc files: {gdoc_count}")

            files = list_md_files(path)

            for file in files[:5]:
                print(f"    - {file}")

            if len(files) > 5:
                print(f"    ... and {len(files)-5} more")
        else:
            print(f"{name}: MISSING")

    print("============================")

def list_characters():
    root = Path.cwd() / "T3_Dossiers"

    if not root.exists():
        return []

    return sorted([
        f.name
        for f in root.iterdir()
        if f.is_dir()
    ])

def list_character_files(character):
    root = Path.cwd() / "T3_Dossiers" / character

    if not root.exists():
        return []

    return sorted([
        p.name
        for p in root.rglob("*.md")
    ])

def load_document(character, document):
    from pathlib import Path

    path = Path.cwd() / "T3_Dossiers" / character / document

    if path.exists():
        return path.read_text(encoding="utf-8")

    return None