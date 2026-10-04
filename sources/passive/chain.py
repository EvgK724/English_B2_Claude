# «Все формы подряд»: It is done. It is being done. … с ровной паузой; метки начала строк — для подсветки.
import json, pathlib, subprocess, sys, wave, tempfile
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here))
from content import FORMS
GAP, LEAD, RATE = 0.6, 0.15, 24000
tmp = pathlib.Path(tempfile.mkdtemp())
af = "silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse"
pcm, pos, marks = bytearray(b"\x00\x00" * int(LEAD * RATE)), int(LEAD * RATE), []
for i in range(len(FORMS)):
    w = tmp / f"f{i}.wav"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(here / "audio" / f"f-{i + 1}.mp3"), "-af", af, "-ar", str(RATE), "-ac", "1", "-sample_fmt", "s16", str(w)], check=True)
    with wave.open(str(w)) as r:
        n = r.getnframes(); marks.append(round(pos / RATE, 2)); pcm += r.readframes(n); pos += n
    pcm += b"\x00\x00" * int(GAP * RATE); pos += int(GAP * RATE)
out = tmp / "forms.wav"
with wave.open(str(out), "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(RATE); w.writeframes(bytes(pcm))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(out), "-c:a", "libmp3lame", "-b:a", "48k", "-ar", str(RATE), "-ac", "1", str(here / "audio" / "forms.mp3")], check=True)
(here / "forms.json").write_text(json.dumps(marks))
print(marks, round(pos / RATE, 2))
