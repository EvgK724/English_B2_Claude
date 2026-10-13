# Записи голосами открытой модели Kyutai Pocket TTS (CC BY 4.0, английская модель апреля 2026) — локально, в ONNX, без PyTorch.
# Голос — VCTK p274 (№8 из образцов 13 октября 2026); в мини-диалогах, где говорят двое («— …? — …»),
# вторую реплику говорит VCTK p273 (№7). Ryan (edge-tts) с 12 октября 2026 недоступен: Microsoft отклоняет синтез (403).
# Каждую запись распознаёт Whisper base.en и меряет темп (как у Ryan, с запасом): пропущено или искажено слово, зациклилась,
# тянет или тараторит — новая попытка (до 12, температура 0,3–0,6), остаётся лучшая; что так и не распозналось точно,
# скрипт печатает — послушать и при необходимости поправить текст.
# Январская версия модели (ONNX для sherpa-onnx) портила начало фраз («know the feeling», «The sunscreen»); в апрельской
# это исправлено (bos_before_voice) — из 27 трудных записей 25 чистые с первой попытки.
# Файлы — в sources/kyutai/ (в git не попадают):
#   https://huggingface.co/KevinAHM/pocket-tts-onnx (CC BY 4.0) — pocket_tts_onnx.py и onnx/english_2026-04/: bundle.json,
#     bos_before_voice.npy, flow_lm_main_int8.onnx, flow_lm_flow_int8.onnx, mimi_decoder_int8.onnx, mimi_encoder.onnx,
#     text_conditioner.onnx, tokenizer.model
#   https://huggingface.co/kyutai/tts-voices — vctk/p274_023_enhanced.wav → p274.wav, vctk/p273_023_enhanced.wav → p273.wav
#     (VCTK, CSTR University of Edinburgh, CC BY 4.0)
#   https://huggingface.co/csukuangfj/sherpa-onnx-whisper-base.en — base.en-encoder.int8.onnx, base.en-decoder.int8.onnx,
#     base.en-tokens.txt (проверка распознаванием)
# Запуск из sources/: pip install onnxruntime sentencepiece safetensors huggingface_hub sherpa-onnx soundfile;
#   python3 <ключ>/clips.py; python3 tts_kyutai.py <ключ> (уже записанные файлы пропускаются),
#   затем python3 <ключ>/build.py и python3 ../tools/mk_shell.py
import json, os, pathlib, re, subprocess, sys, tempfile
import numpy as np, soundfile as sf, sherpa_onnx as so

KDIR = pathlib.Path(os.environ.get("KYUTAI_DIR", pathlib.Path(__file__).parent / "kyutai"))
sys.path.insert(0, str(KDIR))
from pocket_tts_onnx import PocketTTSOnnx

VOICES = ["p274", "p273"]                     # первая реплика (и всё, что не диалог) — p274, ответ в диалоге — p273
SPEAK = {"CO₂": "C O 2", "10:40": "ten forty"}   # как читать то, что модель читает плохо (на экране — как есть)
SAME = {"tonnes": "tons", "okay": "ok"}       # британское написание и варианты, которые Whisper пишет иначе
NUM = {"ten": "", "forty": ""}               # числа словами Whisper пишет цифрами — в сравнении их не учитываем, как и цифры
TEMPS = (0.3, 0.3, 0.4, 0.3, 0.4, 0.5, 0.3, 0.4, 0.5, 0.6, 0.3, 0.4)
PAUSE = 0.4                                   # секунды тишины между репликами диалога

def turns(text):
    t = text.strip()
    for a, b in SPEAK.items():
        t = t.replace(a, b)
    parts = [p.strip() for p in re.split(r"(?:^|(?<=[.!?]))\s*—\s*", t)] if t.startswith("—") else [t]
    return [re.sub(r"\s+—\s+", ", ", p) for p in parts if p]   # тире внутри реплики — пауза запятой

def words(s):
    return [SAME.get(w, w) for w in re.findall(r"[a-z0-9']+", s.lower().replace("’", "'"))
            if not any(ch.isdigit() for ch in w) and w not in NUM]

def wer(ref, hyp):
    r, h = words(ref), words(hyp)
    d = list(range(len(h) + 1))
    for i in range(1, len(r) + 1):
        prev, d[0] = d[0], i
        for j in range(1, len(h) + 1):
            prev, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, prev + (r[i - 1] != h[j - 1]))
    return d[len(h)] / max(1, len(r))

tts = PocketTTSOnnx(models_dir=str(KDIR / "onnx"), language="english_2026-04", precision="int8", temperature=0.3)
asr = so.OfflineRecognizer.from_whisper(encoder=str(KDIR / "base.en-encoder.int8.onnx"), decoder=str(KDIR / "base.en-decoder.int8.onnx"),
                                        tokens=str(KDIR / "base.en-tokens.txt"), language="en", task="transcribe", num_threads=4)
refs = {v: str(KDIR / f"{v}.wav") for v in VOICES}   # кодирование образца модель кэширует сама

def hear(x, sr):
    pcm = subprocess.run(["ffmpeg", "-v", "error", "-f", "f32le", "-ar", str(sr), "-ac", "1", "-i", "-", "-ar", "16000", "-f", "f32le", "-"],
                         input=x.tobytes(), capture_output=True, check=True).stdout
    s = asr.create_stream(); s.accept_waveform(16000, np.frombuffer(pcm, dtype=np.float32)); asr.decode_stream(s)
    return s.result.text.strip()

def frames(x, sr, step=0.02):
    f = int(step * sr); n = len(x) // f
    return np.sqrt(np.mean(x[:n * f].reshape(n, f) ** 2, axis=1)), f

def trim(x, sr):
    """Срезать тишину по краям, оставив 60 мс в начале и 150 мс в конце."""
    e, f = frames(x, sr)
    if not len(e) or e.max() <= 0:
        return x
    loud = np.where(e > e.max() * 0.03)[0]
    a = max(0, loud[0] * f - int(0.06 * sr)); b = min(len(x), (loud[-1] + 1) * f + int(0.15 * sr))
    return x[a:b]

def pace(x, sr, text):
    """Секунд речи на слово: у Ryan 0,22–0,36 (медиана 0,27); годится 0,18–0,5 (у коротких фраз — до 0,8)."""
    n = max(1, len(re.findall(r"[A-Za-z0-9']+", text)))
    v = len(x) / sr / n
    return 0.18 <= v <= (0.8 if n <= 4 else 0.5), round(v, 2)

def say(text, voice):
    best = None
    for temp in TEMPS:
        tts.temperature = temp
        # кадр — 80 мс; не больше ~0,65 с на слово плюс 2,5 с запаса — зациклившаяся попытка обрывается сразу
        raw = np.asarray(tts.generate(text, refs[voice], max_frames=32 + 8 * len(re.findall(r"[A-Za-z0-9']+", text))),
                         dtype=np.float32).reshape(-1)
        sr = tts.sample_rate
        x = trim(raw, sr)
        heard = hear(x, sr); e = wer(text, heard)
        ok, v = pace(x, sr, text)
        score = e + (0 if ok else 0.5)                    # не тот темп (зациклилась, тянет, тараторит) — хуже любой ошибки в слове
        if os.environ.get("TTS_DEBUG"):
            print(f"    t={temp} {len(x) / sr:.1f}s {v} с/слово «{heard}» → {score:.2f}", flush=True)
        if best is None or score < best[0]:
            best = (score, x, sr, f"{heard} [{v} с/слово]")
        if score == 0:
            break
    return best

def main(key):
    here = pathlib.Path(__file__).parent / key
    (here / "audio").mkdir(exist_ok=True)
    clips = json.loads((here / "clips.json").read_text())
    n, doubt = 0, []
    for c in clips:
        path = here / "audio" / f"{c['key']}.mp3"
        if path.exists() and path.stat().st_size > 1024:
            continue
        pieces, sr = [], 24000
        for i, t in enumerate(turns(c["text"])):
            e, x, sr, heard = say(t, VOICES[i % 2])
            if e > 0:
                doubt.append(f"{c['key']}: «{t}» → «{heard}»")
            pieces += [x, np.zeros(int(PAUSE * sr), dtype=np.float32)]
        audio = np.concatenate(pieces[:-1])
        tempo = 1 + int(c["rate"].rstrip("%")) / 100          # "-5%" → 0.95, как в записях Ryan
        with tempfile.NamedTemporaryFile(suffix=".wav") as tmp:
            sf.write(tmp.name, audio, sr)
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp.name, "-af", f"atempo={tempo}", "-ac", "1", "-ar", "24000", "-b:a", "48k",
                            "-map_metadata", "-1", "-id3v2_version", "0", "-write_id3v1", "0", "-write_xing", "0", str(path)], check=True)
        assert path.stat().st_size > 1024, c["key"]
        n += 1
        print(c["key"], flush=True)
    print("записано", n, "из", len(clips), "голосом", " и ".join(VOICES))
    if doubt:
        print("распознано неточно — послушать:\n  " + "\n  ".join(doubt))

if __name__ == "__main__":
    for key in sys.argv[1:] or sys.exit("python3 tts_kyutai.py <ключ тренажёра>"):
        main(key)
