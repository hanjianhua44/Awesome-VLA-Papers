"""
Fetch daily arXiv papers from cs.CV and cs.RO, filter by VLA/AD/robotics relevance.
Outputs a markdown report to daily/YYYY-MM-DD.md
"""
import re
import ssl
import json
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime, timedelta

ROOT = Path(__file__).parent.parent
DAILY_DIR = ROOT / "daily"
DAILY_DIR.mkdir(exist_ok=True)

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

# ---------------------------------------------------------------------------
# Research interest keywords (weighted)
# ---------------------------------------------------------------------------
HIGH_KEYWORDS = [
    "vision-language-action", "VLA", "vision language action",
    "end-to-end driving", "end-to-end autonomous",
    "autonomous driving", "self-driving",
    "robotic manipulation", "robot learning", "robot policy",
    "embodied agent", "embodied AI", "embodied foundation",
    "world model", "action token", "action space",
    "diffusion policy", "flow matching policy",
    "imitation learning", "behavior cloning",
]

MID_KEYWORDS = [
    "multimodal agent", "vision-language model", "VLM",
    "spatial reasoning", "3D understanding", "4D scene",
    "chain-of-thought", "latent reasoning",
    "reinforcement learning from human",
    "sim-to-real", "cross-embodiment",
    "trajectory prediction", "motion planning",
    "visual grounding", "scene generation",
    "physical AI", "physical understanding",
    "foundation model.*robot", "robot.*foundation model",
    "large.*model.*driving", "driving.*large.*model",
    "pretraining.*robot", "robot.*pretraining",
    "video generation.*robot", "robot.*video generation",
    "reward model.*robot", "robot.*reward",
]

LOW_KEYWORDS = [
    "object detection", "segmentation",
    "image generation", "video generation",
    "3D reconstruction", "point cloud",
    "visual question answering",
    "multi-modal", "multimodal",
    "transformer", "attention mechanism",
    "mixture of experts", "MoE",
]

# ---------------------------------------------------------------------------
# Known institution patterns (author name / affiliation hints)
# ---------------------------------------------------------------------------
INST_PATTERNS = {
    # Big tech
    r"\bNVIDIA\b": "NVIDIA",
    r"\bGoogle\b.*\b(DeepMind|Brain|Research)\b": "Google DeepMind",
    r"\bDeepMind\b": "Google DeepMind",
    r"\bMeta\b.*\b(FAIR|AI|Research)\b": "Meta AI",
    r"\bFAIR\b": "Meta AI",
    r"\bMicrosoft\b.*Research": "Microsoft Research",
    r"\bMSRA\b": "MSRA",
    r"\bOpenAI\b": "OpenAI",
    r"\bApple\b": "Apple",
    r"\bAmazon\b": "Amazon",
    r"\bTesla\b": "Tesla",
    r"\bWaymo\b": "Waymo",
    r"\bPhysical Intelligence\b": "Physical Intelligence",
    r"\bBoston Dynamics\b": "Boston Dynamics",
    r"\bToyota\b.*Research": "TRI",
    # Chinese tech
    r"\bBaidu\b": "Baidu",
    r"\bTencent\b": "Tencent",
    r"\bAlibaba\b": "Alibaba",
    r"\bByteDance\b": "ByteDance",
    r"\bHuawei\b": "Huawei",
    r"\bXiaomi\b": "Xiaomi",
    r"\bSenseTime\b": "SenseTime",
    r"\bMegvii\b": "Megvii",
    r"\bHorizon Robotics\b": "Horizon Robotics",
    r"\bBYD\b": "BYD",
    r"\bDJI\b": "DJI",
    r"\bDeepSeek\b": "DeepSeek",
    r"\bLi Auto\b": "Li Auto",
    r"\bNIO\b": "NIO",
    r"\bXPeng\b": "XPeng",
    # Top universities
    r"\bStanford\b": "Stanford",
    r"\bMIT\b": "MIT",
    r"\bBerkeley\b": "UC Berkeley",
    r"\bCMU\b|Carnegie Mellon": "CMU",
    r"\bPrinceton\b": "Princeton",
    r"\bGeorgia Tech\b": "Georgia Tech",
    r"\bUT Austin\b|Univ.*Texas.*Austin": "UT Austin",
    r"\bCornell\b": "Cornell",
    r"\bColumbia\b": "Columbia",
    r"\bNYU\b": "NYU",
    r"\bUCSD\b|UC San Diego": "UCSD",
    r"\bUCLA\b": "UCLA",
    r"\bUMich\b|Univ.*Michigan": "UMich",
    r"\bOxford\b": "Oxford",
    r"\bCambridge\b": "Cambridge",
    r"\bETH\b.*Z": "ETH Zurich",
    r"\bEPFL\b": "EPFL",
    r"\bTsinghua\b": "Tsinghua",
    r"\bPeking\b.*Univ": "PKU",
    r"\bShanghai Jiao Tong\b|SJTU\b": "SJTU",
    r"\bZhejiang\b.*Univ": "ZJU",
    r"\bFudan\b": "Fudan",
    r"\bNanjing\b.*Univ": "Nanjing Univ",
    r"\bUni.*Sci.*Tech.*China\b|USTC\b": "USTC",
    r"\bHuazhong\b|HUST\b": "HUST",
    r"\bSouth China\b.*Tech|SCUT\b": "SCUT",
    r"\bHarbin\b.*Inst|HIT\b": "HIT",
    r"\bBeihang\b|BUAA\b": "BUAA",
    r"\bTianjin\b.*Univ": "Tianjin Univ",
    r"\bDalian\b.*Univ.*Tech|DUT\b": "DUT",
    r"\bXi.an Jiao.*Tong|XJTU\b": "XJTU",
    r"\bSun Yat-sen\b|SYSU\b": "SYSU",
    r"\bRenmin\b|RUC\b": "RUC",
    r"\bWuhan\b.*Univ": "WHU",
    r"\bNorthwest.*Poly|NWPU\b": "NWPU",
    r"\bShanghai AI Lab\b": "Shanghai AI Lab",
    r"\bChinese Univ.*Hong Kong\b|CUHK\b": "CUHK",
    r"\bHong Kong Univ\b|HKU\b": "HKU",
    r"\bPolyU\b|Hong Kong Poly": "PolyU",
    r"\bHKUST\b|Hong Kong.*Sci.*Tech": "HKUST",
    r"\bNTU\b|Nanyang\b": "NTU",
    r"\bNUS\b|National.*Univ.*Singapore": "NUS",
    r"\bKAIST\b": "KAIST",
    r"\bSNU\b|Seoul National": "SNU",
    r"\bTokyo\b.*Univ|Univ.*Tokyo": "Univ of Tokyo",
    r"\bMonash\b": "Monash",
    r"\bShanghaiTech\b": "ShanghaiTech",
    r"\bCAS\b|Chinese Academy of Sci": "CAS",
    r"\bCASIA\b|Inst.*Automation.*CAS": "CASIA",
    r"\bUESTC\b|Univ.*Electronic.*Sci.*Tech": "UESTC",
    r"\bBJTU\b|Beijing Jiaotong": "BJTU",
    r"\bNUDT\b|National Univ.*Defense": "NUDT",
    r"\bXiamen\b.*Univ|XMU\b": "XMU",
    r"\bSoochow\b.*Univ": "Soochow Univ",
    r"\bPCL\b|Peng\s*Cheng\s*Lab": "PCL",
    r"\bTHU\b": "Tsinghua",
    r"\bUber\b": "Uber",
    r"\bQualcomm\b": "Qualcomm",
    r"\bIntel\b.*(?:Lab|Research)": "Intel",
    r"\bSamsung\b": "Samsung",
    r"\bSony\b": "Sony",
    r"\bImperial\b.*College": "Imperial",
}

# Well-known researcher -> institution lookup
RESEARCHER_INST = {
    "Chelsea Finn": "Stanford",
    "Sergey Levine": "UC Berkeley",
    "Pieter Abbeel": "UC Berkeley",
    "Yann LeCun": "Meta AI",
    "Kaiming He": "MIT",
    "Saining Xie": "NYU",
    "Song Han": "MIT",
    "Trevor Darrell": "UC Berkeley",
    "Deva Ramanan": "CMU",
    "Philipp Krahenbuhl": "UT Austin",
    "Marco Pavone": "Stanford",
    "Leonidas Guibas": "Stanford",
    "Andrea Vedaldi": "Oxford",
    "Lerrel Pinto": "NYU",
    "Dieter Fox": "NVIDIA/UW",
    "Shuran Song": "Stanford",
    "Xiaolong Wang": "UCSD",
    "Ming-Yu Liu": "NVIDIA",
    "Sifei Liu": "NVIDIA",
    "Boris Ivanovic": "NVIDIA",
    "Yilun Du": "MIT",
    "Russ Tedrake": "MIT/TRI",
    "Abhinav Gupta": "CMU",
    "Deepak Pathak": "CMU",
    "Mike Zheng Shou": "NUS",
    "Gim Hee Lee": "NUS",
    "Wenqi Shao": "Shanghai AI Lab",
    "Hongyang Li": "Shanghai AI Lab",
    "Jiaming Liu": "PKU",
    "Hang Zhao": "Tsinghua",
    "Hao Zhao": "Tsinghua",
    "Li Zhang": "Fudan",
    "Xinge Zhu": "CUHK",
    "Pheng-Ann Heng": "CUHK",
    "Hesheng Wang": "SJTU",
    "Jingkuan Song": "UESTC",
    "Jianlong Fu": "MSRA",
    "Bei Liu": "MSRA",
    "Yaobo Liang": "MSRA",
}


def scrape_affiliations(arxiv_id: str) -> list:
    """Scrape author affiliations from arXiv abstract page."""
    url = f"https://arxiv.org/abs/{arxiv_id}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "VLA-Paper-Agent/1.0"})
        resp = urllib.request.urlopen(req, context=SSL_CTX, timeout=30)
        html = resp.read().decode("utf-8", errors="ignore")
        # arXiv shows affiliations in parentheses after author names, or in meta tags
        affs = re.findall(r'\(([^)]{3,80})\)', html[html.find("authors"):html.find("authors")+5000] if "authors" in html else "")
        return affs[:10]
    except Exception:
        return []


def identify_institutions(authors: list, abstract: str, extra_text: str = "") -> str:
    """Identify institution from authors list, abstract, and known patterns."""
    text = " ".join(authors) + " " + abstract + " " + extra_text
    found = []

    for author in authors[:6]:
        name = author.strip()
        for known, inst in RESEARCHER_INST.items():
            if known.lower() in name.lower():
                if inst not in found:
                    found.append(inst)

    for pattern, inst in INST_PATTERNS.items():
        if re.search(pattern, text, re.IGNORECASE):
            if inst not in found:
                found.append(inst)

    if not found:
        team_patterns = [
            (r"(\w+)\s+Team", lambda m: m.group(1)),
        ]
        for pat, extractor in team_patterns:
            m = re.search(pat, " ".join(authors[:3]))
            if m:
                found.append(extractor(m))

    return ", ".join(found[:3]) if found else "—"


TIER1_INSTITUTIONS = {
    # Big tech
    "nvidia", "google deepmind", "google", "meta ai", "meta", "openai",
    "apple", "tesla", "waymo", "physical intelligence", "boston dynamics", "tri",
    "microsoft research", "microsoft", "msra", "deepseek", "amazon",
    "bytedance", "tencent", "alibaba", "baidu", "huawei", "huawei noah", "xiaomi",
    "sensetime", "megvii", "horizon robotics", "li auto", "byd", "dji", "nio", "xpeng",
    "uber", "qualcomm", "intel", "samsung", "sony",
    # Top US/EU universities
    "stanford", "mit", "uc berkeley", "berkeley", "cmu", "carnegie mellon",
    "princeton", "georgia tech", "ut austin", "cornell", "columbia", "nyu",
    "ucsd", "uc san diego", "ucla", "umich", "university of michigan",
    "oxford", "cambridge", "eth zurich", "epfl", "imperial",
    # Top CN universities
    "tsinghua", "thu", "pku", "peking", "sjtu", "zju", "zhejiang",
    "fudan", "ustc", "hust", "huazhong", "scut", "buaa", "beihang",
    "hit", "harbin", "xjtu", "nudt", "sysu", "sun yat-sen",
    "whu", "wuhan", "uestc", "bjtu", "ruc", "nanjing univ",
    "tsinghua shenzhen", "hit shenzhen",
    # CN labs & institutes
    "shanghai ai lab", "casia", "cas", "cas shenzhen", "pcl",
    "shanghaitech",
    # HK / SG / KR / JP
    "cuhk", "hku", "hkust", "polyu",
    "ntu", "nanyang", "nus",
    "kaist", "snu", "seoul national",
    "univ of tokyo", "monash",
}


def is_known_institution(inst_str: str) -> bool:
    if inst_str == "—":
        return False
    parts = [s.strip().lower() for s in inst_str.split(",")]
    return any(p in TIER1_INSTITUTIONS for p in parts)


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
            score += 1
            topics.append(kw)

    if "cs.CV" in categories:
        score += 1
    if "cs.RO" in categories:
        score += 1

    return score, topics[:5]


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

    # arXiv new listings appear ~20:00 UTC the day before for next day
    # Use submittedDate range: target day covers papers announced that day
    d = dt.strftime("%Y%m%d")
    d_prev = (dt - timedelta(days=1)).strftime("%Y%m%d")

    # Fetch cs.CV and cs.RO separately for completeness, paginated
    all_raw = []
    seen_ids = set()

    for cat in ["cs.CV", "cs.RO"]:
        query = f"cat:{cat}"
        batch_size = 200
        for start in range(0, 400, batch_size):
            print(f"  Fetching {cat} start={start}...")
            xml_data = fetch_arxiv_batch(query, start, batch_size)
            batch = parse_entries(xml_data)
            if not batch:
                break
            for p in batch:
                if p["arxiv_id"] not in seen_ids:
                    seen_ids.add(p["arxiv_id"])
                    all_raw.append(p)
            time.sleep(5)

    # Filter by published date: keep papers from target day and day before
    # (arXiv listings for day X include papers published on X-1 and X)
    target_dates = {
        dt.strftime("%Y-%m-%d"),
        (dt - timedelta(days=1)).strftime("%Y-%m-%d"),
    }
    date_filtered = [p for p in all_raw if p["published"] in target_dates]

    # If weekend/holiday yields few results, widen to 3 days
    if len(date_filtered) < 30:
        target_dates.add((dt - timedelta(days=2)).strftime("%Y-%m-%d"))
        target_dates.add((dt - timedelta(days=3)).strftime("%Y-%m-%d"))
        date_filtered = [p for p in all_raw if p["published"] in target_dates]

    print(f"  Raw total: {len(all_raw)}, date-filtered ({', '.join(sorted(target_dates))}): {len(date_filtered)}")

    # Score and filter
    results = []
    for p in date_filtered:
        score, topics = compute_relevance(p["title"], p["abstract"], p["categories"])
        aff_text = " ".join(p.get("affiliations", []))
        institution = identify_institutions(p["authors"], p["abstract"], aff_text)

        p["score"] = score
        p["topics"] = topics
        p["institution"] = institution

        known = is_known_institution(institution)
        if known:
            p["score"] += 2

        # Keep if: known institution with any relevance, OR moderate+ keyword relevance
        if known and score >= 2:
            results.append(p)
        elif score >= 4:
            results.append(p)

    results.sort(key=lambda p: p["score"], reverse=True)
    return results, len(date_filtered)


def categorize_paper(topics: list, categories: str) -> str:
    """Assign a rough category based on matched topics."""
    text = " ".join(topics).lower() + " " + categories.lower()
    if any(k in text for k in ["driving", "autonomous", "navigation"]):
        return "Autonomous Driving"
    if any(k in text for k in ["robot", "manipulation", "embodied", "cross-embodiment", "sim-to-real"]):
        return "Robotics"
    if any(k in text for k in ["agent"]):
        return "Agent"
    if any(k in text for k in ["world model", "physical"]):
        return "World Models"
    if any(k in text for k in ["VLA", "vision-language-action", "vision language action"]):
        return "VLA"
    return "Related"


def generate_daily_report(papers: list, date_str: str, total_scanned: int = 0) -> str:
    """Generate markdown report for a given day."""
    lines = []
    lines.append(f"# arXiv Daily Report: {date_str}")
    lines.append("")
    scanned_str = f" (scanned {total_scanned} papers from cs.CV + cs.RO)" if total_scanned else ""
    lines.append(f"> **{len(papers)} relevant papers**{scanned_str} | Focus: VLA, Autonomous Driving, Robotics, Agent")
    lines.append("")
    lines.append("To add a paper to the main list, tell me: `add #N` (e.g. `add #1 #3 #7`)")
    lines.append("")

    by_cat = {}
    for p in papers:
        cat = categorize_paper(p["topics"], p["categories"])
        by_cat.setdefault(cat, []).append(p)

    cat_order = ["VLA", "Autonomous Driving", "Robotics", "Agent", "World Models", "Related"]
    idx = 1

    for cat in cat_order:
        cat_papers = by_cat.get(cat, [])
        if not cat_papers:
            continue

        lines.append(f"## {cat} ({len(cat_papers)})")
        lines.append("")

        for p in cat_papers:
            stars = "⭐" * min(p["score"] // 3, 3)
            inst_str = f" | **{p['institution']}**" if p["institution"] != "—" else ""
            authors_short = ", ".join(p["authors"][:4])
            if len(p["authors"]) > 4:
                authors_short += f" et al. ({len(p['authors'])})"

            lines.append(f"### #{idx}. {p['title']} {stars}")
            lines.append("")
            lines.append(f"**{authors_short}**{inst_str}")
            lines.append("")
            lines.append(f"Categories: `{p['categories']}` | [{p['arxiv_id']}]({p['url']})")
            lines.append("")

            abstract_short = p["abstract"][:400]
            if len(p["abstract"]) > 400:
                abstract_short += "..."
            lines.append(f"> {abstract_short}")
            lines.append("")
            idx += 1

    if not papers:
        lines.append("*No relevant papers found for this date.*")
        lines.append("")

    return "\n".join(lines)


def main():
    import sys
    date_str = sys.argv[1] if len(sys.argv) > 1 else datetime.now().strftime("%Y-%m-%d")

    print(f"Fetching arXiv papers for {date_str} (cs.CV + cs.RO)...")
    papers, total_scanned = fetch_arxiv_papers(date_str)
    print(f"Scanned {total_scanned} papers, {len(papers)} passed relevance + institution filter")

    report = generate_daily_report(papers, date_str, total_scanned)
    out_path = DAILY_DIR / f"{date_str}.md"
    out_path.write_text(report, encoding="utf-8")
    print(f"Report saved to {out_path}")

    # Also save raw JSON for programmatic access
    json_path = DAILY_DIR / f"{date_str}.json"
    json_data = [{k: v for k, v in p.items()} for p in papers]
    json_path.write_text(json.dumps(json_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Raw data saved to {json_path}")


if __name__ == "__main__":
    main()
