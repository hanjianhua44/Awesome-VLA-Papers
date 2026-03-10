"""Regenerate daily MD report from existing JSON data.

Re-identifies institutions using the shared inst_utils module,
so stale/wrong institution data in the JSON gets corrected.
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from inst_utils import identify_institutions, extract_institutions_from_pdf, is_known_institution
from fetch_daily import generate_daily_report

DAILY_DIR = Path(__file__).parent.parent / "daily"


def re_identify_institutions(papers: list, use_pdf: bool = True) -> int:
    """Re-run institution identification on all papers. Returns count of changes."""
    changes = 0
    for p in papers:
        aff_text = " ".join(p.get("affiliations", []))
        new_inst = identify_institutions(p["authors"], aff_text)
        if new_inst != p.get("institution", "—"):
            old = p.get("institution", "—")
            p["institution"] = new_inst
            changes += 1
            print(f"  FIXED: {p['title'][:60]}  [{old}] -> [{new_inst}]")

    if use_pdf:
        no_inst = [p for p in papers if p["institution"] == "—"]
        if no_inst:
            print(f"\n  Enriching {len(no_inst)} papers via PDF...")
            for i, p in enumerate(no_inst):
                pdf_inst = extract_institutions_from_pdf(p["arxiv_id"])
                if pdf_inst:
                    p["institution"] = pdf_inst
                    changes += 1
                    print(f"    PDF: {p['title'][:60]} -> [{pdf_inst}]")
                if (i + 1) % 5 == 0:
                    time.sleep(3)

    return changes


def main():
    date_str = sys.argv[1] if len(sys.argv) > 1 else "2026-03-09"
    use_pdf = "--no-pdf" not in sys.argv

    json_path = DAILY_DIR / f"{date_str}.json"
    if not json_path.exists():
        print(f"No JSON data found for {date_str}")
        return

    papers = json.loads(json_path.read_text(encoding="utf-8"))

    print(f"Re-identifying institutions for {len(papers)} papers...")
    changes = re_identify_institutions(papers, use_pdf=use_pdf)
    print(f"\n{changes} institution(s) changed")

    json_path.write_text(json.dumps(papers, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Updated {json_path}")

    count_info_path = DAILY_DIR / f"{date_str}_meta.json"
    total_scanned = 599
    if count_info_path.exists():
        meta = json.loads(count_info_path.read_text(encoding="utf-8"))
        total_scanned = meta.get("total_scanned", 599)

    report = generate_daily_report(papers, date_str, total_scanned)
    out_path = DAILY_DIR / f"{date_str}.md"
    out_path.write_text(report, encoding="utf-8")
    print(f"Regenerated {out_path} ({len(papers)} papers)")


if __name__ == "__main__":
    main()
