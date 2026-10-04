# Собирает оболочку «Английский»: каталог + индекс звука → build/index.html (для публикации)
import json, pathlib
E = pathlib.Path(__file__).resolve().parent
B = E / "build"
cat = json.loads((B / "catalog.json").read_text())
packs = json.loads((B / "packs.json").read_text())
# в оболочку — только то, что нужно для каталога и счётчиков
slim = {"groups": cat["groups"], "apps": []}
for a in cat["apps"]:
    x = {k: a[k] for k in ("key", "title", "group", "desc", "ids", "ls", "kw", "en")}
    if a.get("deck"):
        x["deck"] = True
        x["items"] = a["items"]
    assert a["key"] in packs, a["key"]
    slim["apps"].append(x)
tpl = (E / "shell.html").read_text()
out = (tpl.replace("/*__CATALOG__*/", json.dumps(slim, ensure_ascii=False, separators=(",", ":")))
          .replace("/*__PACKS__*/", json.dumps(packs, separators=(",", ":"))))
out = out.replace("/*__SILENT__*/", __import__("base64").b64encode((B / "silent.mp3").read_bytes()).decode())
assets = json.loads((B / "assets.json").read_text()) if (B / "assets.json").exists() else {}
out = out.replace("/*__ASSETS__*/", json.dumps(assets, separators=(",", ":")))
assert "/*__" not in out
(B / "index.html").write_text(out)
# проверка размера публикации
total = len(out.encode()) + sum(p.stat().st_size for p in (B / "apps").glob("*.html")) + sum(p.stat().st_size for p in (B / "packs").glob("*.mp3"))
print("ok index", len(out.encode()), "bytes; publish total", total, "bytes;", len(list((B / "apps").glob("*.html"))), "apps,", len(list((B / "packs").glob("*.mp3"))), "packs")
