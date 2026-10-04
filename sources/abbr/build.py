import re, json, base64, html, pathlib, sys
here = pathlib.Path("abbr")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, GROUPS, ERRORS, LETTERS, MIXED_TOPIC
tpl = (here / "template.html").read_text()
esc = html.escape
nb = lambda s: esc(s).replace(" — ", "&nbsp;— ")

letters = "\n".join(
    f'          <button class="lt" type="button" data-key="lt-{l.lower()}" data-text="{esc(say)}" aria-label="Прослушать букву {l}">'
    f'<span class="lt-l" lang="en">{l}</span><span class="lt-i">{ipa}</span></button>'
    for l, ipa, say in LETTERS)
errors = "\n".join(
    f'          <li class="err"><span class="sr">Неверно:</span> <s lang="en">{esc(w)}</s> <span class="arr" aria-hidden="true">→</span> '
    f'<span class="sr">верно:</span> <span class="good" lang="en">{esc(r)}</span><span class="err-note">{nb(note)}</span></li>'
    for w, r, note in ERRORS)

def card_js(k):
    d = {"id": k["id"], "t": k["t"], "ab": k["ab"], "full": k["full"], "ru": k["ru"], "ipa": k["ipa"], "gram": k["gram"],
         "ex": k["ex_mark"], "exRu": k["ex_ru"], "note": k["note"]}
    if k["ctx"]:
        d["ctx"] = k["ctx"]
    d.update({"sa": k["say"], "sl": k["say_l"], "se": k["ex_say"]})
    return json.dumps(d, ensure_ascii=False)

data = ("// ——— Темы по группам\n"
        f"const MIXED_TOPIC = {MIXED_TOPIC};\n"
        "const GROUPS = " + json.dumps(GROUPS, ensure_ascii=False) + ";\n"
        "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Карточки. Новые добавляются сюда, в конец своей темы.\n"
        "// ab — сокращение; full — расшифровка, [x] — буква, от которой оно образовано; ru — перевод; ipa — как читается;\n"
        "// gram — часть речи и артикль; ex, exRu — пример и перевод; note — заметка; ctx — подсказка на лицевой стороне;\n"
        "// sa, sl, se — что озвучить голосом устройства, если запись audio/<id>-a|l|e.mp3 не загрузится.\n"
        "const CARDS = [\n " + ",\n ".join(card_js(k) for k in CARDS) + "\n];")
out = tpl.replace("<!--__LETTERS__-->", letters).replace("<!--__ERRORS__-->", errors).replace("/*__DATA__*/", data)
for size in (180, 192):
    b64 = base64.b64encode((here / "tile" / f"icon-{size}.png").read_bytes()).decode()
    out = out.replace(f"__ICON{size}__", "data:image/png;base64," + b64)
s0 = out.index("<style>"); s1 = out.index("</style>", s0)
out = out[:s0] + re.sub(r"(?<![\w.#-])(\d+(?:\.\d+)?)px", r"calc(\1px*var(--k))", out[s0:s1]) + out[s1:]
assert "__ICON" not in out and "/*__DATA__*/" not in out and "<!--__" not in out
need = set(re.findall(r'data-key="([^"]+)"', out)) | {k["id"] + s for k in CARDS for s in ("-a", "-l", "-e")}
missing = sorted(k for k in need if not (here / "audio" / f"{k}.mp3").exists())
if missing and "--draft" not in sys.argv:
    raise SystemExit(f"нет записей: {len(missing)} — {missing[:8]}")
(here / "index.html").write_text(out)
live = pathlib.Path("artifact-files/17f35b77-ec05-4e16-a5e6-516e7ef5f8d8/index.html").read_text()
(here / "preview.html").write_text(live[:live.index("<body>") + 6] + "\n" + out + "\n</body></html>")
print("ok", len(out), "bytes;", len(TOPICS), "topics;", len(CARDS), "cards;", len(need), "clips used;", len(missing), "missing")
