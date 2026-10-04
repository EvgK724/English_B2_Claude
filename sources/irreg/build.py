import re, json, base64, html, pathlib, sys
here = pathlib.Path("irreg")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, VERBS, GROUPS, SCHEMES, HINTS, TRAPS, ERRORS, MIXED_TOPIC, scheme
tpl = (here / "template.html").read_text()
esc = html.escape
def nw(s):
    s = s.replace(" → ", "\u00a0→ ")
    return re.sub(r"(?<![\w>])(-[a-z]+)", r'<span class="nw">\1</span>', s)
def marked(s):
    # {…} — вторая форма (синий), _…_ — третья (оранжевый); квадратные скобки — транскрипция
    out, last = [], 0
    for m in re.finditer(r"\{([^}]+)\}|_([^_]+)_", s):
        out.append(nw(esc(s[last:m.start()])))
        out.append(f'<span class="st">{esc(m[1])}</span>' if m[1] is not None else f'<span class="pr">{esc(m[2])}</span>')
        last = m.end()
    out.append(nw(esc(s[last:])))
    return "".join(out)
def triple(a, b, c):
    return f'{esc(a)}\u00a0— <span class="st">{esc(b)}</span>\u00a0— <span class="pr">{esc(c)}</span>'
def plural(n, one, few, many):
    a, b = n % 10, n % 100
    if a == 1 and b != 11: return one
    if 2 <= a <= 4 and not 12 <= b <= 14: return few
    return many
count = {}
for v in VERBS: count[scheme(v)] = count.get(scheme(v), 0) + 1
schemes = "\n".join(
    f'          <li><button class="sch-b" type="button" data-g="{g}"><span class="sch-k"><b>{esc(k)}</b> · {esc(d)}</span>'
    f'<span class="sch-n">{count[g]} {plural(count[g], "глагол", "глагола", "глаголов")}</span>'
    f'<span class="sch-ex" lang="en">{triple(*ex)}</span></button></li>'
    for k, d, ex, g in SCHEMES)
hints = "\n".join(f'        <div class="hn"><p class="hn-k">{nw(esc(k))}</p><p class="hn-t">{marked(t)}</p></div>' for k, t in HINTS)
traps = "\n".join(
    '        <div class="tp">' + "".join(
        f'<div class="tp-r"><p class="tp-f" lang="en">{triple(a, b, c)}</p><p class="tp-ru">{esc(ru)}</p></div>' for a, b, c, ru in grp)
    + '</div>' for grp in TRAPS)
errors = "\n".join(
    f'          <li class="err"><span class="sr">Неверно:</span> <s lang="en">{esc(w)}</s> <span class="arr" aria-hidden="true">→</span> '
    f'<span class="sr">верно:</span> <span class="good" lang="en">{esc(r)}</span><span class="err-note">{esc(note)}</span></li>'
    for w, r, note in ERRORS)
verbs = [{k: v[k] for k in ("t", "v", "v2", "v3", "ru", "note", "say", "alt") if v.get(k)} for v in VERBS]
marks = json.loads((here / "fam.json").read_text())
data = ("// ——— Семьи и темы. В правилах: {…} — вторая форма (синий), _…_ — третья (оранжевый), [ ] — транскрипция.\n"
        f"const MIXED_TOPIC = {MIXED_TOPIC};\n"
        "const GROUPS = " + json.dumps(GROUPS, ensure_ascii=False) + ";\n"
        "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Глаголы: семья (t), три формы, перевод, заметка, текст для озвучки.\n"
        "const VERBS = " + json.dumps(verbs, ensure_ascii=False) .replace('}, {', '},\n {') + ";\n\n"
        "// ——— «Вся семья вслух»: секунда, с которой звучит каждый глагол семьи.\n"
        "const FAM_MARKS = " + json.dumps({int(k): v for k, v in marks.items()}) + ";\n\n"
        "// ——— Карточки. opts — варианты, a — правильный, ru — подсказка, say — текст для озвучки.\n"
        "const CARDS = " + json.dumps(CARDS, ensure_ascii=False, indent=1) + ";")
out = (tpl.replace("<!--__SCHEMES__-->", schemes).replace("<!--__HINTS__-->", hints).replace("<!--__TRAPS__-->", traps)
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
print("ok", len(out), "bytes;", len(TOPICS), "topics;", len(CARDS), "cards;", len(VERBS), "verbs")
