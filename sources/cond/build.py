import re, json, base64, html, pathlib, sys
here = pathlib.Path("cond")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, TYPES, RUS_BY, OTHER, WISH, ERRORS, MIXED_TOPIC
tpl = (here / "template.html").read_text()
esc = html.escape
def marked(s):
    s = esc(s)
    s = re.sub(r"\{([^}]+)\}", r'<span class="st">\1</span>', s)
    return re.sub(r"\[([^\]]+)\]", r'<span class="pr">\1</span>', s)
types = "\n".join(
    f'        <div class="ty"><p class="ty-n">{esc(n)}</p><div><p class="ty-when">{esc(when)}</p>'
    f'<p class="ty-f" lang="en"><span class="st">{esc(fi)}</span> <i>→</i> <span class="pr">{esc(fm)}</span></p>'
    f'<p class="ty-ex" lang="en">{marked(ex)}</p><p class="ty-ru">{esc(ru)}</p></div></div>'
    for n, when, fi, fm, ex, ru in TYPES)
rusby = "\n".join(
    f'        <div class="rb"><p class="rb-ru">{esc(ru)} <span class="rb-tag">{esc(tag)}</span></p><p class="rb-en" lang="en">{marked(en)}</p></div>'
    for ru, tag, en in RUS_BY)
other = "\n".join(
    f'        <div class="ot"><div><p class="ot-c" lang="en">{esc(c)}</p><p class="ot-ru">{esc(ru)}</p></div>'
    f'<div><p class="ot-ex" lang="en">{marked(ex)}</p>' + (f'<p class="ot-note">{esc(note)}</p>' if note else "") + '</div></div>'
    for c, ru, ex, note in OTHER)
wish = "\n".join(
    f'        <div class="ot"><div><p class="ot-c" lang="en">{esc(c)}</p><p class="ot-ru">{esc(ru)}</p></div><div><p class="ot-ex" lang="en">{marked(ex)}</p></div></div>'
    for c, ru, ex in WISH)
errors = "\n".join(
    f'          <li class="err"><span class="sr">Неверно:</span> <s lang="en">{esc(w)}</s> <span class="arr" aria-hidden="true">→</span> '
    f'<span class="sr">верно:</span> <span class="good" lang="en">{esc(r)}</span><span class="err-note">{esc(note)}</span></li>'
    for w, r, note in ERRORS)
data = ("// ——— Темы: правило и примеры. {…} — часть с if (синий), […] — главная часть (оранжевый).\n"
        f"const MIXED_TOPIC = {MIXED_TOPIC};\n"
        "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Карточки. opts — варианты, a — правильный, ru — русская фраза (подсказка).\n"
        "const CARDS = " + json.dumps(CARDS, ensure_ascii=False, indent=1) + ";")
out = (tpl.replace("<!--__TYPES__-->", types).replace("<!--__RUSBY__-->", rusby).replace("<!--__OTHER__-->", other)
          .replace("<!--__WISH__-->", wish).replace("<!--__ERRORS__-->", errors).replace("/*__DATA__*/", data))
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
