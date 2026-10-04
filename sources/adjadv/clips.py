# Записи для озвучки: предложения карточек, примеры тем, пары из памятки (hard — hardly…).
import json, pathlib, re, sys
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here))
from content import CARDS, TOPICS, MEMO

def full(c):
    q, a = c["q"], c["a"]
    i = q.index("___")
    before = q[:i].rstrip()
    if before == "" or before[-1] in ".!?": a = a[:1].upper() + a[1:]
    return q.replace("___", a)
def spoken(en):
    s = re.sub(r"[{}|_]", "", en)
    return s.replace(" → ", ", ").replace(" · ", ". ") + ("" if s.rstrip()[-1:] in ".!?" else ".")

clips = [{"key": c["id"], "text": full(c), "rate": "-5%"} for c in CARDS]
for t in TOPICS:
    for i, ex in enumerate(t.get("ex", [])):
        clips.append({"key": f"r{t['n']}-{i + 1}", "text": spoken(ex["en"]), "rate": "-5%"})
pairs = [g for g in MEMO if g["kind"] == "pairs"][0]["pairs"]
for i, (a, _, b, _) in enumerate(pairs):
    clips.append({"key": f"mp-{i + 1}", "text": f"{a}, {b}.", "rate": "-10%"})
keys = [c["key"] for c in clips]
assert len(keys) == len(set(keys))
(here / "clips.json").write_text(json.dumps(clips, ensure_ascii=False, indent=1))
print(len(clips), "clips")
