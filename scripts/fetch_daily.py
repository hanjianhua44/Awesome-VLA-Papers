"""
Fetch daily arXiv papers from cs.CV and cs.RO, filter by VLA/AD/robotics relevance.
Outputs a markdown report to daily/YYYY/MM/YYYY-MM-DD.md
"""
import functools
import re
import io
import ssl
import json
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime, timedelta

print = functools.partial(print, flush=True)

try:
    import pdfplumber
    HAS_PDFPLUMBER = True
except ImportError:
    HAS_PDFPLUMBER = False

ROOT = Path(__file__).parent.parent
DAILY_BASE = ROOT / "daily"


def _daily_dir(date_str: str) -> Path:
    """Return daily/YYYY/MM/ directory for a given date, creating it if needed."""
    year, month = date_str[:4], date_str[5:7]
    d = DAILY_BASE / year / month
    d.mkdir(parents=True, exist_ok=True)
    return d

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

# ---------------------------------------------------------------------------
# Research interest keywords (weighted)
# ---------------------------------------------------------------------------
HIGH_KEYWORDS = [
    # === Core VLA ===
    r"vision.language.action", r"\bVLA\b", r"visuomotor policy",
    r"generalist.{0,10}(policy|robot|agent)", r"language.conditioned.{0,10}(policy|control|manipulation)",
    r"latent action", r"action prediction", r"action generation",
    # === End-to-End Driving ===
    r"end.to.end.{0,10}(driving|autonomous)", r"autonomous driving", r"self.driving",
    # === Robotics Core ===
    r"robotic manipulation", r"robot learning", r"robot policy",
    r"embodied.{0,5}(agent|AI|foundation|intelligence)",
    # === World Models ===
    r"world model", r"driving.{0,10}world", r"robot.{0,10}world model",
    # === Action Representation ===
    r"action token", r"action.{0,5}space", r"action chunking",
    # === Policy Learning ===
    r"diffusion policy", r"flow matching.{0,10}(policy|action|robot)",
    r"imitation learning", r"behavior cloning",
    r"closed.loop.{0,10}(policy|control|driving|learning)",
]

MID_KEYWORDS = [
    # === VLM / Multimodal for Robotics ===
    r"vision.language model", r"\bVLM\b",
    r"multimodal.{0,10}(agent|robot|driving|embodied)",
    # === Reasoning ===
    r"chain.of.thought", r"latent reasoning", r"spatial reasoning",
    r"3D understanding", r"4D.{0,5}(scene|world|understanding)",
    r"embodied reasoning", r"visual reasoning",
    # === RL / Reward ===
    r"reinforcement learning.{0,15}(robot|policy|driving|human|action)",
    r"reward.{0,10}(model|learning|shaping)",
    r"\bRLHF\b", r"\bGRPO\b", r"\bDPO\b", r"\bPPO\b",
    r"online.{0,5}(RL|reinforcement|fine.tun)",
    # === Transfer & Generalization ===
    r"sim.to.real", r"real.to.sim", r"cross.embodiment",
    r"zero.shot.{0,10}(transfer|policy|manipulation|driving)",
    r"few.shot.{0,10}(learning|adapt|robot|policy)",
    r"domain.{0,5}(adapt|random|transfer)",
    # === Trajectory & Planning ===
    r"trajectory.{0,5}(prediction|planning|optimization|forecast)",
    r"motion planning", r"path planning",
    r"long.horizon.{0,10}(planning|task|manipulation)",
    r"task planning", r"task.{0,5}and.{0,5}motion planning",
    # === Scene & Generation ===
    r"visual grounding", r"scene generation",
    r"physical.{0,5}(AI|understanding|simulation|reasoning)",
    # === Foundation Models for Robotics/Driving ===
    r"foundation model.{0,20}(robot|driving|embod|manipul)",
    r"(robot|driving|embod).{0,20}foundation model",
    r"pretrain.{0,15}(robot|driving|embod|policy|action)",
    r"(robot|driving|embod).{0,15}pretrain",
    # === Driving Perception ===
    r"\bBEV\b", r"bird.s.eye.view", r"occupancy.{0,5}(prediction|network|map)",
    r"sensor fusion", r"\bLiDAR\b",
    r"multi.camera", r"multi.view.{0,10}(driving|percep|represent)",
    r"lane.{0,5}(detection|prediction|change)",
    r"scene understanding", r"semantic map",
    r"driving.{0,10}planning", r"planning.{0,10}driving",
    # === Robotics Specific ===
    r"grasp(ing)?", r"dexterous.{0,10}(manipulation|hand)",
    r"(visual|object|robot).{0,5}navigation",
    r"manipulation policy", r"policy.{0,5}learning",
    r"teleoperation", r"human demonstration",
    r"humanoid", r"quadruped", r"legged.{0,5}(robot|locomotion)",
    r"bimanual", r"mobile.{0,5}manipulat",
    r"affordance",
    # === Data & Scaling ===
    r"data.{0,5}engine", r"data.{0,5}(scaling|curation|augment).{0,10}(robot|driving|policy)",
    # === LLM/GPT for Driving/Robotics ===
    r"LLM.{0,10}(robot|driving|embod|manipul|plan)",
    r"(robot|driving|embod).{0,10}LLM",
    r"GPT.{0,10}driv", r"driv.{0,10}GPT",
    # === Video / Visual Prediction ===
    r"video.{0,5}(prediction|world|generation).{0,10}(robot|driving|embod|action)",
    # === Safety ===
    r"safe.{0,5}(driving|robot|policy|RL|reinforcement|control)",
    # === Tokenization ===
    r"action.{0,5}tokeniz", r"visual.{0,5}tokeniz",
    # === Gaussian / NeRF for Driving/Robot ===
    r"gaussian.{0,5}splat.{0,15}(driving|robot|scene|world)",
    r"(NeRF|neural.radiance).{0,15}(driving|robot|scene|world)",
]

LOW_KEYWORDS = [
    r"object detection", r"semantic segmentation",
    r"image generation", r"video generation",
    r"3D reconstruction", r"point cloud",
    r"visual question answering",
    r"\bMoE\b", r"mixture of experts",
    r"scene graph", r"visual relationship",
    r"depth estimation",
    r"benchmark.{0,10}(robot|driving|embod|manipul|autonom)",
    r"survey.{0,10}(robot|driving|embod|VLA|autonomous|world model)",
]

# ---------------------------------------------------------------------------
# Institution identification (shared module)
# ---------------------------------------------------------------------------
from inst_utils import (
    INST_PATTERNS, RESEARCHER_INST, TIER1_INSTITUTIONS,
    extract_institutions_from_pdf, identify_institutions, is_known_institution,
)



def compute_relevance(title: str, abstract: str, categories: str) -> tuple:
    """Return (score, matched_topics) for relevance ranking."""
    text = (title + " " + abstract).lower()
    score = 0
    topics = []

    for kw in HIGH_KEYWORDS:
        if re.search(kw.lower(), text):
            score += 3
            topics.append(kw)

    for kw in MID_KEYWORDS:
        if re.search(kw.lower(), text):
            score += 2
            topics.append(kw)

    for kw in LOW_KEYWORDS:
        if re.search(kw.lower(), text):
            score += 1
            topics.append(kw)

    if "cs.CV" in categories:
        score += 1
    if "cs.RO" in categories:
        score += 1

    return score, topics[:8]


def fetch_arxiv_batch(query: str, start: int, max_results: int, retries: int = 3) -> str:
    """Fetch a single batch from arXiv API with retry."""
    params = {
        "search_query": query,
        "start": start,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"http://export.arxiv.org/api/query?{urllib.parse.urlencode(params)}"
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "VLA-Paper-Agent/1.0"})
            resp = urllib.request.urlopen(req, context=SSL_CTX, timeout=120)
            return resp.read().decode("utf-8")
        except Exception as e:
            if attempt < retries - 1:
                wait = 10 * (attempt + 1)
                print(f"    Retry {attempt+1}/{retries} after {wait}s: {e}")
                time.sleep(wait)
            else:
                raise


def parse_entries(xml_data: str) -> list:
    """Parse arXiv API XML response into paper dicts."""
    ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    root = ET.fromstring(xml_data)
    papers = []

    for entry in root.findall("atom:entry", ns):
        title_el = entry.find("atom:title", ns)
        if title_el is None or title_el.text is None:
            continue
        title = " ".join(title_el.text.strip().split())

        arxiv_id = ""
        id_el = entry.find("atom:id", ns)
        if id_el is not None:
            m = re.search(r"(\d{4}\.\d{4,5})", id_el.text)
            if m:
                arxiv_id = m.group(1)

        if not arxiv_id:
            continue

        abstract = ""
        abs_el = entry.find("atom:summary", ns)
        if abs_el is not None and abs_el.text:
            abstract = " ".join(abs_el.text.strip().split())

        authors = []
        affiliations = []
        for author_el in entry.findall("atom:author", ns):
            name_el = author_el.find("atom:name", ns)
            if name_el is not None:
                authors.append(name_el.text.strip())
            for aff_el in author_el.findall("arxiv:affiliation", ns):
                if aff_el.text:
                    affiliations.append(aff_el.text.strip())

        categories = ""
        for cat_el in entry.findall("atom:category", ns):
            categories += cat_el.get("term", "") + " "

        published = ""
        pub_el = entry.find("atom:published", ns)
        if pub_el is not None:
            published = pub_el.text[:10]

        papers.append({
            "arxiv_id": arxiv_id,
            "title": title,
            "authors": authors,
            "affiliations": affiliations,
            "abstract": abstract,
            "categories": categories.strip(),
            "published": published,
            "url": f"https://arxiv.org/abs/{arxiv_id}",
        })

    return papers


def fetch_arxiv_papers(date_str: str = None):
    """Fetch ALL cs.CV + cs.RO papers, then filter locally by relevance + institution."""
    if date_str:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
    else:
        dt = datetime.now()

    # arXiv listing schedule:
    #   Fri listing  = Thu submissions
    #   (no Sat/Sun listing)
    #   Mon listing  = Fri + Sat + Sun submissions
    #   Tue listing  = Mon submissions
    #   Wed listing  = Tue submissions
    #   Thu listing  = Wed submissions
    weekday = dt.weekday()  # 0=Mon
    if weekday == 0:
        target_dates = {(dt - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(1, 4)}
    else:
        target_dates = {(dt - timedelta(days=1)).strftime("%Y-%m-%d")}

    earliest_target = min(target_dates)
    print(f"  Target dates: {sorted(target_dates)} (earliest: {earliest_target})")

    # Fetch cs.CV and cs.RO separately, paginated
    all_raw = []
    seen_ids = set()
    days_ago = max(0, (datetime.now() - dt).days)

    for cat in ["cs.CV", "cs.RO"]:
        query = f"cat:{cat}"
        batch_size = 200
        base = 800 if cat == "cs.CV" else 400
        max_fetch = base + days_ago * (200 if cat == "cs.CV" else 80)
        for start in range(0, max_fetch, batch_size):
            print(f"  Fetching {cat} start={start}...")
            xml_data = fetch_arxiv_batch(query, start, batch_size)
            batch = parse_entries(xml_data)
            if not batch:
                break
            new_count = 0
            for p in batch:
                if p["arxiv_id"] not in seen_ids:
                    seen_ids.add(p["arxiv_id"])
                    all_raw.append(p)
                    new_count += 1
            batch_dates = [p["published"] for p in batch if p["published"]]
            latest_in_batch = max(batch_dates) if batch_dates else ""
            print(f"    Got {len(batch)} entries, {new_count} new (latest: {latest_in_batch})")
            if new_count == 0:
                break
            if latest_in_batch and latest_in_batch < earliest_target:
                print(f"    Reached papers older than {earliest_target}, stopping")
                break
            time.sleep(5)
    date_filtered = [p for p in all_raw if p["published"] in target_dates]

    print(f"  Raw total: {len(all_raw)}, date-filtered ({', '.join(sorted(target_dates))}): {len(date_filtered)}")

    # Phase 1: Score and broad filter (score >= 5) to build candidate pool
    candidates = []
    for p in date_filtered:
        score, topics = compute_relevance(p["title"], p["abstract"], p["categories"])
        aff_text = " ".join(p.get("affiliations", []))
        institution = identify_institutions(p["authors"], aff_text)

        p["score"] = score
        p["topics"] = topics
        p["institution"] = institution

        if is_known_institution(institution):
            p["score"] += 3

        if score >= 3:
            candidates.append(p)

    print(f"  Candidates after keyword filter: {len(candidates)}/{len(date_filtered)}")

    # Phase 2: PDF enrichment — identify institutions before final filtering
    if HAS_PDFPLUMBER:
        print(f"  Enriching institutions from PDF for {len(candidates)} papers...")
        enriched = 0
        for i, p in enumerate(candidates):
            pdf_inst = extract_institutions_from_pdf(p["arxiv_id"])
            if pdf_inst:
                p["institution"] = pdf_inst
                if is_known_institution(pdf_inst) and not is_known_institution(p.get("_prev_inst", "")):
                    p["score"] += 3
                enriched += 1
            if (i + 1) % 10 == 0:
                print(f"    Processed {i+1}/{len(candidates)}...")
            time.sleep(1)
        print(f"    PDF enrichment: {enriched}/{len(candidates)} institutions found")

    # Phase 3: Keep only papers with at least one TIER1 institution
    results = [p for p in candidates if is_known_institution(p["institution"])]
    results.sort(key=lambda p: p["score"], reverse=True)
    dropped = len(candidates) - len(results)
    print(f"  Final results: {len(results)} (dropped {dropped} without TIER1 institution)")

    return results, len(date_filtered), sorted(target_dates)


def categorize_paper(topics: list, categories: str, title: str = "", abstract: str = "") -> str:
    """Assign a rough category based on matched topics, categories, and content."""
    topic_text = " ".join(topics).lower()
    full_text = (topic_text + " " + title + " " + abstract).lower()
    cats = categories.lower()

    # VLA first (most specific)
    if re.search(r"vision.language.action|\bvla\b|visuomotor.{0,5}policy|generalist.{0,10}(policy|robot)", full_text):
        return "VLA"

    # Autonomous Driving
    if re.search(
        r"autonomous driving|self.driving|end.to.end.{0,5}driv|driving.{0,5}(model|policy|scene|planning|world)"
        r"|lane.{0,5}(detect|predict)|traffic.{0,5}(scene|predict)"
        r"|\bbev\b|bird.s.eye|occupancy.{0,5}(prediction|network)"
        r"|driving.{0,5}simulat|driving.{0,5}benchmark",
        full_text
    ):
        return "Autonomous Driving"

    # World Models
    if re.search(
        r"world model|video.{0,5}prediction|future.{0,5}prediction"
        r"|latent.{0,5}dynamics|physical.{0,5}simulat"
        r"|world.{0,5}simulat|4d.{0,5}generat",
        full_text
    ):
        return "World Models"

    # Robotics
    if re.search(
        r"robot|manipulation|embodied|grasp|dexterous|locomotion|teleoperat"
        r"|sim.to.real|cross.embodiment|imitation learning|behavior cloning"
        r"|diffusion policy|action.{0,5}token|action.{0,5}chunk"
        r"|humanoid|quadruped|legged|bimanual"
        r"|navigation|mobile.{0,5}manipulat"
        r"|affordance|pick.{0,5}(and|&).{0,5}place",
        full_text
    ):
        return "Robotics"
    if "cs.ro" in cats and "cs.cv" not in cats:
        return "Robotics"

    # Agent
    if re.search(r"embodied.{0,5}agent|multi.agent|llm.{0,5}agent|autonomous.{0,5}agent", full_text):
        return "Agent"

    # RL & Policy Optimization
    if re.search(
        r"reinforcement learning|reward.{0,5}(model|learning)|policy.{0,5}(optimiz|gradient)"
        r"|\brlhf\b|\bgrpo\b|\bdpo\b|\bppo\b|online.{0,5}(rl|fine.tun)",
        full_text
    ):
        return "RL & Policy Optimization"

    # Spatial & Perception
    if re.search(
        r"spatial reasoning|3d.{0,5}understand|4d.{0,5}scene"
        r"|depth.{0,5}estim|point cloud|3d.{0,5}reconstruct"
        r"|scene understanding|visual grounding"
        r"|scene graph|gaussian.{0,5}splat|nerf",
        full_text
    ):
        return "Spatial & Perception"

    # Efficient & Architecture
    if re.search(
        r"efficient|compression|pruning|distill"
        r"|tokeniz|mixture of experts|\bmoe\b"
        r"|sparse attention|visual.{0,5}encoder",
        full_text
    ):
        return "Efficient & Architecture"

    return "Related"


CAT_CN = {
    "VLA": ("🤖 VLA 模型", "视觉-语言-动作模型，连接感知、理解与控制的核心架构"),
    "Autonomous Driving": ("🚗 自动驾驶", "端到端驾驶、规划、仿真与安全"),
    "Robotics": ("🦾 机器人操作", "灵巧操作、双臂协同、移动操控与具身智能"),
    "Agent": ("🧠 智能体", "通用智能体、任务规划与多模态决策"),
    "World Models": ("🌍 世界模型", "环境动态建模、视频预测与物理仿真"),
    "RL & Policy Optimization": ("🎯 强化学习与策略优化", "RLHF、GRPO、在线 RL 与奖励建模"),
    "Spatial & Perception": ("👁️ 空间感知与 3D 理解", "3D 重建、空间推理与多模态几何"),
    "Efficient & Architecture": ("⚡ 高效架构与推理加速", "模型压缩、token 优化与部署加速"),
    "Related": ("📎 相关工作", ""),
}

def _make_summary_cn(title: str, abstract: str) -> str:
    """Generate a concise Chinese-style summary from abstract."""
    abs_lower = (title + " " + abstract).lower()
    parts = []

    if "autonomous driving" in abs_lower or "end-to-end driving" in abs_lower:
        domain = "自动驾驶"
    elif "robot" in abs_lower or "manipulation" in abs_lower:
        domain = "机器人"
    elif "embodied" in abs_lower:
        domain = "具身智能"
    else:
        domain = "多模态AI"

    method_keywords = {
        "diffusion": "扩散模型", "flow matching": "流匹配", "reinforcement learning": "强化学习",
        "mixture of experts": "混合专家 (MoE)", "moe": "混合专家 (MoE)",
        "world model": "世界模型", "chain-of-thought": "思维链 (CoT)",
        "transformer": "Transformer", "tokeniz": "动作token化",
        "imitation learning": "模仿学习", "contrastive": "对比学习",
        "distillation": "蒸馏", "pruning": "剪枝", "quantiz": "量化",
        "vla": "VLA", "pretraining": "预训练", "fine-tun": "微调",
        "zero-shot": "零样本", "few-shot": "少样本",
    }
    methods = [cn for en, cn in method_keywords.items() if en in abs_lower]

    sents = abstract.replace("\n", " ").split(". ")
    core_sent = ""
    for s in sents:
        sl = s.lower()
        if any(k in sl for k in ["we propose", "we present", "we introduce", "this paper", "in this work"]):
            core_sent = s.strip().rstrip(".")
            break
    if not core_sent and len(sents) > 1:
        core_sent = sents[1].strip().rstrip(".")

    if core_sent:
        if len(core_sent) > 200:
            core_sent = core_sent[:200] + "..."
        parts.append(core_sent)

    if methods:
        parts.append(f"**关键技术：** {' / '.join(methods[:4])}")

    result_keywords = ["state-of-the-art", "sota", "outperform", "surpass", "improve", "achieve"]
    for s in sents:
        if any(k in s.lower() for k in result_keywords):
            result = s.strip().rstrip(".")
            if len(result) > 150:
                result = result[:150] + "..."
            parts.append(f"**核心结果：** {result}")
            break

    return "\n>\n> ".join(parts) if parts else abstract[:200] + "..."


def _cover_str(date_str: str, cover_dates: list = None) -> str:
    """Build a human-readable coverage string for the report title."""
    if cover_dates and len(cover_dates) > 0:
        short = [d[5:] for d in cover_dates]  # "2026-03-10" -> "03-10"
        if len(short) == 1:
            return short[0]
        return f"{short[0]} ~ {short[-1]}"
    # fallback: compute from date_str
    from datetime import datetime as _dt, timedelta
    dt = _dt.strptime(date_str, "%Y-%m-%d")
    if dt.weekday() == 0:
        dates = sorted((dt - timedelta(days=i)).strftime("%m-%d") for i in range(1, 4))
        return f"{dates[0]} ~ {dates[-1]}"
    return (dt - timedelta(days=1)).strftime("%m-%d")


def generate_daily_report(papers: list, date_str: str, total_scanned: int = 0,
                          cover_dates: list = None) -> str:
    """Generate 机器之心 style Chinese daily report."""
    lines = []

    cover = _cover_str(date_str, cover_dates)
    lines.append(f"# 📄 arXiv VLA 速递 | {cover} 论文")
    lines.append("")
    lines.append(f"> 🔍 扫描 cs.CV + cs.RO 共 **{total_scanned}** 篇，筛选出 **{len(papers)}** 篇与 VLA / 自动驾驶 / 机器人 / Agent 相关的工作")
    lines.append("")

    by_cat = {}
    for p in papers:
        cat = categorize_paper(p["topics"], p["categories"], p.get("title", ""), p.get("abstract", ""))
        by_cat.setdefault(cat, []).append(p)

    cat_order = ["VLA", "Autonomous Driving", "Robotics", "Agent", "World Models",
                 "RL & Policy Optimization", "Spatial & Perception",
                 "Efficient & Architecture", "Related"]

    lines.append("## 📊 今日概览")
    lines.append("")
    lines.append("| 方向 | 数量 | 亮点 |")
    lines.append("|------|------|------|")
    for cat in cat_order:
        cat_papers = by_cat.get(cat, [])
        if not cat_papers:
            continue
        cn_name, _ = CAT_CN.get(cat, (cat, ""))
        top_inst = []
        for p in cat_papers[:3]:
            if p["institution"] != "—" and p["institution"] not in top_inst:
                top_inst.append(p["institution"])
        inst_preview = ", ".join(top_inst[:3]) if top_inst else "—"
        lines.append(f"| {cn_name} | {len(cat_papers)} | {inst_preview} |")
    lines.append("")

    lines.append("> 💡 想要将某篇论文加入主列表？回复 `add #N`（如 `add #1 #3 #7`）")
    lines.append("")
    lines.append("---")
    lines.append("")

    idx = 1
    for cat in cat_order:
        cat_papers = by_cat.get(cat, [])
        if not cat_papers:
            continue

        cn_name, cn_desc = CAT_CN.get(cat, (cat, ""))
        lines.append(f"## {cn_name}（{len(cat_papers)} 篇）")
        if cn_desc:
            lines.append(f"*{cn_desc}*")
        lines.append("")

        for p in cat_papers:
            score = p["score"]
            if score >= 9:
                badge = "🔥"
            elif score >= 6:
                badge = "⭐"
            else:
                badge = "📌"

            inst_tag = ""
            if p["institution"] != "—":
                inst_tag = f" `{p['institution']}`"

            lines.append(f"### {badge} #{idx}｜{p['title']}")
            lines.append("")
            authors_short = ", ".join(p["authors"][:3])
            if len(p["authors"]) > 3:
                authors_short += f" 等 ({len(p['authors'])} 位作者)"

            meta_parts = [f"**{authors_short}**"]
            if inst_tag:
                meta_parts.append(inst_tag)
            lines.append(" | ".join(meta_parts))
            lines.append("")
            lines.append(f"📎 [{p['arxiv_id']}]({p['url']}) | `{p['categories']}`")
            lines.append("")

            summary = _make_summary_cn(p["title"], p["abstract"])
            lines.append(f"> {summary}")
            lines.append("")
            lines.append("---")
            lines.append("")
            idx += 1

    if not papers:
        lines.append("*今日暂无相关论文。*")
        lines.append("")

    lines.append(f"*本报告由 Awesome-VLA-Papers 自动生成，基于 arXiv cs.CV + cs.RO 每日更新。*")
    return "\n".join(lines)


def main():
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    date_str = sys.argv[1] if len(sys.argv) > 1 else datetime.now().strftime("%Y-%m-%d")

    print(f"Fetching arXiv papers for {date_str} (cs.CV + cs.RO)...")
    papers, total_scanned, cover_dates = fetch_arxiv_papers(date_str)
    print(f"Scanned {total_scanned} papers, {len(papers)} passed relevance + institution filter")

    daily_dir = _daily_dir(date_str)
    report = generate_daily_report(papers, date_str, total_scanned, cover_dates)
    out_path = daily_dir / f"{date_str}.md"
    out_path.write_text(report, encoding="utf-8")
    print(f"Report saved to {out_path}")

    # Also save raw JSON for programmatic access
    json_path = daily_dir / f"{date_str}.json"
    json_data = [{k: v for k, v in p.items()} for p in papers]
    json_path.write_text(json.dumps(json_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Raw data saved to {json_path}")


if __name__ == "__main__":
    main()
