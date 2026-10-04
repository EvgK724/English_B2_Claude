import re, json, base64, html, pathlib, sys
here = pathlib.Path("thereit")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, PAIRS, IT_USES, THERE_FORMS, ERRORS, MIXED_TOPIC
tpl = (here / "template.html").read_text()
esc = html.escape
def marked(s):
    s = esc(s)
    s = re.sub(r"\{([^}]+)\}", r'<span class="st">\1</span>', s)
    return re.sub(r"\[([^\]]+)\]", r'<span class="pr">\1</span>', s)
pairs = "\n".join(
    f'            <tr><td><p class="dl" lang="en">{marked(a)}</p><small>{esc(ra)}</small></td>'
    f'<td><p class="dl" lang="en">{marked(b)}</p><small>{esc(rb)}</small></td></tr>'
    for a, b, ra, rb in PAIRS)
ituses = "\n".join(f'        <div class="bw-row"><p class="bw-t">{esc(k)}</p><p class="bw-ex" lang="en">{marked(ex)}</p></div>' for k, ex in IT_USES)
forms = "\n".join(f'        <div class="bw-row"><p class="bw-t">{esc(k)}</p><p class="bw-ex st" lang="en">{esc(ex)}</p></div>' for k, ex in THERE_FORMS)
errors = "\n".join(
    f'          <li class="err"><span class="sr">Неверно:</span> <s lang="en">{esc(w)}</s> <span class="arr" aria-hidden="true">→</span> '
    f'<span class="sr">верно:</span> <span class="good" lang="en">{esc(r)}</span><span class="err-note">{esc(note)}</span></li>'
    for w, r, note in ERRORS)
data = ("// ——— Темы: правило и примеры. {…} — there (синий), […] — it (оранжевый).\n"
        f"const MIXED_TOPIC = {MIXED_TOPIC};\n"
        "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Карточки. opts — варианты, a — правильный, also — тоже допустимые с пояснением.\n"
        "const CARDS = " + json.dumps(CARDS, ensure_ascii=False, indent=1) + ";")
out = (tpl.replace("<!--__PAIRS__-->", pairs).replace("<!--__ITUSES__-->", ituses).replace("<!--__FORMS__-->", forms)
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
