# Записи для озвучки: предложения карточек, примеры тем, все формы, «чего нет в русском».
import json, pathlib, re, sys
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here))
from content import CARDS, TOPICS, FORMS, RUEN

def full(c):
    q, a = c["q"], c["a"]
    i = q.index("___")
    before = q[:i].rstrip()
    if before == "" or before[-1] in ".!?": a = a[:1].upper() + a[1:]
    return q[:i] + a + q[i + 3:]
def plain(en):
    s = re.sub(r"\[([^\]|]+)(?:\|[soapr])?\]", r"\1", en)
    return s + ("" if s.rstrip()[-1:] in ".!?" else ".")

clips = [{"key": c["id"], "text": full(c), "rate": "-5%"} for c in CARDS]
for t in TOPICS:
    for i, ex in enumerate(t.get("ex", [])):
        clips.append({"key": f"r{t['n']}-{i + 1}", "text": plain(ex["en"]), "rate": "-5%"})
for i, f in enumerate(FORMS):
    clips.append({"key": f"fm-{i + 1}", "text": f[6], "rate": "-10%"})
for i, (_, en, _) in enumerate(RUEN):
    clips.append({"key": f"ru-{i + 1}", "text": plain(en), "rate": "-10%"})
keys = [c["key"] for c in clips]
assert len(keys) == len(set(keys))
(here / "clips.json").write_text(json.dumps(clips, ensure_ascii=False, indent=1))
print(len(clips), "clips")
