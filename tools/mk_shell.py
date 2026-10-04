# Собирает оболочку «Английский B2»: tools/shell.html + каталог + индекс звука → site/index.html,
# и офлайн-кэш tools/sw.js → site/sw.js (версии файлов — по их содержимому).
# Запуск из корня проекта: python3 tools/mk_shell.py
import base64, hashlib, json, pathlib

T = pathlib.Path(__file__).resolve().parent          # tools/
SITE = T.parent / "site"

cat = json.loads((T / "catalog.json").read_text())
packs = json.loads((T / "packs.json").read_text())

def h8(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:8]

# в оболочку — только то, что нужно для каталога и счётчиков
slim = {"groups": cat["groups"], "apps": []}
ver = {"a": {}, "p": {}, "t": h8(SITE / "theme.css")}  # ?v= для apps/<ключ>.html, packs/<ключ>.mp3 и theme.css
for a in cat["apps"]:
    x = {k: a[k] for k in ("key", "title", "group", "desc", "ids", "ls", "kw", "en")}
    if a.get("deck"):
        x["deck"] = True
        x["items"] = a["items"]
    app_file, pack_file = SITE / "apps" / (a["key"] + ".html"), SITE / "packs" / (a["key"] + ".mp3")
    assert a["key"] in packs, a["key"]
    assert app_file.exists(), a["key"]
    assert pack_file.exists(), a["key"]
    ver["a"][a["key"]], ver["p"][a["key"]] = h8(app_file), h8(pack_file)
    slim["apps"].append(x)

tpl = (T / "shell.html").read_text()
out = (tpl.replace("/*__CATALOG__*/", json.dumps(slim, ensure_ascii=False, separators=(",", ":")))
          .replace("/*__PACKS__*/", json.dumps(packs, separators=(",", ":")))
          .replace("/*__VER__*/", json.dumps(ver, separators=(",", ":")))
          .replace("/*__SILENT__*/", base64.b64encode((T / "silent.mp3").read_bytes()).decode())
          # В артефакте на claude.ai пять самых больших пакетов лежат в хранилище артефакта.
          # Здесь все пакеты — обычные файлы site/packs/<ключ>.mp3, поэтому список пуст.
          .replace("/*__ASSETS__*/", "{}"))
assert "/*__" not in out
# <head> для GitHub Pages: иконка, манифест, режим приложения на экране «Домой», safe-area.
# Для публикации в артефакт на claude.ai эту часть (до <body> включительно) и хвост </body></html> убирают —
# платформа добавляет свой каркас.
head = (T / "head.html").read_text().rstrip("\n").replace("/*__THEME__*/", ver["t"])
out = head + "\n" + out + "\n\n</body></html>"
(SITE / "index.html").write_text(out)

# офлайн-кэш: заранее — иконки, манифест и все тренажёры; звук — по мере открытия тем
static = ["manifest.webmanifest", "apple-touch-icon.png", "favicon.png", "icon-192.png", "icon-512.png"]
static += sorted("fonts/" + p.name for p in (SITE / "fonts").glob("*.woff2"))
for f in static:
    assert (SITE / f).exists(), f
precache = static + [f"theme.css?v={ver['t']}"] + [f"apps/{k}.html?v={v}" for k, v in ver["a"].items()]
version = hashlib.sha256(out.encode() + json.dumps(precache).encode()).hexdigest()[:12]
sw = (T / "sw.js").read_text().replace("/*__VERSION__*/", version).replace("/*__PRECACHE__*/", json.dumps(precache, indent=1))
assert "/*__" not in sw
(SITE / "sw.js").write_text(sw)

total = len(out.encode()) + sum(p.stat().st_size for p in (SITE / "apps").glob("*.html")) + sum(p.stat().st_size for p in (SITE / "packs").glob("*.mp3"))
print("ok index", len(out.encode()), "bytes; site", total, "bytes;", len(slim["apps"]), "apps; sw", version)
