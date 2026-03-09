"""Parse current README.md and generate structured papers.yaml."""
import re
import yaml
from pathlib import Path

ROOT = Path(__file__).parent.parent
README = ROOT / "README.md"
OUT = ROOT / "data" / "papers.yaml"

DOMAIN_MAP = {
    "End-to-End VLA Architecture": ("ad", "e2e"),
    "World Models 世界模型": ("ad", "world-model"),
    "Simulation & Data 仿真与数据": ("ad", "simulation-data"),
    "Planning & Control 规划与控制": ("ad", "planning"),
    "Safety & Benchmarks 安全与评估": ("ad", "safety-benchmark"),
    "VLA Architecture VLA架构": ("robot", "vla-arch"),
    "Action Tokenization 动作表征与词表": ("robot", "action-token"),
    "World Models & Policy Co-learning 世界模型与策略协同": ("robot", "world-model-policy"),
    "RL & Policy Optimization 强化学习与策略优化": ("robot", "rl-policy"),
    "Data & Pre-training 数据与预训练": ("robot", "data-pretrain"),
    "Spatial Perception & 3D/4D 空间感知": ("general", "spatial"),
    "Latent Reasoning & Chain-of-Thought 潜在推理与思维链": ("general", "latent-reasoning"),
    "Multimodal Architecture & Pre-training 多模态基础架构": ("general", "multimodal-arch"),
    "Efficient Inference 高效推理与压缩": ("general", "efficient"),
    "Physical AI Benchmarks 物理AI评估": ("general", "physical-benchmark"),
    "Surveys 综述": ("general", "survey"),
}

PAPER_RE = re.compile(
    r'^- \*\*(.+?)\*\*\s*(?:⭐\s*)?\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*\[\[Paper\]\]\((.+?)\)(?:\s*\[\[Code\]\]\((.+?)\))?',
)
SURVEY_RE = re.compile(
    r'^- \*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*\[\[Paper\]\]\((.+?)\)',
)
SUMMARY_RE = re.compile(r'^\s*>\s*(.+)')

def extract_arxiv_id(url: str) -> str:
    m = re.search(r'(\d{4}\.\d{4,5})', url)
    return m.group(1) if m else ""

def parse_readme():
    lines = README.read_text(encoding="utf-8").splitlines()
    papers = []
    current_section = None
    current_domain = None
    current_sub = None
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("### "):
            heading = line[4:].strip()
            for key, (dom, sub) in DOMAIN_MAP.items():
                if key in heading:
                    current_domain = dom
                    current_sub = sub
                    break

        m = PAPER_RE.match(line) or SURVEY_RE.match(line)
        if m and current_domain:
            title = m.group(1).strip()
            institution = m.group(2).strip()
            venue = m.group(3).strip()
            paper_url = m.group(4).strip()
            code_url = m.group(5).strip() if m.lastindex >= 5 and m.group(5) else ""
            star = "⭐" in line

            summary = ""
            if i + 1 < len(lines):
                sm = SUMMARY_RE.match(lines[i + 1])
                if sm:
                    summary = sm.group(1).strip()
                    i += 1

            arxiv_id = extract_arxiv_id(paper_url)

            entry = {
                "title": title,
                "arxiv": arxiv_id,
                "url": paper_url,
                "institution": institution,
                "venue": venue,
                "domain": current_domain,
                "subcategory": current_sub,
                "summary": summary,
            }
            if code_url:
                entry["code"] = code_url
            if star:
                entry["star"] = True

            papers.append(entry)
        i += 1
    return papers

def main():
    papers = parse_readme()
    OUT.parent.mkdir(parents=True, exist_ok=True)

    class Dumper(yaml.SafeDumper):
        pass

    def str_representer(dumper, data):
        if "\n" in data:
            return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
        return dumper.represent_scalar("tag:yaml.org,2002:str", data)

    Dumper.add_representer(str, str_representer)

    with open(OUT, "w", encoding="utf-8") as f:
        yaml.dump(papers, f, Dumper=Dumper, allow_unicode=True, default_flow_style=False, sort_keys=False)

    print(f"Converted {len(papers)} papers → {OUT}")

    domains = {}
    for p in papers:
        key = f"{p['domain']}/{p['subcategory']}"
        domains[key] = domains.get(key, 0) + 1
    for k, v in sorted(domains.items()):
        print(f"  {k}: {v}")

if __name__ == "__main__":
    main()
