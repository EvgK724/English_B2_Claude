import re, json, base64, html, pathlib, sys
here = pathlib.Path("gonebeen")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, FORMS, EXTRA, ERRORS, MIXED_TOPIC
tpl = (here / "template.html").read_text()
esc = html.escape
def marked(s):
    s = esc(s)
    s = re.sub(r"\[([^\]]+)\]", r'<span class="pr">\1</span>', s)
    s = re.sub(r"\{([^}]+)\}", r'<span class="st">\1</span>', s)
    return re.sub(r"\|([^|]+)\|", r'<span class="good">\1</span>', s)
ICONS = {
    "oneway": '<circle cx="6" cy="15" r="4" fill="currentColor"/><path d="M13 15h30M36 8l8 7-8 7" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>',
    "round": '<circle cx="6" cy="21" r="4" fill="currentColor"/><path d="M13 21h24a6.5 6.5 0 0 0 0-13H14M20 2l-7 6 7 6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>',
    "inside": '<rect x="12" y="3" width="30" height="24" rx="5" fill="none" stroke="currentColor" stroke-width="2.4"/><circle cx="27" cy="15" r="4.5" fill="currentColor"/>',
}
forms = "\n".join(
    f'        <div class="fm-row"><span class="fm-ic {cls}" aria-hidden="true"><svg viewBox="0 0 52 30">{ICONS[ic]}</svg></span>'
    f'<div><p class="fm-f {cls}" lang="en">{esc(f)}</p><p class="fm-ru">{esc(ru)}</p><p class="fm-ex" lang="en">{esc(ex)}</p></div></div>'
    for f, cls, ic, ru, ex in FORMS)
extra = "\n".join(
    f'        <div class="bw-row"><p class="bw-t">{esc(t)}</p>'
    + (f'<p class="bw-ex" lang="en">{marked(ex)}</p>' if ex else "")
    + f'<p class="bw-ru">{esc(ru)}</p></div>'
    for t, ex, ru in EXTRA)
errors = "\n".join(
    f'          <li class="err"><span class="sr">Неверно:</span> <s lang="en">{esc(w)}</s> <span class="arr" aria-hidden="true">→</span> '
    f'<span class="sr">верно:</span> <span class="good" lang="en">{esc(r)}</span><span class="err-note">{esc(note)}</span></li>'
    for w, r, note in ERRORS)
data = ("// ——— Темы: правило и примеры. […] — gone (оранжевый), {…} — been to (синий), |…| — been in / been at (зелёный).\n"
        f"const MIXED_TOPIC = {MIXED_TOPIC};\n"
        "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Карточки. opts — варианты, a — правильный.\n"
        "const CARDS = " + json.dumps(CARDS, ensure_ascii=False, indent=1) + ";")
out = (tpl.replace("<!--__FORMS__-->", forms).replace("<!--__EXTRA__-->", extra)
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
