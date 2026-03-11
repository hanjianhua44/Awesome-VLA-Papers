"""Shared institution identification utilities.

Used by fetch_daily.py, verify_institutions.py, and regen_daily.py.
Single source of truth for INST_PATTERNS, RESEARCHER_INST, and extraction logic.
"""
import io
import os
import re
import ssl
import time
import urllib.request
from pathlib import Path

try:
    import pdfplumber
    HAS_PDFPLUMBER = True
except ImportError:
    HAS_PDFPLUMBER = False

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

# ---------------------------------------------------------------------------
# Known institution regex patterns (matched against affiliation text / PDF header)
# ---------------------------------------------------------------------------
INST_PATTERNS = {
    # === Big Tech (US/Global) ===
    r"\bNVIDIA\b": "NVIDIA",
    r"\bGoogle\s+(DeepMind|Brain|Research)\b": "Google DeepMind",
    r"\bDeepMind\b": "Google DeepMind",
    r"\bMeta\s+(FAIR|AI|Research)\b": "Meta AI",
    r"\bFAIR\b": "Meta AI",
    r"\bMicrosoft\s+Research": "Microsoft Research",
    r"\bMSRA\b": "MSRA",
    r"\bOpenAI\b": "OpenAI",
    r"Apple\s+(?:Inc|Research|Machine Learning)": "Apple",
    r"\bAmazon\b": "Amazon",
    r"\bTesla\b": "Tesla",
    r"\bUber\b": "Uber",
    r"\bQualcomm\b": "Qualcomm",
    r"\bIntel\b.*?(?:Lab|Research)": "Intel",
    r"\bSamsung\b": "Samsung",
    r"\bSony\b": "Sony",
    # === Autonomous Driving Companies ===
    r"\bWaabi\b": "Waabi",
    r"\bWaymo\b": "Waymo",
    r"\bCruise\b": "Cruise",
    r"\bAurora\b.*?(?:Innovation|Driv)": "Aurora",
    r"\bNuro\b": "Nuro",
    r"\bZoox\b": "Zoox",
    r"\bMotional\b": "Motional",
    r"\bMobileye\b": "Mobileye",
    r"\bWoven\b.*?Planet|Woven\b.*?Toyota": "Woven by Toyota",
    r"\bPony\.?ai\b": "Pony.ai",
    r"\bMomenta\b": "Momenta",
    r"\bTuSimple\b": "TuSimple",
    r"\bBosch\b": "Bosch",
    r"\bValeo\b": "Valeo",
    r"\bContinental\b": "Continental",
    # === Robotics Companies ===
    r"\bPhysical Intelligence\b": "Physical Intelligence",
    r"\bBoston Dynamics\b": "Boston Dynamics",
    r"\bToyota Research\b|\bTRI\b": "TRI",
    r"\bAgility\b.*?Robotics": "Agility Robotics",
    r"\bFigure\s+AI\b": "Figure AI",
    r"\b1X\b.*?Technolog": "1X Technologies",
    r"\bUnitre+\b": "Unitree",
    r"\bCovariant\b": "Covariant",
    r"\bAgibot\b": "Agibot",
    r"\bGalbot\b": "Galbot",
    r"\bUBTECH\b": "UBTECH",
    # === AI Model Companies (Global) ===
    r"\bAnthropic\b": "Anthropic",
    r"\bMistral\b": "Mistral",
    r"\bCohere\b": "Cohere",
    r"\bxAI\b": "xAI",
    r"\bStability\s+AI\b": "Stability AI",
    # === Chinese Tech (Big Companies) ===
    r"\bBaidu\b|\bERNIE\b|\bPaddlePaddle\b": "Baidu",
    r"\bTencent\b": "Tencent",
    r"\bAlibaba\b|DAMO Academy|\bQwen\b|\bTongyi\b": "Alibaba",
    r"\bByteDance\b|\bByteDance Seed\b|\bSeed Team\b": "ByteDance",
    r"\bHuawei\b|Noah.s Ark": "Huawei",
    r"\bXiaomi\b": "Xiaomi",
    r"\bSenseTime\b": "SenseTime",
    r"\bMegvii\b": "Megvii",
    r"\bHorizon Robotics\b": "Horizon Robotics",
    r"\bBYD\b": "BYD",
    r"\bDJI\b": "DJI",
    r"\bDeepSeek\b": "DeepSeek",
    r"\bLi Auto\b": "Li Auto",
    r"\bNIO\b": "NIO",
    r"\bXPeng\b|XMotors": "XPeng",
    r"\bKuaishou\b": "Kuaishou",
    r"\bZhipu\b|\bChatGLM\b|\bGLM-\d": "Zhipu AI",
    r"\bHikvision\b": "Hikvision",
    r"\biFlytek\b": "iFlytek",
    # === Chinese AI Model Companies ===
    r"\bMiniMax\b": "MiniMax",
    r"\bMoonshot\b|\bKimi\b": "Moonshot AI",
    r"\bBaichuan\b": "Baichuan",
    r"\b01\.AI\b|\bYi-Lightning\b|\bYi-Large\b": "01.AI",
    r"\bStepFun\b|\bStep\s*Star\b": "StepFun",
    # === Chinese Tech (Internet/Platform) ===
    r"\bMeituan\b": "Meituan",
    r"\bDiDi\b": "DiDi",
    r"\bJD\.com\b|JD\s+AI|JD Explore": "JD",
    # === Top US Universities ===
    r"\bStanford\b": "Stanford",
    r"\bMIT\b": "MIT",
    r"\bBerkeley\b": "UC Berkeley",
    r"\bCMU\b|Carnegie Mellon": "CMU",
    r"\bPrinceton\b": "Princeton",
    r"\bGeorgia Tech\b": "Georgia Tech",
    r"\bUT Austin\b|Univ.*?Texas.*?Austin": "UT Austin",
    r"\bCornell\b": "Cornell",
    r"\bColumbia\b": "Columbia",
    r"\bNYU\b|New York University": "NYU",
    r"\bUCSD\b|UC San Diego": "UCSD",
    r"\bUCLA\b": "UCLA",
    r"\bUMich\b|Univ.*?Michigan": "UMich",
    r"\bUIUC\b|Univ.*?Illinois.*?Urbana": "UIUC",
    r"\bUSC\b|Univ.*?Southern California": "USC",
    r"\bUW\b.*?(?:Seattle|Madison)|Univ.*?Washington": "UW",
    r"Purdue\b": "Purdue",
    r"Maryland\b.*?Univ|UMD\b": "UMD",
    r"Wisconsin\b": "UW-Madison",
    r"Boston\s*University": "BU",
    r"UC\s+Merced": "UC Merced",
    r"Rice\s+University": "Rice",
    r"Univ.*?Pennsylvania|\bUPenn\b": "UPenn",
    r"Penn\s+State": "Penn State",
    # === Top EU Universities & Labs ===
    r"\bOxford\b": "Oxford",
    r"\bCambridge\b": "Cambridge",
    r"\bETH\b.*?Z": "ETH Zurich",
    r"\bEPFL\b": "EPFL",
    r"\bImperial\b.*?College": "Imperial",
    r"\bTU Munich\b|\bTUM\b": "TUM",
    r"\bFreiburg\b": "Univ of Freiburg",
    r"\bMax Planck\b|\bMPI\b": "Max Planck",
    r"\bDFKI\b": "DFKI",
    r"\bINRIA\b": "INRIA",
    r"\bIIT\b.*?(?:Italian|Genova|Istituto)": "IIT",
    r"Univ.*?Trento": "Univ of Trento",
    r"Univ.*?Edinburgh": "Univ of Edinburgh",
    r"UCL\b|University College London": "UCL",
    r"KTH\b": "KTH",
    r"Sorbonne\b": "Sorbonne",
    r"\bSaclay\b": "Saclay",
    # === Chinese Universities ===
    r"\bTsinghua\b|\bTHU\b": "Tsinghua",
    r"\bPeking\b.*?Univ|\bPKU\b": "PKU",
    r"\bShanghai Jiao Tong\b|\bSJTU\b": "SJTU",
    r"\bZhejiang\b.*?Univ|\bZJU\b": "ZJU",
    r"\bFudan\b": "Fudan",
    r"\bNanjing\b.*?Univ|\bNJU\b": "Nanjing Univ",
    r"\bUSTC\b|University of Science and Technology of China": "USTC",
    r"\bHuazhong\b|\bHUST\b|Huazhong University of Science": "HUST",
    r"South China.*?Tech|\bSCUT\b": "SCUT",
    r"\bHarbin\b.*?Inst|\bHIT\b": "HIT",
    r"\bBeihang\b|\bBUAA\b": "BUAA",
    r"\bTianjin\b.*?Univ": "Tianjin Univ",
    r"\bDalian\b.*?Univ.*?Tech|\bDUT\b": "DUT",
    r"Xi.an Jiao.*?Tong|\bXJTU\b": "XJTU",
    r"Sun Yat.sen|\bSYSU\b": "SYSU",
    r"\bRenmin\b.*?Univ|\bRUC\b": "RUC",
    r"\bWuhan\b.*?Univ|\bWHU\b": "WHU",
    r"Northwest.*?Poly|\bNWPU\b": "NWPU",
    r"\bUESTC\b|Univ.*?Electronic.*?Sci": "UESTC",
    r"Beijing Jiaotong|\bBJTU\b": "BJTU",
    r"\bNUDT\b|National Univ.*?Defense": "NUDT",
    r"\bXiamen\b.*?Univ|\bXMU\b": "XMU",
    r"\bSoochow\b.*?Univ": "Soochow Univ",
    # === Chinese Labs & Institutes ===
    r"\bShanghai AI Lab\b|Shanghai AI Laboratory|\bInternLM\b|\bInternVL\b|\bOpenGVLab\b": "Shanghai AI Lab",
    r"\bCASIA\b|Inst.*?Automation": "CASIA",
    r"Chinese Academy of Sci": "CAS",
    r"Peng\s*Cheng\s*Lab|\bPCL\b": "PCL",
    r"\bShanghaiTech\b": "ShanghaiTech",
    r"\bBAAI\b|Beijing Academy": "BAAI",
    r"\bSIAT\b|Shenzhen Inst.*?Adv": "SIAT",
    r"\bAllen Institute\b|\bAI2\b|Allen\s+Institute\s+for\s+AI": "Allen AI",
    # === HK / SG / KR / JP / AU / CA ===
    r"Chinese Univ.*?Hong Kong|\bCUHK\b": "CUHK",
    r"Hong Kong Univ.*?Sci.*?Tech|\bHKUST\b": "HKUST",
    r"(?<!Chinese )(?:University of )?Hong Kong(?! Poly)(?! .*Sci)|\bHKU\b": "HKU",
    r"\bPolyU\b|Hong Kong Poly": "PolyU",
    r"\bNTU\b|Nanyang": "NTU",
    r"\bNUS\b|National Univ.*?Singapore": "NUS",
    r"\bKAIST\b": "KAIST",
    r"\bSNU\b|Seoul National": "SNU",
    r"Yonsei\b": "Yonsei Univ",
    r"Univ.*?Tokyo|Tokyo.*?Univ": "Univ of Tokyo",
    r"\bMonash\b": "Monash",
    r"\bANU\b|Australian National": "ANU",
    r"McGill\b": "McGill",
    r"Univ.*?Macau": "Univ of Macau",
    r"\bA\*STAR\b|Agency.*?Science.*?Tech": "A*STAR",
    r"Univ.*?Toronto": "Univ of Toronto",
    r"Univ.*?Alberta": "Univ of Alberta",
    r"Univ.*?Waterloo": "Univ of Waterloo",
    # === More US Universities ===
    r"Texas A.?M": "Texas A&M",
    r"Ohio State": "Ohio State",
    r"Iowa State": "Iowa State",
    r"UC Irvine|\bUCI\b": "UC Irvine",
    r"UC Davis": "UC Davis",
    r"UC Santa Barbara|\bUCSB\b": "UC Santa Barbara",
    r"Northeastern\s+Univ": "Northeastern Univ",
    r"Univ.*?Florida|\bUFL\b": "Univ of Florida",
    r"Univ.*?Virginia|\bUVA\b": "UVA",
    r"Duke\s+Univ": "Duke",
    r"Brown\s+Univ": "Brown",
    r"Univ.*?Minnesota": "Univ of Minnesota",
    r"Arizona\s+State|\bASU\b": "ASU",
    r"Rutgers": "Rutgers",
    r"Johns\s+Hopkins|\bJHU\b": "JHU",
    # === Industry ===
    r"Mercedes.Benz": "Mercedes-Benz",
    r"\bFord\b.*(?:Motor|Research)": "Ford",
    r"\bVolvo\b": "Volvo",
    r"\bBMW\b": "BMW",
    r"\bHyundai\b": "Hyundai",
    r"Foxconn": "Foxconn",
    r"Midea": "Midea",
    # === More Chinese Universities ===
    r"Southeast.*?Univ|SEU\b": "Southeast Univ",
    r"Tongji\b": "Tongji",
    r"Beijing\s+Institute\s+of\s+Tech": "BIT",
    r"South.*?Univ.*?Tech|\bSUST\b|Southern University of Science": "SUSTech",
    r"Shandong\s+Univ": "Shandong Univ",
    # === More EU ===
    r"Delft": "TU Delft",
    r"Zurich\b.*Univ|Univ.*Zurich|\bUZH\b": "Univ of Zurich",
    r"Univ.*?Bonn": "Univ of Bonn",
}

# ---------------------------------------------------------------------------
# Known researcher -> institution mapping
# ---------------------------------------------------------------------------
RESEARCHER_INST = {
    # === Stanford ===
    "Chelsea Finn": "Stanford",
    "Dorsa Sadigh": "Stanford",
    "Fei-Fei Li": "Stanford",
    "Jiajun Wu": "Stanford",
    "Marco Pavone": "Stanford",
    "Leonidas Guibas": "Stanford",
    "Shuran Song": "Stanford",
    "Karl Pertsch": "Stanford",
    "Percy Liang": "Stanford",
    # === UC Berkeley ===
    "Sergey Levine": "UC Berkeley",
    "Pieter Abbeel": "UC Berkeley",
    "Trevor Darrell": "UC Berkeley",
    "Jitendra Malik": "UC Berkeley",
    "Oier Mees": "UC Berkeley",
    "Mingyu Ding": "UC Berkeley",
    # === MIT ===
    "Kaiming He": "MIT",
    "Song Han": "MIT",
    "Yilun Du": "MIT",
    "Russ Tedrake": "MIT/TRI",
    "Pulkit Agrawal": "MIT",
    "Leslie Kaelbling": "MIT",
    "Tomas Lozano-Perez": "MIT",
    # === CMU ===
    "Deva Ramanan": "CMU",
    "Abhinav Gupta": "CMU",
    "Deepak Pathak": "CMU",
    "Katerina Fragkiadaki": "CMU",
    # === NYU ===
    "Saining Xie": "NYU",
    "Lerrel Pinto": "NYU",
    # === UCSD ===
    "Xiaolong Wang": "UCSD",
    "Hao Su": "UCSD",  # full name only, _name_match prevents 'Xinhao Sun' false positive
    # === UT Austin ===
    "Philipp Krahenbuhl": "UT Austin",
    "Yuke Zhu": "UT Austin",
    # === Google DeepMind ===
    "Ted Xiao": "Google DeepMind",
    "Brian Ichter": "Google DeepMind",
    "Pete Florence": "Google DeepMind",
    "Andy Zeng": "Google DeepMind",
    "Danny Driess": "Google DeepMind",
    "Karol Hausman": "Google DeepMind",
    # === NVIDIA ===
    "Dieter Fox": "NVIDIA/UW",
    "Ming-Yu Liu": "NVIDIA",
    "Sifei Liu": "NVIDIA",
    "Boris Ivanovic": "NVIDIA",
    "Jim Fan": "NVIDIA",
    "Linxi Fan": "NVIDIA",
    # === Meta AI ===
    "Yann LeCun": "Meta AI",
    "Aravind Rajeswaran": "Meta AI",
    # === Physical Intelligence ===
    "Quan Vuong": "Physical Intelligence",
    "Lachy Groom": "Physical Intelligence",
    # === Other ===
    "Andrea Vedaldi": "Oxford",
    "Wolfram Burgard": "Univ of Freiburg",
    "Wenqi Shao": "Shanghai AI Lab",
    "Hongyang Li": "Shanghai AI Lab",
    "Hang Zhao": "Tsinghua",
    "Hao Zhao": "Tsinghua",
    "Huazhe Xu": "Tsinghua",
    "Hao Dong": "PKU",
    "Cewu Lu": "SJTU",
    "Hesheng Wang": "SJTU",
    "Xinge Zhu": "CUHK",
    "Pheng-Ann Heng": "CUHK",
    "Yao Mu": "HKU",
    "Jingkuan Song": "UESTC",
    "Jianlong Fu": "MSRA",
    "Bei Liu": "MSRA",
    "Yaobo Liang": "MSRA",
    "Yunzhu Li": "UIUC",
    "Mike Zheng Shou": "NUS",
    "Gim Hee Lee": "NUS",
    "Lin Shao": "NUS",
    "Chen Lv": "NTU",
    "Jiangmiao Pang": "Shanghai AI Lab",
}

# Tier-1 institutions for filtering (known big labs)
TIER1_INSTITUTIONS = {
    # --- Big Tech / AI Labs ---
    "nvidia", "nvidia/uw", "nvidia/ut austin",
    "google deepmind", "google", "meta ai", "meta", "openai",
    "apple", "tesla", "amazon", "microsoft research", "msra",
    "uber", "qualcomm", "intel", "samsung", "sony", "deepseek",
    "anthropic", "mistral", "cohere", "xai", "stability ai",
    # --- Autonomous Driving ---
    "waymo", "cruise", "aurora", "nuro", "zoox", "motional", "mobileye",
    "woven by toyota", "pony.ai", "momenta", "tusimple",
    "bosch", "valeo", "continental", "waabi",
    "mercedes-benz", "ford", "volvo", "bmw", "hyundai",
    # --- Robotics Companies ---
    "physical intelligence", "boston dynamics", "tri", "mit/tri",
    "agility robotics", "figure ai", "1x technologies",
    "unitree", "covariant", "agibot", "galbot", "ubtech",
    # --- Chinese Tech ---
    "bytedance", "tencent", "alibaba", "baidu", "huawei",
    "xiaomi", "sensetime", "megvii", "horizon robotics",
    "li auto", "byd", "dji", "nio", "xpeng",
    "kuaishou", "zhipu ai",
    "minimax", "moonshot ai", "baichuan", "01.ai", "stepfun",
    "meituan", "didi", "jd",
    # --- US Top Universities ---
    "stanford", "mit", "uc berkeley", "berkeley", "cmu", "carnegie mellon",
    "princeton", "georgia tech", "ut austin", "cornell", "columbia", "nyu",
    "ucsd", "uc san diego", "ucla", "umich", "uiuc", "uw", "usc",
    # --- Europe Top ---
    "oxford", "cambridge", "eth zurich", "epfl", "imperial",
    # --- China Top Universities ---
    "tsinghua", "thu", "pku", "peking", "sjtu", "zju", "zhejiang",
    "fudan", "ustc", "hust", "scut", "buaa", "hit", "xjtu",
    "nudt", "sysu",
    # --- China Research Institutes ---
    "shanghai ai lab", "casia", "cas", "pcl", "shanghaitech",
    "baai", "allen ai",
    # --- HK ---
    "cuhk", "hku", "hkust",
    # --- Singapore ---
    "ntu", "nanyang", "nus",
}



_CACHE_DIR = Path(__file__).parent.parent / ".pdf_cache"


def _get_first_page_text(arxiv_id: str, max_retries: int = 3) -> str:
    """Get first-page text from PDF, caching the extracted text locally."""
    _CACHE_DIR.mkdir(exist_ok=True)
    safe_id = arxiv_id.replace("/", "_")
    text_cache = _CACHE_DIR / f"{safe_id}.txt"

    if text_cache.exists():
        return text_cache.read_text(encoding="utf-8")

    if not HAS_PDFPLUMBER:
        return ""

    # Check for legacy .pdf cache from previous code version
    pdf_cache = _CACHE_DIR / f"{safe_id}.pdf"
    if pdf_cache.exists():
        try:
            with pdfplumber.open(pdf_cache) as pdf:
                if not pdf.pages:
                    text_cache.write_text("", encoding="utf-8")
                    return ""
                text = pdf.pages[0].extract_text() or ""
            text_cache.write_text(text, encoding="utf-8")
            pdf_cache.unlink(missing_ok=True)
            return text
        except Exception:
            pass

    url = f"https://arxiv.org/pdf/{arxiv_id}"
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            resp = urllib.request.urlopen(req, context=SSL_CTX, timeout=30)
            pdf_bytes = resp.read()
            with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
                if not pdf.pages:
                    text_cache.write_text("", encoding="utf-8")
                    return ""
                text = pdf.pages[0].extract_text() or ""
            text_cache.write_text(text, encoding="utf-8")
            return text
        except Exception:
            if attempt < max_retries - 1:
                time.sleep(3 * (attempt + 1))
    return ""


_ABSTRACT_RE = re.compile(
    r"^\s*(?:Abstract|ABSTRACT)\s*(?:[—\-:.]\s*)?",
    re.MULTILINE,
)

_ARXIV_NOISE_RE = re.compile(
    r"^\s*(?:\d{4}\s*$|[a-zA-Z]{2,4}\s*$|\d{1,2}\s*$|\].*?\[|.*viXra)",
)


def _extract_header_and_footnotes(text: str) -> str:
    """Extract only header (title/authors/affiliations) and page-bottom
    footnotes from first-page text.

    This deliberately excludes the abstract and body paragraphs to avoid
    false institution matches from citations, related-work mentions,
    benchmark descriptions, etc.
    """
    lines = text.split("\n")

    # --- Header: authors+affiliations before "Abstract", skip title ---
    header_end = len(lines)
    for i, line in enumerate(lines):
        if _ABSTRACT_RE.match(line):
            header_end = i
            break

    # Skip title lines (typically first 1-3 lines of all-caps or mixed text
    # before author names appear). Author lines contain commas, superscript
    # digits fused with names, or email-like patterns.
    author_start = 0
    for i in range(min(header_end, 5)):
        line = lines[i].strip()
        if not line:
            continue
        has_comma = "," in line
        has_digit_name = re.search(r"\d[A-Z]", line)
        has_email = "@" in line
        has_superscript = re.search(r"[*†‡∗]", line)
        if has_comma or has_digit_name or has_email or has_superscript:
            author_start = i
            break

    header_raw = "\n".join(lines[author_start:header_end])
    # PDF superscript numbers often fuse with text: "1CASIA 2SJTU"
    header = re.sub(r"(\d)([A-Z])", r"\1 \2", header_raw)

    # --- Footer: extract only footnote-like lines from page bottom ---
    # PDF two-column layout mixes footnotes with body text, so we only
    # keep lines that look like actual footnotes (numbered affiliations,
    # "is with" / "are with" phrases, email addresses, etc.)
    _FOOTNOTE_RE = re.compile(
        r"^\d+\s*[A-Z]"       # "1Yuning Wang..." or "2Pu Zhang..."
        r"|@"                  # email addresses
        r"|\bis\s+with\b"     # "is with the University..."
        r"|\bare\s+with\b"    # "are with ..."
        r"|[Cc]orrespond"     # "Corresponding author"
        r"|[Ee]qual\s+[Cc]ontribution"
        r"|∗|†|‡"             # footnote markers
        r"|[Ww]ork\s+done\s+at"
    )
    footer_start = max(header_end, len(lines) - 20)
    footer_lines = []
    for line in lines[footer_start:]:
        stripped = line.strip()
        if _ARXIV_NOISE_RE.match(stripped):
            continue
        if _FOOTNOTE_RE.search(stripped):
            footer_lines.append(line)
    footer = "\n".join(footer_lines)

    return header + "\n" + footer


def extract_institutions_from_pdf(arxiv_id: str, max_retries: int = 3) -> str:
    """Extract institution names from header + footnotes of page 1.

    Only searches the area above "Abstract" (title / authors / affiliations)
    and the bottom footnotes.  This avoids false positives from body text
    that mentions other institutions in passing.

    First-page text is cached locally in .pdf_cache/ so repeated runs
    skip both the download and PDF parsing.
    """
    try:
        text = _get_first_page_text(arxiv_id, max_retries)
        if not text:
            return ""

        search_text = _extract_header_and_footnotes(text)

        found = []
        for pattern, inst in INST_PATTERNS.items():
            if re.search(pattern, search_text, re.IGNORECASE):
                if inst not in found:
                    found.append(inst)
        return ", ".join(found[:4]) if found else ""
    except Exception:
        return ""


def _name_match(known: str, author: str) -> bool:
    """Exact full-name match (not substring).

    Handles: 'He Wang' == 'He Wang' but NOT 'Zhe Wang'.
    Also handles minor variations like middle initials.
    """
    k = known.lower().strip()
    a = author.lower().strip()
    if k == a:
        return True
    k_parts = k.split()
    a_parts = a.split()
    if len(k_parts) >= 2 and len(a_parts) >= 2:
        if k_parts[0] == a_parts[0] and k_parts[-1] == a_parts[-1]:
            return True
    return False


def identify_institutions(authors: list, affiliations_text: str = "") -> str:
    """Identify institutions from author names and affiliation text only.

    IMPORTANT: Do NOT pass abstract text here — it contains product/model
    names (e.g. 'Unitree G1', 'pi0') that cause false matches.
    """
    found = []

    for author in authors[:8]:
        name = author.strip()
        for known, inst in RESEARCHER_INST.items():
            if _name_match(known, name):
                if inst not in found:
                    found.append(inst)

    search_text = " ".join(authors) + " " + affiliations_text
    for pattern, inst in INST_PATTERNS.items():
        if re.search(pattern, search_text, re.IGNORECASE):
            if inst not in found:
                found.append(inst)

    return ", ".join(found[:3]) if found else "—"


def is_known_institution(inst_str: str) -> bool:
    if inst_str == "—":
        return False
    parts = [s.strip().lower() for s in inst_str.split(",")]
    return any(p in TIER1_INSTITUTIONS for p in parts)
