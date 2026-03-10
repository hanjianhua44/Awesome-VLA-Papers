"""Generate README.md, TIMELINE.md, and BY_INSTITUTION.md from papers.yaml."""
import re
import yaml
from pathlib import Path
from datetime import datetime
from collections import defaultdict

ROOT = Path(__file__).parent.parent
YAML_PATH = ROOT / "data" / "papers.yaml"

DOMAIN_ORDER = ["ad", "robot", "general"]
DOMAIN_LABELS = {
    "ad": "I. Autonomous Driving",
    "robot": "II. Robotics",
    "general": "III. General / Cross-domain",
}

SUB_ORDER = {
    "ad": ["e2e", "world-model", "simulation-data", "planning", "safety-benchmark"],
    "robot": ["vla-arch", "action-token", "world-model-policy", "rl-policy", "data-pretrain"],
    "general": ["spatial", "latent-reasoning", "multimodal-arch", "efficient", "physical-benchmark", "survey"],
}

SUB_LABELS = {
    "e2e": "End-to-End VLA Architecture",
    "world-model": "World Models",
    "simulation-data": "Simulation & Data",
    "planning": "Planning & Control",
    "safety-benchmark": "Safety & Benchmarks",
    "vla-arch": "VLA Architecture",
    "action-token": "Action Tokenization",
    "world-model-policy": "World Models & Policy Co-learning",
    "rl-policy": "RL & Policy Optimization",
    "data-pretrain": "Data & Pre-training",
    "spatial": "Spatial Perception & 3D/4D",
    "latent-reasoning": "Latent Reasoning & Chain-of-Thought",
    "multimodal-arch": "Multimodal Architecture & Pre-training",
    "efficient": "Efficient Inference",
    "physical-benchmark": "Physical AI Benchmarks",
    "survey": "Surveys",
}


def load_papers():
    with open(YAML_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def extract_year(venue: str) -> int:
    m = re.search(r"(\d{4})", venue)
    return int(m.group(1)) if m else 2025


def year_badge(year: int) -> str:
    colors = {2024: "gray", 2025: "blue", 2026: "red"}
    c = colors.get(year, "lightgrey")
    return f"![{year}](https://img.shields.io/badge/{year}-{c}?style=flat-square)"


def make_anchor(text: str) -> str:
    anchor = text.lower().replace(" ", "-")
    anchor = re.sub(r"[^a-z0-9\-/]", "", anchor)
    return anchor


def domain_short(dom: str) -> str:
    return DOMAIN_LABELS[dom].split(". ", 1)[-1]


def paper_row(p: dict) -> str:
    year = extract_year(p["venue"])
    title = p["title"]
    if p.get("star"):
        title += " ⭐"

    links = f"[Paper]({p['url']})"
    if p.get("code"):
        links += f" [Code]({p['code']})"

    return f"| **{title}** | {p['institution']} | {year_badge(year)} | {links} |"


def generate_readme(papers: list) -> str:
    today = datetime.now().strftime("%Y-%m-%d")
    total = len(papers)

    grouped = defaultdict(lambda: defaultdict(list))
    for p in papers:
        grouped[p["domain"]][p["subcategory"]].append(p)

    domain_counts = {dom: sum(len(v) for v in grouped[dom].values()) for dom in DOMAIN_ORDER}
    ad_c, rob_c, gen_c = domain_counts.get("ad", 0), domain_counts.get("robot", 0), domain_counts.get("general", 0)

    lines = []
    lines.append("# Awesome VLA Papers")
    lines.append("")
    lines.append("[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
    lines.append("")
    lines.append("> A curated collection of papers on **Vision-Language-Action (VLA)** models, covering autonomous driving, robotics, world models, spatial reasoning, and more.")
    lines.append("")
    lines.append(f"**{total} papers** | **AD: {ad_c} | Robotics: {rob_c} | General: {gen_c}** | Last updated: {today}")
    lines.append("")
    lines.append("Other views: [Timeline (by date)](TIMELINE.md) | [By Institution](BY_INSTITUTION.md)")
    lines.append("")

    # --- Table of Contents ---
    lines.append("---")
    lines.append("")
    lines.append("## Table of Contents")
    lines.append("")
    for dom in DOMAIN_ORDER:
        label = DOMAIN_LABELS[dom]
        anchor = make_anchor(label)
        lines.append(f"- [{label}](#{anchor})")
        for sub in SUB_ORDER[dom]:
            sub_label = SUB_LABELS[sub]
            a = make_anchor(sub_label)
            cnt = len(grouped[dom][sub])
            lines.append(f"  - [{sub_label} ({cnt})](#{a})")
    lines.append("")

    # --- Sections ---
    for dom in DOMAIN_ORDER:
        label = DOMAIN_LABELS[dom]
        lines.append("---")
        lines.append("")
        lines.append(f"## {label}")
        lines.append("")
        for sub in SUB_ORDER[dom]:
            sub_label = SUB_LABELS[sub]
            sub_papers = grouped[dom][sub]
            if not sub_papers:
                continue
            sub_papers_sorted = sorted(sub_papers, key=lambda p: p.get("arxiv", "0000"), reverse=True)
            cnt = len(sub_papers_sorted)

            lines.append("<details open>")
            lines.append(f"<summary><h3>{sub_label} ({cnt})</h3></summary>")
            lines.append("")
            lines.append("| Paper | Institution | Year | Links |")
            lines.append("|:------|:-----------|:----:|:------|")
            for p in sub_papers_sorted:
                lines.append(paper_row(p))
            lines.append("")
            lines.append("</details>")
            lines.append("")

    # --- Contributing ---
    lines.append("---")
    lines.append("")
    lines.append("## Contributing")
    lines.append("")
    lines.append("PRs welcome! Just add an entry to `data/papers.yaml`:")
    lines.append("")
    lines.append("```yaml")
    lines.append('- title: "Your Paper Title"')
    lines.append('  arxiv: "2603.XXXXX"')
    lines.append('  url: https://arxiv.org/abs/2603.XXXXX')
    lines.append('  institution: "Institution"')
    lines.append('  venue: arXiv 2026')
    lines.append('  domain: robot            # ad / robot / general')
    lines.append('  subcategory: vla-arch    # see categories above')
    lines.append('  summary: "One-line summary"')
    lines.append('  code: "https://github.com/xxx"  # optional')
    lines.append("```")
    lines.append("")
    lines.append("Then run `python scripts/generate_readme.py` to regenerate the README.")
    lines.append("")
    lines.append("## License")
    lines.append("")
    lines.append("[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)")
    lines.append("")

    return "\n".join(lines)


def generate_timeline(papers: list) -> str:
    today = datetime.now().strftime("%Y-%m-%d")
    sorted_papers = sorted(papers, key=lambda p: p.get("arxiv", "0000"), reverse=True)

    by_year = defaultdict(list)
    for p in sorted_papers:
        by_year[extract_year(p["venue"])].append(p)

    lines = []
    lines.append("# VLA Papers Timeline")
    lines.append("")
    lines.append(f"> {len(papers)} papers sorted by date (newest first) | Updated: {today}")
    lines.append("")
    lines.append("[Back to Main](README.md)")
    lines.append("")

    for year in sorted(by_year.keys(), reverse=True):
        ypapers = by_year[year]
        lines.append(f"## {year} ({len(ypapers)} papers)")
        lines.append("")
        lines.append("| # | Paper | Institution | Category | Link |")
        lines.append("|:-:|:------|:-----------|:---------|:-----|")
        for i, p in enumerate(ypapers, 1):
            cat = f"{domain_short(p['domain'])} / {SUB_LABELS[p['subcategory']]}"
            lines.append(f"| {i} | **{p['title']}** | {p['institution']} | {cat} | [Paper]({p['url']}) |")
        lines.append("")

    return "\n".join(lines)


def generate_by_institution(papers: list) -> str:
    today = datetime.now().strftime("%Y-%m-%d")
    inst_papers = defaultdict(list)
    for p in papers:
        for inst in [s.strip() for s in p["institution"].split(",")]:
            inst_papers[inst].append(p)

    sorted_insts = sorted(inst_papers.items(), key=lambda x: -len(x[1]))

    lines = []
    lines.append("# VLA Papers by Institution")
    lines.append("")
    lines.append(f"> {len(papers)} papers across {len(sorted_insts)} institutions | Updated: {today}")
    lines.append("")
    lines.append("[Back to Main](README.md)")
    lines.append("")

    lines.append("## Overview")
    lines.append("")
    lines.append("| Institution | Papers |")
    lines.append("|:-----------|:------:|")
    for inst, plist in sorted_insts:
        if len(plist) >= 2:
            anchor = re.sub(r"[^a-z0-9\u4e00-\u9fff]", "", inst.lower()).replace(" ", "-")
            lines.append(f"| [{inst}](#{anchor}) | {len(plist)} |")
    lines.append("")

    for inst, plist in sorted_insts:
        if len(plist) < 2:
            continue
        lines.append(f"## {inst}")
        lines.append("")
        lines.append("| Paper | Category | Year | Link |")
        lines.append("|:------|:---------|:----:|:-----|")
        for p in sorted(plist, key=lambda x: x.get("arxiv", "0000"), reverse=True):
            lines.append(f"| **{p['title']}** | {SUB_LABELS[p['subcategory']]} | {extract_year(p['venue'])} | [Paper]({p['url']}) |")
        lines.append("")

    singles = [(inst, plist[0]) for inst, plist in sorted_insts if len(plist) == 1]
    if singles:
        lines.append("## Other Institutions (1 paper each)")
        lines.append("")
        lines.append("| Institution | Paper | Link |")
        lines.append("|:-----------|:------|:-----|")
        for inst, p in singles:
            lines.append(f"| {inst} | **{p['title']}** | [Paper]({p['url']}) |")
        lines.append("")

    return "\n".join(lines)


def main():
    papers = load_papers()

    readme = generate_readme(papers)
    (ROOT / "README.md").write_text(readme, encoding="utf-8")
    print(f"Generated README.md ({len(papers)} papers)")

    timeline = generate_timeline(papers)
    (ROOT / "TIMELINE.md").write_text(timeline, encoding="utf-8")
    print("Generated TIMELINE.md")

    by_inst = generate_by_institution(papers)
    (ROOT / "BY_INSTITUTION.md").write_text(by_inst, encoding="utf-8")
    print("Generated BY_INSTITUTION.md")


if __name__ == "__main__":
    main()
