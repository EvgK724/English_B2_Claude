# Записи для озвучки: идиома (-a), идиома со значением (-l), пример (-e).
import json, pathlib, sys
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here))
from content import CARDS

clips = []
for c in CARDS:
    clips.append({"key": c["id"] + "-a", "text": c["say"], "rate": "-10%"})
    clips.append({"key": c["id"] + "-l", "text": c["say_l"], "rate": "-5%"})
    clips.append({"key": c["id"] + "-e", "text": c["ex_say"], "rate": "-5%"})
keys = [c["key"] for c in clips]
assert len(keys) == len(set(keys))
(here / "clips.json").write_text(json.dumps(clips, ensure_ascii=False, indent=1))
print(len(clips), "clips")
