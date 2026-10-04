# Исходные записи без пережатия: из каждого mp3 выбрасываются только целые кадры тишины в начале и в конце.
# Первый оставленный кадр — тишина без данных (part2_3_length = 0); ему ставится main_data_begin = 0,
# поэтому все следующие кадры декодируются бит-в-бит как в исходнике. Кадр Xing/Info (если был) убирается.
import json, pathlib, sys, math

B = pathlib.Path(__file__).resolve().parent / "build"
SR, SPF = 24000, 576                      # MPEG-2 Layer III, 24 кГц: 576 сэмплов на кадр (24 мс)
LEAD_KEEP, TAIL_KEEP = 3, 3               # кадров тишины оставить до речи и после

BR = {3: [0,32,40,48,56,64,80,96,112,128,160,192,224,256,320], 2: [0,8,16,24,32,40,48,56,64,80,96,112,128,144,160]}
SRT = {3: [44100,48000,32000], 2: [22050,24000,16000]}

def frames(b):
    i = 0; out = []
    if b[:3] == b"ID3":
        i = 10 + ((b[6] << 21) | (b[7] << 14) | (b[8] << 7) | b[9])
    while i + 4 <= len(b):
        h = int.from_bytes(b[i:i + 4], "big")
        assert (h >> 21) == 0x7FF, "desync"
        ver = (h >> 19) & 3; prot = (h >> 16) & 1; bri = (h >> 12) & 15; sri = (h >> 10) & 3; pad = (h >> 9) & 1; mode = (h >> 6) & 3
        assert ver == 2 and mode == 3, (ver, mode)       # MPEG-2, моно — так пишет edge-tts
        size = 72 * BR[ver][bri] * 1000 // SRT[ver][sri] + pad
        side = i + 4 + (0 if prot else 2)
        # побитово: main_data_begin(8) private(1) part2_3_length(12)
        bits = int.from_bytes(b[side:side + 3], "big")
        mdb = bits >> 16; p23 = (bits >> 3) & 0xFFF
        body = b[i + 4:i + size]
        xing = body.find(b"Xing") >= 0 or body.find(b"Info") >= 0
        out.append({"at": i, "size": size, "mdb": mdb, "p23": p23, "xing": xing, "side": side})
        i += size
    assert i == len(b), "tail"
    return out

def frame_db(b):
    """Громкость каждого кадра исходника (дБ от полной шкалы) — резать начало можно только в настоящей тишине."""
    import subprocess, numpy as np
    x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-f", "mp3", "-i", "-", "-f", "s16le", "-ac", "1", "-ar", str(SR), "-"],
                                     input=b, capture_output=True, check=True).stdout, dtype=np.int16).astype(np.float32) / 32768
    n = len(x) // SPF
    return [20 * math.log10(float(np.sqrt(np.mean(x[i * SPF:(i + 1) * SPF] ** 2))) + 1e-9) for i in range(n)]

def trim(b, lead_s, dur_s, db=None):
    fr = frames(b)
    start = 1 if fr and fr[0]["xing"] else 0
    # речь по разметке trim.json (там уже 40 мс запаса в начале и 120 мс в конце)
    on = lead_s + 0.04; off = lead_s + dur_s - 0.12
    first = max(start, int(on * SR / SPF) - LEAD_KEEP)
    last = min(len(fr) - 1, math.ceil(off * SR / SPF) + TAIL_KEEP)
    # резать можно только там, где ни один следующий кадр не берёт данные из выброшенных кадров (bit reservoir):
    # M_j — начало области данных кадра j в общем потоке данных; кадру j нужны байты с M_j - main_data_begin
    M = []; acc = 0
    for f in fr:
        M.append(acc); acc += f["size"] - (f["side"] - f["at"]) - 9
    need = [0] * (len(fr) + 1); need[len(fr)] = 10 ** 9
    for j in range(len(fr) - 1, -1, -1): need[j] = min(need[j + 1], M[j] - fr[j]["mdb"])
    quiet = lambda j: db is None or all(db[i] < -55 for i in range(max(0, j - 1), min(len(db), j + 4)))
    while first > start and (need[first + 1] < M[first] or not quiet(first)): first -= 1
    out = bytearray()
    for j in range(first, last + 1):
        f = fr[j]; chunk = bytearray(b[f["at"]:f["at"] + f["size"]])
        if j == first and j > start:
            # первый оставленный кадр делаем цифровой тишиной без ссылки назад:
            # main_data_begin = 0, part2_3_length = 0, big_values = 0. Байты его области данных не трогаем —
            # в них лежит начало данных следующего кадра, он декодируется как в исходнике.
            o = f["side"] - f["at"]
            v = int.from_bytes(chunk[o:o + 9], "big")          # 72 бита side info (MPEG-2, моно)
            v &= ~(0xFF << 64)                                  # main_data_begin (8)
            v &= ~(0xFFF << 51)                                 # part2_3_length (12) после private(1)
            v &= ~(0x1FF << 42)                                 # big_values (9)
            chunk[o:o + 9] = v.to_bytes(9, "big")
        out += chunk
    lead_cut = (first - start) * SPF / SR
    return bytes(out), lead_cut, first, last, len(fr)

if __name__ == "__main__":
    src = json.loads((B / "audio_src.json").read_text())
    tr = json.loads((B / "trim.json").read_text())
    index = {}; total = 0; orig = 0; fallback = 0
    (B / "packs").mkdir(exist_ok=True)
    for app, d in src.items():
        buf = bytearray(); idx = {}
        for k in sorted(d):
            b = pathlib.Path(d[k]).read_bytes(); orig += len(b)
            lead, dur, _ = tr[app][k]
            try:
                data, cut, first, last, n = trim(b, lead, dur, frame_db(b))
            except Exception as e:
                data, cut = b, 0.0; fallback += 1
            idx[k] = [len(buf), len(data), round(cut, 4)]
            buf += data
        (B / "packs" / f"{app}.mp3").write_bytes(bytes(buf))
        index[app] = idx; total += len(buf)
    (B / "packs.json").write_text(json.dumps(index, separators=(",", ":")))
    print("lossless packs", total, "bytes of", orig, "original;", fallback, "clips kept whole")
