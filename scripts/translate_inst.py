"""Replace Chinese institution names with English equivalents in papers.yaml."""
import yaml
from pathlib import Path

ROOT = Path(__file__).parent.parent
YAML_PATH = ROOT / "data" / "papers.yaml"

INST_MAP = {
    "清华": "Tsinghua",
    "清华深圳": "Tsinghua Shenzhen",
    "北大": "PKU",
    "北航": "BUAA",
    "上海AI Lab": "Shanghai AI Lab",
    "上海交大": "SJTU",
    "浙大": "ZJU",
    "复旦": "Fudan",
    "南京大学": "Nanjing Univ",
    "中科院自动化所": "CASIA",
    "中科院": "CAS",
    "中科院深圳": "CAS Shenzhen",
    "中科大": "USTC",
    "华科": "HUST",
    "华中科大": "HUST",
    "华南理工": "SCUT",
    "电子科大": "UESTC",
    "武大": "WHU",
    "中山大学": "SYSU",
    "大连理工": "DUT",
    "西安交大": "XJTU",
    "国防科大": "NUDT",
    "哈工大深圳": "HIT Shenzhen",
    "北京交通大学": "BJTU",
    "天津大学": "Tianjin Univ",
    "苏州大学": "Soochow Univ",
    "厦大": "XMU",
    "人大": "RUC",
    "港中文": "CUHK",
    "港大": "HKU",
    "香港理工": "PolyU",
    "上科大": "ShanghaiTech",
    "澳门大学": "Univ of Macau",
    "延世大学": "Yonsei Univ",
    "鹏城实验室": "PCL",
    "华为": "Huawei",
    "华为诺亚": "Huawei Noah",
    "小米": "Xiaomi",
    "字节跳动": "ByteDance",
    "腾讯": "Tencent",
    "阿里巴巴": "Alibaba",
    "快手": "Kuaishou",
    "微软": "Microsoft",
    "微软亚研": "MSRA",
    "地平线": "Horizon Robotics",
    "理想汽车": "Li Auto",
    "多机构": "Multi-institution",
}

def translate(inst_str: str) -> str:
    parts = [s.strip() for s in inst_str.split(",")]
    translated = []
    for p in parts:
        translated.append(INST_MAP.get(p, p))
    return ", ".join(translated)

def main():
    with open(YAML_PATH, "r", encoding="utf-8") as f:
        papers = yaml.safe_load(f)

    changed = 0
    for p in papers:
        old = p["institution"]
        new = translate(old)
        if old != new:
            p["institution"] = new
            changed += 1

    class Dumper(yaml.SafeDumper):
        pass
    def str_representer(dumper, data):
        if "\n" in data:
            return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
        return dumper.represent_scalar("tag:yaml.org,2002:str", data)
    Dumper.add_representer(str, str_representer)

    with open(YAML_PATH, "w", encoding="utf-8") as f:
        yaml.dump(papers, f, Dumper=Dumper, allow_unicode=True, default_flow_style=False, sort_keys=False)

    print(f"Updated {changed}/{len(papers)} papers")

    # verify no Chinese left in institution field
    import re
    with open(YAML_PATH, "r", encoding="utf-8") as f:
        papers2 = yaml.safe_load(f)
    remaining = set()
    for p in papers2:
        for part in p["institution"].split(","):
            part = part.strip()
            if re.search(r"[\u4e00-\u9fff]", part):
                remaining.add(part)
    if remaining:
        print(f"WARNING - still Chinese: {remaining}")
    else:
        print("All institution names are now in English")

if __name__ == "__main__":
    main()
