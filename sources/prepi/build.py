import re, json, base64, html, pathlib, sys
here = pathlib.Path("prepi")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, MEANINGS, ERRORS, MIXED_TOPIC
tpl = (here / "template.html").read_text()
esc = html.escape
def marked(s):
    s = esc(s)
    s = re.sub(r"\[([^\]]+)\]", r'<span class="pr">\1</span>', s)
    return re.sub(r"\{([^}]+)\}", r'<span class="st">\1</span>', s)
meanings = "\n".join(
    f'        <div class="mb"><p class="mb-adj">{esc(g["ru"])}</p><ul class="mb-list">'
    + "".join(f'<li><p class="mb-l"><b lang="en">{esc(p)}</b> <span class="mb-ru">— {esc(ru)}</span></p><p class="mb-ex" lang="en">{marked(ex)}</p></li>' for p, ru, ex in g["rows"])
    + '</ul></div>'
    for g in MEANINGS)
errors = "\n".join(
    f'          <li class="err"><span class="sr">Неверно:</span> <s lang="en">{esc(w)}</s> <span class="arr" aria-hidden="true">→</span> '
    f'<span class="sr">верно:</span> <span class="good" lang="en">{esc(r)}</span><span class="err-note">{esc(note)}</span></li>'
    for w, r, note in ERRORS)
data = ("// ——— Темы: правило и примеры. {…} — предлог (синий), […] — форма на -ing (оранжевый).\n"
        f"const MIXED_TOPIC = {MIXED_TOPIC};\n"
        "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Карточки. opts — варианты, a — правильный, also — тоже допустимые, ru — перевод (подсказка).\n"
        "const CARDS = " + json.dumps(CARDS, ensure_ascii=False, indent=1) + ";")
out = tpl.replace("<!--__MEANINGS__-->", meanings).replace("<!--__ERRORS__-->", errors).replace("/*__DATA__*/", data)
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
