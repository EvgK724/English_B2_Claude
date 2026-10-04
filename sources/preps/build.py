import re, json, base64, html, pathlib, sys
here = pathlib.Path("preps")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, GROUPS, GRID, MED, ERRORS, MIXED_TOPIC
tpl = (here / "template.html").read_text()
esc = html.escape
CLS = {"at": "st", "on": "pr", "in": "good"}
def marked(s):
    # […] — предлог, цвет по слову
    out, last = [], 0
    for m in re.finditer(r"\[([^\]]+)\]", s):
        out.append(esc(s[last:m.start()]))
        out.append(f'<span class="{CLS.get(m[1].lower(), "hl")}">{esc(m[1])}</span>')
        last = m.end()
    out.append(esc(s[last:]))
    return "".join(out)
def colored(phrase):
    # «at the door» → предлог в цвет своей колонки
    w, rest = phrase.split(" ", 1)
    return f'<span class="{CLS[w]}">{esc(w)}</span> {esc(rest)}'
grid = "\n".join(
    f'            <tr><th scope="row">{label}</th>' + "".join(f'<td lang="en">{colored(p)}</td>' for p in GRID[key]) + '</tr>'
    for key, label in [("place", "Где"), ("time", "Когда")])
PLAY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9.5h3.5L12 5.5v13l-4.5-4H4z"/><path d="M15.5 9a4 4 0 0 1 0 6"/></svg>'
med = "\n".join(
    f'        <div class="md"><div><p class="md-en" lang="en">{marked(en)}</p><p class="md-ru">{esc(ru)}</p></div>'
    f'<button class="ex-play mm-play" type="button" data-key="md-{i + 1}" data-text="{esc(say)}" aria-label="Прослушать: {esc(say)}">{PLAY}</button></div>'
    for i, (en, ru, say) in enumerate(MED))
errors = "\n".join(
    f'          <li class="err"><span class="sr">Неверно:</span> <s lang="en">{esc(w)}</s> <span class="arr" aria-hidden="true">→</span> '
    f'<span class="sr">верно:</span> <span class="good" lang="en">{esc(r)}</span><span class="err-note">{esc(note)}</span></li>'
    for w, r, note in ERRORS)
data = ("// ——— Темы по группам: правило и примеры. […] — предлог (at — синий, on — оранжевый, in — зелёный).\n"
        f"const MIXED_TOPIC = {MIXED_TOPIC};\n"
        "const GROUPS = " + json.dumps(GROUPS, ensure_ascii=False) + ";\n"
        "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Карточки. opts — варианты («» — предлог не нужен), a — правильный, ru — перевод (подсказка).\n"
        "const CARDS = " + json.dumps(CARDS, ensure_ascii=False, indent=1) + ";")
out = tpl.replace("<!--__GRID__-->", grid).replace("<!--__MED__-->", med).replace("<!--__ERRORS__-->", errors).replace("/*__DATA__*/", data)
for n in (180, 192):
    b64 = base64.b64encode((here / "tile" / f"icon-{n}.png").read_bytes()).decode()
    out = out.replace(f"__ICON{n}__", "data:image/png;base64," + b64)
s0 = out.index("<style>"); s1 = out.index("</style>", s0)
out = out[:s0] + re.sub(r"(?<![\w.#-])(\d+(?:\.\d+)?)px", r"calc(\1px*var(--k))", out[s0:s1]) + out[s1:]
assert "__ICON" not in out and "/*__DATA__*/" not in out and "<!--__" not in out
(here / "index.html").write_text(out)
live = pathlib.Path("artifact-files/17f35b77-ec05-4e16-a5e6-516e7ef5f8d8/index.html").read_text()
(here / "preview.html").write_text(live[:live.index("<body>") + 6] + "\n" + out + "\n</body></html>")
print("ok", len(out), "bytes;", len(TOPICS), "topics;", len(CARDS), "cards")
