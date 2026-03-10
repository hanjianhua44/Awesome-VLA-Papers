"""Verify and fix institutions in papers.yaml by extracting from PDFs."""
import io
import re
import ssl
import time
import yaml
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    print("ERROR: pip install pdfplumber")
    exit(1)

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

ROOT = Path(__file__).parent.parent
YAML_PATH = ROOT / "data" / "papers.yaml"

import urllib.request

INST_PATTERNS = {
    r"\bNVIDIA\b": "NVIDIA",
    r"\bGoogle\b.*?(DeepMind|Brain|Research)": "Google DeepMind",
    r"\bDeepMind\b": "Google DeepMind",
    r"\bMeta\b.*?(FAIR|AI|Research)": "Meta AI",
    r"\bFAIR\b": "Meta AI",
    r"\bMicrosoft\b.*?Research": "Microsoft Research",
    r"\bMSRA\b": "MSRA",
    r"\bOpenAI\b": "OpenAI",
    r"\bApple\b": "Apple",
    r"\bAmazon\b": "Amazon",
    r"\bTesla\b": "Tesla",
    r"\bWaabi\b": "Waabi",
    r"\bWaymo\b": "Waymo",
    r"\bCruise\b": "Cruise",
    r"\bZoox\b": "Zoox",
    r"\bMobileye\b": "Mobileye",
    r"\bMomenta\b": "Momenta",
    r"\bPhysical Intelligence\b": "Physical Intelligence",
    r"\bBoston Dynamics\b": "Boston Dynamics",
    r"\bToyota Research\b|\bTRI\b": "TRI",
    r"\bAgility\b.*?Robotics": "Agility Robotics",
    r"\bFigure\s+AI\b": "Figure AI",
    r"\bUnitre+\b": "Unitree",
    r"\bAgibot\b": "Agibot",
    r"\bUBTECH\b": "UBTECH",
    r"\bBaidu\b": "Baidu",
    r"\bTencent\b": "Tencent",
    r"\bAlibaba\b|DAMO Academy": "Alibaba",
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
    r"\bXPeng\b": "XPeng",
    r"\bKuaishou\b": "Kuaishou",
    r"\bHikvision\b": "Hikvision",
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
    r"\bOxford\b": "Oxford",
    r"\bCambridge\b": "Cambridge",
    r"\bETH\b.*?Z": "ETH Zurich",
    r"\bEPFL\b": "EPFL",
    r"\bImperial\b.*?College": "Imperial",
    r"\bTU Munich\b|\bTUM\b": "TUM",
    r"\bFreiburg\b": "Univ of Freiburg",
    r"\bMax Planck\b|\bMPI\b": "Max Planck",
    r"\bTsinghua\b": "Tsinghua",
    r"\bPeking\b.*?Univ": "PKU",
    r"\bShanghai Jiao Tong\b|\bSJTU\b": "SJTU",
    r"\bZhejiang\b.*?Univ|\bZJU\b": "ZJU",
    r"\bFudan\b": "Fudan",
    r"\bNanjing\b.*?Univ|\bNJU\b": "Nanjing Univ",
    r"Univ.*?Sci.*?Tech.*?China|\bUSTC\b": "USTC",
    r"\bHuazhong\b|\bHUST\b": "HUST",
    r"South China.*?Tech|\bSCUT\b": "SCUT",
    r"\bHarbin\b.*?Inst|\bHIT\b": "HIT",
    r"\bBeihang\b|\bBUAA\b": "BUAA",
    r"\bTianjin\b.*?Univ": "Tianjin Univ",
    r"\bDalian\b.*?Univ.*?Tech|\bDUT\b": "DUT",
    r"Xi.an Jiao.*?Tong|\bXJTU\b": "XJTU",
    r"Sun Yat.sen|\bSYSU\b": "SYSU",
    r"\bWuhan\b.*?Univ|\bWHU\b": "WHU",
    r"Northwest.*?Poly|\bNWPU\b": "NWPU",
    r"\bUESTC\b|Univ.*?Electronic.*?Sci": "UESTC",
    r"Beijing Jiaotong|\bBJTU\b": "BJTU",
    r"\bNUDT\b|National Univ.*?Defense": "NUDT",
    r"\bXiamen\b.*?Univ|\bXMU\b": "XMU",
    r"\bSoochow\b.*?Univ": "Soochow Univ",
    r"\bShanghai AI Lab\b": "Shanghai AI Lab",
    r"\bCASIA\b|Inst.*?Automation": "CASIA",
    r"Chinese Academy of Sci": "CAS",
    r"Peng\s*Cheng\s*Lab|\bPCL\b": "PCL",
    r"\bShanghaiTech\b": "ShanghaiTech",
    r"\bBAAI\b|Beijing Academy": "BAAI",
    r"\bAllen Institute\b|\bAI2\b|Allen\s+Institute\s+for\s+AI": "Allen AI",
    r"Chinese Univ.*?Hong Kong|\bCUHK\b": "CUHK",
    r"Hong Kong Univ.*?Sci.*?Tech|\bHKUST\b": "HKUST",
    r"(?<!Chinese )(?:University of )?Hong Kong(?! Poly)(?! .*Sci)|\bHKU\b": "HKU",
    r"\bPolyU\b|Hong Kong Poly": "PolyU",
    r"\bNTU\b|Nanyang": "NTU",
    r"\bNUS\b|National Univ.*?Singapore": "NUS",
    r"\bKAIST\b": "KAIST",
    r"\bSNU\b|Seoul National": "SNU",
    r"Univ.*?Tokyo|Tokyo.*?Univ": "Univ of Tokyo",
    r"\bMonash\b": "Monash",
    r"\bANU\b|Australian National": "ANU",
    r"Yonsei\b": "Yonsei Univ",
    r"McGill\b": "McGill",
    r"Purdue\b": "Purdue",
    r"\bRUC\b|Renmin Univ": "RUC",
    r"Univ.*?Macau|\bUM\b": "Univ of Macau",
    r"SUNY\b|Buffalo\b.*?Univ|State Univ.*?New York": "SUNY Buffalo",
    r"\bA\*STAR\b|Agency.*?Science.*?Tech": "A*STAR",
    r"Boston\s*University": "BU",
    r"Maryland\b.*?Univ|UMD\b": "UMD",
    r"Wisconsin\b": "UW-Madison",
    r"\bRynnAI\b|\bRynn\b": "RynnAI",
    r"S-Lab|S Lab": "S-Lab",
    r"SHI Lab": "SHI Lab",
    r"GigaBrain": "GigaBrain",
}


def extract_from_pdf(arxiv_id):
    """Download and extract institutions from PDF first page."""
    if not arxiv_id:
        return "", ""
    url = f"https://arxiv.org/pdf/{arxiv_id}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        resp = urllib.request.urlopen(req, context=SSL_CTX, timeout=30)
        pdf_bytes = resp.read()
        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
            if not pdf.pages:
                return "", ""
            text = pdf.pages[0].extract_text() or ""
            header = text[:2500]
        found = []
        for pattern, inst in INST_PATTERNS.items():
            if re.search(pattern, header, re.IGNORECASE):
                if inst not in found:
                    found.append(inst)
        aff_snippet = header[:600].replace("\n", " | ")
        return ", ".join(found[:4]) if found else "", aff_snippet
    except Exception as e:
        return f"ERROR: {e}", ""


def main():
    with open(YAML_PATH, "r", encoding="utf-8") as f:
        papers = yaml.safe_load(f)

    import sys
    sys.stdout.reconfigure(encoding='utf-8')

    results = []
    for i, p in enumerate(papers):
        title = p.get("title", "")[:70]
        aid = p.get("arxiv", "")
        old_inst = p.get("institution", "")

        if not aid:
            results.append({"idx": i, "title": title, "old": old_inst, "new": "", "status": "SKIP", "aff": ""})
            print(f"[{i:3d}] SKIP (no arxiv): {title}")
            continue

        pdf_inst, aff_snippet = extract_from_pdf(aid)
        if pdf_inst.startswith("ERROR"):
            results.append({"idx": i, "title": title, "old": old_inst, "new": "", "status": "ERROR", "aff": ""})
            print(f"[{i:3d}] PDF FAIL: {title} | {pdf_inst}")
            time.sleep(2)
            continue

        if pdf_inst:
            if pdf_inst != old_inst:
                status = "MISMATCH"
                print(f"[{i:3d}] MISMATCH: {title}")
                print(f"       YAML: {old_inst}")
                print(f"       PDF:  {pdf_inst}")
            else:
                status = "OK"
                print(f"[{i:3d}] OK: {title} | {old_inst}")
        else:
            status = "NO_PDF_INST"
            print(f"[{i:3d}] NO INST FROM PDF: {title} | YAML: {old_inst}")

        results.append({"idx": i, "title": title, "old": old_inst, "new": pdf_inst, "status": status, "aff": aff_snippet})
        time.sleep(1)

    out_path = ROOT / "scripts" / "verify_output.json"
    import json
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nResults saved to {out_path}")
    print(f"Total: {len(papers)}, Mismatches: {sum(1 for r in results if r['status']=='MISMATCH')}")


if __name__ == "__main__":
    main()
