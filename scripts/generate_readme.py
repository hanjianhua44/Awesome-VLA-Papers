"""Generate README.md, TIMELINE.md, and BY_INSTITUTION.md from papers.yaml."""
import re
import yaml
from pathlib import Path
from datetime import datetime
from collections import defaultdict

ROOT = Path(__file__).parent.parent
YAML_PATH = ROOT / "data" / "papers.yaml"
RESOURCES_PATH = ROOT / "data" / "resources.yaml"
REPO_URL = "https://github.com/hanjianhua44/Awesome-VLA-Papers"

DOMAIN_ORDER = ["ad", "robot", "general"]
DOMAIN_LABELS = {
    "ad": "I. Autonomous Driving",
    "robot": "II. Robotics",
    "general": "III. General / Cross-domain",
}
DOMAIN_NAMES = {
    "ad": "Autonomous Driving",
    "robot": "Robotics",
    "general": "General / Cross-domain",
}
DOMAIN_ICONS = {"ad": "🚗", "robot": "🤖", "general": "🧠"}
DOMAIN_DESCRIPTIONS = {
    "ad": "End-to-end driving, world models, planning, simulation, safety, and evaluation.",
    "robot": "Generalist policies, action representations, robot learning, memory, and manipulation.",
    "general": "Spatial intelligence, multimodal reasoning, efficient inference, benchmarks, and surveys.",
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
SUB_ICONS = {
    "e2e": "🛣️",
    "world-model": "🌍",
    "simulation-data": "🎮",
    "planning": "🧭",
    "safety-benchmark": "🛡️",
    "vla-arch": "🦾",
    "action-token": "🧩",
    "world-model-policy": "🔮",
    "rl-policy": "🎯",
    "data-pretrain": "📚",
    "spatial": "🧊",
    "latent-reasoning": "💭",
    "multimodal-arch": "🌈",
    "efficient": "⚡",
    "physical-benchmark": "🧪",
    "survey": "🗺️",
}
SUB_DESCRIPTIONS = {
    "e2e": "Models that connect visual understanding directly to driving decisions.",
    "world-model": "Predictive models that simulate future scenes, dynamics, and actions.",
    "simulation-data": "Datasets, simulators, synthetic data, and scalable data engines.",
    "planning": "Trajectory generation, control, value estimation, and decision making.",
    "safety-benchmark": "Robustness, safety alignment, attacks, evaluation, and benchmarks.",
    "vla-arch": "Core architectures that connect perception, language, memory, and control.",
    "action-token": "Action representations, tokenizers, diffusion, and flow-based decoding.",
    "world-model-policy": "Policies that learn with prediction, imagination, or world models.",
    "rl-policy": "Reinforcement learning, post-training, alignment, and policy optimization.",
    "data-pretrain": "Robot datasets, pre-training recipes, scaling, and transfer learning.",
    "spatial": "3D/4D perception, geometry, grounding, reconstruction, and spatial intelligence.",
    "latent-reasoning": "Visual reasoning, chain-of-thought, memory, and latent deliberation.",
    "multimodal-arch": "Unified multimodal understanding, generation, and foundation models.",
    "efficient": "Token compression, pruning, acceleration, and efficient architectures.",
    "physical-benchmark": "Evaluation suites for embodied intelligence and physical reasoning.",
    "survey": "Roadmaps and surveys for getting oriented in the field.",
}

RSI_TRACK_LABELS = {
    "foundation": "🧭 Open-ended Foundations",
    "data": "🧪 Data & skill discovery",
    "memory": "🧠 Memory & experience",
    "harness": "🛠️ Harness & scaffold evolution",
    "policy": "🔁 Policy & model updates",
    "safety": "🛡️ Safety & evaluation",
}
RSI_TRACK_DESCRIPTIONS = {
    "foundation": "Foundational systems for open-ended embodied learning and continuously expanding capabilities.",
    "data": "Autonomous data collection, curriculum generation, skill discovery, and reusable experience.",
    "memory": "Reflection, self-correction, and persistent memory that improve future behavior.",
    "harness": "Skills, tools, context, and execution scaffolds that evolve around frozen foundation models.",
    "policy": "Deployment experience or imagined practice used to update policy or model parameters.",
    "safety": "Verification, regression testing, rollback, and evaluation for bounded self-improvement.",
}

INSTITUTION_ALIASES = {
    "Alibaba DAMO": "Alibaba",
    "Alibaba Group": "Alibaba",
    "Ant Digital Technologies": "Ant Group",
    "ByteDance Seed": "ByteDance",
    "DeepSeek AI": "DeepSeek",
    "Edinburgh": "Univ of Edinburgh",
    "HK PolyU": "PolyU",
    "Meta": "Meta AI",
    "Meta FAIR": "Meta AI",
    "Microsoft AI": "Microsoft Research",
    "MSRA": "Microsoft Research",
    "Northeastern": "Northeastern Univ",
    "Tsinghua (AIR)": "Tsinghua",
    "Univ of Oxford": "Oxford",
    "Xiaomi EV": "Xiaomi",
    "XPeng Robotics": "XPeng",
}


def load_papers():
    with open(YAML_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_resources():
    if not RESOURCES_PATH.exists():
        return []
    with open(RESOURCES_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or []


MONTH_NAMES = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def extract_date(p: dict) -> tuple:
    """Return (year, month, day) from the 'date' field or arXiv ID fallback."""
    d = p.get("date", "")
    if d and len(d) >= 10:
        try:
            return int(d[:4]), int(d[5:7]), int(d[8:10])
        except ValueError:
            pass
    aid = p.get("arxiv", "")
    if aid and len(aid) >= 4:
        try:
            yy, mm = int(aid[:2]), int(aid[2:4])
            if 1 <= mm <= 12:
                return 2000 + yy, mm, 1
        except ValueError:
            pass
    m = re.search(r"(\d{4})", p.get("venue", ""))
    return (int(m.group(1)), 1, 1) if m else (2025, 1, 1)


def format_date(year: int, month: int, day: int) -> str:
    return f"{MONTH_NAMES[month]} {day}, {year}"


def make_anchor(text: str) -> str:
    """GitHub-compatible anchor: lowercase, spaces→hyphens, strip non-alnum.
    GitHub keeps consecutive hyphens (e.g. 'A & B' → 'a--b'), so we must too."""
    anchor = text.lower().replace(" ", "-")
    anchor = re.sub(r"[^a-z0-9\-]", "", anchor)
    return anchor


def domain_short(dom: str) -> str:
    return DOMAIN_LABELS[dom].split(". ", 1)[-1]


def markdown_cell(value: str, fallback: str = "Details coming soon.") -> str:
    """Keep YAML text safe inside Markdown tables."""
    text = " ".join(str(value or "").split()).strip()
    if not text:
        text = fallback
    return text.replace("|", "\\|")


def paper_links(p: dict) -> str:
    links = f"[Paper]({p['url']})"
    if p.get("code"):
        links += f" · [Code]({p['code']})"
    if p.get("project"):
        links += f" · [Project]({p['project']})"
    return links


def canonical_institution(name: str) -> str:
    return INSTITUTION_ALIASES.get(name.strip(), name.strip())


def paper_institutions(p: dict) -> list[str]:
    institutions = []
    for raw_name in str(p.get("institution", "")).split(","):
        name = canonical_institution(raw_name)
        if name and name not in institutions:
            institutions.append(name)
    return institutions


def paper_summary(p: dict) -> str:
    """Return a useful one-line description, replacing legacy placeholders."""
    summary = " ".join(str(p.get("summary") or "").split()).strip()
    legacy = {
        "Curated update from the main VLA paper list.",
        "Curated paper from the main VLA list.",
    }
    if summary and summary not in legacy:
        return summary

    fallbacks = {
        "e2e": "Explores end-to-end perception, reasoning, and action design for autonomous driving.",
        "world-model": "Studies predictive world modeling for driving simulation, forecasting, or decision making.",
        "simulation-data": "Contributes data, simulation, or scalable training infrastructure for driving systems.",
        "planning": "Develops planning or control methods for safer and more capable autonomous agents.",
        "safety-benchmark": "Evaluates robustness, safety, or reliability with a dedicated method or benchmark.",
        "vla-arch": "Explores how perception, language, memory, and action can be unified in a VLA model.",
        "action-token": "Studies action representations and decoding strategies for robot control.",
        "world-model-policy": "Connects predictive world models with policy learning or action generation.",
        "rl-policy": "Improves embodied policies through reinforcement learning, alignment, or post-training.",
        "data-pretrain": "Studies data, pre-training, scaling, or transfer for general-purpose robot policies.",
        "spatial": "Advances spatial perception, grounding, geometry, or 3D/4D scene understanding.",
        "latent-reasoning": "Explores visual or latent reasoning for stronger multimodal decision making.",
        "multimodal-arch": "Develops a unified architecture for multimodal understanding and generation.",
        "efficient": "Reduces multimodal inference cost through compression, pruning, or efficient design.",
        "physical-benchmark": "Introduces an evaluation resource for embodied or physical intelligence.",
        "survey": "Organizes the literature and open problems in this research direction.",
    }
    return fallbacks[p["subcategory"]]


def paper_row(p: dict) -> str:
    year, month, day = extract_date(p)
    title = markdown_cell(p["title"])
    summary = markdown_cell(paper_summary(p))
    institution = markdown_cell(", ".join(paper_institutions(p)), "Unknown")
    return (
        f"| **{title}** | {summary} | {institution}<br><sub>{format_date(year, month, day)}</sub> | "
        f"{paper_links(p)} |"
    )


def category_anchor(domain: str, subcategory: str) -> str:
    return f"{domain}-{subcategory}"


_DATE_OVERRIDE = None

def _latest_paper_date(papers: list) -> str:
    if _DATE_OVERRIDE:
        return _DATE_OVERRIDE
    dates = [p.get("date", "") for p in papers if p.get("date")]
    return max(dates) if dates else datetime.now().strftime("%Y-%m-%d")


def generate_readme(papers: list) -> str:
    last_updated = _latest_paper_date(papers)
    total = len(papers)
    resources = load_resources()

    grouped = defaultdict(lambda: defaultdict(list))
    for p in papers:
        grouped[p["domain"]][p["subcategory"]].append(p)

    domain_counts = {dom: sum(len(v) for v in grouped[dom].values()) for dom in DOMAIN_ORDER}
    classics = sorted(
        (p for p in papers if p.get("classic")),
        key=lambda p: (int(p.get("classic_order", 999)), tuple(-v for v in extract_date(p))),
    )
    featured = sorted(
        (p for p in papers if p.get("featured")),
        key=lambda p: (int(p.get("featured_order", 999)), tuple(-v for v in extract_date(p))),
    )
    if not featured:
        featured = sorted(papers, key=extract_date, reverse=True)[:8]
    recent = sorted(papers, key=extract_date, reverse=True)[:8]
    rsi_papers = sorted(
        (p for p in papers if p.get("rsi")),
        key=lambda p: (int(p.get("rsi_order", 999)), tuple(-v for v in extract_date(p))),
    )
    rsi_track_counts = {
        track: sum(1 for p in rsi_papers if p.get("rsi_track") == track)
        + sum(1 for resource in resources if resource.get("rsi_track") == track)
        for track in RSI_TRACK_LABELS
    }
    rsi_total = len(rsi_papers) + len(resources)

    lines = []
    lines.append('<p align="center">')
    lines.append('  <img src="assets/vla-buddy-banner.svg" alt="Awesome VLA Papers — Vision, Language, Action" width="100%">')
    lines.append("</p>")
    lines.append("")
    lines.append('<h1 align="center">Awesome VLA Papers</h1>')
    lines.append("")
    lines.append('<p align="center">')
    lines.append("  A friendly, curated map of Vision-Language-Action research for robotics, autonomous driving, and Physical AI.")
    lines.append("</p>")
    lines.append("")
    lines.append('<p align="center">')
    lines.append('  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>')
    lines.append(f'  <img src="https://img.shields.io/badge/papers-{total}-ff8fbd?style=flat-square" alt="{total} papers">')
    lines.append('  <a href="daily/"><img src="https://img.shields.io/badge/arXiv_feed-auto--updated-8b7de3?style=flat-square" alt="Daily arXiv feed"></a>')
    lines.append('  <a href="https://creativecommons.org/publicdomain/zero/1.0/"><img src="https://img.shields.io/badge/license-CC0-64b6ac?style=flat-square" alt="CC0 license"></a>')
    lines.append("</p>")
    lines.append("")
    lines.append('<p align="center">')
    lines.append("  <a href=\"daily/\"><strong>Daily Feed</strong></a> ·")
    lines.append("  <a href=\"TIMELINE.md\"><strong>Timeline</strong></a> ·")
    lines.append("  <a href=\"BY_INSTITUTION.md\"><strong>By Institution</strong></a> ·")
    lines.append("  <a href=\"WORKFLOW.md\"><strong>How It Works</strong></a> ·")
    lines.append("  <a href=\"CONTRIBUTING.md\"><strong>Contribute</strong></a>")
    lines.append("</p>")
    lines.append("")
    lines.append(f"<p align=\"center\"><sub><strong>{total} curated papers</strong> · Last updated: {last_updated}</sub></p>")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Why this list")
    lines.append("")
    lines.append("A **Vision-Language-Action (VLA)** model connects what an agent *sees*, what a human *asks*, and what the agent *does*. This repository combines a carefully checked foundation set with a continuously updated frontier catalog, so newcomers can learn the field and experienced researchers can track it.")
    lines.append("")
    lines.append("> **Follow the frontier:** the [Daily arXiv Feed](daily/) scans `cs.CV` and `cs.RO`; this main list only promotes papers after curation.")
    lines.append("")
    lines.append("## Learning paths")
    lines.append("")
    lines.append("- **Learn the basics:** [Surveys](#general-survey) → [Multimodal foundations](#general-multimodal-arch) → [VLA architectures](#robot-vla-arch) → [Action tokenization](#robot-action-token)")
    lines.append("- **Build robot policies:** [Data & pre-training](#robot-data-pretrain) → [World models & policy co-learning](#robot-world-model-policy) → [RL & policy optimization](#robot-rl-policy)")
    lines.append("- **Study continual improvement:** [RSI & agent harness](#rsi-papers) → memory, skill discovery, harness evolution, policy updates, and safety")
    lines.append("- **Explore autonomous driving:** [End-to-end VLA](#ad-e2e) → [World models](#ad-world-model) → [Planning & control](#ad-planning) → [Safety & benchmarks](#ad-safety-benchmark)")
    lines.append("")
    if classics:
        lines.append("## Canonical foundations")
        lines.append("")
        lines.append("> A compact reading list of field-shaping work. “Canonical” means historically or technically influential, not a ranking.")
        lines.append("")
        for dom in DOMAIN_ORDER:
            domain_classics = [p for p in classics if p["domain"] == dom]
            if not domain_classics:
                continue
            lines.append(f"### {DOMAIN_ICONS[dom]} {DOMAIN_NAMES[dom]}")
            lines.append("")
            lines.append("| Paper | Why it matters | Topic | Links |")
            lines.append("|:------|:---------------|:------|:------|")
            for p in domain_classics:
                lines.append(
                    f"| **{markdown_cell(p['title'])}** | {markdown_cell(paper_summary(p))} | "
                    f"[{SUB_LABELS[p['subcategory']]}](#{category_anchor(p['domain'], p['subcategory'])}) | "
                    f"{paper_links(p)} |"
                )
            lines.append("")
    lines.append("## Curated spotlights")
    lines.append("")
    lines.append("> A small, opinionated selection of noteworthy newer work — not a benchmark ranking.")
    lines.append("")
    lines.append("| Paper | Why it matters | Topic | Links |")
    lines.append("|:------|:---------------|:------|:------|")
    for p in featured:
        lines.append(
            f"| **{markdown_cell(p['title'])}** | {markdown_cell(paper_summary(p))} | "
            f"[{SUB_LABELS[p['subcategory']]}](#{category_anchor(p['domain'], p['subcategory'])}) | "
            f"{paper_links(p)} |"
        )
    lines.append("")
    lines.append("## Recently added")
    lines.append("")
    lines.append("| Paper | Tiny takeaway | Area | Date |")
    lines.append("|:------|:--------------|:-----|:----:|")
    for p in recent:
        year, month, day = extract_date(p)
        area = f"{DOMAIN_ICONS[p['domain']]} {DOMAIN_NAMES[p['domain']]}"
        lines.append(
            f"| [**{markdown_cell(p['title'])}**]({p['url']}) | {markdown_cell(paper_summary(p))} | "
            f"{area} | {format_date(year, month, day)} |"
        )
    lines.append("")
    lines.append('<a id="paper-map"></a>')
    lines.append("## Explore the map")
    lines.append("")
    lines.append("| Area | Topics | What lives here |")
    lines.append("|:-----|:-------|:----------------|")
    rsi_topic_links = [
        f"[{label} ({rsi_track_counts[track]})](#rsi-{track})"
        for track, label in RSI_TRACK_LABELS.items()
    ]
    lines.append(
        f"| ♻️ **[RSI & Agent Harness](#rsi-papers)** ({rsi_total}) "
        f"| {'<br>'.join(rsi_topic_links)} "
        "| Systems that turn deployment experience into verified, persistent improvements. |"
    )
    for dom in DOMAIN_ORDER:
        topic_links = []
        for sub in SUB_ORDER[dom]:
            sub_label = SUB_LABELS[sub]
            cnt = len(grouped[dom][sub])
            topic_links.append(
                f"[{SUB_ICONS[sub]} {sub_label} ({cnt})](#{category_anchor(dom, sub)})"
            )
        lines.append(
            f"| {DOMAIN_ICONS[dom]} **[{DOMAIN_NAMES[dom]}](#{dom}-papers)** ({domain_counts[dom]}) "
            f"| {'<br>'.join(topic_links)} | {DOMAIN_DESCRIPTIONS[dom]} |"
        )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Complete paper library")
    lines.append("")
    lines.append("> Open a topic to browse its papers. Every entry includes a one-line explanation of why it may be useful.")
    lines.append("")
    lines.append('<a id="rsi-papers"></a>')
    lines.append("## ♻️ 0. RSI & Agent Harness")
    lines.append("")
    lines.append("Cross-cutting work on open-ended learning, persistent memory, skill and harness evolution, policy updates, and safe post-deployment improvement.")
    lines.append("")
    lines.append("> **Scope:** a retry or one-off adaptation only belongs here when experience is verified and retained to improve future behavior. Entries below are topic shortcuts; each paper appears in full only once in the domain catalog.")
    lines.append("")
    lines.append("[Back to the map](#paper-map)")
    lines.append("")
    lines.append("---")
    lines.append("")
    for track, track_label in RSI_TRACK_LABELS.items():
        track_papers = [p for p in rsi_papers if p.get("rsi_track") == track]
        track_resources = [r for r in resources if r.get("rsi_track") == track]
        entry_count = len(track_papers) + len(track_resources)
        entry_word = "entry" if entry_count == 1 else "entries"

        lines.append(f'<a id="rsi-{track}"></a>')
        lines.append("<details>")
        lines.append(
            f"<summary><strong>{track_label}</strong> "
            f"<sub>({entry_count} {entry_word})</sub></summary>"
        )
        lines.append("")
        lines.append(RSI_TRACK_DESCRIPTIONS[track])
        lines.append("")
        for resource in track_resources:
            lines.append(
                f"- **[{markdown_cell(resource['title'])}]({resource['url']})** "
                f"({markdown_cell(resource.get('institution'), 'Independent resource')}) — "
                f"{markdown_cell(resource.get('summary'))}"
            )
        for p in track_papers:
            lines.append(
                f"- **[{markdown_cell(p['title'])}]({p['url']})** — "
                f"{markdown_cell(paper_summary(p))} "
                f"([browse {SUB_LABELS[p['subcategory']]}](#{category_anchor(p['domain'], p['subcategory'])}))"
            )
        lines.append("")
        lines.append("</details>")
        lines.append("")
    for dom in DOMAIN_ORDER:
        lines.append(f'<a id="{dom}-papers"></a>')
        lines.append(f"## {DOMAIN_ICONS[dom]} {DOMAIN_LABELS[dom]}")
        lines.append("")
        lines.append(DOMAIN_DESCRIPTIONS[dom])
        lines.append("")
        lines.append("[Back to the map](#paper-map)")
        lines.append("")

        lines.append("---")
        lines.append("")
        for sub in SUB_ORDER[dom]:
            sub_label = SUB_LABELS[sub]
            sub_papers = grouped[dom][sub]
            if not sub_papers:
                continue
            sub_papers_sorted = sorted(sub_papers, key=extract_date, reverse=True)
            cnt = len(sub_papers_sorted)

            lines.append(f'<a id="{category_anchor(dom, sub)}"></a>')
            lines.append("<details>")
            lines.append(
                f"<summary><strong>{SUB_ICONS[sub]} {sub_label}</strong> "
                f"<sub>({cnt} papers)</sub></summary>"
            )
            lines.append("")
            lines.append(SUB_DESCRIPTIONS[sub])
            lines.append("")
            lines.append("| Paper | Why it matters | Institution & date | Links |")
            lines.append("|:------|:---------------|:-------------------|:------|")
            for p in sub_papers_sorted:
                lines.append(paper_row(p))
            lines.append("")
            lines.append("</details>")
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Help this list grow")
    lines.append("")
    lines.append("Missing an important paper, code release, or institution correction? Contributions are warmly welcome.")
    lines.append("")
    lines.append("1. Read the friendly [contribution guide](CONTRIBUTING.md).")
    lines.append("2. Add or improve an entry in `data/papers.yaml`.")
    lines.append("3. Run `python scripts/validate_papers.py`, `python scripts/generate_readme.py`, and `python scripts/verify_links.py`, then open a pull request.")
    lines.append("")
    lines.append(f"If this map saves you time, consider [starring the repository]({REPO_URL}) so more researchers can find it.")
    lines.append("")
    lines.append("## License")
    lines.append("")
    lines.append("Released under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Paper copyrights remain with their respective authors.")
    lines.append("")

    return "\n".join(lines)


def generate_timeline(papers: list) -> str:
    today = _latest_paper_date(papers)
    for p in papers:
        p["_date_tuple"] = extract_date(p)
    sorted_papers = sorted(papers, key=lambda p: p["_date_tuple"], reverse=True)

    by_ym = defaultdict(list)
    for p in sorted_papers:
        y, m, _ = p["_date_tuple"]
        by_ym[(y, m)].append(p)

    lines = []
    lines.append("# VLA Papers Timeline")
    lines.append("")
    lines.append(f"> {len(papers)} papers sorted by date (newest first) | Updated: {today}")
    lines.append("")
    lines.append("[Back to Main](README.md)")
    lines.append("")

    for (year, month) in sorted(by_ym.keys(), reverse=True):
        ym_papers = by_ym[(year, month)]
        label = f"{MONTH_NAMES[month]} {year}"
        lines.append(f"## {label} ({len(ym_papers)} papers)")
        lines.append("")
        lines.append("| # | Paper | Institution | Date | Category | Link |")
        lines.append("|:-:|:------|:-----------|:----:|:---------|:-----|")
        for i, p in enumerate(ym_papers, 1):
            y, m, d = p["_date_tuple"]
            cat = f"{domain_short(p['domain'])} / {SUB_LABELS[p['subcategory']]}"
            institutions = ", ".join(paper_institutions(p))
            lines.append(f"| {i} | **{p['title']}** | {institutions} | {MONTH_NAMES[m]} {d} | {cat} | [Paper]({p['url']}) |")
        lines.append("")

    for p in papers:
        p.pop("_date_tuple", None)

    return "\n".join(lines)


def generate_by_institution(papers: list) -> str:
    today = _latest_paper_date(papers)
    inst_papers = defaultdict(list)
    for p in papers:
        for inst in paper_institutions(p):
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
        lines.append("| Paper | Category | Date | Link |")
        lines.append("|:------|:---------|:----:|:-----|")
        for p in sorted(plist, key=extract_date, reverse=True):
            y, m, d = extract_date(p)
            lines.append(f"| **{p['title']}** | {SUB_LABELS[p['subcategory']]} | {format_date(y, m, d)} | [Paper]({p['url']}) |")
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
    import sys
    global _DATE_OVERRIDE

    if len(sys.argv) > 1:
        _DATE_OVERRIDE = sys.argv[1]

    papers = load_papers()
    from validate_papers import validate_papers, validate_resources

    errors = validate_papers(papers)
    errors.extend(validate_resources(load_resources()))
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(f"Validation failed with {len(errors)} error(s).")

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
