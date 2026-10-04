import re, json, base64, html, pathlib, sys
here = pathlib.Path("pairs")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, GROUPS, PAIRS, ERRORS, MIXED_TOPIC
tpl = (here / "template.html").read_text()
esc = html.escape
nb = lambda s: esc(s).replace(" — ", "&nbsp;— ")
def tip(s):
    # английские слова в подсказке — засечками, чтобы их было видно
    out, last = [], 0
    for m in re.finditer(r"[A-Za-z][A-Za-z'’-]*(?:\s[A-Za-z][A-Za-z'’-]*)*", s):
        out.append(nb(s[last:m.start()]))
        out.append(f'<span class="tl" lang="en">{esc(m.group(0))}</span>')
        last = m.end()
    out.append(nb(s[last:]))
    return "".join(out)

PLAY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9.5h3.5L12 5.5v13l-4.5-4H4z"/><path d="M15.5 9a4 4 0 0 1 0 6"/></svg>'
titles = {t["n"]: t["title"] for t in TOPICS}
rows, cur = [], None
for i, p in enumerate(PAIRS):
    if p["t"] != cur:
        if cur is not None: rows.append("      </div>")
        cur = p["t"]
        rows.append(f'      <h2 class="lbl">{esc(titles[cur])}</h2>\n      <div class="mx-wrap">')
    lines = "".join(
        f'<p class="pw"><span class="pw-w {cls}" lang="en">{esc(word)}</span> <span class="ipa">{esc(ipa)}</span> <span class="pw-ru">{nb(ru)}</span></p>'
        for cls, (word, ipa, ru) in zip(("st", "pr"), p["w"]))
    pair = f'{p["w"][0][0]} — {p["w"][1][0]}'
    rows.append(f'        <div class="md"><div>{lines}<p class="pw-tip">{tip(p["tip"])}</p></div>'
                f'<button class="ex-play mm-play" type="button" data-key="pr-{i + 1}" data-text="{esc(p["say"])}" aria-label="Прослушать: {esc(pair)}">{PLAY}</button></div>')
rows.append("      </div>")

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
out = tpl.replace("<!--__PAIRS__-->", "\n".join(rows)).replace("<!--__ERRORS__-->", errors).replace("/*__DATA__*/", data)
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
print("ok", len(out), "bytes;", len(TOPICS), "topics;", len(CARDS), "cards;", len(PAIRS), "pairs;", len(need), "clips used")
