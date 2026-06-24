from pathlib import Path


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
        status = "FOUND" if path.exists() else "MISSING"
        print(f"{name}: {status}")

    print("============================")