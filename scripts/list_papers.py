import json

d = json.load(open('data/papers_raw.json', 'r', encoding='utf-8'))
for i, p in enumerate(d):
    cats = ', '.join(p.get('categories', [])[:3])
    aid = p.get('arxiv_id') or 'N/A'
    title = p['title'][:75]
    print(f"{i:3d} | {aid:14s} | {title:75s} | {cats}")
