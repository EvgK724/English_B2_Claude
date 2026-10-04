# Записи для озвучки: карточки, примеры тем, ситуации «разный смысл», группы «старый» и «один».
import json, pathlib, re, sys
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here))
from content import CARDS, TOPICS, CONTRAST, OLD, ALONE

def full(c):
    q, a = c["q"], c["a"]
    i = q.index("___")
    before = q[:i].rstrip()
    if before == "" or before[-1] in ".!?": a = a[:1].upper() + a[1:]
    return q[:i] + a + q[i + 3:]
def plain(en):
    s = re.sub(r"[\[\]]", "", en)
    return s + ("" if s.rstrip()[-1:] in ".!?" else ".")

clips = [{"key": c["id"], "text": full(c), "rate": "-5%"} for c in CARDS]
for t in TOPICS:
    for i, ex in enumerate(t.get("ex", [])):
        clips.append({"key": f"r{t['n']}-{i + 1}", "text": plain(ex["en"]), "rate": "-5%"})
for i, rows in enumerate(CONTRAST):
    clips.append({"key": f"cp-{i + 1}", "text": " ".join(plain(r[0]) for r in rows), "rate": "-10%"})
for pre, items in (("mo", OLD), ("ma", ALONE)):
    for i, row in enumerate(items):
        clips.append({"key": f"{pre}-{i + 1}", "text": row[4], "rate": "-10%"})
keys = [c["key"] for c in clips]
assert len(keys) == len(set(keys))
(here / "clips.json").write_text(json.dumps(clips, ensure_ascii=False, indent=1))
print(len(clips), "clips")
