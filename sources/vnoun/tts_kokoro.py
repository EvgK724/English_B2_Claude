# Записи для «Recycle → recycling» голосом Daniel (bm_daniel) открытой модели Kokoro — локально, как у «I know the feeling».
# Ryan (edge-tts) с 12 октября 2026 недоступен: сервис Microsoft отклоняет синтез (403), 13 октября — так же.
# Модель — с GitHub: https://github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files-v1.0
#   (kokoro-v1.0.onnx и voices-v1.0.bin) в папку KOKORO_DIR (по умолчанию sources/encour/kokoro/, в git не попадает).
# Запуск из sources/: pip install kokoro-onnx soundfile; python3 vnoun/clips.py; python3 vnoun/tts_kokoro.py
#   (уже записанные файлы пропускаются), затем python3 vnoun/build.py и python3 ../tools/mk_shell.py
import json, os, pathlib, re, subprocess, tempfile
import soundfile as sf
from kokoro_onnx import Kokoro

here = pathlib.Path(__file__).parent
kdir = pathlib.Path(os.environ.get("KOKORO_DIR", here.parent / "encour" / "kokoro"))
VOICE = "bm_daniel"
# как читать то, что модель читает плохо (на экране остаётся как есть)
SPEAK = {"CO₂": "C O 2", "PM2.5": "P M 2 point 5"}
k = Kokoro(str(kdir / "kokoro-v1.0.onnx"), str(kdir / "voices-v1.0.bin"))
(here / "audio").mkdir(exist_ok=True)
clips = json.loads((here / "clips.json").read_text())
n = 0
for c in clips:
    path = here / "audio" / f"{c['key']}.mp3"
    if path.exists() and path.stat().st_size > 1024:
        continue
    speed = 1 + int(c["rate"].rstrip("%")) / 100          # "-5%" → 0.95, как в записях Ryan
    text = re.sub(r"\s+—\s+", ", ", c["text"]).strip()     # тире Kokoro не читает — пауза запятой
    for a, b in SPEAK.items():
        text = text.replace(a, b)
    samples, sr = k.create(text, voice=VOICE, speed=speed, lang="en-gb")
    with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
        sf.write(tmp.name, samples, sr)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp.name, "-ac", "1", "-ar", "24000", "-b:a", "48k",
                        "-map_metadata", "-1", "-id3v2_version", "0", "-write_id3v1", "0", "-write_xing", "0", str(path)], check=True)
    assert path.stat().st_size > 1024, c["key"]
    n += 1
print("записано", n, "из", len(clips), "голосом", VOICE)
