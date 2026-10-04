import re, base64, pathlib, sys
here = pathlib.Path("phrasal")
src = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "artifact-files/17f35b77-ec05-4e16-a5e6-516e7ef5f8d8/index.html").read_text()
tpl = (here / "template.html").read_text()
MARK = "// НОВАЯ КАРТОЧКА ВСТАВЛЯЕТСЯ ВЫШЕ ЭТОЙ СТРОКИ"
start = src.index("const CARDS = [")
mpos = src.index(MARK, start)
end = src.index("];", mpos) + 2
block = src[start:end]
assert block.count(MARK) == 1
# дата добавления у сегодняшней карточки
if 'id: "rule-out"' in block and "added:" not in block.split('id: "rule-out"')[1].split("}")[0]:
    block = block.replace('id: "rule-out",\n    au: 1,\n', 'id: "rule-out",\n    au: 1,\n    added: "2026-09-23",\n', 1)
assert 'added: "2026-09-23"' in block
out = tpl.replace("/*__CARDS__*/", block)
for n in (180, 192):
    b64 = base64.b64encode((here / "tile" / f"icon-{n}.png").read_bytes()).decode()
    out = out.replace(f"__ICON{n}__", "data:image/png;base64," + b64)
# масштаб: px → calc(px * --k) только в первом блоке стилей
s0 = out.index("<style>"); s1 = out.index("</style>", s0)
css = out[s0:s1]
css = re.sub(r"(?<![\w.#-])(\d+(?:\.\d+)?)px", r"calc(\1px*var(--k))", css)
out = out[:s0] + css + out[s1:]
assert "__ICON" not in out and "/*__CARDS__*/" not in out
(here / "index.html").write_text(out)
print("ok", len(out), "bytes;", block.count("id:"), "cards")
