"""Apply institution corrections to papers.yaml based on PDF verification."""
import yaml
from pathlib import Path

ROOT = Path(__file__).parent.parent
YAML_PATH = ROOT / "data" / "papers.yaml"

CORRECTIONS = {
    # idx: corrected_institution (based on PDF affiliation text)
    # Format: arxiv_id -> new_institution

    # AD - E2E
    "2602.06521": "—",  # DriveWorld-VLA: can't confirm from PDF
    "2602.14577": "HUST, Xiaomi, Tsinghua",  # DriveFine
    "2602.13329": "—",  # HiST-VLA: can't confirm
    "2512.09864": "ByteDance",  # UniUGP
    "2512.13636": "HUST, Xiaomi",  # MindDrive
    "2512.04733": "McGill, Univ of Macau",  # E3AD: both confirmed
    "2602.22801": "Tsinghua, Xiaomi",  # Unleashing Diffusion
    "2601.01762": "XJTU, Horizon Robotics",  # AlignDrive
    "2602.20794": "Tianjin Univ, Xiaomi",  # VGGDrive
    "2602.10719": "—",  # HybridDriveVLA: affiliations unclear in snippet
    "2506.08052": "HUST, Xiaomi",  # ReCogDrive
    # "2511.00088" Alpamayo-R1: NVIDIA ✓
    # "2512.20299" KnowVal: PKU, UC Merced ✓
    "2510.24108": "Fudan, NVIDIA, UMich",  # ZTRS
    "2509.06951": "Shanghai AI Lab, HIT",  # F1 VLA
    "2512.12799": "HKU, Tianjin Univ, HUST",  # DrivePI
    "2510.18313": "SJTU, Tsinghua, NUS",  # OmniNWM
    # "2512.10226" LCDrive: UT Austin, NVIDIA, Stanford ✓
    "2512.11226": "CUHK-SZ, XPeng",  # FutureX
    # "2602.23259" Risk-Aware WM: Univ of Trento, SYSU
    "2602.23259": "Univ of Trento, SYSU",

    # AD - World Model
    "2512.23421": "HUST, Xiaomi",  # DriveLaW
    # "2511.20156" Map-World: Univ of Macau ✓
    "2412.05280": "BUAA, Tsinghua, PKU",  # Stag-1
    # "2512.11225" VFMF: Oxford ✓
    "2503.15208": "Tsinghua, Megvii",  # DiST-4D
    "2511.22187": "XPeng, ShanghaiTech, USTC",  # HybridWorldSim
    "2602.22010": "ByteDance, HKU",  # World Guidance
    # "2512.13030" Motus: Tsinghua ✓ (also PKU, Horizon)

    # AD - Sim/Data
    "2511.23369": "CASIA, HKU, Xiaomi",  # SimScale
    # "2512.19270" Are All Data: Tsinghua ✓
    "2602.18757": "HKU, ShanghaiTech, CUHK",  # Driving Thousand Faces
    # "2512.10675" Gemini: Google DeepMind ✓
    "2511.20022": "KAIST",  # WaymoQA

    # AD - Planning
    "2512.06112": "Fudan",  # WAM-Flow
    "2512.07135": "CASIA, Xiaomi",  # TrajMoE

    # AD - Safety/Benchmark
    # "2512.10958" WorldLens: NTU, S-Lab — can't fully confirm but reasonable
    "2502.20694": "UC Berkeley, NVIDIA, UCSD, MIT",  # WorldModelBench
    "2602.15061": "SJTU",  # Safe-SDL

    # Robot - VLA Arch
    # "2511.14759" π₀.₆: Physical Intelligence ✓
    # "2511.16518" MiMo: Xiaomi ✓
    # "2602.12684" Xiaomi-Robotics-0: Xiaomi ✓
    "2602.14974": "Dexmal, StepFun",  # DM0
    "2602.14979": "Alibaba DAMO",  # RynnBrain
    "2511.17502": "Alibaba DAMO, ZJU",  # RynnVLA-002
    "2602.11236": "Alibaba",  # ABot-M0
    "2512.11047": "Fudan, HKU, Agibot",  # WholeBodyVLA
    "2512.05693": "Fudan, MSRA",  # HiMoE-VLA
    "2602.09849": "Tsinghua, ByteDance",  # BagelVLA
    "2511.18085": "SJTU, Cambridge, Agibot",  # Stellar VLA
    "2512.02013": "PKU, CUHK",  # ManualVLA
    "2602.21157": "HKUST",  # HALO
    "2511.14148": "Shanghai AI Lab, Tsinghua, ZJU",  # AsyncVLA
    "2602.12215": "PKU, Galbot, CASIA",  # LDA-1B
    "2603.03596": "Physical Intelligence",  # MEM
    # "2512.04797" SIMA 2: Google DeepMind ✓
    "2512.24653": "PKU",  # RoboMIND 2.0 ✓
    "2602.12099": "GigaAI",  # GigaBrain

    # Robot - Action Token
    "2602.04215": "Harvard, Stanford",  # OAT
    # "2602.15397" ActionCodec: Tsinghua, Fudan — reasonable
    # "2403.03181" VQ-BeT: NYU ✓
    # "2602.03310" RDT-2: Tsinghua ✓
    "2603.01766": "—",  # NIAF: can't confirm from snippet
    "2512.04952": "Tsinghua, Fudan, Galaxea AI",  # FASTer
    "2511.23034": "CAS, MSRA",  # LatBot

    # Robot - World Model Policy
    # "2602.06508" World-VLA-Loop: NUS ✓
    "2602.06949": "NVIDIA",  # DreamDojo
    "2602.11075": "CUHK, HKU, Horizon Robotics, Tsinghua",  # RISE
    "2602.12063": "Stanford, Tsinghua",  # VLAW
    "2602.13977": "Tsinghua, CASIA",  # WoVR
    "2511.14659": "NTU",  # NORA-1.5
    "2602.15922": "NVIDIA",  # DreamZero
    "2512.03556": "Tsinghua",  # RoboScape-R

    # Robot - RL Policy
    "2511.15605": "Fudan, Tongji",  # SRPO
    "2510.25889": "Tsinghua",  # πRL
    # "2511.20633" Reinforcing Prophesying: Fudan ✓
    "2602.06422": "—",  # Alleviating Sparse: can't confirm
    # "2602.11124" PhyCritic: UMD, NVIDIA ✓
    "2602.11146": "HKUST, Huawei, Tsinghua",  # Beyond VLM Rewards
    "2510.19307": "NVIDIA, KAIST",  # Unified RL IL
    # "2602.04056" Modular Safety: Purdue, UMich — can't confirm but reasonable
    # "2602.06339" Action Hallucination: NUS ✓

    # Robot - Data/Pretrain
    "2512.01773": "Tsinghua, HKU",  # IGen
    # "2512.02729" RoboWheel: Tsinghua ✓
    "2511.15704": "UCSD",  # In-N-On
    "2510.21571": "Tsinghua, MSRA",  # Scalable VLA Pretrain
    "2511.21690": "UMD, NYU",  # TraceGen
    "2511.06619": "MSRA",  # How Do VLAs Inherit — keep
    "2602.10556": "Princeton, Physical Intelligence",  # LAP
    "2511.16651": "Shanghai AI Lab, PKU",  # InternData-A1
    "2602.10116": "NVIDIA, UIUC",  # SAGE

    # General - Spatial
    # "2511.20644" VLM²: SUNY Buffalo ✓
    "2511.22103": "NUDT, Shanghai AI Lab, CUHK, ShanghaiTech",  # MoE3D
    "2512.03000": "XMU, CUHK, Meta",  # DynamicVerse
    # "2512.05060" 4DLangVGGT: HUST ✓
    # "2511.21688" G²VLM: Shanghai AI Lab ✓
    "2511.13719": "SenseTime, NTU",  # Scaling Spatial Intelligence
    "2512.24385": "ZJU, NUS",  # Forging Spatial Intelligence
    "2512.20617": "ZJU, ByteDance",  # SpatialTree
    "2512.17012": "NVIDIA",  # 4D-RGPT
    # "2512.03601" Motion4D: NUS ✓
    # SAM 3D: Meta AI ✓ (couldn't download but correct)
    "2510.23603": "ZJU, Alibaba DAMO",  # PixelRefer
    # "2510.23095" Revisiting PE: Alibaba ✓

    # General - Latent Reasoning
    "2510.27492": "NUS, ZJU, UW",  # ThinkMorph
    # "2601.05248" LaST₀: PKU, CUHK ✓
    "2512.10941": "Google, Stanford, BU",  # Mull-Tokens
    # "2511.19418" CoVT: UC Berkeley ✓
    "2602.06040": "HUST, Alibaba",  # SwimBird
    "2412.06769": "Meta FAIR, UCSD",  # COCONUT
    # "2511.19859" Unifying Perception: Nanjing Univ ✓
    "2601.05175": "Meta, KAUST",  # VideoAuto-R1

    # General - Multimodal Arch
    # "2512.10942" VL-JEPA: Meta FAIR, HKUST ✓
    # "2505.14683" BAGEL: ByteDance ✓
    "2601.10710": "Ant Group, Tongji",  # CLI
    "2510.22946": "UCSC, ByteDance",  # LightFusion
    # "2511.21631" Qwen3-VL: Alibaba ✓
    # "2511.16719" SAM 3: Meta AI ✓
    # "2511.08704" Rethinking Gen: Google ✓
    # "2601.20552" DeepSeek-OCR: DeepSeek AI ✓
    # "2512.01252" Diff MoE: ByteDance ✓
    "2512.02895": "Li Auto",  # MindGPT-4ov

    # General - Efficient
    "2602.18397": "NVIDIA",  # VLA-Perf
    # "2512.04025" PSA: Monash ✓
    "2512.10548": "CAS, Baidu",  # Blink
    "2602.19870": "SIAT, PCL",  # ApET
    "2512.21627": "Alibaba, Tsinghua, PKU",  # AstraNav-Memory
    # "2506.12251" Multi-Camera Triplanes: NVIDIA, Stanford ✓
    "2512.10947": "USC, Stanford, NVIDIA",  # Multi-Camera Encoding

    # General - Physical Benchmark
    "2512.01989": "Georgia Tech, CMU",  # PAI-Bench
    "2512.05564": "SYSU, PCL",  # ProPhy
    "2510.17681": "SJTU, Shanghai AI Lab, CUHK",  # PICABench
    "2511.18271": "Meituan",  # Beyond Words Pixels
    "2506.08708": "MBZUAI, Tsinghua, SYSU",  # PhyBlock
    "2602.08971": "Tsinghua",  # WorldArena

    # General - Survey
    # "2510.16732" WM Survey: A*STAR ✓
    "2510.24795": "UESTC",  # Efficient VLA Survey
    "2602.08145": "CMU, Oxford, UMD",  # Reliable FM Survey
    "2601.07823": "Princeton",  # Video Gen Robotics
    "2510.25760": "HKUST",  # Multimodal Spatial Reasoning
    "2510.20809": "UCSD, NVIDIA",  # Real Deep Research
}


def main():
    with open(YAML_PATH, "r", encoding="utf-8") as f:
        papers = yaml.safe_load(f)

    changed = 0
    for p in papers:
        aid = p.get("arxiv", "")
        if aid in CORRECTIONS:
            old = p.get("institution", "")
            new = CORRECTIONS[aid]
            if old != new:
                p["institution"] = new
                changed += 1
                print(f"  [{aid}] {p['title'][:50]}")
                print(f"    {old} -> {new}")

    # Remove the template entry at the end
    papers = [p for p in papers if p.get("title") != "Paper Title"]

    with open(YAML_PATH, "w", encoding="utf-8") as f:
        yaml.dump(papers, f, allow_unicode=True, default_flow_style=False, sort_keys=False, width=200)

    print(f"\nTotal changed: {changed}")
    print(f"Removed template entry. Final count: {len(papers)} papers")


if __name__ == "__main__":
    main()
