# Список записей для озвучки: тройки глаголов, предложения карточек, примеры тем.
import json, pathlib, re, sys
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here))
from content import VERBS, CARDS, TOPICS

def full(c):
    if c.get("say"): return c["say"]
    q, a = c["q"], c["a"]
    i = q.index("___")
    before = q[:i].rstrip()
    if before == "" or before[-1] in ".!?": a = a[:1].upper() + a[1:]
    return q.replace("___", a)

clips = []
for v in VERBS:
    clips.append({"key": "v-" + v["v"], "text": v["say"], "rate": "-10%"})
for c in CARDS:
    if c.get("form"): continue
    clips.append({"key": c["id"], "text": full(c), "rate": "-5%"})
for t in TOPICS:
    for i, ex in enumerate(t.get("ex", [])):
        clips.append({"key": f"r{t['n']}-{i + 1}", "text": re.sub(r"[{}|_]", "", ex["en"]), "rate": "-5%"})
keys = [c["key"] for c in clips]
assert len(keys) == len(set(keys))
(here / "clips.json").write_text(json.dumps(clips, ensure_ascii=False, indent=1))
print(len(clips), "clips")
