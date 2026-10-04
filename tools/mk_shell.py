# Собирает оболочку «Английский B2»: tools/shell.html + каталог + индекс звука → site/index.html
# Запуск из корня проекта: python3 tools/mk_shell.py
import base64, json, pathlib

T = pathlib.Path(__file__).resolve().parent          # tools/
SITE = T.parent / "site"

cat = json.loads((T / "catalog.json").read_text())
packs = json.loads((T / "packs.json").read_text())

# в оболочку — только то, что нужно для каталога и счётчиков
slim = {"groups": cat["groups"], "apps": []}
for a in cat["apps"]:
    x = {k: a[k] for k in ("key", "title", "group", "desc", "ids", "ls", "kw", "en")}
    if a.get("deck"):
        x["deck"] = True
        x["items"] = a["items"]
    assert a["key"] in packs, a["key"]
    assert (SITE / "apps" / (a["key"] + ".html")).exists(), a["key"]
    assert (SITE / "packs" / (a["key"] + ".mp3")).exists(), a["key"]
    slim["apps"].append(x)

tpl = (T / "shell.html").read_text()
out = (tpl.replace("/*__CATALOG__*/", json.dumps(slim, ensure_ascii=False, separators=(",", ":")))
          .replace("/*__PACKS__*/", json.dumps(packs, separators=(",", ":")))
          .replace("/*__SILENT__*/", base64.b64encode((T / "silent.mp3").read_bytes()).decode())
          # В артефакте на claude.ai пять самых больших пакетов лежат в хранилище артефакта.
          # Здесь все пакеты — обычные файлы site/packs/<ключ>.mp3, поэтому список пуст.
          .replace("/*__ASSETS__*/", "{}"))
assert "/*__" not in out
# каркас страницы — тот же, что добавляет публикация артефакта на claude.ai (doctype, meta viewport, safe-area)
head = (T / "skeleton-head.html").read_text().rstrip("\n")
out = head + "\n" + out + "\n\n</body></html>"
(SITE / "index.html").write_text(out)
total = len(out.encode()) + sum(p.stat().st_size for p in (SITE / "apps").glob("*.html")) + sum(p.stat().st_size for p in (SITE / "packs").glob("*.mp3"))
print("ok index", len(out.encode()), "bytes; site", total, "bytes;", len(slim["apps"]), "apps")
