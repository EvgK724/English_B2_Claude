import re, json, base64, html, pathlib, sys
here = pathlib.Path("top10")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, CHECK, BONUS, MIXED_TOPIC
tpl = (here / "template.html").read_text()
esc = html.escape
def nw(s):
    return re.sub(r"(?<![\w>])(-[a-z]+)", r'<span class="nw">\1</span>', s)
def lang_en(s):
    return "" if re.search("[а-яё]", s, re.I) else ' lang="en"'
check = "\n".join(
    f'          <li><button class="ck" type="button" data-n="{i + 1}"><span class="ck-n">{i + 1}</span><span class="ck-t">{nw(esc(t))}</span>'
    f'<span class="ck-ex"{lang_en(ex)}>{esc(ex)}</span></button></li>'
    for i, (t, ex) in enumerate(CHECK))
bonus = "\n".join(
    f'          <li class="err"><span class="sr">Неверно:</span> <s lang="en">{esc(w)}</s> <span class="arr" aria-hidden="true">→</span> '
    f'<span class="sr">верно:</span> <span class="good" lang="en">{esc(r)}</span><span class="err-note">{nw(esc(note))}</span></li>'
    for w, r, note in BONUS)
data = ("// ——— Ошибки: откуда, правило, пары «неверно → верно» (|…| — что исправили), шаг к B2.\n"
        f"const MIXED_TOPIC = {MIXED_TOPIC};\n"
        "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Карточки. opts — варианты, a — правильный, ru — перевод; pick — «выбери правильную фразу», b2 — шаг к B2.\n"
        "const CARDS = " + json.dumps(CARDS, ensure_ascii=False, indent=1) + ";")
out = tpl.replace("<!--__CHECK__-->", check).replace("<!--__BONUS__-->", bonus).replace("/*__DATA__*/", data)
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
