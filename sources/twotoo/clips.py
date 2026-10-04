# Записи для озвучки: предложения карточек, примеры тем, три слова с примерами.
import json, pathlib, re, sys
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here))
from content import CARDS, TOPICS, WORDS

def full(c):
    q, a = c["q"], c["a"]
    i = q.index("___")
    before, after = q[:i].rstrip(), q[i + 3:]
    start = before == "" or before[-1] in ".!?"
    if a == "":
        after = after.lstrip()
        return q[:i] + (after[:1].upper() + after[1:] if start else after)
    if start: a = a[:1].upper() + a[1:]
    return q[:i] + a + after
def spoken(en):
    s = re.sub(r"[{}|_]", "", en)
    return s + ("" if s.rstrip()[-1:] in ".!?" else ".")

clips = [{"key": c["id"], "text": full(c), "rate": "-5%"} for c in CARDS]
for t in TOPICS:
    for i, ex in enumerate(t.get("ex", [])):
        clips.append({"key": f"r{t['n']}-{i + 1}", "text": spoken(ex["en"]), "rate": "-5%"})
for w in WORDS:
    clips.append({"key": "w-" + w["w"], "text": w["say"], "rate": "-10%"})
keys = [c["key"] for c in clips]
assert len(keys) == len(set(keys))
(here / "clips.json").write_text(json.dumps(clips, ensure_ascii=False, indent=1))
print(len(clips), "clips")
