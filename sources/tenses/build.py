import re, json, base64, html, pathlib, sys
here = pathlib.Path("tenses")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, TENSES, TIMES, ASPECTS, TRAPS, MARKERS, FUTURE, ERRORS, MIXED_TOPIC
from timeline import svg
tpl = (here / "template.html").read_text()
esc = html.escape
def marked(s):
    s = esc(s)
    s = re.sub(r"\{([^}]+)\}", r'<span class="st">\1</span>', s)
    return re.sub(r"\[([^\]]+)\]", r'<span class="pr">\1</span>', s)
by = {(t["time"], t["aspect"]): t for t in TENSES}
def nw(s):
    return s.replace("-ing", '<span class="nw">-ing</span>')
rows = []
cols = "".join(f'<span lang="en">{esc(en)}<small>{esc(ru)}</small></span>' for _, en, ru in TIMES)
rows.append(f'      <div class="tg" role="group" aria-label="Таблица времён: колонки — прошлое, настоящее, будущее; строки — Simple, Continuous, Perfect, Perfect Continuous">\n        <div class="tg-cols" aria-hidden="true">{cols}</div>')
for key, en, ru in ASPECTS:
    cells = []
    for tkey, _, _ in TIMES:
        t = by[(tkey, key)]
        cls = "tc rare" if t.get("rare") else "tc"
        cells.append(f'<button class="{cls}" type="button" data-id="{t["id"]}" aria-pressed="false"><span class="sr">{esc(t["name"])}: </span><span lang="en">{marked(t["cell"])}</span></button>')
    rows.append(f'        <div class="tg-row"><p class="tg-asp"><b lang="en">{esc(en)}</b>{nw(esc(ru))}</p><div class="tg-cells">{"".join(cells)}</div></div>')
rows.append("      </div>")
grid = "\n".join(rows)
traps = "\n".join(
    f'        <div class="rb"><p class="rb-ru">{esc(ru)}</p><p class="rb-en" lang="en">{marked(en)}</p><p class="ot-note">{esc(note)}</p></div>'
    for ru, en, note in TRAPS)
markers = "\n".join(f'        <div class="mk"><p class="mk-w" lang="en">{esc(w)}</p><p class="mk-t" lang="en">{esc(tn)}</p></div>' for w, tn in MARKERS)
future = "\n".join(
    f'        <div class="ot"><div><p class="ot-c" lang="en">{esc(c)}</p><p class="ot-ru">{esc(ru)}</p></div><div><p class="ot-ex" lang="en">{marked(ex)}</p></div></div>'
    for c, ru, ex in FUTURE)
errors = "\n".join(
    f'          <li class="err"><span class="sr">Неверно:</span> <s lang="en">{esc(w)}</s> <span class="arr" aria-hidden="true">→</span> '
    f'<span class="sr">верно:</span> <span class="good" lang="en">{esc(r)}</span><span class="err-note">{esc(note)}</span></li>'
    for w, r, note in ERRORS)
tenses = [dict(t, svg=svg(t)) for t in TENSES]
data = ("// ——— Темы: правило и примеры. […] — форма времени (оранжевый), {…} — слово-подсказка (синий).\n"
        f"const MIXED_TOPIC = {MIXED_TOPIC};\n"
        "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Таблица: двенадцать времён со схемой (svg), формулой и примерами.\n"
        "const TENSES = " + json.dumps(tenses, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Карточки. opts — варианты, a — правильный, ru — подсказка, say — текст для озвучки.\n"
        "const CARDS = " + json.dumps(CARDS, ensure_ascii=False, indent=1) + ";")
out = (tpl.replace("<!--__GRID__-->", grid).replace("<!--__TRAPS__-->", traps).replace("<!--__MARKERS__-->", markers)
          .replace("<!--__FUTURE__-->", future).replace("<!--__ERRORS__-->", errors).replace("/*__DATA__*/", data))
for n in (180, 192):
    b64 = base64.b64encode((here / "tile" / f"icon-{n}.png").read_bytes()).decode()
    out = out.replace(f"__ICON{n}__", "data:image/png;base64," + b64)
s0 = out.index("<style>"); s1 = out.index("</style>", s0)
out = out[:s0] + re.sub(r"(?<![\w.#-])(\d+(?:\.\d+)?)px", r"calc(\1px*var(--k))", out[s0:s1]) + out[s1:]
assert "__ICON" not in out and "/*__DATA__*/" not in out and "<!--__" not in out
(here / "index.html").write_text(out)
live = pathlib.Path("artifact-files/17f35b77-ec05-4e16-a5e6-516e7ef5f8d8/index.html").read_text()
(here / "preview.html").write_text(live[:live.index("<body>") + 6] + "\n" + out + "\n</body></html>")
print("ok", len(out), "bytes;", len(TOPICS), "topics;", len(CARDS), "cards;", len(TENSES), "tenses")
