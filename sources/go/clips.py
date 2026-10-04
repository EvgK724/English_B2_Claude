# Записи для озвучки: карточки, примеры тем, пары «с артиклем или без», фразовые глаголы, выражения.
import json, pathlib, re, sys
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here))
from content import CARDS, TOPICS, CONTRAST, PHRASAL, SET

def full(c):
    q, a = c["q"], c["a"]
    i = q.index("___")
    before = q[:i].rstrip()
    if before == "" or before[-1] in ".!?": a = a[:1].upper() + a[1:]
    return q[:i] + a + q[i + 3:]
def plain(en):
    s = re.sub(r"\[([^\]|]+)(?:\|b)?\]", r"\1", en)
    return s + ("" if s.rstrip()[-1:] in ".!?" else ".")
def cap(s): return s[:1].upper() + s[1:]

clips = [{"key": c["id"], "text": full(c), "rate": "-5%"} for c in CARDS]
for t in TOPICS:
    for i, ex in enumerate(t.get("ex", [])):
        clips.append({"key": f"r{t['n']}-{i + 1}", "text": plain(ex["en"]), "rate": "-5%"})
for i, (a, b) in enumerate(CONTRAST):
    clips.append({"key": f"cp-{i + 1}", "text": plain(a[0]) + " " + plain(b[0]), "rate": "-10%"})
for i, (p, _, ex) in enumerate(PHRASAL):
    clips.append({"key": f"ph-{i + 1}", "text": cap(p) + ". " + ex, "rate": "-10%"})
for i, (p, _) in enumerate(SET):
    clips.append({"key": f"st-{i + 1}", "text": plain(cap(p)), "rate": "-10%"})
keys = [c["key"] for c in clips]
assert len(keys) == len(set(keys))
(here / "clips.json").write_text(json.dumps(clips, ensure_ascii=False, indent=1))
print(len(clips), "clips")
