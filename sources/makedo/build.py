import re, json, base64, html, pathlib, sys
here = pathlib.Path("makedo")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, GROUPS, GRID, SPORT, ALWAYS_MAKE, ALWAYS_DO, NEITHER, ERRORS, MIXED_TOPIC
sys.path.insert(0, str(here))
from clips import phrase
tpl = (here / "template.html").read_text()
esc = html.escape
nb = lambda s: esc(s).replace(" — ", "&nbsp;— ")
CLS = {}
for cls, forms in (("st", "make makes made making go goes went gone going"), ("pr", "do does did done doing"), ("good", "play plays played playing")):
    for w in forms.split(): CLS[w] = cls
def colored(p, keep=False):
    # первое слово — глагол в цвет, остальное как есть; keep — не рвать сочетание
    w, rest = p.split(" ", 1)
    rest = esc(rest).replace(" ", "&nbsp;") if keep else esc(rest)
    return f'<span class="{CLS.get(w, "hl")}">{esc(w)}</span>{"&nbsp;" if keep else " "}{rest}'

grid = "\n".join(
    f'            <tr><th scope="row">{esc(label)}</th><td lang="en">{colored(m)}</td><td lang="en">{colored(d)}</td></tr>'
    for label, m, d in GRID)
sport = "\n".join('            <tr>' + "".join(f'<td lang="en">{esc(w)}</td>' for w in row) + '</tr>' for row in SPORT)

PLAY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9.5h3.5L12 5.5v13l-4.5-4H4z"/><path d="M15.5 9a4 4 0 0 1 0 6"/></svg>'
def rows(pre, items):
    return "\n".join(
        f'        <div class="md"><div><p class="wd-w"><span class="ph" lang="en">{colored(p, keep=True)}</span> <span class="wd-ru">{nb(ru)}</span></p>'
        f'<p class="wd-p" lang="en">{esc(ex)}</p></div>'
        f'<button class="ex-play mm-play" type="button" data-key="{pre}-{i + 1}" data-text="{esc(phrase(p) + " " + ex)}" aria-label="Прослушать: {esc(p)}">{PLAY}</button></div>'
        for i, (p, ru, ex) in enumerate(items))

errors = "\n".join(
    f'          <li class="err"><span class="sr">Неверно:</span> <s lang="en">{esc(w)}</s> <span class="arr" aria-hidden="true">→</span> '
    f'<span class="sr">верно:</span> <span class="good" lang="en">{esc(r)}</span><span class="err-note">{nb(note)}</span></li>'
    for w, r, note in ERRORS)
data = ("// ——— Темы по группам: правило и примеры. […] — глагол (make и go — синий, do — оранжевый, play — зелёный).\n"
        f"const MIXED_TOPIC = {MIXED_TOPIC};\n"
        "const GROUPS = " + json.dumps(GROUPS, ensure_ascii=False) + ";\n"
        "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Карточки. opts — варианты, a — правильный, ru — перевод (подсказка).\n"
        "const CARDS = " + json.dumps(CARDS, ensure_ascii=False, indent=1) + ";")
out = (tpl.replace("<!--__GRID__-->", grid).replace("<!--__SPORT__-->", sport)
          .replace("<!--__MAKE__-->", rows("rm", ALWAYS_MAKE)).replace("<!--__DO__-->", rows("rd", ALWAYS_DO))
          .replace("<!--__NEITHER__-->", rows("rt", NEITHER))
          .replace("<!--__ERRORS__-->", errors).replace("/*__DATA__*/", data))
for size in (180, 192):
    b64 = base64.b64encode((here / "tile" / f"icon-{size}.png").read_bytes()).decode()
    out = out.replace(f"__ICON{size}__", "data:image/png;base64," + b64)
s0 = out.index("<style>"); s1 = out.index("</style>", s0)
out = out[:s0] + re.sub(r"(?<![\w.#-])(\d+(?:\.\d+)?)px", r"calc(\1px*var(--k))", out[s0:s1]) + out[s1:]
assert "__ICON" not in out and "/*__DATA__*/" not in out and "<!--__" not in out
# все записи на месте
need = set(re.findall(r'data-key="([^"]+)"', out)) | {c["id"] for c in CARDS} | {f"r{t['n']}-{i + 1}" for t in TOPICS for i in range(len(t["ex"]))}
missing = [k for k in need if not (here / "audio" / f"{k}.mp3").exists()]
assert not missing, missing
(here / "index.html").write_text(out)
live = pathlib.Path("artifact-files/17f35b77-ec05-4e16-a5e6-516e7ef5f8d8/index.html").read_text()
(here / "preview.html").write_text(live[:live.index("<body>") + 6] + "\n" + out + "\n</body></html>")
print("ok", len(out), "bytes;", len(TOPICS), "topics;", len(CARDS), "cards;", len(need), "clips used")
