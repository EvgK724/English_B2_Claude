# Записи для озвучки: предложения карточек, примеры тем, строки таблицы форм.
import json, pathlib, re, sys
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here))
from content import CARDS, TOPICS, FORMS

def full(c):
    q, a = c["q"], c["a"]
    i = q.index("___")
    before = q[:i].rstrip()
    if before == "" or before[-1] in ".!?": a = a[:1].upper() + a[1:]
    return q.replace("___", a)

clips = [{"key": c["id"], "text": full(c), "rate": "-5%"} for c in CARDS]
for t in TOPICS:
    for i, ex in enumerate(t.get("ex", [])):
        clips.append({"key": f"r{t['n']}-{i + 1}", "text": re.sub(r"[{}|_]", "", ex["en"]), "rate": "-5%"})
for i, f in enumerate(FORMS):
    clips.append({"key": f"f-{i + 1}", "text": f"It {f[2]} {f[3]}.", "rate": "-10%"})
keys = [c["key"] for c in clips]
assert len(keys) == len(set(keys))
(here / "clips.json").write_text(json.dumps(clips, ensure_ascii=False, indent=1))
print(len(clips), "clips")
