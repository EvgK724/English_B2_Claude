import re, json, base64, pathlib, sys
here = pathlib.Path("kogo")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS
tpl = (here / "template.html").read_text()
data = ("// ——— Темы: правило и примеры. {…} — «кого» (синий), […] — нужная форма (зелёный).\n"
        "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Карточки. opts — варианты (\"\" — ничего не нужно), a — правильный.\n"
        "const CARDS = " + json.dumps(CARDS, ensure_ascii=False, indent=1) + ";")
out = tpl.replace("/*__DATA__*/", data)
for n in (180, 192):
    b64 = base64.b64encode((here / "tile" / f"icon-{n}.png").read_bytes()).decode()
    out = out.replace(f"__ICON{n}__", "data:image/png;base64," + b64)
s0 = out.index("<style>"); s1 = out.index("</style>", s0)
css = re.sub(r"(?<![\w.#-])(\d+(?:\.\d+)?)px", r"calc(\1px*var(--k))", out[s0:s1])
out = out[:s0] + css + out[s1:]
assert "__ICON" not in out and "/*__DATA__*/" not in out
(here / "index.html").write_text(out)
live_head = pathlib.Path("artifact-files/17f35b77-ec05-4e16-a5e6-516e7ef5f8d8/index.html").read_text()
head = live_head[:live_head.index("<body>") + len("<body>")]
(here / "preview.html").write_text(head + "\n" + out + "\n</body></html>")
print("ok", len(out), "bytes;", len(TOPICS), "topics;", len(CARDS), "cards")
