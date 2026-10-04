import re, json, base64, html, pathlib, sys
here = pathlib.Path("into")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, GROUPS, CONTRAST, INTO, ERRORS, MIXED_TOPIC
tpl = (here / "template.html").read_text()
esc = html.escape
nb = lambda s: esc(s).replace(" — ", "&nbsp;— ")
CLS = {"in": "st", "on": "st", "into": "pr", "onto": "pr"}
def marked(s, keep=False):
    out, last = [], 0
    for m in re.finditer(r"\[([^\]]+)\]", s):
        out.append(esc(s[last:m.start()]))
        out.append(f'<span class="{CLS.get(m.group(1).lower(), "hl")}">{esc(m.group(1))}</span>')
        last = m.end()
    out.append(esc(s[last:]))
    h = "".join(out)
    return h.replace(" ", "&nbsp;") if keep else h
def plain(en):
    s = re.sub(r"[\[\]]", "", en)
    return s + ("" if s.rstrip()[-1:] in ".!?" else ".")

PLAY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9.5h3.5L12 5.5v13l-4.5-4H4z"/><path d="M15.5 9a4 4 0 0 1 0 6"/></svg>'
def btn(key, say, label):
    return f'<button class="ex-play mm-play" type="button" data-key="{key}" data-text="{esc(say)}" aria-label="Прослушать: {esc(label)}">{PLAY}</button>'
contrast = "\n".join(
    f'        <div class="md"><div><p class="cp-en" lang="en">{marked(a[0])}</p><p class="cp-ru">{nb(a[1])}</p>'
    f'<p class="cp-en" lang="en">{marked(b[0])}</p><p class="cp-ru">{nb(b[1])}</p></div>'
    + btn(f"cp-{i + 1}", plain(a[0]) + " " + plain(b[0]), plain(a[0]) + " / " + plain(b[0])) + '</div>'
    for i, (a, b) in enumerate(CONTRAST))
into = "\n".join(
    f'        <div class="md"><div><p class="pw"><span class="pw-w" lang="en">{marked(p, keep=True)}</span> <span class="pw-ru">{nb(ru)}</span></p>'
    f'<p class="snd-ex" lang="en">{esc(ex)}</p></div>'
    + btn(f"it-{i + 1}", plain(p)[:1].upper() + plain(p)[1:] + " " + ex, re.sub(r"[\[\]]", "", p)) + '</div>'
    for i, (p, ru, ex) in enumerate(INTO))
errors = "\n".join(
    f'          <li class="err"><span class="sr">Неверно:</span> <s lang="en">{esc(w)}</s> <span class="arr" aria-hidden="true">→</span> '
    f'<span class="sr">верно:</span> <span class="good" lang="en">{esc(r)}</span><span class="err-note">{nb(note)}</span></li>'
    for w, r, note in ERRORS)
data = ("// ——— Темы по группам: правило и примеры. […] — предлог (in, on — синий; into, onto — оранжевый).\n"
        f"const MIXED_TOPIC = {MIXED_TOPIC};\n"
        "const GROUPS = " + json.dumps(GROUPS, ensure_ascii=False) + ";\n"
        "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Карточки. opts — варианты, a — правильный, also — тоже верно (с пояснением), ru — перевод (подсказка).\n"
        "const CARDS = " + json.dumps(CARDS, ensure_ascii=False, indent=1) + ";")
out = (tpl.replace("<!--__CONTRAST__-->", contrast).replace("<!--__INTO__-->", into)
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
