import re, json, base64, html, pathlib, sys
here = pathlib.Path("life")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, GROUPS, SOUNDS, EXPR, ERRORS, MIXED_TOPIC
tpl = (here / "template.html").read_text()
esc = html.escape
nb = lambda s: esc(s).replace(" — ", "&nbsp;— ")
def marked(s):
    return re.sub(r"\[([^\]]+)\]", lambda m: f'<span class="pr">{m.group(1)}</span>', esc(s).replace(" ", "&nbsp;"))

PLAY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9.5h3.5L12 5.5v13l-4.5-4H4z"/><path d="M15.5 9a4 4 0 0 1 0 6"/></svg>'
def row(key, head, ru, ex, say, label):
    return (f'        <div class="md"><div><p class="pw">{head} <span class="pw-ru">{nb(ru)}</span></p>'
            f'<p class="snd-ex" lang="en">{esc(ex)}</p></div>'
            f'<button class="ex-play mm-play" type="button" data-key="{key}" data-text="{esc(say)}" aria-label="Прослушать: {esc(label)}">{PLAY}</button></div>')
sounds = "\n".join(row(f"sd-{i + 1}", f'<span class="pw-w pr" lang="en">{esc(w)}</span> <span class="ipa">{esc(ipa)}</span>', ru, ex, say, f"{w} {ipa}")
                   for i, (w, ipa, ru, ex, say) in enumerate(SOUNDS))
expr = "\n".join(row(f"ex-{i + 1}", f'<span class="pw-w" lang="en">{marked(p)}</span>', ru, ex, say, re.sub(r"[\[\]]", "", p))
                 for i, (p, ru, ex, say) in enumerate(EXPR))
errors = "\n".join(
    f'          <li class="err"><span class="sr">Неверно:</span> <s lang="en">{esc(w)}</s> <span class="arr" aria-hidden="true">→</span> '
    f'<span class="sr">верно:</span> <span class="good" lang="en">{esc(r)}</span><span class="err-note">{nb(note)}</span></li>'
    for w, r, note in ERRORS)
data = ("// ——— Темы по группам: правило и примеры. […] — слово в фокусе (оранжевый).\n"
        f"const MIXED_TOPIC = {MIXED_TOPIC};\n"
        "const GROUPS = " + json.dumps(GROUPS, ensure_ascii=False) + ";\n"
        "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Карточки. opts — варианты, a — правильный, ru — перевод (подсказка).\n"
        "const CARDS = " + json.dumps(CARDS, ensure_ascii=False, indent=1) + ";")
out = (tpl.replace("<!--__SOUNDS__-->", sounds).replace("<!--__EXPR__-->", expr)
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
