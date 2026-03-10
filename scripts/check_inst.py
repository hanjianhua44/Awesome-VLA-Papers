import json
d = json.load(open("daily/2026-03-09.json", "r", encoding="utf-8"))
known = [p for p in d if p["institution"] != "\u2014"]
print(f"Total: {len(d)}, Identified: {len(known)}, Unknown: {len(d)-len(known)}")
print()
for p in d:
    tag = "OK" if p["institution"] != "\u2014" else "??"
    print(f"[{tag}] {p['institution']:30s} | {p['title'][:65]}")
