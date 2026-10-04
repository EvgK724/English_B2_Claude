# Записи для озвучки: правильные предложения карточек, исправленные фразы из пар, слова «ложных друзей».
import json, pathlib, sys
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here))
from content import CARDS, TOPICS

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

clips = [{"key": c["id"], "text": full(c), "rate": "-5%"} for c in CARDS]
for t in TOPICS:
    for i, p in enumerate(t.get("pairs", [])):
        clips.append({"key": f"r{t['n']}-{i + 1}", "text": p["good"].replace("|", ""), "rate": "-5%"})
    for i, f in enumerate(t.get("ff", [])):
        clips.append({"key": f"fw-{i + 1}", "text": f["en"] + ".", "rate": "-10%"})
keys = [c["key"] for c in clips]
assert len(keys) == len(set(keys))
for c in clips: assert "|" not in c["text"] and "___" not in c["text"], c
(here / "clips.json").write_text(json.dumps(clips, ensure_ascii=False, indent=1))
print(len(clips), "clips")
