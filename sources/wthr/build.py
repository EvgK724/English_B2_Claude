import re, json, base64, html, pathlib, sys
here = pathlib.Path("wthr")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, GROUPS, STRENGTH, CHANGES, SUN, RAIN, FOG, COLD, WIND, STORM, CONTRAST, ERRORS, MIXED_TOPIC
from clips import say
tpl = (here / "template.html").read_text()
esc = html.escape
nb = lambda s: esc(s).replace(" — ", "&nbsp;— ")
def marked(s):
    return re.sub(r"\[([^\]]+)\]", lambda m: f'<span class="pr">{m.group(1)}</span>', esc(s))
def plain(en):
    s = re.sub(r"[\[\]]", "", en)
    return s + ("" if s.rstrip()[-1:] in ".!?" else ".")
def keep(s):
    # каждое сочетание целиком; переносить можно только между ними
    return re.sub(r" (·|↔) ", r" \1 ", " · ".join(esc(x).replace(" ", "&nbsp;") for x in s.split(" · ")).replace("&nbsp;↔&nbsp;", " ↔ "))
def note(n):
    if not n: return ""
    if " — " in n:
        ru, en = n.split(" — ", 1)
        return f'<small>{esc(ru)}&nbsp;— <i lang="en">{esc(en)}</i></small>'
    if n.startswith("не "):
        return f'<small>не <i lang="en">{esc(n[3:])}</i></small>'
    return f"<small>{esc(n)}</small>"
def head(w, ru):
    return f'<th scope="row"><span lang="en">{esc(w)}</span><small>{esc(ru)}</small></th>'
def lines(v, cls):
    return "".join(f'<span class="f {cls}" lang="en">{esc(x)}</span>' for x in v.split(" · "))
strength = "\n".join(
    f'            <tr>{head(w, ru)}<td>{lines(s_, "pr")}{note(n1)}</td><td>{lines(w_, "st")}{note(n2)}</td></tr>'
    for w, ru, s_, n1, w_, n2 in STRENGTH)
def two(v, cls):
    first, *rest = v.split(" · ")
    return f'<span class="f {cls}" lang="en">{esc(first)}</span>' + "".join(f'<i lang="en">{esc(r)}</i>' for r in rest)
changes = "\n".join(f'            <tr>{head(w, ru)}<td>{two(worse, "pr")}</td><td>{two(better, "st")}</td></tr>' for w, ru, worse, better in CHANGES)

PLAY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9.5h3.5L12 5.5v13l-4.5-4H4z"/><path d="M15.5 9a4 4 0 0 1 0 6"/></svg>'
def btn(key, text, label):
    return f'<button class="ex-play mm-play" type="button" data-key="{key}" data-text="{esc(text)}" aria-label="Прослушать: {esc(label)}">{PLAY}</button>'
def rows(pre, items):
    return "\n".join(
        f'        <div class="md"><div><p class="wd-w"><span class="ph pr" lang="en">{keep(p)}</span> <span class="wd-ru">{nb(ru)}</span></p>'
        f'<p class="wd-p" lang="en">{esc(ex)}</p></div>' + btn(f"{pre}-{i + 1}", say(p, ex), p) + '</div>'
        for i, (p, ru, ex) in enumerate(items))
contrast = "\n".join(
    '        <div class="md"><div>' + "".join(f'<p class="cp-en" lang="en">{marked(en)}</p><p class="cp-ru">{nb(ru)}</p>' for en, ru in rows_) + '</div>'
    + btn(f"cp-{i + 1}", " ".join(plain(r[0]) for r in rows_), " / ".join(plain(r[0]) for r in rows_)) + '</div>'
    for i, rows_ in enumerate(CONTRAST))
errors = "\n".join(
    f'          <li class="err"><span class="sr">Неверно:</span> <s lang="en">{esc(w)}</s> <span class="arr" aria-hidden="true">→</span> '
    f'<span class="sr">верно:</span> <span class="good" lang="en">{esc(r)}</span><span class="err-note">{nb(note_)}</span></li>'
    for w, r, note_ in ERRORS)
data = ("// ——— Темы по группам: правило и примеры. […] — сочетание в фокусе (оранжевый).\n"
        f"const MIXED_TOPIC = {MIXED_TOPIC};\n"
        "const GROUPS = " + json.dumps(GROUPS, ensure_ascii=False) + ";\n"
        "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Карточки. opts — варианты, a — правильный, also — тоже верно (с пояснением), ru — перевод (подсказка).\n"
        "const CARDS = " + json.dumps(CARDS, ensure_ascii=False, indent=1) + ";")
out = tpl.replace("<!--__STRENGTH__-->", strength).replace("<!--__CHANGES__-->", changes)
for key, pre, items in (("SUN", "ms", SUN), ("RAIN", "mr", RAIN), ("FOG", "mf", FOG), ("COLD", "mc", COLD), ("WIND", "mw", WIND), ("STORM", "mx", STORM)):
    out = out.replace(f"<!--__{key}__-->", rows(pre, items))
out = out.replace("<!--__CONTRAST__-->", contrast).replace("<!--__ERRORS__-->", errors).replace("/*__DATA__*/", data)
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
