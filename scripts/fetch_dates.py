"""Fetch exact publication dates from arXiv API and add to papers.yaml."""
import ssl
import sys
import time
import yaml
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).parent.parent
YAML_PATH = ROOT / "data" / "papers.yaml"

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

NS = {"atom": "http://www.w3.org/2005/Atom"}

sys.stdout.reconfigure(encoding='utf-8')


def fetch_dates_batch(arxiv_ids: list, retries=3) -> dict:
    """Fetch publication dates for a batch of arXiv IDs."""
    id_list = ",".join(arxiv_ids)
    url = f"http://export.arxiv.org/api/query?id_list={id_list}&max_results={len(arxiv_ids)}"
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            resp = urllib.request.urlopen(req, context=SSL_CTX, timeout=60)
            xml_data = resp.read().decode("utf-8")
            root = ET.fromstring(xml_data)
            dates = {}
            for entry in root.findall("atom:entry", NS):
                eid = entry.find("atom:id", NS).text.strip().split("/")[-1]
                eid = eid.split("v")[0]
                published = entry.find("atom:published", NS).text.strip()[:10]
                dates[eid] = published
            return dates
        except Exception as e:
            print(f"      Attempt {attempt+1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(10 * (attempt + 1))
    return {}


def main():
    with open(YAML_PATH, "r", encoding="utf-8") as f:
        papers = yaml.safe_load(f)

    need_date = [(i, p) for i, p in enumerate(papers) if p.get("arxiv") and not p.get("date")]
    print(f"Total papers: {len(papers)}, need date: {len(need_date)}")

    batch_size = 10
    for start in range(0, len(need_date), batch_size):
        batch = need_date[start:start + batch_size]
        ids = [p["arxiv"] for _, p in batch]
        print(f"  Batch {start // batch_size + 1}/{(len(need_date)-1)//batch_size+1} ({len(ids)} papers)...")

        dates = fetch_dates_batch(ids)
        for idx, p in batch:
            aid = p["arxiv"]
            if aid in dates:
                papers[idx]["date"] = dates[aid]
                print(f"    {aid} -> {dates[aid]}")
            else:
                print(f"    {aid} -> NOT FOUND")

        time.sleep(5)

    with open(YAML_PATH, "w", encoding="utf-8") as f:
        yaml.dump(papers, f, allow_unicode=True, default_flow_style=False, sort_keys=False, width=200)

    dated = sum(1 for p in papers if p.get("date"))
    print(f"\nDone. {dated}/{len(papers)} papers have dates.")


if __name__ == "__main__":
    main()
