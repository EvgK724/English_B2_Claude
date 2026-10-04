import re, json, base64, html, pathlib, sys
here = pathlib.Path("adjadv")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, MEMO, ERRORS, MIXED_TOPIC
tpl = (here / "template.html").read_text()
esc = html.escape
def nw(s):
    return re.sub(r"(?<![\w>])(-[a-z]+)", r'<span class="nw">\1</span>', s)
PLAY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9.5h3.5L12 5.5v13l-4.5-4H4z"/><path d="M15.5 9a4 4 0 0 1 0 6"/></svg>'
COLOR = {"adj": "st", "adv": "pr", "both": ""}
boxes = []
for n, g in enumerate(MEMO, 1):
    h = f'        <p class="mm-h"><span class="mm-n">{n}</span>{esc(g["h"])}</p>'
    if g["kind"] == "pairs":
        rows = "\n".join(
            f'        <div class="mm-pair"><p><span lang="en">{esc(a)}</span><small>{esc(ra)}</small></p>'
            f'<p><span class="pr" lang="en">{esc(b)}</span><small>{esc(rb)}</small></p>'
            f'<button class="mm-play" type="button" data-key="mp-{i + 1}" data-text="{esc(a)}, {esc(b)}." aria-label="Прослушать: {esc(a)}, {esc(b)}">{PLAY}</button></div>'
            for i, (a, ra, b, rb) in enumerate(g["pairs"]))
        body = rows
    else:
        cls = COLOR[g["kind"]]
        cells = "".join(f'<p class="mm-w"><span{(" class=" + chr(34) + cls + chr(34)) if cls else ""} lang="en">{esc(w)}</span><small>{esc(ru)}</small></p>' for w, ru in g["words"])
        body = f'        <div class="mm-grid">{cells}</div>'
    note = f'\n        <p class="mm-note">{nw(esc(g["note"]))}</p>' if g["note"] else ""
    boxes.append(f'      <div class="mm">\n{h}\n{body}{note}\n      </div>')
memo = "\n".join(boxes)
errors = "\n".join(
    f'          <li class="err"><span class="sr">Неверно:</span> <s lang="en">{esc(w)}</s> <span class="arr" aria-hidden="true">→</span> '
    f'<span class="sr">верно:</span> <span class="good" lang="en">{esc(r)}</span><span class="err-note">{nw(esc(note))}</span></li>'
    for w, r, note in ERRORS)
data = ("// ——— Темы: правило и примеры. {…} — прилагательное (синий), _…_ — наречие (оранжевый).\n"
        f"const MIXED_TOPIC = {MIXED_TOPIC};\n"
        "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Карточки. opts — варианты, a — правильный, ru — перевод (подсказка), also — тоже верные варианты.\n"
        "const CARDS = " + json.dumps(CARDS, ensure_ascii=False, indent=1) + ";")
out = tpl.replace("<!--__MEMO__-->", memo).replace("<!--__ERRORS__-->", errors).replace("/*__DATA__*/", data)
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
