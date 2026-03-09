# VLA 领域论文整理分析报告

> 共收录 **141 篇**论文 | 生成日期: 2026-03-09
>
> 分类: 自动驾驶 / 机器人 / 通用跨领域，涵盖 VLA 架构、世界模型、动作表征、推理链、空间感知、数据、RL、高效推理、安全评估、Survey 等方向

---

## 目录

- [I. 自动驾驶 (Autonomous Driving)](#i-自动驾驶-autonomous-driving)
  - [A1. 端到端 VLA 架构](#a1-端到端-vla-架构)
  - [A2. 世界模型](#a2-世界模型)
  - [A3. 快慢系统与推理链](#a3-快慢系统与推理链)
  - [A4. 仿真与数据](#a4-仿真与数据)
  - [A5. 规划与控制](#a5-规划与控制)
  - [A6. 安全与评估基准](#a6-安全与评估基准)
- [II. 机器人 (Robotics)](#ii-机器人-robotics)
  - [B1. VLA 整体架构](#b1-vla-整体架构)
  - [B2. 动作表征与词表](#b2-动作表征与词表)
  - [B3. 世界模型与策略协同](#b3-世界模型与策略协同)
  - [B4. 强化学习与策略优化](#b4-强化学习与策略优化)
  - [B5. 数据与预训练](#b5-数据与预训练)
- [III. 通用/跨领域 (General)](#iii-通用跨领域-general)
  - [C1. 空间感知与 3D/4D 理解](#c1-空间感知与-3d4d-理解)
  - [C2. 潜在推理与思维链](#c2-潜在推理与思维链)
  - [C3. 多模态基础架构与预训练](#c3-多模态基础架构与预训练)
  - [C4. 高效推理与压缩](#c4-高效推理与压缩)
  - [C5. Survey 综述](#c5-survey-综述)
  - [C6. 物理 AI 评估基准](#c6-物理-ai-评估基准)

---

## I. 自动驾驶 (Autonomous Driving)

### A1. 端到端 VLA 架构

| # | 论文 | 机构 | 会议/来源 | 简介 |
|---|------|------|-----------|------|
| 1 | **DriveWorld-VLA: Unified Latent-Space World Modeling with VLA for AD** | 北京交通大学, 华南理工 | arXiv 2602.06521 [[链接]](https://arxiv.org/abs/2602.06521) | 在潜空间统一世界模型与 VLA 规划，用世界模型潜在状态作为 VLA 的决策状态，避免像素级 rollout，NAVSIM SOTA |
| 2 | **DriveFine: Refining-Augmented Masked Diffusion VLA** | 华南理工, 大连理工 | arXiv 2602.14577 [[链接]](https://arxiv.org/abs/2602.14577) | 提出掩码扩散 VLA + 可插拔 Block-MoE，将生成专家和修正专家解耦，结合混合 RL 策略实现自纠错 |
| 3 | **E3AD: Emotion-Aware VLA for Human-Centric E2E AD** | 澳门大学, 港中文, McGill | arXiv 2512.04733 [[链接]](https://arxiv.org/abs/2512.04733) | 首个情感感知的自动驾驶 VLA，引入 VAD 情绪模型和双路径空间推理，实现以人为中心的规划 |
| 4 | **HiST-VLA: Hierarchical Spatio-Temporal VLA for E2E AD** | 未公开 | arXiv 2602.13329 [[链接]](https://arxiv.org/abs/2602.13329) | 层次化时空 VLA 架构，融合多尺度时空特征用于端到端驾驶的感知、预测与规划 |
| 5 | **MindDrive: VLA for AD via Online RL** | 国防科大, 中山大学 | arXiv 2512.13636 [[链接]](https://arxiv.org/abs/2512.13636) | 将在线强化学习引入自动驾驶 VLA 训练，替代纯模仿学习，提升策略在闭环场景中的鲁棒性 |
| 6 | **UniUGP: Unifying Understanding, Generation, and Planning for E2E AD** | 未公开 | arXiv 2512.09864 [[链接]](https://arxiv.org/abs/2512.09864) | 统一场景理解、视频生成与轨迹规划三大任务，端到端多任务联合训练 |
| 7 | **Unleashing the Potential of Diffusion Models for E2E AD** | 未公开 | arXiv 2602.22801 [[链接]](https://arxiv.org/abs/2602.22801) | 系统性探索扩散模型在自动驾驶端到端规划中的应用范式和训练策略 |
| 8 | **AlignDrive: Aligned Lateral-Longitudinal Planning for E2E AD** | 未公开 | arXiv 2601.01762 [[链接]](https://arxiv.org/abs/2601.01762) | 横纵向对齐规划，解耦横向和纵向决策以提升端到端规划精度 |
| 9 | **VGGDrive: Cross-View Geometric Grounding for AD** | 天津大学, 香港理工 | arXiv 2602.20794 [[链接]](https://arxiv.org/abs/2602.20794) | 将成熟 3D 基础模型的跨视图几何特征注入 VLM，通过层次自适应注入赋予 VLM 3D 感知能力 |
| 10 | **ReCogDrive: Reinforced Cognitive Framework for E2E AD** | 未公开 | arXiv 2506.08052 [[链接]](https://arxiv.org/abs/2506.08052) | 强化认知框架，增强端到端驾驶系统的场景认知理解与推理决策能力 |
| 11 | **From Representational Complementarity to Dual Systems (HybridDriveVLA)** | 未公开 | arXiv 2602.10719 [[链接]](https://arxiv.org/abs/2602.10719) | 发现 VLM 与纯视觉 backbone 具有互补行为特性，提出快慢双系统策略，VLM 仅在低置信时介入 |
| 12 | **Alpamayo-R1: Reasoning and Action Prediction for AD in the Long Tail** | NVIDIA | arXiv 2511.00088 [[链接]](https://arxiv.org/abs/2511.00088) | NVIDIA 提出面向长尾场景的推理-动作桥接方案，增强自动驾驶泛化能力 |
| 13 | **KnowVal: Knowledge-Augmented and Value-Guided AD System** | 北大, UC Merced | arXiv 2512.20299 [[链接]](https://arxiv.org/abs/2512.20299) | 构建驾驶知识图谱（交规+防御性驾驶+伦理），通过价值模型实现知识增强的可解释规划 |
| 14 | **ZTRS: Zero-Imitation E2E AD with Trajectory Scoring** | 未公开 | arXiv 2510.24108 [[链接]](https://arxiv.org/abs/2510.24108) | 零模仿学习范式，通过轨迹评分替代传统模仿，实现端到端自动驾驶 |
| 15 | **F1: A VLA Bridging Understanding and Generation to Actions** | 中科院自动化所 | arXiv 2509.06951 [[链接]](https://arxiv.org/abs/2509.06951) | 统一视觉理解与生成能力的 VLA 模型，克服反应式策略的局限 |
| 16 | **ColaVLA: Cognitive Latent Reasoning for Hierarchical Trajectory Planning in AD** | 未公开 | arXiv (用户提供) | 认知潜在推理驱动的层次化并行轨迹规划，面向自动驾驶 |
| 17 | **DrivePI: Spatial-aware 4D MLLM for Unified AD** | 未公开 | arXiv 2512.12799 [[链接]](https://arxiv.org/abs/2512.12799) | 空间感知的 4D 多模态大模型，统一自动驾驶的理解、感知、预测和规划 |

### A2. 世界模型

| # | 论文 | 机构 | 会议/来源 | 简介 |
|---|------|------|-----------|------|
| 1 | **OmniNWM: Omniscient Driving Navigation World Models** | 清华, 鹏城实验室 | arXiv 2510.18313 [[链接]](https://arxiv.org/abs/2510.18313) | 全景导航世界模型，联合生成 RGB/语义/深度/3D 占据，支持精确动作控制与基于占据的奖励 |
| 2 | **Latent CoT World Modeling for E2E Driving (LCDrive)** | UT Austin, NVIDIA, Stanford | arXiv 2512.10226 [[链接]](https://arxiv.org/abs/2512.10226) | 在动作对齐的潜空间中交替生成动作提议 token 和世界模型 token，统一推理与决策 |
| 3 | **FutureX: Latent CoT World Model for E2E AD** | 哈工大深圳, CUHK-SZ | arXiv 2512.11226 [[链接]](https://arxiv.org/abs/2512.11226) | 自动判断是否需要推理（Auto-think Switch），仅在复杂场景启用潜在世界模型 CoT rollout |
| 4 | **Risk-Aware World Model Predictive Control for E2E AD** | 未公开 | arXiv 2602.23259 [[链接]](https://arxiv.org/abs/2602.23259) | 风险感知的世界模型预测控制，提升端到端驾驶在不确定环境下的泛化能力 |
| 5 | **DriveLaW: Unifying Planning and Video Generation in a Latent Driving World** | 未公开 | arXiv 2512.23421 [[链接]](https://arxiv.org/abs/2512.23421) | 在潜在空间统一规划与视频生成，构建紧耦合的驾驶世界模型 |
| 6 | **Map-World: Masked Action Planning and Path-Integral World Model for AD** | 澳门大学 | arXiv 2511.20156 [[链接]](https://arxiv.org/abs/2511.20156) | 掩码动作规划 + 路径积分世界模型，高效处理多模态未来不确定性 |
| 7 | **Stag-1: Towards Realistic 4D Driving Simulation with Video Generation** | 上海AI Lab, 港大 | arXiv 2412.05280 [[链接]](https://arxiv.org/abs/2412.05280) | 利用视频生成模型构建逼真的 4D 驾驶仿真场景 |
| 8 | **VFMF: World Modeling by Forecasting Vision Foundation Model Features** | 未公开 | arXiv 2512.11225 [[链接]](https://arxiv.org/abs/2512.11225) | 在视觉基础模型的特征空间中进行世界建模，预测未来特征而非像素 |
| 9 | **DiST-4D: Disentangled Spatiotemporal Diffusion for 4D Driving Scene Generation** | 未公开 | arXiv 2503.15208 [[链接]](https://arxiv.org/abs/2503.15208) | 解耦空间与时间维度的扩散模型，用度量深度实现 4D 驾驶场景生成 |
| 10 | **HybridWorldSim: Scalable High-fidelity Simulator for AD** | 未公开 | arXiv 2511.22187 [[链接]](https://arxiv.org/abs/2511.22187) | 混合式高保真自动驾驶仿真器，兼顾可控性与可扩展性 |
| 11 | **World Guidance: World Modeling in Condition Space for Action Generation** | 未公开 | arXiv 2602.22010 [[链接]](https://arxiv.org/abs/2602.22010) | 在条件空间中进行世界建模，以世界模型预测结果指导动作生成 |
| 12 | **Motus: A Unified Latent Action World Model** | 未公开 | arXiv 2512.13030 [[链接]](https://arxiv.org/abs/2512.13030) | 统一的潜在动作世界模型，在潜空间中联合建模动作与环境动态 |

### A3. 快慢系统与推理链

| # | 论文 | 机构 | 会议/来源 | 简介 |
|---|------|------|-----------|------|
| 1 | **HybridDriveVLA (Dual Systems)** | — | arXiv 2602.10719 [[链接]](https://arxiv.org/abs/2602.10719) | （见 A1-11）ViT 默认运行 + VLM 仅低置信介入的快慢双系统策略 |
| 2 | **LCDrive (Latent CoT)** | — | arXiv 2512.10226 [[链接]](https://arxiv.org/abs/2512.10226) | （见 A2-2）潜在语言推理替代自然语言 CoT，推理更快更紧凑 |
| 3 | **FutureX (Auto-think Switch)** | — | arXiv 2512.11226 [[链接]](https://arxiv.org/abs/2512.11226) | （见 A2-3）自适应 Thinking/Instant 模式切换 |

### A4. 仿真与数据

| # | 论文 | 机构 | 会议/来源 | 简介 |
|---|------|------|-----------|------|
| 1 | **SimScale: Learning to Drive via Real-World Simulation at Scale** | 未公开 | arXiv 2511.23369 [[链接]](https://arxiv.org/abs/2511.23369) | 基于真实数据的大规模仿真框架，通过 3D 渲染与轨迹扰动覆盖更多安全关键状态 |
| 2 | **Are All Data Necessary? Efficient Data Pruning for AD Dataset** | 未公开 | arXiv 2512.19270 [[链接]](https://arxiv.org/abs/2512.19270) | 通过轨迹熵最大化高效裁剪大规模自动驾驶数据集 |
| 3 | **Driving with A Thousand Faces: Closed-Loop Personalized E2E AD Benchmark** | 未公开 | arXiv 2602.18757 [[链接]](https://arxiv.org/abs/2602.18757) | 首个闭环个性化端到端驾驶评估基准 |
| 4 | **Evaluating Gemini Robotics Policies in a Veo World Simulator** | Google DeepMind | arXiv 2512.10675 [[链接]](https://arxiv.org/abs/2512.10675) | 用 Veo 视频基础模型构建机器人策略评估系统，覆盖 OOD 泛化和安全性测试 |
| 5 | **WaymoQA: Multi-View VQA for Safety-Critical Reasoning in AD** | 延世大学 | arXiv 2511.20022 [[链接]](https://arxiv.org/abs/2511.20022) | 面向安全关键推理的多视角驾驶场景 VQA 数据集 |

### A5. 规划与控制

| # | 论文 | 机构 | 会议/来源 | 简介 |
|---|------|------|-----------|------|
| 1 | **WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching** | 未公开 | arXiv 2512.06112 [[链接]](https://arxiv.org/abs/2512.06112) | 并行粗到细运动规划，利用离散流匹配实现高效自动驾驶轨迹生成 |
| 2 | **TrajMoE: Scene-Adaptive Trajectory Planning with MoE and RL** | 未公开 | arXiv 2512.07135 [[链接]](https://arxiv.org/abs/2512.07135) | 场景自适应轨迹规划，用 MoE 和强化学习实现不同场景的专家路由 |

### A6. 安全与评估基准

| # | 论文 | 机构 | 会议/来源 | 简介 |
|---|------|------|-----------|------|
| 1 | **WorldLens: Full-Spectrum Evaluations of Driving World Models** | NTU, S-Lab | arXiv 2512.10958 [[链接]](https://arxiv.org/abs/2512.10958) | 全谱系驾驶世界模型评估基准，覆盖生成、重建、动作跟随、下游任务与人类偏好五个维度 |
| 2 | **WorldModelBench: Judging Video Generation Models As World Models** | Berkeley, MIT, NVIDIA | arXiv 2502.20694 [[链接]](https://arxiv.org/abs/2502.20694) | 评估视频生成模型的世界建模能力，包含指令跟随和物理遵循维度，67K 人工标注 |
| 3 | **Safe-SDL: Safety Boundaries for AI-Driven Self-Driving Labs** | 未公开 | arXiv 2602.15061 [[链接]](https://arxiv.org/abs/2602.15061) | 为 AI 驱动的自动实验室建立安全边界和控制机制（ODD + CBF + 事务安全协议） |

---

## II. 机器人 (Robotics)

### B1. VLA 整体架构

| # | 论文 | 机构 | 会议/来源 | 简介 |
|---|------|------|-----------|------|
| 1 | **pi0.6: a VLA That Learns From Experience** | Physical Intelligence | arXiv 2511.14759 [[链接]](https://arxiv.org/abs/2511.14759) | PI 公司 VLA 系列，通过自主经验积累提升策略，支持 few-shot 泛化 |
| 2 | **MiMo-Embodied: X-Embodied Foundation Model Technical Report** | 小米 | arXiv 2511.16518 [[链接]](https://arxiv.org/abs/2511.16518) | 小米跨具身基础模型技术报告，支持多机器人形态的统一策略 |
| 3 | **Xiaomi-Robotics-0: Open-Sourced VLA with Real-Time Execution** | 小米 | arXiv 2602.12684 [[链接]](https://arxiv.org/abs/2602.12684) | 小米开源 VLA 模型，强调实时推理执行能力 |
| 4 | **DM0: Embodied-Native VLA towards Physical AI** | 未公开 | arXiv 2602.14974 [[链接]](https://arxiv.org/abs/2602.14974) | 具身原生的 VLA 模型，面向物理 AI 的端到端架构设计 |
| 5 | **RynnBrain: Open Embodied Foundation Models** | 未公开 | arXiv 2602.14979 [[链接]](https://arxiv.org/abs/2602.14979) | 开放的具身基础模型，统一多任务多模态的机器人策略 |
| 6 | **RynnVLA-002: A Unified VLA and World Model** | 未公开 | arXiv 2511.17502 [[链接]](https://arxiv.org/abs/2511.17502) | 统一 VLA 与世界模型的双能力架构 |
| 7 | **ABot-M0: VLA Foundation Model with Action Manifold Learning** | 未公开 | arXiv 2602.11236 [[链接]](https://arxiv.org/abs/2602.11236) | 通过动作流形学习构建机器人操作 VLA 基础模型 |
| 8 | **WholeBodyVLA: Unified Latent VLA for Whole-Body Loco-Manipulation** | 上海AI Lab | arXiv 2512.11047 [[链接]](https://arxiv.org/abs/2512.11047) | 全身运动操作 VLA，支持从无动作标注的自我中心视频学习，含定制的运动 RL 控制器 |
| 9 | **HiMoE-VLA: Hierarchical MoE for Generalist VLA Policies** | 微软, 复旦 | arXiv 2512.05693 [[链接]](https://arxiv.org/abs/2512.05693) | 层次 MoE 架构处理跨具身/动作空间的异构机器人数据，逐层抽象为共享知识表征 |
| 10 | **BagelVLA: Long-Horizon Manipulation via Interleaved VLA Generation** | 未公开 | arXiv 2602.09849 [[链接]](https://arxiv.org/abs/2602.09849) | 交错式视觉-语言-动作生成，增强长时域操作任务能力 |
| 11 | **Stellar VLA: Continually Evolving Skill Knowledge in VLA** | 上海交大 | arXiv 2511.18085 [[链接]](https://arxiv.org/abs/2511.18085) | 知识驱动的持续学习 VLA 框架，通过知识空间建模和专家路由实现技能不断进化 |
| 12 | **ManualVLA: CoT Manual Generation and Robotic Manipulation** | 未公开 | arXiv 2512.02013 [[链接]](https://arxiv.org/abs/2512.02013) | 统一 VLA，同时生成思维链操作手册和执行机器人操作 |
| 13 | **HALO: Unified VLA for Embodied Multimodal CoT Reasoning** | 未公开 | arXiv 2602.21157 [[链接]](https://arxiv.org/abs/2602.21157) | 统一的 VLA + 多模态 CoT 推理，增强长时域和 OOD 场景的操作能力 |
| 14 | **AsyncVLA: Asynchronous Flow Matching for VLA Models** | 未公开 | arXiv 2511.14148 [[链接]](https://arxiv.org/abs/2511.14148) | 异步流匹配 VLA，解耦视觉-语言理解与动作生成的频率 |
| 15 | **LDA-1B: Scaling Latent Dynamics Action Model** | 未公开 | arXiv 2602.12215 [[链接]](https://arxiv.org/abs/2602.12215) | 10 亿参数的潜在动力学动作模型，通过通用具身数据摄取实现规模化 |
| 16 | **MEM: Multi-Scale Embodied Memory for VLA Models** | Stanford, Google DeepMind | arXiv 2603.03596 [[链接]](https://arxiv.org/abs/2603.03596) | 多尺度记忆（视频短时 + 文本长时），支持长达 15 分钟的复杂多阶段操作任务 |
| 17 | **SIMA 2: A Generalist Embodied Agent for Virtual Worlds** | Google DeepMind | arXiv 2512.04797 [[链接]](https://arxiv.org/abs/2512.04797) | DeepMind 通用虚拟世界具身智能体，跨游戏环境泛化 |
| 18 | **Counterfactual VLA / RoboMIND 2.0** | 未公开 | arXiv 2512.24653 [[链接]](https://arxiv.org/abs/2512.24653) | 多模态双臂移动操作数据集，面向通用机器人策略训练 |
| 19 | **GigaBrain-0.5M: VLA from World Model-Based RL** | 未公开 | arXiv 2602.12099 [[链接]](https://arxiv.org/abs/2602.12099) | 基于世界模型强化学习训练的 VLA 模型 |

### B2. 动作表征与词表

| # | 论文 | 机构 | 会议/来源 | 简介 |
|---|------|------|-----------|------|
| 1 | **OAT: Ordered Action Tokenization** | MIT | arXiv 2602.04215 [[链接]](https://arxiv.org/abs/2602.04215) | 有序动作词元化：高压缩 + 因果有序 + 前缀可解码，支持推理时精度-速度任意权衡 |
| 2 | **ActionCodec: What Makes for Good Action Tokenizers** | 上海交大, 天津大学 | arXiv 2602.15397 [[链接]](https://arxiv.org/abs/2602.15397) | 从 VLA 优化角度建立动作词元化设计原则（时间重叠、词表精简、多模态互信息、token 独立性） |
| 3 | **VQ-BeT: Behavior Generation with Latent Actions** | NYU | arXiv 2403.03181 [[链接]](https://arxiv.org/abs/2403.03181) | 用层次化向量量化增强行为 Transformer，处理多模态连续动作，推理速度 5 倍于扩散策略 |
| 4 | **RDT-2: Scaling UMI Data with RVQ** | 清华 | arXiv 2602.03310 [[链接]](https://arxiv.org/abs/2602.03310) | 7B VLM 基础的机器人基础模型，用 RVQ 对齐语言与连续控制，首次实现跨具身零样本泛化 |
| 5 | **NIAF: Neural Implicit Action Fields** | 未公开 | arXiv 2603.01766 [[链接]](https://arxiv.org/abs/2603.01766) | 将动作预测从离散路径点重构为连续函数回归，用 MLLM 作层次频谱调制器生成无限分辨率轨迹 |
| 6 | **FASTer: Efficient Autoregressive VLA via Neural Action Tokenization** | 未公开 | arXiv 2512.04952 [[链接]](https://arxiv.org/abs/2512.04952) | 神经动作词元化加速自回归 VLA，大幅压缩动作序列长度 |
| 7 | **LatBot: Distilling Universal Latent Actions for VLA** | 中科院 | arXiv 2511.23034 [[链接]](https://arxiv.org/abs/2511.23034) | 从大规模操作视频中蒸馏通用潜在动作表征，具身无关的可迁移动作空间 |

### B3. 世界模型与策略协同

| # | 论文 | 机构 | 会议/来源 | 简介 |
|---|------|------|-----------|------|
| 1 | **World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy** | 未公开 | arXiv 2602.06508 [[链接]](https://arxiv.org/abs/2602.06508) | 视频世界模型与 VLA 策略的闭环协同学习 |
| 2 | **DreamDojo: Generalist Robot World Model from Large-Scale Human Videos** | UC San Diego | arXiv 2602.06949 [[链接]](https://arxiv.org/abs/2602.06949) | 从大规模人类视频学习通用机器人世界模型 |
| 3 | **RISE: Self-Improving Robot Policy with Compositional World Model** | 未公开 | arXiv 2602.11075 [[链接]](https://arxiv.org/abs/2602.11075) | 组合式世界模型驱动的机器人策略自我进化 |
| 4 | **VLAW: Iterative Co-Improvement of VLA Policy and World Model** | 未公开 | arXiv 2602.12063 [[链接]](https://arxiv.org/abs/2602.12063) | VLA 策略与世界模型的迭代协同提升 |
| 5 | **WoVR: World Models as Reliable Simulators for Post-Training VLA with RL** | 未公开 | arXiv 2602.13977 [[链接]](https://arxiv.org/abs/2602.13977) | 将世界模型作为可靠模拟器，用于 VLA 后训练的强化学习 |
| 6 | **NORA-1.5: VLA Trained using World Model and Action-based Preference Rewards** | 未公开 | arXiv 2511.14659 [[链接]](https://arxiv.org/abs/2511.14659) | 结合世界模型与动作偏好奖励训练的 VLA 模型 |
| 7 | **World Action Models are Zero-shot Policies (DreamZero)** | KAIST, Google | arXiv 2602.15922 [[链接]](https://arxiv.org/abs/2602.15922) | 世界动作模型直接作为零样本策略使用，无需额外策略训练 |
| 8 | **RoboScape-R: Unified Reward-Observation World Models for RL** | 未公开 | arXiv 2512.03556 [[链接]](https://arxiv.org/abs/2512.03556) | 统一奖励-观测世界模型，面向泛化的机器人 RL 训练 |
| 9 | **Motus: A Unified Latent Action World Model** | 未公开 | arXiv 2512.13030 [[链接]](https://arxiv.org/abs/2512.13030) | （跨领域）统一的潜在动作世界模型，联合建模动作与环境动态 |

### B4. 强化学习与策略优化

| # | 论文 | 机构 | 会议/来源 | 简介 |
|---|------|------|-----------|------|
| 1 | **SRPO: Self-Referential Policy Optimization for VLA** | 未公开 | arXiv 2511.15605 [[链接]](https://arxiv.org/abs/2511.15605) | 自参照策略优化，VLA 用自身预测做参考信号进行策略改进 |
| 2 | **piRL: Online RL Fine-tuning for Flow-based VLA** | UC Berkeley | arXiv 2510.25889 [[链接]](https://arxiv.org/abs/2510.25889) | 面向流匹配 VLA 的在线 RL 微调方法 |
| 3 | **Reinforcing Action Policies by Prophesying** | 未公开 | arXiv 2511.20633 [[链接]](https://arxiv.org/abs/2511.20633) | 通过预言（预测未来状态）来强化动作策略，重要工作 |
| 4 | **Alleviating Sparse Rewards in Flow-Based GRPO** | 未公开 | arXiv 2602.06422 [[链接]](https://arxiv.org/abs/2602.06422) | 解决流式 GRPO 中稀疏奖励问题，建模逐步和长期采样效应 |
| 5 | **PhyCritic: Multimodal Critic Models for Physical AI** | 未公开 | arXiv 2602.11124 [[链接]](https://arxiv.org/abs/2602.11124) | 多模态物理 Critic 模型，评估动作的物理合理性 |
| 6 | **Beyond VLM-Based Rewards: Diffusion-Native Latent Reward Modeling** | 未公开 | arXiv 2602.11146 [[链接]](https://arxiv.org/abs/2602.11146) | 扩散原生的潜在奖励建模，替代基于 VLM 的奖励函数 |
| 7 | **Unified RL and Imitation Learning for VLMs** | 未公开 | arXiv 2510.19307 [[链接]](https://arxiv.org/abs/2510.19307) | 统一强化学习与模仿学习的 VLM 训练范式 |
| 8 | **Modular Safety Guardrails for FM-Enabled Robots** | Purdue, UMich | arXiv 2602.04056 [[链接]](https://arxiv.org/abs/2602.04056) | 模块化安全护栏架构，覆盖动作安全、决策安全和以人为中心的安全三个维度 |
| 9 | **Action Hallucination in Generative VLA Models** | NUS | arXiv 2602.06339 [[链接]](https://arxiv.org/abs/2602.06339) | 分析生成式 VLA 中的动作幻觉问题（拓扑/精度/视野障碍），提出结构性解释 |

### B5. 数据与预训练

| # | 论文 | 机构 | 会议/来源 | 简介 |
|---|------|------|-----------|------|
| 1 | **IGen: Scalable Data Generation for Robot Learning from Open-World Images** | 未公开 | arXiv 2512.01773 [[链接]](https://arxiv.org/abs/2512.01773) | 从开放世界图像生成逼真的视觉观测和可执行动作，纯合成数据媲美真实数据训练效果 |
| 2 | **RoboWheel: Data Engine from Real-World Human Demonstrations** | 清华 | arXiv 2512.02729 [[链接]](https://arxiv.org/abs/2512.02729) | 将人手-物体交互视频转化为跨具身机器人训练数据，首次量化证明 HOI 数据可有效监督机器人学习 |
| 3 | **In-N-On: Scaling Egocentric Manipulation with Wild+On-task Data** | UC San Diego | arXiv 2511.15704 [[链接]](https://arxiv.org/abs/2511.15704) | 提出 1000+ 小时自我中心数据的收集与使用配方，训练大规模流匹配策略 Human0 |
| 4 | **Scalable VLA Pretraining with Real-Life Human Activity Videos** | 未公开 | arXiv 2510.21571 [[链接]](https://arxiv.org/abs/2510.21571) | 利用真实人类活动视频预训练 VLA 模型，扩展机器人操作的数据规模 |
| 5 | **TraceGen: World Modeling in 3D Trace Space** | 未公开 | arXiv 2511.21690 [[链接]](https://arxiv.org/abs/2511.21690) | 在 3D 轨迹空间中建模，从跨具身视频中学习操作策略 |
| 6 | **How Do VLAs Effectively Inherit from VLMs?** | 未公开 | arXiv 2511.06619 [[链接]](https://arxiv.org/abs/2511.06619) | 系统研究 VLA 如何有效继承 VLM 的预训练知识 |
| 7 | **LAP: Language-Action Pre-Training for Zero-shot Cross-Embodiment Transfer** | Princeton | arXiv 2602.10556 [[链接]](https://arxiv.org/abs/2602.10556) | 将动作直接表示为自然语言，无需学习词元化器即可实现跨具身零样本迁移 |
| 8 | **InternData-A1: High-Fidelity Synthetic Data for Pre-training Generalist Policy** | 上海AI Lab | arXiv 2511.16651 [[链接]](https://arxiv.org/abs/2511.16651) | 高保真合成数据生成管线，面向通用策略预训练 |
| 9 | **SAGE: Scalable Agentic 3D Scene Generation for Embodied AI** | 未公开 | arXiv 2602.10116 [[链接]](https://arxiv.org/abs/2602.10116) | 可扩展的智能体式 3D 场景生成，为具身 AI 提供训练环境 |

---

## III. 通用/跨领域 (General)

### C1. 空间感知与 3D/4D 理解

| # | 论文 | 机构 | 会议/来源 | 简介 |
|---|------|------|-----------|------|
| 1 | **VLM²: Vision-Language Memory for Spatial Reasoning** | SUNY Buffalo | arXiv 2511.20644 [[链接]](https://arxiv.org/abs/2511.20644) | 双记忆模块（工作记忆+情景记忆）实现视图一致的 3D 感知空间推理 |
| 2 | **MoE3D: MoE meets Multi-Modal 3D Understanding** | 哈工大, 上科大 | arXiv 2511.22103 [[链接]](https://arxiv.org/abs/2511.22103) | 将 MoE 引入多模态 3D 理解，专家网络分别处理不同模态 |
| 3 | **DynamicVerse: Physically-Aware Multimodal 4D World Modeling** | 厦大, Meta | arXiv 2512.03000 [[链接]](https://arxiv.org/abs/2512.03000) | 100K+ 视频规模的物理尺度多模态 4D 标注框架（几何/运动/语义/描述） |
| 4 | **4DLangVGGT: 4D Language-Visual Geometry Grounded Transformer** | 华科 | arXiv 2512.05060 [[链接]](https://arxiv.org/abs/2512.05060) | 首个 Transformer 前馈式 4D 语言接地框架，联合几何感知与语言对齐 |
| 5 | **G²VLM: Geometry Grounded VLM with Unified 3D Reconstruction and Spatial Reasoning** | 上海AI Lab | arXiv 2511.21688 [[链接]](https://arxiv.org/abs/2511.21688) | 赋予 VLM 几何视觉基础，统一 3D 重建与空间推理 |
| 6 | **Scaling Spatial Intelligence with Multimodal Foundation Models** | 上海AI Lab | arXiv 2511.13719 [[链接]](https://arxiv.org/abs/2511.13719) | 探索规模化多模态基础模型以培养空间智能 |
| 7 | **Forging Spatial Intelligence: Roadmap of Multi-Modal Pre-Training for Autonomous Systems** | 未公开 | arXiv 2512.24385 [[链接]](https://arxiv.org/abs/2512.24385) | 面向自主系统的多模态数据预训练空间智能路线图 |
| 8 | **SpatialTree: How Spatial Abilities Branch Out in MLLMs** | 未公开 | arXiv 2512.20617 [[链接]](https://arxiv.org/abs/2512.20617) | 空间能力层次化评估：从感知→推理→交互，揭示 MLLM 空间发展路径 |
| 9 | **4D-RGPT: Region-level 4D Understanding via Perceptual Distillation** | NVIDIA | arXiv 2512.17012 [[链接]](https://arxiv.org/abs/2512.17012) | NVIDIA 提出区域级 4D 理解，通过感知蒸馏增强时空推理 |
| 10 | **Motion4D: Learning 3D-Consistent Motion and Semantics for 4D Scene Understanding** | NUS | arXiv 2512.03601 [[链接]](https://arxiv.org/abs/2512.03601) | 学习 3D 一致的运动和语义用于 4D 场景理解 |
| 11 | **SAM 3D: 3Dfy Anything in Images** | Meta AI | arXiv 2511.16624 [[链接]](https://arxiv.org/abs/2511.16624) | Meta 的单图像 3D 物体重建生成模型（几何+纹理+布局） |
| 12 | **PixelRefer: Unified Spatio-Temporal Object Referring** | 未公开 | arXiv 2510.23603 [[链接]](https://arxiv.org/abs/2510.23603) | 统一框架实现任意粒度的时空对象引用 |
| 13 | **Multimodal Spatial Reasoning Survey** | 未公开 | arXiv 2510.25760 [[链接]](https://arxiv.org/abs/2510.25760) | 大模型时代的多模态空间推理综述与基准 |
| 14 | **Revisiting Multimodal Positional Encoding in VLMs** | 未公开 | arXiv 2510.23095 [[链接]](https://arxiv.org/abs/2510.23095) | 系统分析 VLM 中多模态位置编码的设计选择 |

### C2. 潜在推理与思维链

| # | 论文 | 机构 | 会议/来源 | 简介 |
|---|------|------|-----------|------|
| 1 | **ThinkMorph: Emergent Properties in Multimodal Interleaved CoT Reasoning** | UW, Microsoft | arXiv 2510.27492 [[链接]](https://arxiv.org/abs/2510.27492) | 交错文本-图像推理链，展现涌现的多模态智能（未见视觉操作技能、自适应推理模式） |
| 2 | **LaST₀: Latent Spatio-Temporal CoT for Robotic VLA** | 北大, 港中文 | arXiv 2601.05248 [[链接]](https://arxiv.org/abs/2601.05248) | 潜在时空 CoT + 双系统 MoT 架构（低频推理+高频动作），实机 10 任务提升 13-14% |
| 3 | **Mull-Tokens: Modality-Agnostic Latent Thinking** | BU, Meta, Stanford | arXiv 2512.10941 [[链接]](https://arxiv.org/abs/2512.10941) | 模态无关的潜在 token，让模型自由地在图像和文本空间中思考 |
| 4 | **Chain-of-Visual-Thought: Teaching VLMs with Continuous Visual Tokens** | Stanford | arXiv 2511.19418 [[链接]](https://arxiv.org/abs/2511.19418) | 连续视觉 token 形成的视觉思维链，增强 VLM 的密集视觉感知推理 |
| 5 | **SwimBird: Switchable Reasoning Mode in Hybrid Autoregressive MLLMs** | 未公开 | arXiv 2602.06040 [[链接]](https://arxiv.org/abs/2602.06040) | 混合自回归 MLLM 中可切换的推理模式，按需激活语言或视觉推理 |
| 6 | **COCONUT: Training LLMs to Reason in Continuous Latent Space** | Meta FAIR | arXiv 2412.06769 [[链接]](https://arxiv.org/abs/2412.06769) | 训练 LLM 在连续潜空间中推理，突破语言推理的表征瓶颈 |
| 7 | **Unifying Perception and Action: Implicit Visual CoT for Robotic Action Generation** | 未公开 | arXiv 2511.19859 [[链接]](https://arxiv.org/abs/2511.19859) | 混合模态管线 + 隐式视觉 CoT，统一感知与动作生成 |
| 8 | **VideoAuto-R1: Video Auto Reasoning via Thinking Once, Answering Twice** | Meta | arXiv 2601.05175 [[链接]](https://arxiv.org/abs/2601.05175) | 按需推理策略：先直接回答，低置信时才激活推理，响应长度减少 3.3 倍 |

### C3. 多模态基础架构与预训练

| # | 论文 | 机构 | 会议/来源 | 简介 |
|---|------|------|-----------|------|
| 1 | **VL-JEPA: Joint Embedding Predictive Architecture for Vision-language** | HKUST, Meta FAIR | arXiv 2512.10942 [[链接]](https://arxiv.org/abs/2512.10942) | 基于 JEPA 的视觉语言模型，在连续嵌入空间而非 token 空间中预测，参数少 50% 性能更强 |
| 2 | **BAGEL: Emerging Properties in Unified Multimodal Pretraining** | 字节跳动 | arXiv 2505.14683 [[链接]](https://arxiv.org/abs/2505.14683) | 统一多模态理解和生成的开源基础模型，展现涌现能力 |
| 3 | **CLI: Dynamic Cross-Layer Injection for Deep Vision-Language Fusion** | 电子科大 | arXiv 2601.10710 [[链接]](https://arxiv.org/abs/2601.10710) | 动态多对多跨层注入，让 LLM 按需访问完整视觉层次，18 个基准显著提升 |
| 4 | **LightFusion/LIGHTBAGEL: Double Fusion for Unified Multimodal Understanding and Generation** | 未公开 | arXiv 2510.22946 [[链接]](https://arxiv.org/abs/2510.22946) | 轻量双融合框架，统一多模态理解与生成 |
| 5 | **Qwen3-VL Technical Report** | 阿里巴巴 | arXiv 2511.21631 [[链接]](https://arxiv.org/abs/2511.21631) | Qwen 系列最强视觉语言模型，原生支持交错多模态和 agentic 能力 |
| 6 | **SAM 3: Segment Anything with Concepts** | Meta AI | arXiv 2511.16719 [[链接]](https://arxiv.org/abs/2511.16719) | SAM 第三代，统一基于概念提示的图像/视频检测、分割与跟踪 |
| 7 | **Rethinking Generative Image Pretraining: Scaling Next-Pixel Prediction** | Google | arXiv 2511.08704 [[链接]](https://arxiv.org/abs/2511.08704) | 系统研究自回归逐像素预测的缩放特性，为统一视觉模型建立基准 |
| 8 | **DeepSeek-OCR 2: Visual Causal Flow** | DeepSeek AI | arXiv 2601.20552 [[链接]](https://arxiv.org/abs/2601.20552) | DeepSeek 视觉因果流模型，面向 OCR 和视觉理解 |
| 9 | **Efficient Training of Diffusion MoE Models: A Practical Recipe** | 未公开 | arXiv 2512.01252 [[链接]](https://arxiv.org/abs/2512.01252) | 扩散 MoE 模型高效训练的实用配方 |
| 10 | **Dream-VL & Dream-VLA: Diffusion Language Model Backbone** | 未公开 | arXiv (用户提供) | 基于扩散语言模型 backbone 的开放视觉语言和 VLA 模型 |
| 11 | **MindGPT-4ov: Enhanced MLLM via Multi-Stage Post-Training** | 未公开 | arXiv 2512.02895 [[链接]](https://arxiv.org/abs/2512.02895) | 多阶段后训练范式增强多模态大模型 |

### C4. 高效推理与压缩

| # | 论文 | 机构 | 会议/来源 | 简介 |
|---|------|------|-----------|------|
| 1 | **VLA-Perf: Demystifying VLA Inference Performance** | 未公开 | arXiv 2602.18397 [[链接]](https://arxiv.org/abs/2602.18397) | 系统分析 VLA 推理性能瓶颈的首个基准工具 |
| 2 | **PSA: Pyramid Sparse Attention for Efficient Video Understanding** | 未公开 | arXiv 2512.04025 [[链接]](https://arxiv.org/abs/2512.04025) | 金字塔稀疏注意力，高效视频理解与生成 |
| 3 | **Blink: Dynamic Visual Token Resolution for Multimodal Understanding** | 未公开 | arXiv 2512.10548 [[链接]](https://arxiv.org/abs/2512.10548) | 动态视觉 token 分辨率，按需分配计算资源 |
| 4 | **ApET: Approximation-Error Guided Token Compression for Efficient VLMs** | 未公开 | arXiv 2602.19870 [[链接]](https://arxiv.org/abs/2602.19870) | 近似误差引导的 token 压缩，高效 VLM 推理 |
| 5 | **AstraNav-Memory: Contexts Compression for Long Memory** | 未公开 | arXiv 2512.21627 [[链接]](https://arxiv.org/abs/2512.21627) | 面向长程记忆的上下文压缩方法 |
| 6 | **Efficient Multi-Camera Tokenization with Triplanes for E2E Driving** | 未公开 | arXiv 2506.12251 [[链接]](https://arxiv.org/abs/2506.12251) | 三平面表示实现高效多相机词元化 |
| 7 | **Towards Efficient Multi-Camera Encoding for E2E Driving** | 未公开 | arXiv 2512.10947 [[链接]](https://arxiv.org/abs/2512.10947) | 面向端到端驾驶的高效多相机编码方案 |

### C5. Survey 综述

| # | 论文 | 机构 | 会议/来源 | 简介 |
|---|------|------|-----------|------|
| 1 | **A Comprehensive Survey on World Models for Embodied AI** | 未公开 | arXiv 2510.16732 [[链接]](https://arxiv.org/abs/2510.16732) | 具身 AI 世界模型全面综述 |
| 2 | **A Survey on Efficient Vision-Language-Action Models** | 未公开 | arXiv 2510.24795 [[链接]](https://arxiv.org/abs/2510.24795) | 高效 VLA 模型综述 |
| 3 | **Reliable and Responsible Foundation Models: A Comprehensive Survey** | 多机构联合 | arXiv 2602.08145 [[链接]](https://arxiv.org/abs/2602.08145) | 可靠且负责任的基础模型综述（偏差/安全/隐私/可解释性/分布偏移） |
| 4 | **Video Generation Models in Robotics: Applications, Challenges, Future** | 未公开 | arXiv 2601.07823 [[链接]](https://arxiv.org/abs/2601.07823) | 视频生成模型在机器人中的应用综述 |
| 5 | **Multimodal Spatial Reasoning in the Large Model Era: Survey** | 未公开 | arXiv 2510.25760 [[链接]](https://arxiv.org/abs/2510.25760) | 多模态空间推理综述 |
| 6 | **Forging Spatial Intelligence: Roadmap** | 未公开 | arXiv 2512.24385 [[链接]](https://arxiv.org/abs/2512.24385) | 空间智能路线图 |
| 7 | **Real Deep Research for AI, Robotics and Beyond** | 未公开 | arXiv 2510.20809 [[链接]](https://arxiv.org/abs/2510.20809) | AI 与机器人深度研究综述 |

### C6. 物理 AI 评估基准

| # | 论文 | 机构 | 会议/来源 | 简介 |
|---|------|------|-----------|------|
| 1 | **PAI-Bench: A Comprehensive Benchmark For Physical AI** | CMU, SHI Lab | arXiv 2512.01989 [[链接]](https://arxiv.org/abs/2512.01989) | 物理 AI 统一基准，评估视频生成/理解模型的物理感知与预测能力，2808 个真实案例 |
| 2 | **ProPhy: Progressive Physical Alignment for Dynamic World Simulation** | 中山大学 | arXiv 2512.05564 [[链接]](https://arxiv.org/abs/2512.05564) | 渐进式物理对齐框架，MoE 物理专家 + VLM 物理推理迁移，生成物理一致视频 |
| 3 | **PICABench: How Far from Physically Realistic Image Editing?** | 港中文, 上海AI Lab | arXiv 2510.17681 [[链接]](https://arxiv.org/abs/2510.17681) | 首个系统评估 T2I 编辑物理真实性的基准（光学/力学/状态转换） |
| 4 | **Beyond Words and Pixels: Implicit World Knowledge Reasoning Benchmark** | 快手 | arXiv 2511.18271 [[链接]](https://arxiv.org/abs/2511.18271) | 评估 T2I 模型隐含世界知识和物理因果推理的基准，1100 个提示 |
| 5 | **PhyBlock: Progressive Benchmark for Physical Understanding via 3D Block Assembly** | CMU | arXiv 2506.08708 [[链接]](https://arxiv.org/abs/2506.08708) | 通过 3D 积木组装的渐进式物理理解与规划基准 |
| 6 | **WorldArena: Unified Benchmark for Embodied World Models** | 未公开 | arXiv 2602.08971 [[链接]](https://arxiv.org/abs/2602.08971) | 统一评估具身世界模型的感知与功能效用 |

---

## 统计概览

| 类别 | 论文数 |
|------|--------|
| **I. 自动驾驶** | |
| A1. 端到端 VLA 架构 | 17 |
| A2. 世界模型 | 12 |
| A3. 快慢系统 (交叉引用) | 3 |
| A4. 仿真与数据 | 5 |
| A5. 规划与控制 | 2 |
| A6. 安全与评估 | 3 |
| **II. 机器人** | |
| B1. VLA 整体架构 | 19 |
| B2. 动作表征与词表 | 7 |
| B3. 世界模型与策略协同 | 9 |
| B4. 强化学习与策略优化 | 9 |
| B5. 数据与预训练 | 9 |
| **III. 通用/跨领域** | |
| C1. 空间感知与 3D/4D | 14 |
| C2. 潜在推理与思维链 | 8 |
| C3. 多模态基础架构 | 11 |
| C4. 高效推理与压缩 | 7 |
| C5. Survey 综述 | 7 |
| C6. 物理 AI 评估 | 6 |

> 部分论文在多个类别中交叉出现

---

*本报告由 Cursor AI 自动分析生成，论文元信息来自 arXiv API。*
