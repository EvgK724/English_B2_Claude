# Записи для озвучки: сокращение (-a), сокращение с расшифровкой (-l), пример (-e), трудные буквы (lt-*).
import json, pathlib, sys
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here))
from content import CARDS, LETTERS

clips = []
for c in CARDS:
    clips.append({"key": c["id"] + "-a", "text": c["say"], "rate": "-10%"})
    clips.append({"key": c["id"] + "-l", "text": c["say_l"], "rate": "-5%"})
    clips.append({"key": c["id"] + "-e", "text": c["ex_say"], "rate": "-5%"})
for l, ipa, text in LETTERS:
    clips.append({"key": "lt-" + l.lower(), "text": text, "rate": "-10%"})
keys = [c["key"] for c in clips]
assert len(keys) == len(set(keys))
(here / "clips.json").write_text(json.dumps(clips, ensure_ascii=False, indent=1))
print(len(clips), "clips")
