import re, json, base64, html, pathlib, sys
here = pathlib.Path("twotoo")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, WORDS, ERRORS, MIXED_TOPIC
tpl = (here / "template.html").read_text()
esc = html.escape
PLAY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9.5h3.5L12 5.5v13l-4.5-4H4z"/><path d="M15.5 9a4 4 0 0 1 0 6"/></svg>'
words = "\n".join(
    f'      <div class="mm"><div class="wb">'
    f'<p class="wb-h"><span class="wb-w {w["cls"]}" lang="en">{esc(w["w"])}</span><span class="wb-s">{esc(w["sound"])} · {esc(w["mean"])}</span></p>'
    f'<button class="ex-play mm-play" type="button" data-key="w-{esc(w["w"])}" data-text="{esc(w["say"])}" aria-label="Прослушать примеры: {esc(w["w"])}">{PLAY}</button>'
    f'<p class="wb-ex" lang="en">{" · ".join(esc(e) for e in w["ex"])}</p></div>'
    f'<p class="mm-note">{esc(w["tip"]).replace(" → ", "&nbsp;→ ")}</p></div>'
    for w in WORDS)
errors = "\n".join(
    f'          <li class="err"><span class="sr">Неверно:</span> <s lang="en">{esc(w)}</s> <span class="arr" aria-hidden="true">→</span> '
    f'<span class="sr">верно:</span> <span class="good" lang="en">{esc(r)}</span><span class="err-note">{esc(note)}</span></li>'
    for w, r, note in ERRORS)
data = ("// ——— Темы: правило и примеры. {…} — two (синий), _…_ — too (оранжевый), |…| — to (зелёный).\n"
        f"const MIXED_TOPIC = {MIXED_TOPIC};\n"
        "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Карточки. opts — варианты («» — ничего не нужно), a — правильный, ru — перевод (подсказка).\n"
        "const CARDS = " + json.dumps(CARDS, ensure_ascii=False, indent=1) + ";")
out = tpl.replace("<!--__WORDS__-->", words).replace("<!--__ERRORS__-->", errors).replace("/*__DATA__*/", data)
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
