import re, json, base64, html, pathlib, sys
here = pathlib.Path("toing")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, TO_GROUPS, ING_GROUPS, DUAL, ERRORS, SORT_TOPIC, MIXED_TOPIC
tpl = (here / "template.html").read_text()
esc = html.escape
def verbs_html(vs):
    return ", ".join(esc(w.rstrip("*")) + ('<sup aria-label="меняет смысл">*</sup>' if w.endswith("*") else "") for w in vs)
def groups_html(gs):
    return "\n".join(f'          <div class="grp-row"><p class="grp-name">{esc(g["ru"])}</p><p class="grp-verbs" lang="en">{verbs_html(g["verbs"])}</p></div>' for g in gs)
dual = "\n".join(
    f'            <tr><th scope="row" lang="en">{esc(v)}</th>'
    f'<td><span class="st" lang="en">{esc(s1)}</span><small>{esc(s2)}</small></td>'
    f'<td><span class="pr" lang="en">{esc(p1)}</span><small>{esc(p2)}</small></td></tr>'
    for v, s1, s2, p1, p2 in DUAL)
errors = "\n".join(
    f'          <li class="err"><span class="sr">Неверно:</span> <s lang="en">{esc(w)}</s> <span class="arr" aria-hidden="true">→</span> '
    f'<span class="sr">верно:</span> <span class="good" lang="en">{esc(r)}</span></li>'
    for w, r in ERRORS)
data = ("// ——— Темы: правило и примеры. {…} — форма с to (синий), […] — форма на -ing (оранжевый).\n"
        f"const SORT_TOPIC = {SORT_TOPIC};\nconst MIXED_TOPIC = {MIXED_TOPIC};\n"
        "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Карточки. opts — варианты, a — правильный, also — тоже допустимые с пояснением, ru — перевод глагола (тема 11).\n"
        "const CARDS = " + json.dumps(CARDS, ensure_ascii=False, indent=1) + ";")
out = (tpl.replace("<!--__TO__-->", groups_html(TO_GROUPS)).replace("<!--__ING__-->", groups_html(ING_GROUPS))
          .replace("<!--__DUAL__-->", dual).replace("<!--__ERRORS__-->", errors).replace("/*__DATA__*/", data))
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
