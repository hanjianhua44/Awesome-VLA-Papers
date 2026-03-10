"""Verify institutions in papers.yaml against PDF extraction."""
import json
import sys
import time
import yaml
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from inst_utils import extract_institutions_from_pdf

ROOT = Path(__file__).parent.parent
YAML_PATH = ROOT / "data" / "papers.yaml"


def main():
    with open(YAML_PATH, "r", encoding="utf-8") as f:
        papers = yaml.safe_load(f)

    sys.stdout.reconfigure(encoding='utf-8')

    results = []
    for i, p in enumerate(papers):
        title = p.get("title", "")[:70]
        aid = p.get("arxiv", "")
        old_inst = p.get("institution", "")

        if not aid:
            results.append({"idx": i, "title": title, "old": old_inst, "new": "", "status": "SKIP"})
            print(f"[{i:3d}] SKIP (no arxiv): {title}")
            continue

        pdf_inst = extract_institutions_from_pdf(aid)

        if pdf_inst:
            status = "MISMATCH" if pdf_inst != old_inst else "OK"
            if status == "MISMATCH":
                print(f"[{i:3d}] MISMATCH: {title}")
                print(f"       YAML: {old_inst}")
                print(f"       PDF:  {pdf_inst}")
            else:
                print(f"[{i:3d}] OK: {title} | {old_inst}")
        else:
            status = "NO_PDF_INST"
            print(f"[{i:3d}] NO INST FROM PDF: {title} | YAML: {old_inst}")

        results.append({"idx": i, "title": title, "old": old_inst, "new": pdf_inst, "status": status})
        time.sleep(1)

    out_path = ROOT / "scripts" / "verify_output.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nResults saved to {out_path}")
    print(f"Total: {len(papers)}, Mismatches: {sum(1 for r in results if r['status']=='MISMATCH')}")


if __name__ == "__main__":
    main()
