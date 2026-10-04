# Звук для «Английского»: обрезать тишину по краям записей, пережать в MP3 24 кГц моно и склеить по тренажёрам.
# Фаза trim: build/pcm/<app>/<key>.raw + build/trim.json; фаза pack: build/packs/<app>.mp3 + build/packs.json
import json, pathlib, subprocess, sys, numpy as np
from concurrent.futures import ProcessPoolExecutor

B = pathlib.Path(__file__).resolve().parent / "build"
SR = 24000
KEEP_LEAD, KEEP_TAIL = 0.04, 0.12

def trim_one(args):
    app, key, src = args
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-f", "s16le", "-ac", "1", "-ar", str(SR), "-"],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
    win = int(SR * 0.01)
    n = len(x) // win
    if n == 0:
        return app, key, 0.0, len(x) / SR, 0.0
    rms = np.sqrt(np.mean(x[:n * win].reshape(n, win) ** 2, axis=1) + 1e-12)
    db = 20 * np.log10(rms)
    thr = max(-50.0, db.max() - 42.0)
    voiced = np.nonzero(db > thr)[0]
    if len(voiced) == 0:
        a, b = 0, len(x)
    else:
        a = max(0, int((voiced[0] * 0.01 - KEEP_LEAD) * SR))
        b = min(len(x), int(((voiced[-1] + 1) * 0.01 + KEEP_TAIL) * SR))
    out = B / "pcm" / app / (key + ".raw")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes((np.clip(x[a:b], -1, 1) * 32767).astype(np.int16).tobytes())
    return app, key, a / SR, (b - a) / SR, len(x) / SR

def enc_one(args):
    app, key, br = args
    src = B / "pcm" / app / (key + ".raw")
    return app, key, subprocess.run(
        ["ffmpeg", "-v", "error", "-f", "s16le", "-ar", str(SR), "-ac", "1", "-i", str(src),
         "-c:a", "libmp3lame", "-b:a", f"{br}k", "-map_metadata", "-1", "-id3v2_version", "0", "-write_id3v1", "0",
         "-f", "mp3", "-"], capture_output=True, check=True).stdout

if __name__ == "__main__":
    phase = sys.argv[1]
    src = json.loads((B / "audio_src.json").read_text())
    if phase == "trim":
        jobs = [(a, k, p) for a, d in src.items() for k, p in d.items()]
        res = {}
        with ProcessPoolExecutor(2) as ex:
            for i, (a, k, lead, dur, orig) in enumerate(ex.map(trim_one, jobs, chunksize=16)):
                res.setdefault(a, {})[k] = [round(lead, 4), round(dur, 4), round(orig, 4)]
                if i % 500 == 0: print("trim", i, "/", len(jobs), flush=True)
        (B / "trim.json").write_text(json.dumps(res))
        tot = sum(v[1] for d in res.values() for v in d.values()); orig = sum(v[2] for d in res.values() for v in d.values())
        print("trimmed seconds", round(tot), "of", round(orig), flush=True)
    elif phase == "pack":
        br = int(sys.argv[2])
        trim = json.loads((B / "trim.json").read_text())
        jobs = [(a, k, br) for a, d in trim.items() for k in sorted(d)]
        clips = {}
        with ProcessPoolExecutor(2) as ex:
            for i, (a, k, data) in enumerate(ex.map(enc_one, jobs, chunksize=16)):
                clips.setdefault(a, {})[k] = data
                if i % 500 == 0: print("enc", i, "/", len(jobs), flush=True)
        index = {}; total = 0
        (B / "packs").mkdir(exist_ok=True)
        for a, d in clips.items():
            buf = bytearray(); idx = {}
            for k in sorted(d):
                data = d[k]
                assert data[:2] in (b"\xff\xf3", b"\xff\xf2", b"\xff\xfb"), (a, k, data[:4])
                idx[k] = [len(buf), len(data), trim[a][k][0]]
                buf += data
            (B / "packs" / f"{a}.mp3").write_bytes(bytes(buf))
            index[a] = idx; total += len(buf)
        (B / "packs.json").write_text(json.dumps(index, separators=(",", ":")))
        print("packed", len(index), "apps", total, "bytes at", br, "kbps", flush=True)
