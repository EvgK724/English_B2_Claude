# Дописывает в колоду «Фразовые глаголы» (phrasal) или «Фразы из Breaking Bad» (bbapp) карточки,
# которые ежедневная задача добавила в отдельное приложение колоды, вместе с их записями.
#
#   python3 tools/deck_sync.py phrasal <папка>   # в папке: index.html колоды и audio/<id>-t.mp3, audio/<id>-x.mp3
#   python3 tools/deck_sync.py bbapp   <папка>   # то же, записи в audio/us/
#   python3 tools/mk_shell.py                     # затем пересобрать оболочку
#
# Что меняется: site/apps/<ключ>.html (новые объекты встают над строкой-маркером), site/packs/<ключ>.mp3
# (записи дописываются в конец, тишина по краям срезается без пережатия, как в tools/reference/lossless.py),
# tools/packs.json и tools/catalog.json (ids, items, kw, size). Уже известные карточки не трогаются.
# Нужен ffmpeg.
import array, importlib.util, json, math, pathlib, re, subprocess, sys

T = pathlib.Path(__file__).resolve().parent
SITE = T.parent / "site"
MARK = "  // НОВАЯ КАРТОЧКА ВСТАВЛЯЕТСЯ ВЫШЕ ЭТОЙ СТРОКИ"
AUDIO_DIR = {"phrasal": "audio", "bbapp": "audio/us"}
SR, SPF = 24000, 576

spec = importlib.util.spec_from_file_location("lossless", T / "reference" / "lossless.py")
lossless = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lossless)


def card_blocks(html):
    """Объекты карточек из const CARDS = [ … ] — как текст, в порядке файла: [(id, текст)]."""
    i = html.index("const CARDS = [")
    j = html.index(MARK, i)
    body = html[i:j]
    out = []
    for m in re.finditer(r"^  \{\n.*?^  \},?[ \t]*$", body, re.S | re.M):
        text = m.group(0).rstrip()
        if not text.endswith(","):
            text += ","
        cid = re.search(r'^\s*id:\s*"([^"]+)"', text, re.M).group(1)
        out.append((cid, text))
    return out


def field(text, name):
    m = re.search(r'^\s*' + name + r':\s*"((?:[^"\\]|\\.)*)"', text, re.M)
    if not m:
        return None
    return json.loads('"' + m.group(1).replace("\\'", "'") + '"')


def short_ru(ru):
    """Короткий перевод для главного экрана — как deckItems() в tools/shell.html."""
    s = (ru or "").split(" — ")[0].split(". ")[0]
    return s[:-1] if s.endswith(".") else s


def pcm(b):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-f", "mp3", "-i", "-", "-f", "s16le", "-ac", "1", "-ar", str(SR), "-"],
                         input=b, capture_output=True, check=True).stdout
    a = array.array("h"); a.frombytes(raw)
    return [v / 32768.0 for v in a]


def db_of(x, n):
    return [20 * math.log10(math.sqrt(sum(v * v for v in x[i * n:(i + 1) * n]) / n) + 1e-9) for i in range(len(x) // n)]


def trim_clip(b):
    """Речь по громкости (окна 10 мс, как tools/reference/audio.py) и обрезка целыми кадрами без пережатия."""
    x = pcm(b)
    db = db_of(x, int(SR * 0.01))
    if not db:
        return b, 0.0
    thr = max(-50.0, max(db) - 42.0)
    voiced = [i for i, v in enumerate(db) if v > thr]
    if not voiced:
        return b, 0.0
    a = max(0, int((voiced[0] * 0.01 - 0.04) * SR))
    e = min(len(x), int(((voiced[-1] + 1) * 0.01 + 0.12) * SR))
    try:
        data, cut, *_ = lossless.trim(b, a / SR, (e - a) / SR, db_of(x, SPF))
        return data, round(cut, 4)
    except Exception:
        return b, 0.0                                   # необычный mp3 — кладём целиком


def main():
    key, src = sys.argv[1], pathlib.Path(sys.argv[2])
    if key not in AUDIO_DIR:
        sys.exit("ключ: phrasal или bbapp")
    app_path = SITE / "apps" / (key + ".html")
    html = app_path.read_text()
    have = {cid for cid, _ in card_blocks(html)}
    new = [(cid, text) for cid, text in card_blocks((src / "index.html").read_text()) if cid not in have]
    if not new:
        print(key, ": новых карточек нет")
        return

    packs = json.loads((T / "packs.json").read_text())
    cat = json.loads((T / "catalog.json").read_text())
    app = next(a for a in cat["apps"] if a["key"] == key)
    pack_path = SITE / "packs" / (key + ".mp3")
    pack = bytearray(pack_path.read_bytes())

    for cid, text in new:
        if re.search(r"^\s*au:\s*1\b", text, re.M):
            files = [src / AUDIO_DIR[key] / f"{cid}-{s}.mp3" for s in "tx"]
            if all(f.exists() and f.stat().st_size > 1024 for f in files):
                for s, f in zip("tx", files):
                    data, lead = trim_clip(f.read_bytes())
                    packs[key][f"{cid}-{s}"] = [len(pack), len(data), lead]
                    pack += data
            else:                                       # записей нет — карточку озвучит голос устройства
                text = re.sub(r"^\s*au:\s*1,\n", "", text, flags=re.M)
        html = html.replace(MARK, text + "\n" + MARK, 1)
        term, added = field(text, "term"), field(text, "added")
        app["ids"].append(cid)
        item = {"id": cid, "term": term, "ru": short_ru(field(text, "ru"))}
        if added:
            item["added"] = added
        app["items"].append(item)
        app["kw"] = (app.get("kw") + " · " if app.get("kw") else "") + term
        print(key, "+", cid, added or "", "звук" if f"{cid}-t" in packs[key] else "без записей")

    app_path.write_text(html)
    pack_path.write_bytes(bytes(pack))
    app["size"] = len(html.encode())
    (T / "packs.json").write_text(json.dumps(packs, separators=(",", ":")))
    (T / "catalog.json").write_text(json.dumps(cat, ensure_ascii=False))


if __name__ == "__main__":
    main()
