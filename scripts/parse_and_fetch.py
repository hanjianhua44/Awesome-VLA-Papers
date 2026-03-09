"""
Parse raw paper list text, extract titles + URLs, deduplicate,
and fetch metadata from arXiv API.
"""

import re
import json
import ssl
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

RAW_TEXT = r"""
Vision-Language Memory for Spatial Reasoning
https://arxiv.org/pdf/2511.20644
Evaluating Gemini Robotics Policies in a Veo World Simulator
https://arxiv.org/pdf/2512.10675
OmniNWM: Omniscient Driving Navigation World Models
https://arxiv.org/pdf/2510.18313
IGen: Scalable Data Generation for Robot Learning from Open-World Images
https://arxiv.org/pdf/2512.01773
RoboWheel: A Data Engine from Real-World Human Demonstrations for Cross-Embodiment Robotic Learning
https://arxiv.org/pdf/2512.02729
In-N-On: Scaling Egocentric Manipulation with in-the-wild and on-task Data
https://arxiv.org/abs/2511.15704
WHOLEBODYVLA: TOWARDS UNIFIED LATENT VLA FOR WHOLE-BODY LOCO-MANIPULATION CONTROL
https://arxiv.org/pdf/2512.11047
MoE3D: Mixture of Experts meets Multi-Modal 3D Understanding
https://arxiv.org/pdf/2511.22103
DynamicVerse: A Physically-Aware Multimodal Framework for 4D World Modeling
https://arxiv.org/pdf/2512.03000
4DLANGVGGT: 4D LANGUAGE-VISUAL GEOMETRY GROUNDED TRANSFORMER
https://arxiv.org/pdf/2512.05060
VGGDrive: Empowering Vision-Language Models with Cross-View Geometric Grounding for Autonomous Driving
https://arxiv.org/pdf/2602.20794v1
Continually Evolving Skill Knowledge in Vision Language Action Model
https://arxiv.org/pdf/2511.18085
HIMOE-VLA: HIERARCHICAL MIXTURE-OF-EXPERTS FOR GENERALIST VISION-LANGUAGE-ACTION POLICIES
https://arxiv.org/pdf/2512.05693
THINKMORPH: EMERGENT PROPERTIES IN MULTIMODAL INTERLEAVED CHAIN-OF-THOUGHT REASONING
https://arxiv.org/pdf/2510.27492v1
Beyond Words and Pixels: A Benchmark for Implicit World Knowledge Reasoning in Generative Models
https://arxiv.org/pdf/2511.18271
WorldModelBench: Judging Video Generation Models As World Models
https://arxiv.org/pdf/2502.20694
PICABENCH: HOW FAR ARE WE FROM PHYSICALLY REALISTIC IMAGE EDITING?
https://arxiv.org/pdf/2510.17681v1
PAI-Bench: A Comprehensive Benchmark For Physical AI
https://arxiv.org/pdf/2512.01989
ProPhy: Progressive Physical Alignment for Dynamic World Simulation
https://arxiv.org/pdf/2512.05564
WorldLens: Full-Spectrum Evaluations of Driving World Models in Real World
https://arxiv.org/pdf/2512.10958
Latent Chain-of-Thought World Modeling for End-to-End Autonomous Driving
https://arxiv.org/pdf/2512.10226
FutureX: Enhance End-to-End Autonomous Driving via Latent Chain-of-Thought World Model
https://arxiv.org/pdf/2512.11226
DriveWorld-VLA: Unified Latent-Space World Modeling with Vision-Language-Action for Autonomous Driving
https://arxiv.org/pdf/2602.06521
DriveFine: Refining-Augmented Masked Diffusion VLA for Precise and Robust Driving
https://arxiv.org/pdf/2602.14577v1
MEM: Multi-Scale Embodied Memory for Vision Language Action Models
https://arxiv.org/pdf/2603.03596
OAT: Ordered Action Tokenization
https://arxiv.org/pdf/2602.04215
ActionCodec: What Makes for Good Action Tokenizers
https://arxiv.org/pdf/2602.15397v1
RVQ for Action Tokenization
https://arxiv.org/pdf/2403.03181
RDT-2 with RVQ
https://arxiv.org/pdf/2602.03310
Neural Implicit Action Fields: From Discrete Waypoints to Continuous Functions for Vision-Language-Action Models
https://arxiv.org/pdf/2603.01766
From One-to-One to Many-to-Many: Dynamic Cross-Layer Injection for Deep Vision-Language Fusion
https://arxiv.org/pdf/2601.10710
LAP: Language-Action Pre-Training Enables Zero-shot Cross-Embodiment Transfer
https://www.arxiv.org/pdf/2602.10556
KnowVal: A Knowledge-Augmented and Value-Guided Autonomous Driving System
https://arxiv.org/pdf/2512.20299
Modular Safety Guardrails Are Necessary for Foundation-Model-Enabled Robots in the Real World
https://arxiv.org/pdf/2602.04056
Safe-SDL: Establishing Safety Boundaries and Control Mechanisms for AI-Driven Self-Driving Laboratories
https://arxiv.org/pdf/2602.15061v1
LaST0: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model
https://arxiv.org/pdf/2601.05248
VideoAuto-R1: Video Auto Reasoning via Thinking Once, Answering Twice
http://arxiv.org/pdf/2601.05175
From Representational Complementarity to Dual Systems: Synergizing VLM and Vision-Only Backbones for End-to-End Driving
https://arxiv.org/pdf/2602.10719v1
E3AD: An Emotion-Aware Vision-Language-Action Model for Human-Centric End-to-End Autonomous Driving
https://arxiv.org/pdf/2512.04733
VL-JEPA: Joint Embedding Predictive Architecture for Vision-language
https://arxiv.org/pdf/2512.10942
Null-Tokens: Modality-Agnostic Latent Thinking
https://arxiv.org/pdf/2512.10941
Action Hallucination in Generative Visual-Language-Action Models
https://arxiv.org/pdf/2602.06339
Reliable and Responsible Foundation Models: A Comprehensive Survey
https://arxiv.org/pdf/2602.08145
Driving with A Thousand Faces: A Benchmark for Closed-Loop Personalized End-to-End Autonomous Driving
https://arxiv.org/pdf/2602.18757v1
Forging Spatial Intelligence: A Roadmap of Multi-Modal Data Pre-Training for Autonomous Systems
https://arxiv.org/pdf/2512.24385
Are All Data Necessary? Efficient Data Pruning for Large-scale Autonomous Driving Dataset via Trajectory Entropy Maximization
https://arxiv.org/pdf/2512.19270
InternData-A1: Pioneering High-Fidelity Synthetic Data for Pre-training Generalist Policy
https://arxiv.org/pdf/2511.16651
Alpamayo-R1: Bridging Reasoning and Action Prediction for Generalizable Autonomous Driving in the Long Tail
https://arxiv.org/pdf/2511.00088
Risk-Aware World Model Predictive Control for Generalizable End-to-End Autonomous Driving
https://arxiv.org/pdf/2602.23259v1
World Guidance: World Modeling in Condition Space for Action Generation
https://arxiv.org/pdf/2602.22010v1
GigaBrain-0.5M: a VLA That Learns From World Model-Based Reinforcement Learning
https://arxiv.org/pdf/2602.12099v1
SAGE: Scalable Agentic 3D Scene Generation for Embodied AI
https://arxiv.org/pdf/2602.10116
WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models
https://arxiv.org/pdf/2602.08971
DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos
https://arxiv.org/pdf/2602.06949
World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy
https://arxiv.org/pdf/2602.06508
Video Generation Models in Robotics: Applications, Research Challenges, Future Directions
https://arxiv.org/pdf/2601.07823
A Comprehensive Survey on World Models for Embodied AI
https://arxiv.org/pdf/2510.16732v1
RynnVLA-002: A Unified Vision-Language-Action and World Model
https://arxiv.org/pdf/2511.17502
ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation
https://arxiv.org/pdf/2512.02013
Stag-1: Towards Realistic 4D Driving Simulation with Video Generation Model
https://arxiv.org/pdf/2412.05280
SIMA 2: A Generalist Embodied Agent for Virtual Worlds
https://arxiv.org/pdf/2512.04797
VFMF: World Modeling by Forecasting Vision Foundation Model Features
https://arxiv.org/pdf/2512.11225
DiST-4D: Disentangled Spatiotemporal Diffusion with Metric Depth for 4D Driving Scene Generation
https://arxiv.org/pdf/2503.15208
Real Deep Research for AI, Robotics and Beyond
https://arxiv.org/pdf/2510.20809v1
Scalable Vision-Language-Action Model Pretraining for Robotic Manipulation with Real-Life Human Activity Videos
https://arxiv.org/pdf/2510.21571v1
TraceGen: World Modeling in 3D Trace-Space Enables Learning from Cross-Embodiment Videos
https://arxiv.org/pdf/2511.21690
How Do VLAs Effectively Inherit from VLMs?
https://arxiv.org/pdf/2511.06619v1
LDA-1B: Scaling Latent Dynamics Action Model via Universal Embodied Data Ingestion
https://arxiv.org/pdf/2602.12215v1
PixelRefer: A Unified Framework for Spatio-Temporal Object Referring with Arbitrary Granularity
https://arxiv.org/pdf/2510.23603v1
ZTRS: ZERO-IMITATION END-TO-END AUTONOMOUS DRIVING WITH TRAJECTORY SCORING
https://arxiv.org/pdf/2510.24108v1
Unified Reinforcement and Imitation Learning for Vision-Language Models
https://arxiv.org/pdf/2510.19307v1
SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models
https://arxiv.org/pdf/2511.15605v1
NORA-1.5: A Vision-Language-Action Model Trained using World Model and Action-based Preference Rewards
https://arxiv.org/pdf/2511.14659v1
WMPO: World Model-based Policy Optimization for Vision-Language-Action Models
https://wm-po.github.io/
MindGPT-4ov: An Enhanced MLLM via a Multi-Stage Post-Training Paradigm
https://arxiv.org/pdf/2512.02895
Reinforcing Action Policies by Prophesying
https://arxiv.org/pdf/2511.20633
piRL: ONLINE RL FINE-TUNING FOR FLOW-BASED VISION-LANGUAGE-ACTION MODELS
https://arxiv.org/pdf/2510.25889
RECOGDRIVE: A REINFORCED COGNITIVE FRAMEWORK FOR END-TO-END AUTONOMOUS DRIVING
https://arxiv.org/pdf/2506.08052
RoboScape-R: Unified Reward-Observation World Models for Generalizable Robotics Training via RL
https://arxiv.org/pdf/2512.03556
Alleviating Sparse Rewards by Modeling Step-Wise and Long-Term Sampling Effects in Flow-Based GRPO
https://arxiv.org/pdf/2602.06422
PhyCritic: Multimodal Critic Models for Physical AI
https://arxiv.org/pdf/2602.11124v1
PhyBlock: A Progressive Benchmark for Physical Understanding and Planning via 3D Block Assembly
https://arxiv.org/pdf/2506.08708
Beyond VLM-Based Rewards: Diffusion-Native Latent Reward Modeling
https://arxiv.org/pdf/2602.11146v1
RISE: Self-Improving Robot Policy with Compositional World Model
https://arxiv.org/pdf/2602.11075v1
VLAW: Iterative Co-Improvement of Vision-Language-Action Policy and World Model
https://arxiv.org/pdf/2602.12063v1
WoVR: World Models as Reliable Simulators for Post-Training VLA Policies with RL
https://arxiv.org/pdf/2602.13977v1
A Survey on Efficient Vision-Language-Action Models
https://arxiv.org/pdf/2510.24795v1
LIGHTBAGEL: A LIGHT-WEIGHTED, DOUBLE FUSION FRAMEWORK FOR UNIFIED MULTIMODAL UNDERSTANDING AND GENERATION
https://arxiv.org/pdf/2510.22946v1
Efficient Multi-Camera Tokenization with Triplanes for End-to-End Driving
https://arxiv.org/pdf/2506.12251
PSA: Pyramid Sparse Attention for Efficient Video Understanding and Generation
https://arxiv.org/pdf/2512.04025
FASTER: TOWARD EFFICIENT AUTOREGRESSIVE VISION LANGUAGE ACTION MODELING VIA NEURAL ACTION TOKENIZATION
https://arxiv.org/pdf/2512.04952
TrajMoE: Scene-Adaptive Trajectory Planning with Mixture of Experts and Reinforcement Learning
https://arxiv.org/pdf/2512.07135
Blink: Dynamic Visual Token Resolution for Enhanced Multimodal Understanding
https://arxiv.org/pdf/2512.10548
Towards Efficient and Effective Multi-Camera Encoding for End-to-End Driving
https://arxiv.org/pdf/2512.10947
AstraNav-Memory: Contexts Compression for Long Memory
https://arxiv.org/pdf/2512.21627
DeepSeek-OCR 2: Visual Causal Flow
http://arxiv.org/pdf/2601.20552
ApET: Approximation-Error Guided Token Compression for Efficient VLMs
https://arxiv.org/pdf/2602.19870v1
How Fast Can I Run My VLA? Demystifying VLA Inference Performance with VLA-Perf
https://arxiv.org/pdf/2602.18397v1
BagelVLA: Enhancing Long-Horizon Manipulation via Interleaved Vision-Language-Action Generation
https://arxiv.org/pdf/2602.09849
ALIGNDRIVE: ALIGNED LATERAL-LONGITUDINAL PLANNING FOR END-TO-END AUTONOMOUS DRIVING
https://arxiv.org/pdf/2601.01762
Counterfactual VLA: Self-Reflective Vision-Language-Action Model with Adaptive Reasoning
https://arxiv.org/pdf/2512.24653
DriveLaW: Unifying Planning and Video Generation in a Latent Driving World
https://arxiv.org/pdf/2512.23421
MiMo-Embodied: X-Embodied Foundation Model Technical Report
https://arxiv.org/pdf/2511.16518
pi0.6: a VLA That Learns From Experience
https://arxiv.org/pdf/2511.14759v1
SIMSCALE: Learning to Drive via Real-World Simulation at Scale
https://arxiv.org/pdf/2511.23369
HybridWorldSim: A Scalable and Controllable High-fidelity Simulator for Autonomous Driving
https://arxiv.org/pdf/2511.22187
UniUGP: Unifying Understanding, Generation, and Planning For End-to-end Autonomous Driving
https://arxiv.org/pdf/2512.09864
MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning
https://arxiv.org/pdf/2512.13636
WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving
https://arxiv.org/pdf/2512.06112
Motus: A Unified Latent Action World Model
https://arxiv.org/pdf/2512.13030
DrivePI: Spatial-aware 4D MLLM for Unified Autonomous Driving Understanding, Perception, Prediction and Planning
https://arxiv.org/pdf/2512.12799
ABot-M0: VLA Foundation Model for Robotic Manipulation with Action Manifold Learning
https://arxiv.org/pdf/2602.11236v1
Xiaomi-Robotics-0: An Open-Sourced Vision-Language-Action Model with Real-Time Execution
https://arxiv.org/pdf/2602.12684v1
RynnBrain: Open Embodied Foundation Models
https://arxiv.org/pdf/2602.14979v1
DM0: An Embodied-Native Vision-Language-Action Model towards Physical AI
https://arxiv.org/pdf/2602.14974v1
HiST-VLA: A Hierarchical Spatio-Temporal Vision-Language-Action Model for End-to-End Autonomous Driving
https://arxiv.org/pdf/2602.13329v1
World Action Models are Zero-shot Policies
https://arxiv.org/pdf/2602.15922v1
HALO: A Unified Vision-Language-Action Model for Embodied Multimodal Chain-of-Thought Reasoning
https://arxiv.org/pdf/2602.21157v1
Unleashing the Potential of Diffusion Models for End-to-End Autonomous Driving
https://arxiv.org/pdf/2602.22801v1
A VISION-LANGUAGE-ACTION MODEL BRIDGING UNDERSTANDING AND GENERATION TO ACTIONS
https://arxiv.org/pdf/2509.06951
Emerging Properties in Unified Multimodal Pretraining
https://arxiv.org/pdf/2505.14683
AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models
https://arxiv.org/pdf/2511.14148v1
Efficient Training of Diffusion Mixture-of-Experts Models: A Practical Recipe
https://arxiv.org/pdf/2512.01252
SwimBird: Eliciting Switchable Reasoning Mode in Hybrid Autoregressive MLLMs
https://arxiv.org/pdf/2602.06040
Chain-of-Visual-Thought: Teaching VLMs to See and Think Better with Continuous Visual Tokens
https://arxiv.org/pdf/2511.19418
Qwen3-VL Technical Report
https://arxiv.org/pdf/2511.21631
SAM 3D: 3Dfy Anything in Images
https://arxiv.org/pdf/2511.16624
Rethinking generative image pretraining: How far are we from scaling up next-pixel prediction?
https://arxiv.org/pdf/2511.08704
4D-RGPT: Toward Region-level 4D Understanding via Perceptual Distillation
https://arxiv.org/pdf/2512.17012
G2VLM: Geometry Grounded Vision Language Model with Unified 3D Reconstruction and Spatial Reasoning
https://arxiv.org/pdf/2511.21688
Multimodal Spatial Reasoning in the Large Model Era: A Survey and Benchmarks
https://arxiv.org/pdf/2510.25760v1
REVISITING MULTIMODAL POSITIONAL ENCODING IN VISION-LANGUAGE MODELS
https://arxiv.org/pdf/2510.23095v1
Unifying Perception and Action: A Hybrid-Modality Pipeline with Implicit Visual Chain-of-Thought for Robotic Action Generation
https://arxiv.org/pdf/2511.19859
Scaling Spatial Intelligence with Multimodal Foundation Models
https://arxiv.org/pdf/2511.13719v1
LatBot: Distilling Universal Latent Actions for Vision-Language-Action Models
https://arxiv.org/pdf/2511.23034
Motion4D: Learning 3D-Consistent Motion and Semantics for 4D Scene Understanding
https://arxiv.org/pdf/2512.03601
SpatialTree: How Spatial Abilities Branch Out in MLLMs
https://arxiv.org/pdf/2512.20617
ColaVLA: Leveraging Cognitive Latent Reasoning for Hierarchical Parallel Trajectory Planning in Autonomous Driving
https://arxiv.org/pdf/2511.20022
Fast-ThinkAct: Efficient Vision-Language-Action Reasoning via Verbalizable Latent Planning
https://arxiv.org/pdf/2511.20156
Reasoning Palette: Modulating Reasoning via Latent Contextualization for Controllable Exploration for (V)LMs
https://arxiv.org/pdf/2412.06769
Dream-VL and Dream-VLA: Open Vision-Language and Vision-Language-Action Models with Diffusion Language Model Backbone
https://arxiv.org/pdf/2511.16719
"""

def extract_arxiv_id(url):
    """Extract arXiv ID from various URL formats."""
    if not url:
        return None
    url = url.strip()
    patterns = [
        r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5}(?:v\d+)?)',
        r'arxiv\.org/(?:abs|pdf)/([a-z\-]+/\d+)',
    ]
    for pat in patterns:
        m = re.search(pat, url)
        if m:
            raw = m.group(1)
            return re.sub(r'v\d+$', '', raw)
    return None


def parse_papers(text):
    """Parse raw text into list of {title, url, arxiv_id}."""
    lines = [l.strip() for l in text.strip().split('\n') if l.strip()]

    papers = []
    seen_ids = set()
    i = 0
    while i < len(lines):
        line = lines[i]
        # Skip lines that are just numbers or notes
        if re.match(r'^[\d\.\s]+$', line) or line.startswith('简介') or line.startswith('*:'):
            i += 1
            continue

        url = None
        title = None

        if re.match(r'https?://', line):
            url = line
            arxiv_id = extract_arxiv_id(url)
            if arxiv_id:
                title = None  # will fetch from API
            i += 1
        else:
            # Clean up title: remove leading numbers, dots, etc.
            title = re.sub(r'^[\d]+[\.\)。、\s]+\s*', '', line).strip()
            title = re.sub(r'\s*\(十分重要\)\s*', '', title)
            title = re.sub(r'\s*，\s*NVIDIA\s*$', '', title)
            title = re.sub(r'\s*\(NVIDIA\)\s*$', '', title)
            if not title or len(title) < 5:
                i += 1
                continue

            # Check if next line is a URL
            if i + 1 < len(lines) and re.match(r'https?://', lines[i + 1]):
                url = lines[i + 1].strip()
                i += 2
            else:
                i += 1

            arxiv_id = extract_arxiv_id(url) if url else None

        if arxiv_id:
            if arxiv_id in seen_ids:
                continue
            seen_ids.add(arxiv_id)
            papers.append({
                'title': title or '',
                'url': url or '',
                'arxiv_id': arxiv_id
            })
        elif title:
            papers.append({
                'title': title,
                'url': url or '',
                'arxiv_id': None
            })

    return papers


def fetch_arxiv_batch(arxiv_ids, batch_size=20):
    """Fetch metadata for a batch of arXiv IDs."""
    results = {}
    for start in range(0, len(arxiv_ids), batch_size):
        batch = arxiv_ids[start:start + batch_size]
        id_list = ','.join(batch)
        api_url = f'http://export.arxiv.org/api/query?id_list={id_list}&max_results={len(batch)}'

        print(f"  Fetching batch {start // batch_size + 1} ({len(batch)} papers)...")
        try:
            req = urllib.request.Request(api_url, headers={'User-Agent': 'VLA-Paper-Agent/1.0'})
            with urllib.request.urlopen(req, timeout=30, context=SSL_CTX) as resp:
                xml_data = resp.read().decode('utf-8')

            ns = {'atom': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}
            root = ET.fromstring(xml_data)

            for entry in root.findall('atom:entry', ns):
                eid_el = entry.find('atom:id', ns)
                if eid_el is None:
                    continue
                eid = eid_el.text.strip()
                aid = extract_arxiv_id(eid)
                if not aid:
                    continue

                title = entry.find('atom:title', ns)
                summary = entry.find('atom:summary', ns)
                published = entry.find('atom:published', ns)

                authors = []
                for author in entry.findall('atom:author', ns):
                    name = author.find('atom:name', ns)
                    if name is not None:
                        authors.append(name.text.strip())

                categories = []
                for cat in entry.findall('atom:category', ns):
                    term = cat.get('term')
                    if term:
                        categories.append(term)

                results[aid] = {
                    'title': ' '.join(title.text.strip().split()) if title is not None else '',
                    'abstract': ' '.join(summary.text.strip().split()) if summary is not None else '',
                    'authors': authors,
                    'published': published.text.strip()[:10] if published is not None else '',
                    'categories': categories,
                }
        except Exception as e:
            print(f"  Error fetching batch: {e}")

        if start + batch_size < len(arxiv_ids):
            time.sleep(3)

    return results


def main():
    print("Step 1: Parsing papers...")
    papers = parse_papers(RAW_TEXT)
    print(f"  Found {len(papers)} unique entries")

    arxiv_ids = [p['arxiv_id'] for p in papers if p['arxiv_id']]
    print(f"  {len(arxiv_ids)} have arXiv IDs")

    print("\nStep 2: Fetching arXiv metadata...")
    metadata = fetch_arxiv_batch(arxiv_ids)
    print(f"  Got metadata for {len(metadata)} papers")

    print("\nStep 3: Merging data...")
    merged = []
    for p in papers:
        aid = p['arxiv_id']
        if aid and aid in metadata:
            meta = metadata[aid]
            entry = {
                'title': meta['title'] or p['title'],
                'arxiv_id': aid,
                'url': f"https://arxiv.org/abs/{aid}",
                'authors': meta['authors'],
                'abstract': meta['abstract'],
                'date': meta['published'],
                'categories': meta['categories'],
            }
        else:
            entry = {
                'title': p['title'],
                'arxiv_id': aid,
                'url': p.get('url', ''),
                'authors': [],
                'abstract': '',
                'date': '',
                'categories': [],
            }
        merged.append(entry)

    out_path = Path(__file__).parent.parent / 'data' / 'papers_raw.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)

    print(f"\nDone! Saved {len(merged)} papers to {out_path}")

    no_abstract = [p for p in merged if not p['abstract']]
    if no_abstract:
        print(f"\nWarning: {len(no_abstract)} papers without abstracts:")
        for p in no_abstract:
            print(f"  - {p['title']}")


if __name__ == '__main__':
    main()
