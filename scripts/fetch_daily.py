"""
Fetch daily arXiv papers from cs.CV and cs.RO, filter by VLA/AD/robotics relevance.
Outputs a markdown report to daily/YYYY-MM-DD.md
"""
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

try:
    import pdfplumber
    HAS_PDFPLUMBER = True
except ImportError:
    HAS_PDFPLUMBER = False

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
# Known institution patterns (author name / affiliation hints)
# ---------------------------------------------------------------------------
INST_PATTERNS = {
    # === Big Tech (US/Global) ===
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
    r"\bUber\b": "Uber",
    r"\bQualcomm\b": "Qualcomm",
    r"\bIntel\b.*(?:Lab|Research)": "Intel",
    r"\bSamsung\b": "Samsung",
    r"\bSony\b": "Sony",
    # === Autonomous Driving Companies ===
    r"\bWaabi\b": "Waabi",
    r"\bWaymo\b": "Waymo",
    r"\bCruise\b": "Cruise",
    r"\bAurora\b.*(?:Innovation|Driv)": "Aurora",
    r"\bNuro\b": "Nuro",
    r"\bZoox\b": "Zoox",
    r"\bMotional\b": "Motional",
    r"\bMobileye\b": "Mobileye",
    r"\bWoven\b.*Planet|Woven\b.*Toyota": "Woven by Toyota",
    r"\bPony\.?ai\b": "Pony.ai",
    r"\bMomenta\b": "Momenta",
    r"\bTuSimple\b": "TuSimple",
    r"\bBosch\b": "Bosch",
    r"\bValeo\b": "Valeo",
    r"\bContinental\b": "Continental",
    # === Robotics Companies ===
    r"\bPhysical Intelligence\b|\bpi0\b|\\u03C0.*Intelligence": "Physical Intelligence",
    r"\bBoston Dynamics\b": "Boston Dynamics",
    r"\bToyota\b.*Research|\bTRI\b": "TRI",
    r"\bAgility\b.*Robotics": "Agility Robotics",
    r"\bFigure\b.*AI|Figure\b.*Robot": "Figure AI",
    r"\b1X\b.*Technolog": "1X Technologies",
    r"\bUnitre+\b": "Unitree",
    r"\bCovariant\b": "Covariant",
    r"\bAgibot\b": "Agibot",
    r"\bGalbot\b": "Galbot",
    r"\bUBTECH\b": "UBTECH",
    # === Chinese Tech ===
    r"\bBaidu\b": "Baidu",
    r"\bTencent\b": "Tencent",
    r"\bAlibaba\b|DAMO\s*Academy": "Alibaba",
    r"\bByteDance\b": "ByteDance",
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
    r"\bZhipu\b|GLM": "Zhipu AI",
    r"\bHikvision\b": "Hikvision",
    r"\biFlytek\b": "iFlytek",
    # === Top US Universities ===
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
    r"\bUIUC\b|Univ.*Illinois.*Urbana": "UIUC",
    r"\bUSC\b|Univ.*Southern.*California": "USC",
    r"\bUW\b.*(?:Seattle|Madison)|Univ.*Washington": "UW",
    # === Top EU Universities & Labs ===
    r"\bOxford\b": "Oxford",
    r"\bCambridge\b": "Cambridge",
    r"\bETH\b.*Z": "ETH Zurich",
    r"\bEPFL\b": "EPFL",
    r"\bImperial\b.*College": "Imperial",
    r"\bTU Munich\b|\bTUM\b": "TUM",
    r"\bFreiburg\b": "Univ of Freiburg",
    r"\bMax Planck\b|\bMPI\b": "Max Planck",
    r"\bDFKI\b": "DFKI",
    r"\bINRIA\b": "INRIA",
    r"\bIIT\b.*(?:Italian|Genova|Istituto)": "IIT",
    # === Chinese Universities ===
    r"\bTsinghua\b|\bTHU\b": "Tsinghua",
    r"\bPeking\b.*Univ|\bPKU\b": "PKU",
    r"\bShanghai Jiao Tong\b|\bSJTU\b": "SJTU",
    r"\bZhejiang\b.*Univ|\bZJU\b": "ZJU",
    r"\bFudan\b": "Fudan",
    r"\bNanjing\b.*Univ|\bNJU\b": "Nanjing Univ",
    r"\bUni.*Sci.*Tech.*China\b|\bUSTC\b": "USTC",
    r"\bHuazhong\b|\bHUST\b": "HUST",
    r"\bSouth China\b.*Tech|\bSCUT\b": "SCUT",
    r"\bHarbin\b.*Inst|\bHIT\b": "HIT",
    r"\bBeihang\b|\bBUAA\b": "BUAA",
    r"\bTianjin\b.*Univ": "Tianjin Univ",
    r"\bDalian\b.*Univ.*Tech|\bDUT\b": "DUT",
    r"\bXi.an Jiao.*Tong|\bXJTU\b": "XJTU",
    r"\bSun Yat-sen\b|\bSYSU\b": "SYSU",
    r"\bRenmin\b|\bRUC\b": "RUC",
    r"\bWuhan\b.*Univ|\bWHU\b": "WHU",
    r"\bNorthwest.*Poly|\bNWPU\b": "NWPU",
    r"\bUESTC\b|Univ.*Electronic.*Sci.*Tech": "UESTC",
    r"\bBJTU\b|Beijing Jiaotong": "BJTU",
    r"\bNUDT\b|National Univ.*Defense": "NUDT",
    r"\bXiamen\b.*Univ|\bXMU\b": "XMU",
    r"\bSoochow\b.*Univ": "Soochow Univ",
    # === Chinese Labs & Institutes ===
    r"\bShanghai AI Lab\b": "Shanghai AI Lab",
    r"\bCASIA\b|Inst.*Automation.*CAS": "CASIA",
    r"\bCAS\b|Chinese Academy of Sci": "CAS",
    r"\bPCL\b|Peng\s*Cheng\s*Lab": "PCL",
    r"\bShanghaiTech\b": "ShanghaiTech",
    r"\bBAAI\b|Beijing Academy": "BAAI",
    r"\bQi\s*Zhi\b": "Qi Zhi Institute",
    r"\bAllen\s*(?:AI|Institute)|AI2\b": "Allen AI",
    # === HK / SG / KR / JP / AU ===
    r"\bChinese Univ.*Hong Kong\b|\bCUHK\b": "CUHK",
    r"\bHong Kong Univ\b|\bHKU\b": "HKU",
    r"\bPolyU\b|Hong Kong Poly": "PolyU",
    r"\bHKUST\b|Hong Kong.*Sci.*Tech": "HKUST",
    r"\bNTU\b|Nanyang\b": "NTU",
    r"\bNUS\b|National.*Univ.*Singapore": "NUS",
    r"\bKAIST\b": "KAIST",
    r"\bSNU\b|Seoul National": "SNU",
    r"\bTokyo\b.*Univ|Univ.*Tokyo": "Univ of Tokyo",
    r"\bMonash\b": "Monash",
    r"\bANU\b|Australian National": "ANU",
}

RESEARCHER_INST = {
    # === Stanford (VLA/Robotics) ===
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
    "Hao Su": "UCSD",
    # === UT Austin ===
    "Philipp Krahenbuhl": "UT Austin",
    "Yuke Zhu": "UT Austin",
    # === Google DeepMind / Brain ===
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
    "Yuke Zhu": "NVIDIA/UT Austin",
    "Linxi Fan": "NVIDIA",
    # === Meta AI ===
    "Yann LeCun": "Meta AI",
    "Aravind Rajeswaran": "Meta AI",
    # === Physical Intelligence ===
    "Quan Vuong": "Physical Intelligence",
    # === Other US/EU ===
    "Andrea Vedaldi": "Oxford",
    "Wolfram Burgard": "Univ of Freiburg",
    # === Chinese Researchers ===
    "Wenqi Shao": "Shanghai AI Lab",
    "Hongyang Li": "Shanghai AI Lab",
    "Hang Zhao": "Tsinghua",
    "Hao Zhao": "Tsinghua",
    "Huazhe Xu": "Tsinghua",
    "He Wang": "PKU",
    "Hao Dong": "PKU",
    "Li Zhang": "Fudan",
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
    # === NUS/NTU ===
    "Mike Zheng Shou": "NUS",
    "Gim Hee Lee": "NUS",
    "Lin Shao": "NUS",
}


def extract_institutions_from_pdf(arxiv_id: str) -> str:
    """Download PDF first page and extract institution names."""
    if not HAS_PDFPLUMBER:
        return ""
    url = f"https://arxiv.org/pdf/{arxiv_id}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        resp = urllib.request.urlopen(req, context=SSL_CTX, timeout=30)
        pdf_bytes = resp.read()
        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
            if not pdf.pages:
                return ""
            text = pdf.pages[0].extract_text() or ""
            header = text[:2500]

        # Phase 1: match known institution patterns
        found = []
        for pattern, inst in INST_PATTERNS.items():
            if re.search(pattern, header, re.IGNORECASE):
                if inst not in found:
                    found.append(inst)
        if found:
            return ", ".join(found[:3])

        # Phase 2: broader heuristic — extract any university/institute/lab name
        broad_patterns = [
            r"([A-Z][\w\s]{2,35}University)",
            r"(University\s+of\s+[A-Z][\w\s]{2,25})",
            r"([A-Z][\w\s]{2,30}Institute\s+of\s+Technology)",
            r"([A-Z][\w\s]{2,30}Research\s+(?:Lab|Center|Institute))",
        ]
        for bp in broad_patterns:
            m = re.search(bp, header)
            if m:
                name = re.sub(r"[\d\n\r]+", " ", m.group(1)).strip()
                name = re.sub(r"\s+", " ", name)
                # Reject garbage patterns
                reject = ["Department", "Science and", "the University",
                          "USA University", "This University"]
                if (len(name) > 8 and name[0].isupper()
                        and not any(r in name for r in reject)):
                    return name

        return ""
    except Exception:
        return ""


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
    # Big tech (US/Global)
    "nvidia", "nvidia/uw", "nvidia/ut austin",
    "google deepmind", "google", "meta ai", "meta", "openai",
    "apple", "tesla", "amazon", "microsoft research", "msra",
    "uber", "qualcomm", "intel", "samsung", "sony", "deepseek",
    # Autonomous driving companies
    "waymo", "cruise", "aurora", "nuro", "zoox", "motional", "mobileye",
    "woven by toyota", "pony.ai", "momenta", "tusimple",
    "bosch", "valeo", "continental", "waabi",
    # Robotics companies
    "physical intelligence", "boston dynamics", "tri", "mit/tri",
    "agility robotics", "figure ai", "1x technologies",
    "unitree", "covariant", "agibot", "galbot", "ubtech",
    # Chinese tech
    "bytedance", "tencent", "alibaba", "baidu", "huawei",
    "xiaomi", "sensetime", "megvii", "horizon robotics",
    "li auto", "byd", "dji", "nio", "xpeng",
    "kuaishou", "zhipu ai", "hikvision", "iflytek",
    # Top US universities
    "stanford", "mit", "uc berkeley", "berkeley", "cmu", "carnegie mellon",
    "princeton", "georgia tech", "ut austin", "cornell", "columbia", "nyu",
    "ucsd", "uc san diego", "ucla", "umich", "uiuc", "uw", "usc",
    # Top EU universities & labs
    "oxford", "cambridge", "eth zurich", "epfl", "imperial",
    "tum", "univ of freiburg", "max planck", "dfki", "inria", "iit",
    # Top CN universities
    "tsinghua", "thu", "pku", "peking", "sjtu", "zju", "zhejiang",
    "fudan", "ustc", "hust", "scut", "buaa", "hit", "xjtu",
    "nudt", "sysu", "whu", "uestc", "bjtu", "ruc", "nanjing univ",
    # CN labs & institutes
    "shanghai ai lab", "casia", "cas", "pcl", "shanghaitech",
    "baai", "qi zhi institute", "allen ai",
    # HK / SG / KR / JP / AU
    "cuhk", "hku", "hkust", "polyu",
    "ntu", "nanyang", "nus",
    "kaist", "snu", "seoul national",
    "univ of tokyo", "monash", "anu",
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
        # cs.CV can have 150-200/day, weekends accumulate; fetch up to 800
        max_fetch = 800 if cat == "cs.CV" else 400
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
            print(f"    Got {len(batch)} entries, {new_count} new")
            if new_count == 0:
                break
            time.sleep(5)

    # arXiv listing schedule:
    #   Mon listing = Thu~Sun submissions (4 days)
    #   Tue listing = Mon submissions (1 day)
    #   Wed listing = Tue submissions (1 day)
    #   Thu listing = Wed submissions (1 day)
    #   Fri listing = Thu submissions (1 day)
    weekday = dt.weekday()  # 0=Mon
    if weekday == 0:
        lookback = 4  # Mon: covers Thu-Sun
    elif weekday == 1:
        lookback = 2  # Tue: covers Mon (+ buffer)
    else:
        lookback = 2  # Wed-Fri: covers previous day (+ buffer)

    target_dates = set()
    for i in range(lookback):
        target_dates.add((dt - timedelta(days=i)).strftime("%Y-%m-%d"))
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
            p["score"] += 3

        # Keep if: known institution with some relevance, OR strong keyword relevance
        # Target: ~20-30% pass rate
        if known and score >= 2:
            results.append(p)
        elif score >= 5:
            results.append(p)

    results.sort(key=lambda p: p["score"], reverse=True)

    # Phase 2: enrich institutions via PDF for papers missing them
    if HAS_PDFPLUMBER:
        no_inst = [p for p in results if p["institution"] == "\u2014"]
        if no_inst:
            print(f"  Enriching institutions from PDF for {len(no_inst)} papers...")
            for i, p in enumerate(no_inst):
                pdf_inst = extract_institutions_from_pdf(p["arxiv_id"])
                if pdf_inst:
                    p["institution"] = pdf_inst
                    if is_known_institution(pdf_inst):
                        p["score"] += 3
                if (i + 1) % 10 == 0:
                    print(f"    Processed {i+1}/{len(no_inst)}...")
                time.sleep(1)
            enriched = sum(1 for p in no_inst if p["institution"] != "\u2014")
            print(f"    PDF enrichment: {enriched}/{len(no_inst)} institutions found")

    return results, len(date_filtered)


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
        cat = categorize_paper(p["topics"], p["categories"], p.get("title", ""), p.get("abstract", ""))
        by_cat.setdefault(cat, []).append(p)

    cat_order = ["VLA", "Autonomous Driving", "Robotics", "Agent", "World Models",
                 "RL & Policy Optimization", "Spatial & Perception",
                 "Efficient & Architecture", "Related"]
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
