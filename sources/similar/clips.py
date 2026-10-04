# Записи для озвучки: предложения карточек, примеры тем, слова с сочетаниями.
import json, pathlib, re, sys
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here))
from content import CARDS, TOPICS, WORDS

def full(c):
    q, a = c["q"], c["a"]
    i = q.index("___")
    before = q[:i].rstrip()
    if before == "" or before[-1] in ".!?": a = a[:1].upper() + a[1:]
    return q[:i] + a + q[i + 3:]
def spoken(en):
    s = re.sub(r"[\[\]]", "", en)
    return s + ("" if s.rstrip()[-1:] in ".!?" else ".")
def caps(s):
    return re.sub(r"(^|[.!?]\s+)([a-z])", lambda m: m.group(1) + m.group(2).upper(), s)

clips = [{"key": c["id"], "text": full(c), "rate": "-5%"} for c in CARDS]
for t in TOPICS:
    for i, ex in enumerate(t.get("ex", [])):
        clips.append({"key": f"r{t['n']}-{i + 1}", "text": spoken(ex["en"]), "rate": "-5%"})
n = 0
for g, rows in WORDS.items():
    for w in rows:
        n += 1
        clips.append({"key": f"wd-{n}", "text": caps(w[3]), "rate": "-10%"})
keys = [c["key"] for c in clips]
assert len(keys) == len(set(keys))
(here / "clips.json").write_text(json.dumps(clips, ensure_ascii=False, indent=1))
print(len(clips), "clips")
