import re, json, base64, html, pathlib, sys
here = pathlib.Path("go")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, GROUPS, CONTRAST, PHRASAL, SET, ERRORS, MIXED_TOPIC
tpl = (here / "template.html").read_text()
esc = html.escape
nb = lambda s: esc(s).replace(" — ", "&nbsp;— ")
def marked(s):
    out, last = [], 0
    for m in re.finditer(r"\[([^\]|]+)(?:\|(b))?\]", s):
        out.append(esc(s[last:m.start()]))
        out.append(f'<span class="{"st" if m.group(2) else "pr"}">{esc(m.group(1))}</span>')
        last = m.end()
    out.append(esc(s[last:]))
    return "".join(out)
def plain(en):
    s = re.sub(r"\[([^\]|]+)(?:\|b)?\]", r"\1", en)
    return s + ("" if s.rstrip()[-1:] in ".!?" else ".")
cap = lambda s: s[:1].upper() + s[1:]
def gocolor(p):
    # go в сочетании — оранжевым, остальное как есть; сочетание не рвём
    h = esc(p).replace(" ", "&nbsp;")
    return re.sub(r"\b(go|goes|going)\b", r'<span class="pr">\1</span>', h, count=1)

PLAY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9.5h3.5L12 5.5v13l-4.5-4H4z"/><path d="M15.5 9a4 4 0 0 1 0 6"/></svg>'
def btn(key, say, label):
    return f'<button class="ex-play mm-play" type="button" data-key="{key}" data-text="{esc(say)}" aria-label="Прослушать: {esc(label)}">{PLAY}</button>'
contrast = "\n".join(
    f'        <div class="md"><div><p class="cp-en" lang="en">{marked(a[0])}</p><p class="cp-ru">{nb(a[1])}</p>'
    f'<p class="cp-en" lang="en">{marked(b[0])}</p><p class="cp-ru">{nb(b[1])}</p></div>'
    + btn(f"cp-{i + 1}", plain(a[0]) + " " + plain(b[0]), plain(a[0]) + " / " + plain(b[0])) + '</div>'
    for i, (a, b) in enumerate(CONTRAST))
phrasal = "\n".join(
    f'        <div class="md"><div><p class="pw"><span class="pw-w" lang="en">{gocolor(p)}</span> <span class="pw-ru">{nb(ru)}</span></p>'
    f'<p class="snd-ex" lang="en">{esc(ex)}</p></div>'
    + btn(f"ph-{i + 1}", cap(p) + ". " + ex, p) + '</div>'
    for i, (p, ru, ex) in enumerate(PHRASAL))
setx = "\n".join(
    f'        <div class="md"><div><p class="pw"><span class="pw-w" lang="en">{gocolor(p)}</span></p><p class="cp-ru">{nb(ru)}</p></div>'
    + btn(f"st-{i + 1}", plain(cap(p)), p) + '</div>'
    for i, (p, ru) in enumerate(SET))
errors = "\n".join(
    f'          <li class="err"><span class="sr">Неверно:</span> <s lang="en">{esc(w)}</s> <span class="arr" aria-hidden="true">→</span> '
    f'<span class="sr">верно:</span> <span class="good" lang="en">{esc(r)}</span><span class="err-note">{nb(note)}</span></li>'
    for w, r, note in ERRORS)
data = ("// ——— Темы по группам: правило и примеры. […] — ключевая часть (оранжевый), [...|b] — без артикля или без to (синий).\n"
        f"const MIXED_TOPIC = {MIXED_TOPIC};\n"
        "const GROUPS = " + json.dumps(GROUPS, ensure_ascii=False) + ";\n"
        "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Карточки. opts — варианты, a — правильный, also — тоже верно (с пояснением), ru — перевод (подсказка).\n"
        "const CARDS = " + json.dumps(CARDS, ensure_ascii=False, indent=1) + ";")
out = (tpl.replace("<!--__CONTRAST__-->", contrast).replace("<!--__PHRASAL__-->", phrasal).replace("<!--__SET__-->", setx)
          .replace("<!--__ERRORS__-->", errors).replace("/*__DATA__*/", data))
for size in (180, 192):
    b64 = base64.b64encode((here / "tile" / f"icon-{size}.png").read_bytes()).decode()
    out = out.replace(f"__ICON{size}__", "data:image/png;base64," + b64)
s0 = out.index("<style>"); s1 = out.index("</style>", s0)
out = out[:s0] + re.sub(r"(?<![\w.#-])(\d+(?:\.\d+)?)px", r"calc(\1px*var(--k))", out[s0:s1]) + out[s1:]
assert "__ICON" not in out and "/*__DATA__*/" not in out and "<!--__" not in out
need = set(re.findall(r'data-key="([^"]+)"', out)) | {c["id"] for c in CARDS} | {f"r{t['n']}-{i + 1}" for t in TOPICS for i in range(len(t["ex"]))}
missing = [k for k in need if not (here / "audio" / f"{k}.mp3").exists()]
assert not missing, missing
(here / "index.html").write_text(out)
live = pathlib.Path("artifact-files/17f35b77-ec05-4e16-a5e6-516e7ef5f8d8/index.html").read_text()
(here / "preview.html").write_text(live[:live.index("<body>") + 6] + "\n" + out + "\n</body></html>")
print("ok", len(out), "bytes;", len(TOPICS), "topics;", len(CARDS), "cards;", len(need), "clips used")
