import re, json, base64, html, pathlib, sys
here = pathlib.Path("stative")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, GROUPS, DUAL
tpl = (here / "template.html").read_text()
esc = html.escape
def verbs_html(v):
    return ", ".join(esc(w.rstrip("*")) + ('<sup aria-label="двойной">*</sup>' if w.endswith("*") else "") for w in [x.strip() for x in v.split(",")])
groups = "\n".join(f'          <div class="grp-row"><p class="grp-name">{esc(g["ru"])}</p><p class="grp-verbs" lang="en">{verbs_html(g["verbs"])}</p></div>' for g in GROUPS)
dual = "\n".join(
    f'            <tr><th scope="row" lang="en">{esc(v)}</th>'
    f'<td><span class="st" lang="en">{esc(s1)}</span><small>{esc(s2)}</small></td>'
    f'<td><span class="pr" lang="en">{esc(p1)}</span><small>{esc(p2)}</small></td></tr>'
    for v, s1, s2, p1, p2 in DUAL)
data = ("// ——— Темы: правило и примеры. {…} — состояние (синий), […] — процесс с -ing (оранжевый).\n"
        "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Карточки. opts — варианты, a — правильный, also — тоже допустимые с пояснением.\n"
        "const CARDS = " + json.dumps(CARDS, ensure_ascii=False, indent=1) + ";")
out = tpl.replace("<!--__GROUPS__-->", groups).replace("<!--__DUAL__-->", dual).replace("/*__DATA__*/", data)
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
