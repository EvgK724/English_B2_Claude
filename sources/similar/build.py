import re, json, base64, html, pathlib, sys
here = pathlib.Path("similar")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, GROUPS, KEYS, WORDS, ERRORS, MIXED_TOPIC
tpl = (here / "template.html").read_text()
esc = html.escape
nb = lambda s: esc(s).replace(" — ", "&nbsp;— ")
# сочетания не рвутся посередине: перенос только между ними
keep = lambda pat: "&nbsp;· ".join(esc(x).replace(" ", "&nbsp;") for x in pat.split(" · "))

keys = "\n".join(
    f'          <li><span class="sn">{i + 1}</span><div><p class="s-t"><b>{esc(g)}</b></p><dl class="kv">'
    + "".join(f'<dt lang="en">{esc(w)}</dt><dd>{esc(ru)}</dd>' for w, ru in rows) + '</dl></div></li>'
    for i, (g, rows) in enumerate(KEYS))

PLAY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9.5h3.5L12 5.5v13l-4.5-4H4z"/><path d="M15.5 9a4 4 0 0 1 0 6"/></svg>'
def caps(s):
    return re.sub(r"(^|[.!?]\s+)([a-z])", lambda m: m.group(1) + m.group(2).upper(), s)
TITLES = {"look": "Смотреть", "say": "Говорить", "trip": "Поездки", "learn": "Учиться и знать"}
words, n = [], 0
for g, rows in WORDS.items():
    words.append(f'      <h2 class="lbl">{TITLES[g]}</h2>\n      <div class="mx-wrap">')
    for w, ru, pat, say in rows:
        n += 1
        words.append(
            f'        <div class="md"><div><p class="wd-w"><span class="pr" lang="en">{esc(w)}</span> <span class="wd-ru">{nb(ru)}</span></p>'
            f'<p class="wd-p" lang="en">{keep(pat)}</p></div>'
            f'<button class="ex-play mm-play" type="button" data-key="wd-{n}" data-text="{esc(caps(say))}" aria-label="Прослушать: {esc(w)}">{PLAY}</button></div>')
    words.append('      </div>')
words = "\n".join(words)

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
out = (tpl.replace("<!--__KEYS__-->", keys).replace("<!--__WORDS__-->", words)
          .replace("<!--__ERRORS__-->", errors).replace("/*__DATA__*/", data))
for size in (180, 192):
    b64 = base64.b64encode((here / "tile" / f"icon-{size}.png").read_bytes()).decode()
    out = out.replace(f"__ICON{size}__", "data:image/png;base64," + b64)
s0 = out.index("<style>"); s1 = out.index("</style>", s0)
out = out[:s0] + re.sub(r"(?<![\w.#-])(\d+(?:\.\d+)?)px", r"calc(\1px*var(--k))", out[s0:s1]) + out[s1:]
assert "__ICON" not in out and "/*__DATA__*/" not in out and "<!--__" not in out
# все записи на месте
for k in re.findall(r'data-key="([^"]+)"', out) + [c["id"] for c in CARDS]:
    assert (here / "audio" / f"{k}.mp3").exists(), k
(here / "index.html").write_text(out)
live = pathlib.Path("artifact-files/17f35b77-ec05-4e16-a5e6-516e7ef5f8d8/index.html").read_text()
(here / "preview.html").write_text(live[:live.index("<body>") + 6] + "\n" + out + "\n</body></html>")
print("ok", len(out), "bytes;", len(TOPICS), "topics;", len(CARDS), "cards;", n, "words")
