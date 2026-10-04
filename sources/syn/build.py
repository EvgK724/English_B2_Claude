import re, json, base64, html, pathlib, sys
here = pathlib.Path("syn")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, GROUPS, PAIRS, WIN, CARRY, OLD, ALONE, CONTRAST, ERRORS, MIXED_TOPIC
tpl = (here / "template.html").read_text()
esc = html.escape
nb = lambda s: esc(s).replace(" — ", "&nbsp;— ")
def marked(s):
    return re.sub(r"\[([^\]]+)\]", lambda m: f'<span class="pr">{m.group(1)}</span>', esc(s))
def plain(en):
    s = re.sub(r"[\[\]]", "", en)
    return s + ("" if s.rstrip()[-1:] in ".!?" else ".")
def ex(s):
    # сочетания через « · » — каждое целиком, без переноса внутри
    return " · ".join(esc(x).replace(" ", "&nbsp;") for x in s.split(" · "))

def row(w, key, e, ru, cls="", tr=""):
    return (f'            <tr{tr}><th scope="row"><span class="w{cls}" lang="en">{esc(w)}</span><span class="p">{nb(key)}</span></th>'
            f'<td><span class="e" lang="en">{ex(e)}</span><span class="r">{nb(ru)}</span></td></tr>')
pairs = "\n".join(row(*a, tr=' class="pa"') + "\n" + row(*b, cls=" st", tr=' class="pb"') for a, b in PAIRS)
WCLS = {"beat": " st"}
CCLS = {"take": " good", "carry": " st"}
win = "\n".join(row(*r, cls=WCLS.get(r[0], "")) for r in WIN)
carry = "\n".join(row(*r, cls=CCLS.get(r[0], "")) for r in CARRY)

PLAY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9.5h3.5L12 5.5v13l-4.5-4H4z"/><path d="M15.5 9a4 4 0 0 1 0 6"/></svg>'
def btn(key, say, label):
    return f'<button class="ex-play mm-play" type="button" data-key="{key}" data-text="{esc(say)}" aria-label="Прослушать: {esc(label)}">{PLAY}</button>'
def words(pre, items):
    return "\n".join(
        f'        <div class="md"><div><p class="wd-w"><span class="ph pr" lang="en">{esc(w)}</span> <span class="ipa">{esc(ipa)}</span> <span class="wd-ru">{nb(ru)}</span></p>'
        f'<p class="wd-p" lang="en">{ex(colls)}</p></div>' + btn(f"{pre}-{i + 1}", say, w) + '</div>'
        for i, (w, ipa, ru, colls, say) in enumerate(items))
contrast = "\n".join(
    '        <div class="md"><div>' + "".join(f'<p class="cp-en" lang="en">{marked(en)}</p><p class="cp-ru">{nb(ru)}</p>' for en, ru in rows) + '</div>'
    + btn(f"cp-{i + 1}", " ".join(plain(r[0]) for r in rows), " / ".join(plain(r[0]) for r in rows)) + '</div>'
    for i, rows in enumerate(CONTRAST))
errors = "\n".join(
    f'          <li class="err"><span class="sr">Неверно:</span> <s lang="en">{esc(w)}</s> <span class="arr" aria-hidden="true">→</span> '
    f'<span class="sr">верно:</span> <span class="good" lang="en">{esc(r)}</span><span class="err-note">{nb(note)}</span></li>'
    for w, r, note in ERRORS)
data = ("// ——— Темы по группам: правило и примеры. […] — слово в фокусе (оранжевый).\n"
        f"const MIXED_TOPIC = {MIXED_TOPIC};\n"
        "const GROUPS = " + json.dumps(GROUPS, ensure_ascii=False) + ";\n"
        "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Карточки. opts — варианты, a — правильный, also — тоже верно (с пояснением), ru — перевод (подсказка).\n"
        "const CARDS = " + json.dumps(CARDS, ensure_ascii=False, indent=1) + ";")
out = (tpl.replace("<!--__PAIRS__-->", pairs).replace("<!--__WIN__-->", win).replace("<!--__CARRY__-->", carry)
          .replace("<!--__OLD__-->", words("mo", OLD)).replace("<!--__ALONE__-->", words("ma", ALONE))
          .replace("<!--__CONTRAST__-->", contrast).replace("<!--__ERRORS__-->", errors).replace("/*__DATA__*/", data))
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
