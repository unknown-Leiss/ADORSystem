import subprocess
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = PROJECT_ROOT / "☆Docs"

DOC_UPDATE_TARGETS = {
    "91": DOCS_DIR / "91_Runtime_Implementation_Map.md",
    "92": DOCS_DIR / "92_Runtime_Module_Specification.md",
    "93": DOCS_DIR / "93_Runtime_Development_Log.md",
}


RUNTIME_AREA_RULES = [
    {
        "keywords": ["recognition"],
        "runtime_area": "Recognition Runtime",
        "rules": ["Rule-011", "Rule-026"],
        "docs": ["91", "92", "93"],
    },
    {
        "keywords": ["structural"],
        "runtime_area": "Structural Runtime",
        "rules": ["Rule-011", "Rule-026"],
        "docs": ["91", "92", "93"],
    },
    {
        "keywords": ["meaning_verification"],
        "runtime_area": "Meaning Verification Runtime",
        "rules": ["Rule-027", "Rule-028"],
        "docs": ["91", "92", "93"],
    },
    {
        "keywords": ["meaning_reconstruction"],
        "runtime_area": "Meaning Reconstruction Runtime",
        "rules": ["Rule-026"],
        "docs": ["91", "92", "93"],
    },
    {
        "keywords": ["scenario_interpretation"],
        "runtime_area": "Scenario Interpretation Runtime",
        "rules": ["Rule-027", "Rule-028"],
        "docs": ["91", "92", "93"],
    },
    {
        "keywords": ["character_understanding"],
        "runtime_area": "Character Understanding Runtime",
        "rules": ["Rule-027", "Rule-028"],
        "docs": ["91", "92", "93"],
    },
    {
        "keywords": ["docs_runtime"],
        "runtime_area": "Documentation Runtime",
        "rules": [],
        "docs": ["93"],
    },
    {
        "keywords": ["package_reader"],
        "runtime_area": "Package Reader Runtime",
        "rules": [],
        "docs": ["93"],
    },
    {
        "keywords": ["source_routing"],
        "runtime_area": "Source Routing Runtime",
        "rules": [],
        "docs": ["93"],
    },
]


def run_git_command(args):
    result = subprocess.run(
        ["git", *args],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    if result.returncode != 0:
        return []

    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def get_changed_files():
    changed_files = set()

    for file_path in run_git_command(["diff", "--name-only"]):
        changed_files.add(file_path)

    for file_path in run_git_command(["diff", "--cached", "--name-only"]):
        changed_files.add(file_path)

    for file_path in run_git_command(["ls-files", "--others", "--exclude-standard"]):
        changed_files.add(file_path)

    return sorted(changed_files)


def is_runtime_file(file_path):
    return file_path.startswith("runtime/") and file_path.endswith(".py")


def detect_runtime_mapping(file_path):
    lowered_path = file_path.lower()

    for rule in RUNTIME_AREA_RULES:
        for keyword in rule["keywords"]:
            if keyword in lowered_path:
                return rule

    return {
        "runtime_area": "Unclassified Runtime Area",
        "rules": [],
        "docs": ["93"],
    }


def build_docs_update_candidates(changed_files):
    candidates = []

    for file_path in changed_files:
        if not is_runtime_file(file_path):
            continue

        mapping = detect_runtime_mapping(file_path)

        candidates.append(
            {
                "file": file_path,
                "runtime_area": mapping["runtime_area"],
                "related_rules": mapping["rules"],
                "suggested_docs": mapping["docs"],
            }
        )

    return candidates


def print_header(title):
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)


def print_changed_files(changed_files):
    print_header("Changed Files")

    if not changed_files:
        print("No changed files detected.")
        return

    for file_path in changed_files:
        print(f"- {file_path}")


def print_docs_candidates(candidates):
    print_header("Documentation Update Candidates")

    if not candidates:
        print("No runtime documentation update candidates detected.")
        return

    for candidate in candidates:
        print()
        print(f"File: {candidate['file']}")
        print(f"Runtime Area: {candidate['runtime_area']}")

        if candidate["related_rules"]:
            print("Related Rules: " + ", ".join(candidate["related_rules"]))
        else:
            print("Related Rules: Not detected")

        print("Suggested Docs:")
        for doc_key in candidate["suggested_docs"]:
            doc_path = DOC_UPDATE_TARGETS.get(doc_key)
            print(f"- {doc_key}: {doc_path}")

        print("Implementation Check:")
        print("- Review whether 91 requires mapping updates.")
        print("- Review whether 92 requires module responsibility updates.")
        print("- Record the decision in 93 before or after implementation.")
        print("- Do not update 90 unless a new development rule is required.")


def run_docs_runtime():
    print_header("ADORSystem Documentation Runtime PoC")

    changed_files = get_changed_files()
    candidates = build_docs_update_candidates(changed_files)

    print_changed_files(changed_files)
    print_docs_candidates(candidates)

    print()
    print("Status: Review candidates only. No document was modified.")


if __name__ == "__main__":
    run_docs_runtime()