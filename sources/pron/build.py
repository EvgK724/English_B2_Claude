import re, json, base64, html, pathlib, sys
here = pathlib.Path("pron")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, GROUPS, FORMS, RUEN, ERRORS, MIXED_TOPIC
tpl = (here / "template.html").read_text()
esc = html.escape
nb = lambda s: esc(s).replace(" — ", "&nbsp;— ")
CLS = {"s": "hl", "o": "st", "a": "pr", "p": "good", "r": "hl"}
def marked(s):
    out, last = [], 0
    for m in re.finditer(r"\[([^\]|]+)(?:\|([soapr]))?\]", s):
        out.append(esc(s[last:m.start()]))
        out.append(f'<span class="{CLS.get(m.group(2), "pr")}">{esc(m.group(1))}</span>')
        last = m.end()
    out.append(esc(s[last:]))
    return "".join(out)
def plain(en):
    s = re.sub(r"\[([^\]|]+)(?:\|[soapr])?\]", r"\1", en)
    return s + ("" if s.rstrip()[-1:] in ".!?" else ".")

table = "\n".join(
    f'            <tr><td lang="en">{esc(sb)}</td><td class="st" lang="en">{esc(ob)}</td><td class="pr" lang="en">{esc(ad)}</td>'
    + (f'<td class="good" lang="en">{esc(pp)}</td>' if pp != "—" else '<td class="rn" aria-label="нет формы">—</td>') + '</tr>'
    for sb, ob, ad, pp, *_ in FORMS)

PLAY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9.5h3.5L12 5.5v13l-4.5-4H4z"/><path d="M15.5 9a4 4 0 0 1 0 6"/></svg>'
def btn(key, say, label):
    return f'<button class="ex-play mm-play" type="button" data-key="{key}" data-text="{esc(say)}" aria-label="Прослушать: {esc(label)}">{PLAY}</button>'
SEP = ' <span class="sep">·</span> '
forms = "\n".join(
    f'        <div class="md"><div><p class="fm-w" lang="en"><span>{esc(sb)}</span>{SEP}<span class="st">{esc(ob)}</span>{SEP}<span class="pr">{esc(ad)}</span>'
    + (f'{SEP}<span class="good">{esc(pp)}</span>' if pp != "—" else "") + '</p>'
    f'<p class="re" lang="en">{marked(ex)}</p><p class="rn">{nb(ru)}</p></div>'
    + btn(f"fm-{i + 1}", say, f"{sb}, {ob}, {ad}" + (f", {pp}" if pp != "—" else "")) + '</div>'
    for i, (sb, ob, ad, pp, ex, ru, say) in enumerate(FORMS))
ruen = "\n".join(
    f'        <div class="md"><div><p class="rs">{esc(ru)}</p><p class="re" lang="en">{marked(en)}</p><p class="rn">{nb(note)}</p></div>'
    + btn(f"ru-{i + 1}", plain(en), plain(en)) + '</div>'
    for i, (ru, en, note) in enumerate(RUEN))
errors = "\n".join(
    f'          <li class="err"><span class="sr">Неверно:</span> <s lang="en">{esc(w)}</s> <span class="arr" aria-hidden="true">→</span> '
    f'<span class="sr">верно:</span> <span class="good" lang="en">{esc(r)}</span><span class="err-note">{nb(note)}</span></li>'
    for w, r, note in ERRORS)
data = ("// ——— Темы по группам: правило и примеры. [слово|x] — форма (o — кого?, a — чей? + сущ., p — чей? без сущ.).\n"
        f"const MIXED_TOPIC = {MIXED_TOPIC};\n"
        "const GROUPS = " + json.dumps(GROUPS, ensure_ascii=False) + ";\n"
        "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Карточки. opts — варианты, a — правильный, ru — перевод (подсказка).\n"
        "const CARDS = " + json.dumps(CARDS, ensure_ascii=False, indent=1) + ";")
out = (tpl.replace("<!--__TABLE__-->", table).replace("<!--__FORMS__-->", forms).replace("<!--__RUEN__-->", ruen)
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
