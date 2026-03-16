"""One-time script to add new papers to papers.yaml."""
import yaml
import sys

sys.stdout.reconfigure(encoding="utf-8")

new_papers = [
    {
        "title": "Unleashing VLA Potentials in Autonomous Driving via Explicit Learning from Failures",
        "arxiv": "2603.01063",
        "url": "https://arxiv.org/abs/2603.01063",
        "institution": "Tsinghua, Univ of Macau",
        "venue": "arXiv 2026",
        "domain": "ad",
        "subcategory": "e2e",
        "summary": "VLA自动驾驶模型通过显式失败学习突破RL优化性能瓶颈，引入失败案例辅助探索",
        "date": "2026-03-01",
    },
    {
        "title": "How Many Tokens Do 3D Point Cloud Transformer Architectures Really Need?",
        "arxiv": "2511.05449",
        "url": "https://arxiv.org/abs/2511.05449",
        "institution": "DFKI",
        "venue": "arXiv 2025",
        "domain": "general",
        "subcategory": "efficient",
        "summary": "探索3D点云Transformer中token数量与性能的关系，提出高效token减少策略",
        "date": "2025-11-07",
    },
    {
        "title": "Token Merging: Your ViT But Faster",
        "arxiv": "2210.09461",
        "url": "https://arxiv.org/abs/2210.09461",
        "institution": "Georgia Tech, Meta AI",
        "venue": "ICLR 2023",
        "domain": "general",
        "subcategory": "efficient",
        "summary": "Token Merging (ToMe)，无需训练即可通过渐进合并相似token加速ViT推理",
        "date": "2022-10-17",
    },
    {
        "title": "FASTer: Focal Token Acquiring-and-Scaling Transformer for Long-term 3D Object Detection",
        "arxiv": "2503.01899",
        "url": "https://arxiv.org/abs/2503.01899",
        "institution": "HUST",
        "venue": "arXiv 2025",
        "domain": "general",
        "subcategory": "efficient",
        "summary": "焦点token获取与缩放Transformer，用于长时序LiDAR 3D目标检测的高效时序融合",
        "date": "2025-02-28",
    },
    {
        "title": "DriveVGGT: Visual Geometry Transformer for Autonomous Driving",
        "arxiv": "2511.22264",
        "url": "https://arxiv.org/abs/2511.22264",
        "institution": "SJTU, Fudan",
        "venue": "arXiv 2025",
        "domain": "ad",
        "subcategory": "world-model",
        "summary": "将视觉几何基础模型VGGT适配到自动驾驶场景的前馈3D重建",
        "date": "2025-11-27",
    },
    {
        "title": "V-DPM: 4D Video Reconstruction with Dynamic Point Maps",
        "arxiv": "2601.09499",
        "url": "https://arxiv.org/abs/2601.09499",
        "institution": "Univ of Oxford",
        "venue": "arXiv 2026",
        "domain": "general",
        "subcategory": "spatial",
        "summary": "Dynamic Point Maps扩展静态3D重建到4D视频场景，基于VGGT实现动态场景重建",
        "date": "2026-01-14",
    },
    {
        "title": "DynamicVGGT: Learning Dynamic Point Maps for 4D Scene Reconstruction in Autonomous Driving",
        "arxiv": "2603.08254",
        "url": "https://arxiv.org/abs/2603.08254",
        "institution": "Huawei, Fudan, CUHK",
        "venue": "arXiv 2026",
        "domain": "ad",
        "subcategory": "world-model",
        "summary": "动态点图用于自动驾驶4D场景重建，处理时序变化和运动物体",
        "date": "2026-03-09",
    },
    {
        "title": "ACE-Brain-0: Spatial Intelligence as a Shared Scaffold for Universal Embodiments",
        "arxiv": "2603.03198",
        "url": "https://arxiv.org/abs/2603.03198",
        "institution": "SJTU, Fudan, USTC, SYSU",
        "venue": "arXiv 2026",
        "domain": "robot",
        "subcategory": "vla-arch",
        "summary": "以空间智能为统一支架，构建跨自动驾驶/机器人/无人机的通用具身智能",
        "date": "2026-03-03",
    },
    {
        "title": "Beyond Language Modeling: An Exploration of Multimodal Pretraining",
        "arxiv": "2603.03276",
        "url": "https://arxiv.org/abs/2603.03276",
        "institution": "Meta AI, NYU",
        "venue": "arXiv 2026",
        "domain": "general",
        "subcategory": "multimodal-arch",
        "summary": "超越语言建模，系统性探索原生多模态预训练的设计空间",
        "date": "2026-03-03",
    },
]

data = yaml.safe_load(open("data/papers.yaml", encoding="utf-8"))
existing_ids = {p["arxiv"] for p in data}

added = 0
for np_ in new_papers:
    if np_["arxiv"] in existing_ids:
        print(f"Skip {np_['arxiv']}: already exists")
        continue
    insert_idx = len(data)
    for i, p in enumerate(data):
        if p.get("domain") == np_["domain"] and p.get("subcategory") == np_["subcategory"]:
            insert_idx = i + 1
    data.insert(insert_idx, np_)
    added += 1
    print(f"Added {np_['arxiv']}: {np_['title'][:50]}... at index {insert_idx}")

with open("data/papers.yaml", "w", encoding="utf-8") as f:
    yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False, width=200)

print(f"\nDone. Added {added} papers. Total: {len(data)}")
