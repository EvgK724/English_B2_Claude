import re, json, base64, html, pathlib, sys
here = pathlib.Path("tofor")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, TO_GROUPS, FOR_GROUPS, MULTI, BARE, WITH_TO, ERRORS, SORT_TOPIC, MIXED_TOPIC
tpl = (here / "template.html").read_text()
esc = html.escape
def marked(s):
    s = esc(s)
    s = re.sub(r"\{([^}]+)\}", r'<span class="st">\1</span>', s)
    s = re.sub(r"\[([^\]]+)\]", r'<span class="pr">\1</span>', s)
    return re.sub(r"\|([^|]+)\|", r'<span class="good">\1</span>', s)
def verbs_html(vs):
    return ", ".join(esc(w.rstrip("*")) + ('<sup aria-label="и с to, и с for">*</sup>' if w.endswith("*") else "") for w in vs)
def groups_html(gs):
    return "\n".join(f'          <div class="grp-row"><p class="grp-name">{esc(g["ru"])}</p><p class="grp-verbs" lang="en">{verbs_html(g["verbs"])}</p></div>' for g in gs)
multi = "\n".join(
    f'        <div class="mb"><p class="mb-adj" lang="en">{esc(m["verb"])}</p><ul class="mb-list">'
    + "".join(f'<li><b class="{"st" if p == "to" else "pr"}" lang="en">{esc(p)}</b><span class="mb-ru">{esc(ru)}</span><span class="mb-ex" lang="en">{marked(ex)}</span></li>' for p, ru, ex in m["rows"])
    + '</ul></div>'
    for m in MULTI)
bare = "\n".join(
    f'        <div class="bw-row"><p class="bw-t">{esc(t)}</p><p class="bw-ex" lang="en">{marked(ex)}</p><p class="bw-ru">{esc(ru)}</p></div>'
    for t, ex, ru in BARE)
errors = "\n".join(
    f'          <li class="err"><span class="sr">Неверно:</span> <s lang="en">{esc(w)}</s> <span class="arr" aria-hidden="true">→</span> '
    f'<span class="sr">верно:</span> <span class="good" lang="en">{esc(r)}</span><span class="err-note">{esc(note)}</span></li>'
    for w, r, note in ERRORS)
data = ("// ——— Темы: правило и примеры. {…} — to (синий), […] — for (оранжевый), |…| — глагол без to (зелёный).\n"
        f"const SORT_TOPIC = {SORT_TOPIC};\nconst MIXED_TOPIC = {MIXED_TOPIC};\n"
        "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Карточки. opts — варианты, a — правильный, also — тоже допустимые с пояснением, ru — перевод фразы (тема 10).\n"
        "const CARDS = " + json.dumps(CARDS, ensure_ascii=False, indent=1) + ";")
out = (tpl.replace("<!--__TO__-->", groups_html(TO_GROUPS)).replace("<!--__FOR__-->", groups_html(FOR_GROUPS))
          .replace("<!--__MULTI__-->", multi).replace("<!--__BARE__-->", bare).replace("<!--__ERRORS__-->", errors)
          .replace("__WITHTO__", esc(", ".join(WITH_TO))).replace("/*__DATA__*/", data))
for n in (180, 192):
    b64 = base64.b64encode((here / "tile" / f"icon-{n}.png").read_bytes()).decode()
    out = out.replace(f"__ICON{n}__", "data:image/png;base64," + b64)
s0 = out.index("<style>"); s1 = out.index("</style>", s0)
out = out[:s0] + re.sub(r"(?<![\w.#-])(\d+(?:\.\d+)?)px", r"calc(\1px*var(--k))", out[s0:s1]) + out[s1:]
assert "__ICON" not in out and "/*__DATA__*/" not in out and "<!--__" not in out and "__WITHTO__" not in out
(here / "index.html").write_text(out)
live = pathlib.Path("artifact-files/17f35b77-ec05-4e16-a5e6-516e7ef5f8d8/index.html").read_text()
(here / "preview.html").write_text(live[:live.index("<body>") + 6] + "\n" + out + "\n</body></html>")
print("ok", len(out), "bytes;", len(TOPICS), "topics;", len(CARDS), "cards")
