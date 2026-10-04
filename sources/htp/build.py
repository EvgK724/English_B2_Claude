import re, json, base64, html, pathlib, sys
here = pathlib.Path("htp")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, GROUPS, TABLE, CONTRAST, ERRORS, HAVE, TAKE, PAY, MIXED_TOPIC
tpl = (here / "template.html").read_text()
esc = html.escape
nb = lambda s: esc(s).replace(" — ", "&nbsp;— ")
CLS = {}
for cls, forms in (("pr", "have has had having"), ("st", "take takes took taken taking"), ("good", "pay pays paid paying")):
    for w in forms.split(): CLS[w] = cls
def mcls(t):
    return CLS.get(t.split(" ")[0].lower(), "hl")
def marked(s):
    return re.sub(r"\[([^\]]+)\]", lambda m: f'<span class="{mcls(m.group(1))}">{m.group(1)}</span>', esc(s))
def plain(en):
    s = re.sub(r"[\[\]]", "", en)
    return s + ("" if s.rstrip()[-1:] in ".!?" else ".")
def cap(s):
    return s[:1].upper() + s[1:]
def colored(p):
    # глагол в цвет; внутри вариантов не рвём строку, между вариантами (/) — можно
    w, rest = p.split(" ", 1)
    rest = " / ".join(esc(x).replace(" ", "&nbsp;") for x in rest.split(" / ")).replace("+&nbsp;", "+&nbsp;")
    return f'<span class="{CLS.get(w, "hl")}">{esc(w)}</span>&nbsp;{rest}'

table = "\n".join(
    f'            <tr><th scope="row"><span class="w {mcls(v)}" lang="en">{esc(v)}</span><span class="p">{esc(pat).replace("+ ", "+&nbsp;")}</span></th>'
    f'<td><span class="e" lang="en">{esc(ex)}</span><span class="r">{nb(ru)}</span></td></tr>'
    for v, pat, ex, ru in TABLE)

PLAY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9.5h3.5L12 5.5v13l-4.5-4H4z"/><path d="M15.5 9a4 4 0 0 1 0 6"/></svg>'
def btn(key, say, label):
    return f'<button class="ex-play mm-play" type="button" data-key="{key}" data-text="{esc(say)}" aria-label="Прослушать: {esc(label)}">{PLAY}</button>'
def rows(pre, items):
    return "\n".join(
        f'        <div class="md"><div><p class="wd-w"><span class="ph" lang="en">{colored(p)}</span> <span class="wd-ru">{nb(ru)}</span></p>'
        f'<p class="wd-p" lang="en">{esc(ex)}</p></div>' + btn(f"{pre}-{i + 1}", cap(say) + ". " + ex, p) + '</div>'
        for i, (p, ru, ex, say) in enumerate(items))
contrast = "\n".join(
    '        <div class="md"><div>' + "".join(f'<p class="cp-en" lang="en">{marked(en)}</p><p class="cp-ru">{nb(ru)}</p>' for en, ru in rows_) + '</div>'
    + btn(f"cp-{i + 1}", " ".join(plain(r[0]) for r in rows_), " / ".join(plain(r[0]) for r in rows_)) + '</div>'
    for i, rows_ in enumerate(CONTRAST))
errors = "\n".join(
    f'          <li class="err"><span class="sr">Неверно:</span> <s lang="en">{esc(w)}</s> <span class="arr" aria-hidden="true">→</span> '
    f'<span class="sr">верно:</span> <span class="good" lang="en">{esc(r)}</span><span class="err-note">{nb(note)}</span></li>'
    for w, r, note in ERRORS)
data = ("// ——— Темы по группам: правило и примеры. […] — сочетание (have — оранжевый, take — синий, pay — зелёный).\n"
        f"const MIXED_TOPIC = {MIXED_TOPIC};\n"
        "const GROUPS = " + json.dumps(GROUPS, ensure_ascii=False) + ";\n"
        "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Карточки. opts — варианты, a — правильный, also — тоже верно (с пояснением), ru — перевод (подсказка).\n"
        "const CARDS = " + json.dumps(CARDS, ensure_ascii=False, indent=1) + ";")
out = (tpl.replace("<!--__TABLE__-->", table).replace("<!--__HAVE__-->", rows("mh", HAVE)).replace("<!--__TAKE__-->", rows("mt", TAKE))
          .replace("<!--__PAY__-->", rows("mp", PAY)).replace("<!--__CONTRAST__-->", contrast)
          .replace("<!--__ERRORS__-->", errors).replace("/*__DATA__*/", data))
for size in (180, 192):
    b64 = base64.b64encode((here / "tile" / f"icon-{size}.png").read_bytes()).decode()
    out = out.replace(f"__ICON{size}__", "data:image/png;base64," + b64)
s0 = out.index("<style>"); s1 = out.index("</style>", s0)
out = out[:s0] + re.sub(r"(?<![\w.#-])(\d+(?:\.\d+)?)px", r"calc(\1px*var(--k))", out[s0:s1]) + out[s1:]
assert "__ICON" not in out and "/*__DATA__*/" not in out and "<!--__" not in out
need = set(re.findall(r'data-key="([^"]+)"', out)) | {c["id"] for c in CARDS} | {f"r{t['n']}-{i + 1}" for t in TOPICS for i in range(len(t["ex"]))}
missing = sorted(k for k in need if not (here / "audio" / f"{k}.mp3").exists())
if missing and "--draft" not in sys.argv:
    raise SystemExit(f"нет записей: {len(missing)} — {missing[:8]}")
(here / "index.html").write_text(out)
live = pathlib.Path("artifact-files/17f35b77-ec05-4e16-a5e6-516e7ef5f8d8/index.html").read_text()
(here / "preview.html").write_text(live[:live.index("<body>") + 6] + "\n" + out + "\n</body></html>")
print("ok", len(out), "bytes;", len(TOPICS), "topics;", len(CARDS), "cards;", len(need), "clips used;", len(missing), "missing")
