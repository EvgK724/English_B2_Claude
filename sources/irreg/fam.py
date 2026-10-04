# Склейка «вся семья вслух»: тройки глаголов семьи подряд с ровной паузой.
# Метки начала каждой тройки (в секундах) нужны странице, чтобы подсвечивать строку таблицы.
import json, pathlib, subprocess, sys, wave, tempfile
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here))
from content import VERBS, FAMILIES

GAP = 0.7          # пауза между тройками
LEAD = 0.15        # тишина в начале файла
RATE = 24000
tmp = pathlib.Path(tempfile.mkdtemp())

def trimmed(key):
    out = tmp / (key + ".wav")
    af = ("silenceremove=start_periods=1:start_threshold=-45dB,areverse,"
          "silenceremove=start_periods=1:start_threshold=-45dB,areverse")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(here / "audio" / (key + ".mp3")), "-af", af,
                    "-ar", str(RATE), "-ac", "1", "-sample_fmt", "s16", str(out)], check=True)
    with wave.open(str(out)) as w:
        return out, w.getnframes()

marks = {}
for f in FAMILIES:
    n = f["n"]
    frames, pos, m = [], int(LEAD * RATE), []
    silence = lambda sec: b"\x00\x00" * int(sec * RATE)
    pcm = bytearray(silence(LEAD))
    for v in [v for v in VERBS if v["t"] == n]:
        path, cnt = trimmed("v-" + v["v"])
        m.append(round(pos / RATE, 2))
        with wave.open(str(path)) as w:
            pcm += w.readframes(cnt)
        pos += cnt
        pcm += silence(GAP); pos += int(GAP * RATE)
    wav = tmp / f"fam-{n}.wav"
    with wave.open(str(wav), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(RATE); w.writeframes(bytes(pcm))
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(wav), "-c:a", "libmp3lame", "-b:a", "48k", "-ar", str(RATE), "-ac", "1",
                    str(here / "audio" / f"fam-{n}.mp3")], check=True)
    marks[n] = m
(here / "fam.json").write_text(json.dumps(marks))
print({n: (len(m), m[-1]) for n, m in marks.items()})
