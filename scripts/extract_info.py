"""Extract key info from papers_raw.json for report generation."""
import json
from pathlib import Path

data = json.load(open(Path(__file__).parent.parent / 'data' / 'papers_raw.json', 'r', encoding='utf-8'))

for i, p in enumerate(data):
    aid = p.get('arxiv_id') or 'N/A'
    title = p['title']
    authors = p.get('authors', [])
    first3 = ', '.join(authors[:3])
    if len(authors) > 3:
        first3 += ' et al.'
    date = p.get('date', '')
    cats = ', '.join(p.get('categories', []))
    ab = p.get('abstract', '')[:200]
    print(f"=== {i} ===")
    print(f"Title: {title}")
    print(f"ID: {aid}")
    print(f"Authors: {first3}")
    print(f"Date: {date}")
    print(f"Categories: {cats}")
    print(f"Abstract: {ab}...")
    print()
