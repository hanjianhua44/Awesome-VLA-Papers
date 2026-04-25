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
    r"\bNVIDIA\b|\bCosmos\b|\bNemotron\b|\bNeMo\b": "NVIDIA",
    r"\bGoogle\s+(DeepMind|Brain|Research)\b": "Google DeepMind",
    r"\bDeepMind\b|\bGemini\b|\bGemma\b|\bPaLM\b": "Google DeepMind",
    r"\bMeta\s+(FAIR|AI|Research)\b": "Meta AI",
    r"\bFAIR\b|\bLLaMA\b|\bLlama\b": "Meta AI",
    r"\bMicrosoft\s+Research": "Microsoft Research",
    r"\bMSRA\b|\bOrca\b|\bFlorence\b": "MSRA",
    r"\bOpenAI\b|\bGPT-\d|\bDALL[-\s]E\b|\bSora\b|\bWhisper\b|\bCLIP\b": "OpenAI",
    r"Apple\s+(?:Inc|Research|Machine Learning)": "Apple",
    r"\bAmazon\b|\bAlexa\s+AI\b": "Amazon",
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
    r"\bAnthropic\b|\bClaude\b": "Anthropic",
    r"\bMistral\b|\bMixtral\b": "Mistral",
    r"\bCohere\b|\bCommand[\-\s]R\b": "Cohere",
    r"\bxAI\b|\bGrok\b": "xAI",
    r"\bStability\s+AI\b|\bStable\s+Diffusion\b": "Stability AI",
    # === Chinese Tech (Big Companies) ===
    r"\bBaidu\b|\bERNIE\b|\bPaddlePaddle\b": "Baidu",
    r"\bTencent\b|\bHunyuan\b": "Tencent",
    r"\bAlibaba\b|DAMO Academy|\bQwen\b|\bTongyi\b": "Alibaba",
    r"\bByte\s*Dance\b|\bByte\s*Dance Seed\b|\bSeed Team\b|\bSeed\b": "ByteDance",
    r"\bHuawei\b|Noah.s Ark|\bPanGu\b": "Huawei",
    r"\bXiaomi\b": "Xiaomi",
    r"\bSenseTime\b|\bSenseNova\b": "SenseTime",
    r"\bMegvii\b": "Megvii",
    r"\bHorizon Robotics\b": "Horizon Robotics",
    r"\bBYD\b": "BYD",
    r"\bDJI\b": "DJI",
    r"\bDeepSeek\b": "DeepSeek",
    r"\bLi Auto\b": "Li Auto",
    r"\bNIO\b": "NIO",
    r"\bXPeng\b|XMotors": "XPeng",
    r"\bKuaishou\b|\bKwaiVGI\b|\bKling\b": "Kuaishou",
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
    r"\bGeorgia Tech\b|Georgia Inst.*?Tech": "Georgia Tech",
    r"\bUT Austin\b|Univ.*?Texas.*?Austin": "UT Austin",
    r"\bCornell\b": "Cornell",
    r"\bColumbia\b": "Columbia",
    r"\bNYU\b|New York University": "NYU",
    r"\bUCSD\b|UC San Diego": "UCSD",
    r"\bUCLA\b": "UCLA",
    r"\bUMich\b|Univ.*?Michigan": "UMich",
    r"\bUIUC\b|Univ.*?Illinois.*?Urbana|illinois\.edu": "UIUC",
    r"\bUSC\b|Univ.*?Southern California": "USC",
    r"\bUW\b.*?(?:Seattle|Madison)|Univ.*?Washington": "UW",
    r"Purdue\b": "Purdue",
    r"Maryland\b.*?Univ|Univ.*?Maryland|UMD\b": "UMD",
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
    # === Additional Missing ===
    r"Caltech|California Inst.*?Tech": "Caltech",
    r"Yale\b": "Yale",
    r"Harvard\b": "Harvard",
    r"Univ.*?Chicago": "Univ of Chicago",
    r"Northwestern\b(?!.*?Poly)": "Northwestern",
    r"King.s College London": "King's College London",
    r"Hunan\s+Univ": "Hunan Univ",
    r"Jilin\s+Univ": "Jilin Univ",
    r"Univ.*?Texas.*?Dallas": "UT Dallas",
    r"IIT\s+Delhi|Indian\s+Inst.*?Tech.*?Delhi": "IIT Delhi",
    r"IIT\s+Bombay|Indian\s+Inst.*?Tech.*?Bombay": "IIT Bombay",
    r"IIT\s+Kanpur|Indian\s+Inst.*?Tech.*?Kanpur": "IIT Kanpur",
    r"Indian\s+Inst.*?Tech": "IIT",
    r"Univ.*?British Columbia|\bUBC\b": "UBC",
    r"Univ.*?Sydney": "Univ of Sydney",
    r"Univ.*?Melbourne": "Univ of Melbourne",
    r"\bKU Leuven\b|Katholieke\b": "KU Leuven",
    r"Tsinghua.*?Shenzhen|TBSI\b": "Tsinghua Shenzhen",
    r"CityU|City Univ.*?Hong Kong": "CityU HK",
    r"Nanjing\s+Univ.*?Aero|NUAA\b": "NUAA",
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
    "google deepmind", "google", "meta ai", "meta", "meta fair", "openai",
    "apple", "tesla", "amazon", "microsoft research", "msra",
    "deepseek", "deepseek ai",
    "anthropic", "mistral", "cohere", "xai", "stability ai",
    # --- Autonomous Driving ---
    "waymo", "cruise", "aurora", "nuro", "zoox", "motional", "mobileye",
    "pony.ai", "momenta", "tusimple", "waabi",
    "bosch", "valeo", "continental",
    # --- Robotics Companies ---
    "physical intelligence", "boston dynamics", "tri", "mit/tri",
    "agility robotics", "figure ai", "1x technologies",
    "unitree", "covariant", "agibot", "galbot", "ubtech",
    # --- Chinese Tech ---
    "bytedance", "tencent", "alibaba", "alibaba damo", "ant group",
    "baidu", "huawei",
    "xiaomi", "sensetime", "megvii", "horizon robotics",
    "li auto", "byd", "dji", "nio", "xpeng",
    "kuaishou", "zhipu ai",
    "minimax", "moonshot ai", "baichuan", "01.ai", "stepfun",
    "meituan", "didi", "jd",
    # --- US Top Universities ---
    "stanford", "mit", "caltech", "harvard", "yale", "princeton",
    "uc berkeley", "berkeley", "cmu", "carnegie mellon",
    "georgia tech", "ut austin", "cornell", "columbia", "nyu",
    # --- Europe Top ---
    "oxford", "cambridge", "eth zurich", "epfl", "imperial",
    # --- China Top Universities ---
    "tsinghua", "thu", "tsinghua shenzhen",
    "pku", "peking", "sjtu", "zju", "zhejiang",
    "fudan", "ustc", "hust", "scut", "buaa", "hit", "xjtu",
    "sysu",
    # --- China Research Institutes ---
    "shanghai ai lab", "casia", "cas", "pcl", "shanghaitech",
    "baai", "siat", "allen ai",
    # --- HK ---
    "cuhk", "cuhk-sz", "hku", "hkust", "polyu",
    # --- Singapore ---
    "ntu", "nanyang", "nus", "s-lab", "a*star",
}



_CACHE_DIR = Path(__file__).parent.parent / ".pdf_cache"


def _get_first_page_text(arxiv_id: str, max_retries: int = None) -> str:
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

    if max_retries is None:
        max_retries = int(os.getenv("PDF_FETCH_RETRIES", "2"))
    timeout_s = int(os.getenv("PDF_FETCH_TIMEOUT", "12"))
    max_pdf_mb = int(os.getenv("PDF_PARSE_MAX_MB", "12"))
    url = f"https://arxiv.org/pdf/{arxiv_id}"
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            resp = urllib.request.urlopen(req, context=SSL_CTX, timeout=timeout_s)
            pdf_bytes = resp.read()
            # Extremely large PDFs can stall parsing on some hosts; skip safely.
            if len(pdf_bytes) > max_pdf_mb * 1024 * 1024:
                text_cache.write_text("", encoding="utf-8")
                return ""
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

_HEADER_STOP_RE = re.compile(
    r"^\s*(?:Abstract|ABSTRACT)\s*(?:[—\-:.]\s*)?"
    r"|^\s*Fig\.\s*\d"
    r"|^\s*Figure\s+\d"
    r"|^\s*Table\s+\d"
    r"|^\s*\(a\)\s",
)

_AFFIL_LINE_RE = re.compile(
    r"Universit|Institut|Laborator|\bLab\b|Academy|Departm"
    r"|School|College|Center|Centre|\bCorp\b|\bInc\b|\bLtd\b"
    r"|Company|\bCo\.\b|Technolog|Research|Foundation"
    r"|@|https?://"
    r"|[Cc]orrespond|\bEqual\b",
    re.IGNORECASE,
)

_ARXIV_NOISE_RE = re.compile(
    r"^\s*(?:\d{4}\s*$|[a-zA-Z]{2,4}\s*$|\d{1,2}\s*$|\].*?\[|.*viXra)",
)

_FOOTNOTE_RE = re.compile(
    r"^\d+\s*[A-Z]"
    r"|@"
    r"|\bis\s+with\b"
    r"|\bare\s+with\b"
    r"|[Cc]orrespond"
    r"|[Ee]qual\s+[Cc]ontribution"
    r"|∗|†|‡"
    r"|[Ww]ork\s+done\s+at"
)

_AFFIL_KW_RE = re.compile(
    r"Universit|Institut|Laborator|\bLab\b|Academy|Departm"
    r"|School|College|Center|Centre|\bCorp\b|\bInc\b|\bLtd\b"
    r"|Company|\bCo\.\b|Technology|Research|Foundation"
    r"|@"
    r"|[Cc]orrespond",
    re.IGNORECASE,
)


def _extract_header_and_footnotes(text: str) -> str:
    """Extract only header (title/authors/affiliations) and page-bottom
    footnotes from first-page text.

    Header extraction stops at "Abstract", "Fig.", "Figure", "Table" lines,
    and also trims after the last line that looks like an affiliation
    (contains institution keywords, emails, URLs, etc.).

    Footer extraction keeps only lines with affiliation-related content.
    """
    lines = text.split("\n")

    # --- Header: find hard stop (Abstract / Fig. / Table) ---
    header_end = len(lines)
    for i, line in enumerate(lines):
        if _HEADER_STOP_RE.match(line):
            header_end = i
            break

    # Skip title lines — author lines contain commas, superscript digits
    # fused with names, email, or footnote markers.
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

    # Trim header at last line with affiliation indicators, capped at
    # 12 lines from author_start to avoid body text leaking in papers
    # without explicit "Abstract" headers (e.g. NeurIPS/ICLR format).
    max_header = min(header_end, author_start + 12)
    affil_end = author_start + 1
    for i in range(author_start, max_header):
        line_stripped = lines[i].strip()
        if _AFFIL_LINE_RE.search(lines[i]):
            affil_end = i + 1
        # Short numbered affiliation lines (e.g. "2 NVIDIA", "3 Meta") that
        # contain only a company/lab name and no keywords. Require the line
        # to start with a digit-superscript marker and be under 40 chars to
        # avoid matching body text that happens to start with a digit.
        elif len(line_stripped) <= 40 and re.match(r"^\d+\s*[A-Z][A-Za-z&\.\s/-]{1,35}$", line_stripped):
            affil_end = i + 1

    header_raw = "\n".join(lines[author_start:affil_end])
    header = re.sub(r"(\d)([A-Z])", r"\1 \2", header_raw)

    # --- Footer: only affiliation-bearing footnote lines from page bottom ---
    # If _HEADER_STOP_RE never fired (abstract got garbled by PDF extraction),
    # header_end == len(lines) would otherwise skip the whole footer. Fall
    # back to the last 20 lines so multi-column papers with footer-only
    # affiliations still get processed.
    if header_end >= len(lines):
        footer_start = max(0, len(lines) - 20)
    else:
        footer_start = max(header_end, len(lines) - 20)
    footer_lines = []
    # We iterate with index so we can merge multi-line affiliation blocks:
    # a line matching _FOOTNOTE_RE is kept, and subsequent non-digit, non-
    # empty continuation lines (up to 2) that contain affiliation keywords
    # are appended to capture institution names wrapped across lines.
    raw_tail = lines[footer_start:]
    i = 0
    while i < len(raw_tail):
        line = raw_tail[i]
        stripped = line.strip()
        if _ARXIV_NOISE_RE.match(stripped) or not _FOOTNOTE_RE.search(stripped):
            i += 1
            continue
        # Numbered footnotes (e.g. "1Since CLIP...") must also contain
        # an affiliation keyword to avoid methodological footnotes.
        if re.match(r"^\d+\s*[A-Z]", stripped) and not _AFFIL_KW_RE.search(stripped):
            i += 1
            continue
        merged = line[:200]
        # Greedily merge up to 2 continuation lines that carry affiliation
        # content but don't start with a new footnote marker. This catches
        # affiliations wrapped across 2–3 physical lines (common in IEEE
        # footnotes and two-column layouts).
        for j in range(1, 3):
            if i + j >= len(raw_tail):
                break
            cont = raw_tail[i + j].strip()
            if not cont:
                break
            # Stop at new numbered footnote or arxiv noise.
            if re.match(r"^\d+\s*[A-Z]", cont) or _ARXIV_NOISE_RE.match(cont):
                break
            # Only absorb continuations that actually contain affiliation
            # keywords or email/URL tokens — avoid swallowing body text.
            if _AFFIL_KW_RE.search(cont):
                merged += " " + cont[:200]
            else:
                break
        footer_lines.append(merged)
        i += 1
    footer = "\n".join(footer_lines)

    return header + "\n" + footer


def _normalize_pdf_text(text: str) -> str:
    """Fix common PDF extraction artifacts: missing spaces between words.

    Many PDF extractors concatenate words (e.g. 'UniversityofMaryland').
    This inserts spaces at camelCase boundaries and around fused prepositions.
    """
    _PREPS = r"of|and|the|for|in|at|de|des|di|von|und|du"
    # Insert space between lowercase and uppercase: 'CollegeLondon' → 'College London'
    text = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
    # Split acronym from following word: 'KTHRoyal' → 'KTH Royal', 'MITPress' → 'MIT Press'
    text = re.sub(r"([A-Z]{2,})([A-Z][a-z])", r"\1 \2", text)
    # 'Universityof Technology' → 'University of Technology' (prep fused to preceding word, space after)
    text = re.sub(r"([a-zA-Z])(" + _PREPS + r")\s", r"\1 \2 ", text)
    # 'Instituteof Technology' → 'Institute of Technology' (prep fused both sides)
    text = re.sub(r"([a-zA-Z])(" + _PREPS + r")([A-Z])", r"\1 \2 \3", text)
    # 'ofMaryland' → 'of Maryland' (prep fused to following word)
    text = re.sub(r"\b(" + _PREPS + r")([A-Z])", r"\1 \2", text)
    # Fix digits fused to letters: '1University' → '1 University'
    text = re.sub(r"(\d)([A-Z][a-z])", r"\1 \2", text)
    # Fix broken emails from PDF: 'illinois.e du' → 'illinois.edu'
    text = re.sub(r"\.e\s+du\b", ".edu", text)
    # Fix common PDF word splits: 'Mc Gill' → 'McGill', 'De ep' → 'Deep'
    text = re.sub(r"\bMc\s+Gill\b", "McGill", text)
    text = re.sub(r"\bDe\s+ep\b", "Deep", text)
    return text


def extract_institutions_from_pdf(arxiv_id: str, max_retries: int = None) -> str:
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
        search_text = _normalize_pdf_text(search_text)
        search_text = search_text.replace("\n", " ")

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
