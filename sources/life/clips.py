# Записи для озвучки: предложения карточек, примеры тем, как звучит, выражения.
import json, pathlib, re, sys
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here))
from content import CARDS, TOPICS, SOUNDS, EXPR

def full(c):
    q, a = c["q"], c["a"]
    i = q.index("___")
    before = q[:i].rstrip()
    if before == "" or before[-1] in ".!?": a = a[:1].upper() + a[1:]
    return q[:i] + a + q[i + 3:]
def spoken(en):
    s = re.sub(r"[\[\]]", "", en)
    return s + ("" if s.rstrip()[-1:] in ".!?" else ".")

clips = [{"key": c["id"], "text": full(c), "rate": "-5%"} for c in CARDS]
for t in TOPICS:
    for i, ex in enumerate(t.get("ex", [])):
        clips.append({"key": f"r{t['n']}-{i + 1}", "text": spoken(ex["en"]), "rate": "-5%"})
for i, s in enumerate(SOUNDS):
    clips.append({"key": f"sd-{i + 1}", "text": s[4], "rate": "-10%"})
for i, e in enumerate(EXPR):
    clips.append({"key": f"ex-{i + 1}", "text": e[3], "rate": "-10%"})
keys = [c["key"] for c in clips]
assert len(keys) == len(set(keys))
(here / "clips.json").write_text(json.dumps(clips, ensure_ascii=False, indent=1))
print(len(clips), "clips")
