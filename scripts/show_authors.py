import json
from pathlib import Path

data = json.load(open(Path(__file__).parent.parent / 'data' / 'papers_raw.json', 'r', encoding='utf-8'))

for i, p in enumerate(data):
    aid = p.get('arxiv_id') or 'N/A'
    title = p['title'][:65]
    authors = p.get('authors', [])
    auth_str = ', '.join(authors[:6])
    if len(authors) > 6:
        auth_str += f' ... (+{len(authors)-6})'
    print(f"{i:3d}|{aid:14s}|{title}")
    print(f"   Authors: {auth_str}")
    print()
