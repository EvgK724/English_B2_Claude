# Дописывает в колоду «Фразовые глаголы» (phrasal) или «Фразы из Breaking Bad» (bbapp) карточки,
# которые ежедневная задача добавила в отдельное приложение колоды, вместе с их записями.
#
#   python3 tools/deck_sync.py phrasal <папка>            # в папке: index.html колоды и audio/<id>-t.mp3, audio/<id>-x.mp3
#   python3 tools/deck_sync.py bbapp   <папка>            # то же, записи в audio/us/
#   python3 tools/mk_shell.py                              # затем пересобрать оболочку
#
#   python3 tools/deck_sync.py phrasal <папка> --check    # только показать новые карточки и каких записей не хватает
#   python3 tools/deck_sync.py phrasal <папка> --export <id> [<куда>]
#                                                          # card-<id>.json и audio-<id>.json для базы артефакта
#                                                          # «Английский B2» (data/decks/<ключ> и data/decks/<ключ>-audio)
#
# Что меняется: site/apps/<ключ>.html (новые объекты встают над строкой-маркером), site/packs/<ключ>.mp3
# (записи дописываются в конец, тишина по краям срезается без пережатия, как в tools/reference/lossless.py),
# tools/packs.json и tools/catalog.json (ids, items, kw, size). Уже известные карточки не трогаются.
# Без ffmpeg записи кладутся целиком, без обрезки тишины.
import array, base64, importlib.util, json, math, pathlib, re, subprocess, sys

T = pathlib.Path(__file__).resolve().parent
SITE = T.parent / "site"
MARK = "  // НОВАЯ КАРТОЧКА ВСТАВЛЯЕТСЯ ВЫШЕ ЭТОЙ СТРОКИ"
AUDIO_DIR = {"phrasal": "audio", "bbapp": "audio/us"}
SR, SPF = 24000, 576

spec = importlib.util.spec_from_file_location("lossless", T / "reference" / "lossless.py")
lossless = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lossless)


def cards_body(html):
    i = html.index("const CARDS = [")
    return html[i:html.index(MARK.strip(), i)]


def card_blocks(html):
    """Объекты карточек из const CARDS = [ … ] — как текст, в порядке файла: [(id, текст)].
    Каждая карточка — объект на нескольких строках, по полю на строку (так пишет ежедневная задача)."""
    out = []
    for m in re.finditer(r"^[ \t]*\{[ \t]*\n.*?^[ \t]*\},?[ \t]*$", cards_body(html), re.S | re.M):
        text = m.group(0).rstrip()
        if not text.endswith(","):
            text += ","
        cid = re.search(r'^\s*id:\s*"([^"]+)"', text, re.M).group(1)
        out.append((cid, text))
    return out


def js_string(raw):
    return json.loads('"' + raw.replace("\\'", "'") + '"')


def field(text, name):
    m = re.search(r'^\s*' + name + r':\s*"((?:[^"\\]|\\.)*)"', text, re.M)
    return js_string(m.group(1)) if m else None


def card_object(text):
    """Все поля карточки по порядку: строки и числа. Строку, которую не удалось разобрать, не пропускаем молча."""
    obj = {}
    for line in text.splitlines()[1:-1]:
        line = line.strip()
        if not line or line.startswith("//"):
            continue
        m = re.fullmatch(r'(\w+):\s*(?:"((?:[^"\\]|\\.)*)"|(-?\d+(?:\.\d+)?))\s*,?', line)
        if not m:
            raise ValueError("не разобрал строку карточки: " + line[:80])
        obj[m.group(1)] = js_string(m.group(2)) if m.group(2) is not None else json.loads(m.group(3))
    for k in ("id", "term", "ru"):
        if not obj.get(k):
            raise ValueError("в карточке нет поля " + k)
    return obj


def short_ru(ru):
    """Короткий перевод для главного экрана — как deckItems() в tools/shell.html."""
    s = (ru or "").split(" — ")[0].split(". ")[0]
    return s[:-1] if s.endswith(".") else s


def check_parsed(html, where):
    """Сколько id в массиве — столько и разобранных карточек, иначе карточка в непривычном виде потерялась бы."""
    n_ids = len(re.findall(r'(?:^|[{,])[ \t]*id:[ \t]*"', cards_body(html), re.M))
    n = len(card_blocks(html))
    if n != n_ids:
        sys.exit(f"{where}: разобрано {n} карточек из {n_ids} — проверьте формат новых объектов (поле на строку)")


def pcm(b):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-f", "mp3", "-i", "-", "-f", "s16le", "-ac", "1", "-ar", str(SR), "-"],
                         input=b, capture_output=True, check=True).stdout
    a = array.array("h"); a.frombytes(raw)
    return [v / 32768.0 for v in a]


def db_of(x, n):
    return [20 * math.log10(math.sqrt(sum(v * v for v in x[i * n:(i + 1) * n]) / n) + 1e-9) for i in range(len(x) // n)]


def trim_clip(b):
    """Речь по громкости (окна 10 мс, как tools/reference/audio.py) и обрезка целыми кадрами без пережатия."""
    try:
        x = pcm(b)
    except (OSError, subprocess.CalledProcessError):
        return b, 0.0                                   # нет ffmpeg или он не прочитал файл — кладём целиком
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


def export(key, src, cid, out):
    blocks = dict(card_blocks((src / "index.html").read_text()))
    if cid not in blocks:
        sys.exit(f"{cid}: нет такой карточки в {src / 'index.html'}")
    card = card_object(blocks[cid])
    out.mkdir(parents=True, exist_ok=True)
    files = [src / AUDIO_DIR[key] / f"{cid}-{s}.mp3" for s in "tx"]
    have_audio = all(f.exists() and f.stat().st_size > 1024 for f in files)
    if card.get("au") and not have_audio:
        del card["au"]                                  # без записей карточку озвучит голос устройства
    (out / f"card-{cid}.json").write_text(json.dumps(card, ensure_ascii=False))
    print(out / f"card-{cid}.json")
    if card.get("au"):
        audio = {s: base64.b64encode(f.read_bytes()).decode() for s, f in zip("tx", files)}
        (out / f"audio-{cid}.json").write_text(json.dumps(audio))
        print(out / f"audio-{cid}.json")


def main():
    args = sys.argv[1:]
    if len(args) < 2 or args[0] not in AUDIO_DIR:
        sys.exit("python3 tools/deck_sync.py phrasal|bbapp <папка> [--check | --export <id> [<куда>]]")
    key, src = args[0], pathlib.Path(args[1])
    if "--export" in args:
        i = args.index("--export")
        export(key, src, args[i + 1], pathlib.Path(args[i + 2]) if len(args) > i + 2 else src)
        return
    app_path = SITE / "apps" / (key + ".html")
    html = app_path.read_text()
    src_html = (src / "index.html").read_text()
    check_parsed(src_html, src / "index.html")
    have = {cid for cid, _ in card_blocks(html)}
    new = [(cid, text) for cid, text in card_blocks(src_html) if cid not in have]
    if "--check" in args:
        for cid, text in new:
            card_object(text)                           # формат полей
            missing = [f"{AUDIO_DIR[key]}/{cid}-{s}.mp3" for s in "tx"
                       if re.search(r"^\s*au:\s*1\b", text, re.M) and not (src / AUDIO_DIR[key] / f"{cid}-{s}.mp3").exists()]
            print("новая:", cid, ("нет записей: " + " ".join(missing)) if missing else "")
        if not new:
            print(key, ": новых карточек нет")
        return
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
