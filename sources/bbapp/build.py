import re, base64, pathlib, sys
here = pathlib.Path("bbapp")
src = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "artifact-files/63c4fa4f-95e7-4be6-812a-689d838c98c5/index.html").read_text()
tpl = (here / "template.html").read_text()
MARK = "// НОВАЯ КАРТОЧКА ВСТАВЛЯЕТСЯ ВЫШЕ ЭТОЙ СТРОКИ"
start = src.index("const CARDS = [")
end = src.index("];", src.index(MARK, start)) + 2
block = src[start:end]
assert block.count(MARK) == 1
# дата добавления у сегодняшних фраз
for cid in ("its-all-good", "in-danger"):
    old = f'id: "{cid}",\n    au: 1,\n'
    if old in block and f'id: "{cid}",\n    au: 1,\n    added:' not in block:
        block = block.replace(old, old + '    added: "2026-09-23",\n', 1)
assert block.count('added: "2026-09-23"') == 2
out = tpl.replace("/*__CARDS__*/", block)
for n in (180, 192):
    b64 = base64.b64encode((here / "tile" / f"icon-{n}.png").read_bytes()).decode()
    out = out.replace(f"__ICON{n}__", "data:image/png;base64," + b64)
s0 = out.index("<style>"); s1 = out.index("</style>", s0)
out = out[:s0] + re.sub(r"(?<![\w.#-])(\d+(?:\.\d+)?)px", r"calc(\1px*var(--k))", out[s0:s1]) + out[s1:]
assert "__ICON" not in out and "/*__CARDS__*/" not in out and out.count(MARK) == 1
assert "<body>" not in out and "</body></html>" not in out
(here / "index.html").write_text(out)
head = src[:src.index("<body>") + len("<body>")]
(here / "preview.html").write_text(head + "\n" + out + "\n</body></html>")
print("ok", len(out), "bytes;", block.count("\n    id:"), "cards")
