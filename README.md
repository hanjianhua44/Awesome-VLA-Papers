# Awesome VLA Papers

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated collection of papers on **Vision-Language-Action (VLA)** models, covering autonomous driving, robotics, world models, spatial reasoning, and more.
>
> VLA 领域论文精选列表，涵盖自动驾驶、机器人操作、世界模型、空间感知、推理链、动作表征等方向。

**收录论文: 141 篇 | 最近更新: 2026-03-09**

---

## Table of Contents

- [I. Autonomous Driving 自动驾驶](#i-autonomous-driving-自动驾驶)
  - [End-to-End VLA Architecture 端到端VLA架构](#end-to-end-vla-architecture-端到端vla架构)
  - [World Models 世界模型](#world-models-世界模型)
  - [Simulation & Data 仿真与数据](#simulation--data-仿真与数据)
  - [Planning & Control 规划与控制](#planning--control-规划与控制)
  - [Safety & Benchmarks 安全与评估](#safety--benchmarks-安全与评估)
- [II. Robotics 机器人](#ii-robotics-机器人)
  - [VLA Architecture VLA架构](#vla-architecture-vla架构)
  - [Action Tokenization 动作表征与词表](#action-tokenization-动作表征与词表)
  - [World Models & Policy Co-learning 世界模型与策略协同](#world-models--policy-co-learning-世界模型与策略协同)
  - [RL & Policy Optimization 强化学习与策略优化](#rl--policy-optimization-强化学习与策略优化)
  - [Data & Pre-training 数据与预训练](#data--pre-training-数据与预训练)
- [III. General 通用跨领域](#iii-general-通用跨领域)
  - [Spatial Perception & 3D/4D 空间感知](#spatial-perception--3d4d-空间感知)
  - [Latent Reasoning & Chain-of-Thought 潜在推理与思维链](#latent-reasoning--chain-of-thought-潜在推理与思维链)
  - [Multimodal Architecture & Pre-training 多模态基础架构](#multimodal-architecture--pre-training-多模态基础架构)
  - [Efficient Inference 高效推理与压缩](#efficient-inference-高效推理与压缩)
  - [Physical AI Benchmarks 物理AI评估](#physical-ai-benchmarks-物理ai评估)
  - [Surveys 综述](#surveys-综述)

---

## I. Autonomous Driving 自动驾驶

### End-to-End VLA Architecture 端到端VLA架构

- **DriveWorld-VLA: Unified Latent-Space World Modeling with VLA for AD** | 北京交通大学 | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.06521)
  > 在潜空间统一世界模型与VLA规划，用世界模型潜在状态作为VLA决策状态，NAVSIM SOTA

- **DriveFine: Refining-Augmented Masked Diffusion VLA** | 华南理工 | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.14577)
  > 掩码扩散VLA + 可插拔Block-MoE，生成/修正专家解耦，结合混合RL自纠错

- **HiST-VLA: Hierarchical Spatio-Temporal VLA for E2E AD** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.13329)
  > 层次化时空VLA，融合多尺度时空特征用于端到端驾驶感知预测规划

- **UniUGP: Unifying Understanding, Generation, and Planning for E2E AD** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.09864)
  > 统一场景理解、视频生成与轨迹规划，端到端多任务联合训练

- **MindDrive: VLA for AD via Online RL** | 国防科大 | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.13636)
  > 将在线RL引入自动驾驶VLA训练，提升闭环场景鲁棒性

- **E3AD: Emotion-Aware VLA for Human-Centric E2E AD** | 澳门大学, McGill | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.04733)
  > 首个情感感知自动驾驶VLA，VAD情绪模型+双路径空间推理

- **Unleashing the Potential of Diffusion Models for E2E AD** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.22801)
  > 系统性探索扩散模型在端到端自动驾驶规划中的范式

- **AlignDrive: Aligned Lateral-Longitudinal Planning for E2E AD** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2601.01762)
  > 横纵向对齐规划，解耦横向和纵向决策提升端到端规划精度

- **VGGDrive: Cross-View Geometric Grounding for AD** | 天津大学, 香港理工 | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.20794)
  > 将3D基础模型的跨视图几何特征注入VLM，层次自适应注入赋予3D感知

- **From Representational Complementarity to Dual Systems (HybridDriveVLA)** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.10719)
  > VLM与纯视觉backbone互补，快慢双系统策略，VLM仅低置信时介入，吞吐量提升3.2x

- **ReCogDrive: Reinforced Cognitive Framework for E2E AD** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2506.08052)
  > 强化认知框架，增强端到端驾驶场景理解与推理决策

- **Alpamayo-R1: Reasoning and Action Prediction for AD in the Long Tail** | NVIDIA | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.00088)
  > 面向长尾场景的推理-动作桥接方案，增强自动驾驶泛化能力

- **KnowVal: Knowledge-Augmented and Value-Guided AD System** | 北大, UC Merced | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.20299)
  > 驾驶知识图谱（交规+防御驾驶+伦理）+ 价值模型，知识增强可解释规划

- **ZTRS: Zero-Imitation E2E AD with Trajectory Scoring** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2510.24108)
  > 零模仿学习，通过轨迹评分替代传统模仿实现端到端驾驶

- **F1: A VLA Bridging Understanding and Generation to Actions** | 中科院自动化所 | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2509.06951)
  > 统一视觉理解与生成能力的VLA，克服反应式策略的局限

- **DrivePI: Spatial-aware 4D MLLM for Unified AD** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.12799)
  > 空间感知的4D多模态大模型，统一感知、预测和规划

### World Models 世界模型

- **OmniNWM: Omniscient Driving Navigation World Models** | 清华, 鹏城实验室 | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2510.18313)
  > 全景导航世界模型，联合生成RGB/语义/深度/3D占据，支持精确动作控制

- **LCDrive: Latent CoT World Modeling for E2E Driving** | UT Austin, NVIDIA, Stanford | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.10226)
  > 潜空间交替生成动作提议token和世界模型token，统一推理与决策

- **FutureX: Latent CoT World Model for E2E AD** | 哈工大深圳, CUHK-SZ | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.11226)
  > Auto-think Switch自适应启用潜在世界模型CoT rollout

- **Risk-Aware World Model Predictive Control for E2E AD** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.23259)
  > 风险感知的世界模型预测控制，提升不确定环境泛化

- **DriveLaW: Unifying Planning and Video Generation in a Latent Driving World** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.23421)
  > 潜空间统一规划与视频生成

- **Map-World: Masked Action Planning and Path-Integral World Model for AD** | 澳门大学 | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.20156)
  > 掩码动作规划+路径积分世界模型，高效处理多模态未来

- **Stag-1: Realistic 4D Driving Simulation with Video Generation** | 上海AI Lab, 港大 | arXiv 2024 | [[Paper]](https://arxiv.org/abs/2412.05280)
  > 视频生成模型构建逼真4D驾驶仿真

- **VFMF: World Modeling by Forecasting Vision Foundation Model Features** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.11225)
  > 在视觉基础模型特征空间中预测未来而非像素

- **DiST-4D: Disentangled Spatiotemporal Diffusion for 4D Driving Scene Generation** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2503.15208)
  > 解耦空间时间的扩散+度量深度，4D驾驶场景生成

- **HybridWorldSim: Scalable High-fidelity Simulator for AD** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.22187)
  > 混合式高保真自动驾驶仿真器

- **World Guidance: World Modeling in Condition Space for Action Generation** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.22010)
  > 条件空间世界建模指导动作生成

- **Motus: A Unified Latent Action World Model** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.13030)
  > 统一潜在动作世界模型，联合建模动作与环境动态

### Simulation & Data 仿真与数据

- **SimScale: Learning to Drive via Real-World Simulation at Scale** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.23369)
  > 真实数据大规模仿真框架，3D渲染+轨迹扰动覆盖安全关键状态

- **Are All Data Necessary? Efficient Data Pruning for AD Dataset** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.19270)
  > 轨迹熵最大化高效裁剪大规模自动驾驶数据集

- **Driving with A Thousand Faces: Closed-Loop Personalized E2E AD Benchmark** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.18757)
  > 首个闭环个性化端到端驾驶评估基准

- **Evaluating Gemini Robotics Policies in a Veo World Simulator** | Google DeepMind | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.10675)
  > Veo视频基础模型构建策略评估系统，覆盖OOD泛化与安全测试

- **WaymoQA: Multi-View VQA for Safety-Critical Reasoning in AD** | 延世大学 | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.20022)
  > 面向安全关键推理的多视角驾驶VQA数据集

### Planning & Control 规划与控制

- **WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.06112)
  > 并行粗到细运动规划，离散流匹配高效轨迹生成

- **TrajMoE: Scene-Adaptive Trajectory Planning with MoE and RL** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.07135)
  > 场景自适应轨迹规划，MoE+RL专家路由

### Safety & Benchmarks 安全与评估

- **WorldLens: Full-Spectrum Evaluations of Driving World Models** | NTU, S-Lab | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.10958)
  > 五维度全谱系驾驶世界模型评估（生成/重建/动作跟随/下游任务/人类偏好）

- **WorldModelBench: Judging Video Generation Models As World Models** | Berkeley, MIT, NVIDIA | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2502.20694)
  > 世界建模能力评估，67K人工标注，含物理遵循维度

- **Safe-SDL: Safety Boundaries for AI-Driven Self-Driving Labs** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.15061)
  > AI自动实验室安全框架（ODD + CBF + 事务安全协议）

---

## II. Robotics 机器人

### VLA Architecture VLA架构

- **π₀.₆: a VLA That Learns From Experience** | Physical Intelligence | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.14759)
  > PI公司VLA，通过自主经验积累提升策略

- **MiMo-Embodied: X-Embodied Foundation Model** | 小米 | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.16518)
  > 小米跨具身基础模型，支持多机器人形态统一策略

- **Xiaomi-Robotics-0: Open-Sourced VLA with Real-Time Execution** | 小米 | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.12684)
  > 小米开源VLA，强调实时推理

- **DM0: Embodied-Native VLA towards Physical AI** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.14974)
  > 具身原生VLA，面向Physical AI的端到端设计

- **RynnBrain: Open Embodied Foundation Models** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.14979)
  > 开放具身基础模型，统一多任务多模态

- **RynnVLA-002: A Unified VLA and World Model** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.17502)
  > 统一VLA与世界模型的双能力架构

- **ABot-M0: VLA Foundation Model with Action Manifold Learning** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.11236)
  > 动作流形学习构建机器人操作VLA

- **WholeBodyVLA: Unified Latent VLA for Whole-Body Loco-Manipulation** | 上海AI Lab | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.11047)
  > 全身运动操作VLA，从无标注自我中心视频学习+定制运动RL控制器

- **HiMoE-VLA: Hierarchical MoE for Generalist VLA** | 微软, 复旦 | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.05693)
  > 层次MoE处理跨具身/动作空间异构数据，逐层抽象共享知识

- **BagelVLA: Long-Horizon Manipulation via Interleaved VLA Generation** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.09849)
  > 交错式VLA生成，增强长时域操作能力

- **Stellar VLA: Continually Evolving Skill Knowledge** | 上海交大 | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.18085)
  > 知识驱动持续学习VLA，知识空间建模+专家路由实现技能进化

- **ManualVLA: CoT Manual Generation and Robotic Manipulation** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.02013)
  > 同时生成思维链操作手册和执行机器人操作

- **HALO: Unified VLA for Embodied Multimodal CoT Reasoning** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.21157)
  > VLA + 多模态CoT推理，增强长时域和OOD场景

- **AsyncVLA: Asynchronous Flow Matching for VLA** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.14148)
  > 异步流匹配，解耦视觉语言理解与动作生成频率

- **LDA-1B: Scaling Latent Dynamics Action Model** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.12215)
  > 10亿参数潜在动力学动作模型，通用具身数据摄取

- **MEM: Multi-Scale Embodied Memory for VLA** | Stanford, Google DeepMind | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2603.03596)
  > 多尺度记忆（视频短时+文本长时），支持15分钟复杂多阶段任务

- **SIMA 2: Generalist Embodied Agent for Virtual Worlds** | Google DeepMind | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.04797)
  > 通用虚拟世界具身智能体，跨游戏环境泛化

- **RoboMIND 2.0: Multimodal Bimanual Mobile Manipulation Dataset** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.24653)
  > 多模态双臂移动操作数据集

- **GigaBrain-0.5M: VLA from World Model-Based RL** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.12099)
  > 基于世界模型RL训练的VLA

### Action Tokenization 动作表征与词表

- **OAT: Ordered Action Tokenization** | MIT | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.04215)
  > 有序动作词元化，高压缩+因果有序+前缀可解码，推理时精度-速度任意权衡

- **ActionCodec: What Makes for Good Action Tokenizers** | 上海交大, 天津大学 | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.15397)
  > 从VLA优化角度建立动作词元化设计原则，SmolVLM-2.2B LIBERO 95.5%

- **VQ-BeT: Behavior Generation with Latent Actions** | NYU | arXiv 2024 | [[Paper]](https://arxiv.org/abs/2403.03181)
  > 层次化VQ增强行为Transformer，推理5x快于扩散策略

- **RDT-2: Scaling UMI Data with RVQ** | 清华 | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.03310)
  > 7B VLM + RVQ对齐语言与连续控制，首次跨具身零样本泛化

- **NIAF: Neural Implicit Action Fields** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2603.01766)
  > 动作预测重构为连续函数回归，MLLM层次频谱调制器生成无限分辨率轨迹

- **FASTer: Efficient Autoregressive VLA via Neural Action Tokenization** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.04952)
  > 神经动作词元化加速自回归VLA

- **LatBot: Distilling Universal Latent Actions for VLA** | 中科院 | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.23034)
  > 大规模操作视频蒸馏通用潜在动作表征

### World Models & Policy Co-learning 世界模型与策略协同

- **World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.06508)
  > 视频世界模型与VLA策略闭环协同学习

- **DreamDojo: Generalist Robot World Model from Human Videos** | UC San Diego | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.06949)
  > 从大规模人类视频学习通用机器人世界模型

- **RISE: Self-Improving Robot Policy with Compositional World Model** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.11075)
  > 组合式世界模型驱动机器人策略自我进化

- **VLAW: Iterative Co-Improvement of VLA Policy and World Model** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.12063)
  > VLA策略与世界模型迭代协同提升

- **WoVR: World Models as Reliable Simulators for Post-Training VLA with RL** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.13977)
  > 世界模型作为可靠模拟器用于VLA后训练RL

- **NORA-1.5: VLA with World Model and Action-based Preference Rewards** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.14659)
  > 世界模型+动作偏好奖励训练VLA

- **World Action Models are Zero-shot Policies (DreamZero)** | KAIST, Google | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.15922)
  > 世界动作模型直接作为零样本策略，无需额外训练

- **RoboScape-R: Unified Reward-Observation World Models for RL** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.03556)
  > 统一奖励-观测世界模型，面向泛化机器人RL

### RL & Policy Optimization 强化学习与策略优化

- **SRPO: Self-Referential Policy Optimization for VLA** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.15605)
  > 自参照策略优化，用自身预测做参考信号

- **πRL: Online RL Fine-tuning for Flow-based VLA** | UC Berkeley | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2510.25889)
  > 面向流匹配VLA的在线RL微调

- **Reinforcing Action Policies by Prophesying** ⭐ | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.20633)
  > 通过预言（预测未来状态）强化动作策略

- **Alleviating Sparse Rewards in Flow-Based GRPO** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.06422)
  > 建模逐步和长期采样效应，缓解流式GRPO稀疏奖励

- **PhyCritic: Multimodal Critic Models for Physical AI** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.11124)
  > 多模态物理Critic，评估动作物理合理性

- **Beyond VLM-Based Rewards: Diffusion-Native Latent Reward Modeling** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.11146)
  > 扩散原生潜在奖励建模

- **Unified RL and Imitation Learning for VLMs** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2510.19307)
  > 统一RL与模仿学习的VLM训练范式

- **Modular Safety Guardrails for FM-Enabled Robots** | Purdue, UMich | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.04056)
  > 模块化安全护栏：动作安全+决策安全+以人为中心安全

- **Action Hallucination in Generative VLA Models** | NUS | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.06339)
  > 分析VLA动作幻觉（拓扑/精度/视野障碍），提出结构性解释

### Data & Pre-training 数据与预训练

- **IGen: Scalable Data Generation from Open-World Images** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.01773)
  > 开放世界图像→逼真视觉观测+可执行动作，合成数据媲美真实

- **RoboWheel: Data Engine from Real-World Human Demonstrations** | 清华 | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.02729)
  > HOI视频→跨具身训练数据，首次量化证明HOI可监督机器人学习

- **In-N-On: Scaling Egocentric Manipulation with Wild+On-task Data** | UC San Diego | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.15704)
  > 1000+小时自我中心数据配方，训练大规模流匹配策略Human0

- **Scalable VLA Pretraining with Real-Life Human Activity Videos** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2510.21571)
  > 人类活动视频预训练VLA，扩展数据规模

- **TraceGen: World Modeling in 3D Trace Space** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.21690)
  > 3D轨迹空间建模，跨具身视频学习操作

- **How Do VLAs Effectively Inherit from VLMs?** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.06619)
  > 系统研究VLA继承VLM预训练知识的机制

- **LAP: Language-Action Pre-Training for Zero-shot Cross-Embodiment** | Princeton | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.10556)
  > 动作直接用自然语言表示，无需词元化器即可跨具身零样本迁移

- **InternData-A1: High-Fidelity Synthetic Data for Generalist Policy** | 上海AI Lab | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.16651)
  > 高保真合成数据管线，面向通用策略预训练

- **SAGE: Scalable Agentic 3D Scene Generation for Embodied AI** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.10116)
  > 智能体式3D场景生成，为具身AI提供训练环境

---

## III. General 通用跨领域

### Spatial Perception & 3D/4D 空间感知

- **VLM²: Vision-Language Memory for Spatial Reasoning** | SUNY Buffalo | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.20644)
  > 双记忆模块（工作记忆+情景记忆），视图一致3D空间推理

- **MoE3D: MoE meets Multi-Modal 3D Understanding** | 哈工大 | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.22103)
  > MoE引入多模态3D理解，专家分别处理不同模态

- **DynamicVerse: Physically-Aware Multimodal 4D World Modeling** | 厦大, Meta | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.03000)
  > 100K+视频物理尺度多模态4D标注框架

- **4DLangVGGT: 4D Language-Visual Geometry Grounded Transformer** | 华科 | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.05060)
  > 首个Transformer前馈式4D语言接地框架

- **G²VLM: Geometry Grounded VLM** | 上海AI Lab | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.21688)
  > 统一3D重建与空间推理的几何VLM

- **Scaling Spatial Intelligence with Multimodal Foundation Models** | 上海AI Lab | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.13719)
  > 规模化多模态基础模型培养空间智能

- **Forging Spatial Intelligence: Roadmap** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.24385)
  > 面向自主系统的多模态数据预训练空间智能路线图

- **SpatialTree: How Spatial Abilities Branch Out in MLLMs** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.20617)
  > 空间能力层次评估：感知→推理→交互

- **4D-RGPT: Region-level 4D Understanding** | NVIDIA | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.17012)
  > 感知蒸馏实现区域级4D时空推理

- **Motion4D: 3D-Consistent Motion and Semantics for 4D Scene Understanding** | NUS | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.03601)
  > 3D一致运动+语义，4D场景理解

- **SAM 3D: 3Dfy Anything in Images** | Meta AI | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.16624)
  > 单图像3D物体重建（几何+纹理+布局）

- **PixelRefer: Unified Spatio-Temporal Object Referring** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2510.23603)
  > 任意粒度时空对象引用框架

- **Revisiting Multimodal Positional Encoding in VLMs** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2510.23095)
  > 系统分析VLM多模态位置编码设计

### Latent Reasoning & Chain-of-Thought 潜在推理与思维链

- **ThinkMorph: Emergent Properties in Multimodal Interleaved CoT** | UW, Microsoft | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2510.27492)
  > 交错文本-图像推理链，涌现多模态智能

- **LaST₀: Latent Spatio-Temporal CoT for Robotic VLA** | 北大, 港中文 | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2601.05248)
  > 潜在时空CoT + 双系统MoT（低频推理+高频动作），实机提升13-14%

- **Mull-Tokens: Modality-Agnostic Latent Thinking** | BU, Meta, Stanford | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.10941)
  > 模态无关潜在token，自由在图像/文本空间思考

- **Chain-of-Visual-Thought: Teaching VLMs with Continuous Visual Tokens** | Stanford | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.19418)
  > 连续视觉token视觉思维链，增强密集视觉感知

- **SwimBird: Switchable Reasoning Mode in Hybrid Autoregressive MLLMs** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.06040)
  > 按需切换语言/视觉推理模式

- **COCONUT: Training LLMs to Reason in Continuous Latent Space** | Meta FAIR | arXiv 2024 | [[Paper]](https://arxiv.org/abs/2412.06769)
  > LLM连续潜空间推理，突破语言推理表征瓶颈

- **Unifying Perception and Action: Implicit Visual CoT** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.19859)
  > 混合模态管线+隐式视觉CoT统一感知与动作

- **VideoAuto-R1: Video Auto Reasoning (Thinking Once, Answering Twice)** | Meta | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2601.05175)
  > 按需推理，低置信才激活，响应长度减少3.3x

### Multimodal Architecture & Pre-training 多模态基础架构

- **VL-JEPA: Joint Embedding Predictive Architecture for Vision-language** | HKUST, Meta FAIR | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.10942)
  > JEPA范式VLM，嵌入空间预测，参数少50%性能更强

- **BAGEL: Emerging Properties in Unified Multimodal Pretraining** | 字节跳动 | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2505.14683)
  > 统一多模态理解和生成的开源基础模型

- **CLI: Dynamic Cross-Layer Injection for Deep VL Fusion** | 电子科大 | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2601.10710)
  > 动态多对多跨层注入，LLM按需访问完整视觉层次

- **LightFusion: Double Fusion for Unified Multimodal** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2510.22946)
  > 轻量双融合框架统一理解与生成

- **Qwen3-VL Technical Report** | 阿里巴巴 | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.21631)
  > Qwen系列最强VLM，原生交错多模态+agentic能力

- **SAM 3: Segment Anything with Concepts** | Meta AI | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.16719)
  > SAM第三代，概念提示驱动的统一检测分割跟踪

- **Rethinking Generative Image Pretraining: Scaling Next-Pixel Prediction** | Google | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.08704)
  > 自回归逐像素预测缩放特性研究

- **DeepSeek-OCR 2: Visual Causal Flow** | DeepSeek AI | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2601.20552)
  > 视觉因果流模型

- **Efficient Training of Diffusion MoE: A Practical Recipe** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.01252)
  > 扩散MoE高效训练配方

- **MindGPT-4ov: Enhanced MLLM via Multi-Stage Post-Training** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.02895)
  > 多阶段后训练增强多模态大模型

### Efficient Inference 高效推理与压缩

- **VLA-Perf: Demystifying VLA Inference Performance** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.18397)
  > 首个VLA推理性能分析基准工具

- **PSA: Pyramid Sparse Attention for Efficient Video** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.04025)
  > 金字塔稀疏注意力，高效视频理解/生成

- **Blink: Dynamic Visual Token Resolution** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.10548)
  > 动态视觉token分辨率

- **ApET: Approximation-Error Guided Token Compression** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.19870)
  > 近似误差引导token压缩

- **AstraNav-Memory: Contexts Compression for Long Memory** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.21627)
  > 长程记忆上下文压缩

- **Efficient Multi-Camera Tokenization with Triplanes** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2506.12251)
  > 三平面高效多相机词元化

- **Towards Efficient Multi-Camera Encoding for E2E Driving** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.10947)
  > 高效多相机编码方案

### Physical AI Benchmarks 物理AI评估

- **PAI-Bench: A Comprehensive Benchmark For Physical AI** | CMU, SHI Lab | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.01989)
  > 物理AI统一基准，2808真实案例评估感知与预测

- **ProPhy: Progressive Physical Alignment for Dynamic World Simulation** | 中山大学 | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2512.05564)
  > 渐进式物理对齐，MoE物理专家+VLM推理迁移

- **PICABench: How Far from Physically Realistic Image Editing?** | 港中文, 上海AI Lab | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2510.17681)
  > 系统评估T2I编辑物理真实性（光学/力学/状态转换）

- **Beyond Words and Pixels: Implicit World Knowledge Reasoning** | 快手 | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2511.18271)
  > T2I模型隐含世界知识与物理因果推理评估

- **PhyBlock: Physical Understanding via 3D Block Assembly** | CMU | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2506.08708)
  > 3D积木组装的渐进式物理理解基准

- **WorldArena: Unified Benchmark for Embodied World Models** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.08971)
  > 统一评估具身世界模型感知与功能效用

### Surveys 综述

- **A Comprehensive Survey on World Models for Embodied AI** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2510.16732)
- **A Survey on Efficient Vision-Language-Action Models** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2510.24795)
- **Reliable and Responsible Foundation Models: A Comprehensive Survey** | 多机构 | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2602.08145)
- **Video Generation Models in Robotics** | — | arXiv 2026 | [[Paper]](https://arxiv.org/abs/2601.07823)
- **Multimodal Spatial Reasoning in the Large Model Era: Survey** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2510.25760)
- **Real Deep Research for AI, Robotics and Beyond** | — | arXiv 2025 | [[Paper]](https://arxiv.org/abs/2510.20809)

---

## Contributing

欢迎提交 PR 补充论文。格式：

```markdown
- **Paper Title** | Institution | Venue Year | [[Paper]](link) [[Code]](link)
  > 一句话中文简介
```

## License

[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)
