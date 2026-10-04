import re, json, base64, html, pathlib, sys
here = pathlib.Path("passive")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, FORMS, RUS, NO_PASSIVE, ERRORS, MIXED_TOPIC
tpl = (here / "template.html").read_text()
esc = html.escape
def marked(s):
    # {…} — be (синий), _…_ — третья форма (оранжевый), |…| — зелёный
    out, last = [], 0
    for m in re.finditer(r"\{([^}]+)\}|_([^_]+)_|\|([^|]+)\|", s):
        out.append(esc(s[last:m.start()]))
        cls, txt = ("st", m[1]) if m[1] is not None else ("pr", m[2]) if m[2] is not None else ("good", m[3])
        out.append(f'<span class="{cls}">{esc(txt)}</span>')
        last = m.end()
    out.append(esc(s[last:]))
    return "".join(out)
forms = "\n".join(
    f'        <div class="fm" data-i="{i}"><div><p class="fm-t" lang="en">{esc(t)}</p><p class="fm-ru">{esc(ru)}</p></div>'
    f'<p class="fm-be st" lang="en">{esc(be)}</p><p class="fm-v3 pr" lang="en">{esc(v3)}</p></div>'
    for i, (t, ru, be, v3) in enumerate(FORMS))
rus = "\n".join(f'        <div class="rb"><p class="rb-ru">{esc(ru)}</p><p class="rb-en" lang="en">{marked(en)}</p></div>' for ru, en in RUS)
nopass = "\n".join(f'          <div class="np"><span class="np-v" lang="en">{esc(v)}</span><span class="np-ru">{esc(ru)}</span></div>' for v, ru in NO_PASSIVE)
errors = "\n".join(
    f'          <li class="err"><span class="sr">Неверно:</span> <s lang="en">{esc(w)}</s> <span class="arr" aria-hidden="true">→</span> '
    f'<span class="sr">верно:</span> <span class="good" lang="en">{esc(r)}</span><span class="err-note">{esc(note)}</span></li>'
    for w, r, note in ERRORS)
marks = json.loads((here / "forms.json").read_text())
data = ("// ——— Темы: правило и примеры. {…} — be (синий), _…_ — третья форма (оранжевый), |…| — зелёный.\n"
        f"const MIXED_TOPIC = {MIXED_TOPIC};\n"
        "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Формы по временам и секунды, с которых звучит каждая строка в записи «все формы подряд».\n"
        "const FORMS = " + json.dumps(FORMS, ensure_ascii=False) + ";\n"
        "const FORMS_MARKS = " + json.dumps(marks) + ";\n\n"
        "// ——— Карточки. opts — варианты, a — правильный, ru — перевод (подсказка).\n"
        "const CARDS = " + json.dumps(CARDS, ensure_ascii=False, indent=1) + ";")
out = (tpl.replace("<!--__FORMS__-->", forms).replace("<!--__RUS__-->", rus).replace("<!--__NOPASS__-->", nopass)
          .replace("<!--__ERRORS__-->", errors).replace("/*__DATA__*/", data))
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
