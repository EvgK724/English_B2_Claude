# Сборка тренажёра «Косвенные вопросы» сразу в общее приложение.
# Запуск из sources/:
#   python3 indq/mk_template.py      # шаблон из sounds/template.html
#   python3 indq/clips.py            # список записей → indq/clips.json
#   python3 indq/tts.py              # записи голосом Ryan → indq/audio/ (нужен доступ к speech.platform.bing.com;
#                                     #   без записей фразы читает голос устройства, пакет пустой)
#   python3 indq/build.py            # site/apps/indq.html, site/packs/indq.mp3, tools/packs.json, tools/catalog.json
#   cd .. && python3 tools/mk_shell.py
# indq/index.html и indq/preview.html — та же страница без моста, для локальной проверки (indq/test.py).
import base64, importlib.util, json, html, pathlib, re, sys
here = pathlib.Path("indq")
sys.path.insert(0, str(here))
from content import TOPICS, CARDS, GROUPS, TABLE, CONTRAST, ERRORS, MIXED_TOPIC

KEY = "indq"
ROOT = pathlib.Path("..")
SITE, TOOLS = ROOT / "site", ROOT / "tools"
tpl = (here / "template.html").read_text()
esc = html.escape

# Русская типографика: неразрывный пробел перед тире и после однобуквенных слов (в, к, с, о, у, и, а, я)
NB = " "
def ru(s):
    s = s.replace(" — ", NB + "— ")
    return re.sub(r"(?<![\w-])([вксоуиаяВКСОУИАЯ]) ", r"\1" + NB, s)
def ru_html(s):
    return esc(ru(s)).replace(NB, "&nbsp;")

# разметка [слово|a] — оранжевый, |b — синий, |c — зелёный, без метки — подчёркнуто (как markCls в шаблоне)
MARK = re.compile(r"\[([^\]|]+)(?:\|([abc]))?\]")
def mcls(k):
    return {"a": "pr", "b": "st", "c": "good"}.get(k, "hl")
def marked(s):
    return MARK.sub(lambda m: f'<span class="{mcls(m.group(2))}">{m.group(1)}</span>', esc(s))
def plain(en):
    s = MARK.sub(r"\1", en)
    return s + ("" if s.rstrip()[-1:] in ".!?" else ".")

def aff(text):
    # «be — в конец, …»: главное — жирным
    head, _, rest = text.partition(" — ")
    return f'<b class="h">{ru_html(head)}</b>' + ru_html(rest)
def forms(nf):
    return " <span class=\"sep\">·</span> ".join(esc(x).replace(" ", "&nbsp;") for x in nf.split(" · "))
table = "\n".join(
    f'          <tbody><tr><th colspan="2" scope="rowgroup" class="pr" lang="en">{esc(v)}</th></tr>'
    f'<tr><td>{aff(a)}</td><td><span class="f st" lang="en">{forms(nouns)}</span></td></tr></tbody>'
    for v, a, nouns in TABLE)

PLAY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9.5h3.5L12 5.5v13l-4.5-4H4z"/><path d="M15.5 9a4 4 0 0 1 0 6"/></svg>'
def btn(key, say, label):
    return f'<button class="ex-play mm-play" type="button" data-key="{key}" data-text="{esc(say)}" aria-label="Прослушать: {esc(label)}">{PLAY}</button>'
contrast = "\n".join(
    '        <div class="md"><div>' + "".join(f'<p class="cp-en" lang="en">{marked(en)}</p><p class="cp-ru">{ru_html(r)}</p>' for en, r in rows) + '</div>'
    + btn(f"cp-{i + 1}", " ".join(plain(r[0]) for r in rows), " / ".join(plain(r[0]) for r in rows)) + '</div>'
    for i, rows in enumerate(CONTRAST))
errors = "\n".join(
    f'          <li class="err"><span class="sr">Неверно:</span> <s lang="en">{esc(w)}</s> <span class="arr" aria-hidden="true">→</span> '
    f'<span class="sr">верно:</span> <span class="good" lang="en">{esc(r)}</span><span class="err-note">{ru_html(note)}</span></li>'
    for w, r, note in ERRORS)

# в данные — с русской типографикой (английские поля не трогаем)
groups = {k: ru(v) for k, v in GROUPS.items()}
topics = [dict(t, title=ru(t["title"]), sub=ru(t["sub"]), rule=ru(t["rule"]), ex=[dict(e, ru=ru(e["ru"])) for e in t["ex"]]) for t in TOPICS]
cards = [dict(c, ru=ru(c["ru"]), why=ru(c["why"]), **({"also": {k: ru(v) for k, v in c["also"].items()}} if "also" in c else {})) for c in CARDS]
data = ("// ——— Темы по группам: правило и примеры. [слово|a] — вопросительное слово, if, whether; [слова|b] — подлежащее и глагол.\n"
        "// late — насколько позже тема вступает в общую тренировку: сначала B1, потом B1+, потом B2.\n"
        f"const MIXED_TOPIC = {MIXED_TOPIC};\n"
        "const GROUPS = " + json.dumps(groups, ensure_ascii=False) + ";\n"
        "const TOPICS = " + json.dumps(topics, ensure_ascii=False, indent=1) + ";\n\n"
        "// ——— Карточки. opts — варианты, a — правильный, also — тоже верно (с пояснением), ru — перевод (подсказка),\n"
        "// say — что произносить вместо предложения с ответом (ударение REcord и reCORD, вопросы о звуке).\n"
        "const CARDS = " + json.dumps(cards, ensure_ascii=False, indent=1) + ";")
out = (tpl.replace("<!--__TABLE__-->", table).replace("<!--__CONTRAST__-->", contrast)
          .replace("<!--__ERRORS__-->", errors).replace("/*__DATA__*/", data))
# значки для экрана «Домой» внутри общего приложения не нужны (как в tools/reference/collect.py)
out = out.replace('"__ICON180__"', '""').replace('"__ICON192__"', '""')
s0 = out.index("<style>"); s1 = out.index("</style>", s0)
out = out[:s0] + re.sub(r"(?<![\w.#-])(\d+(?:\.\d+)?)px", r"calc(\1px*var(--k))", out[s0:s1]) + out[s1:]
assert "__ICON" not in out and "/*__DATA__*/" not in out and "<!--__" not in out
assert out.startswith("<title>") and out.count("new Audio(") == 1
assert out.count('db.doc("data/users/" + uid + "/progress")') == 1

# записи: все ключи страницы должны быть озвучены
clips = json.loads((here / "clips.json").read_text())
need = set(re.findall(r'data-key="([^"]+)"', out)) | {c["id"] for c in CARDS} | {f"r{t['n']}-{i + 1}" for t in TOPICS for i in range(len(t["ex"]))}
assert need == {c["key"] for c in clips}, sorted(need ^ {c["key"] for c in clips})
# записей может не быть (нет доступа к сервису озвучки) — тогда эти фразы читает голос устройства (TTS_LANG en-GB)
have = [k for k in sorted(need) if (here / "audio" / f"{k}.mp3").exists() and (here / "audio" / f"{k}.mp3").stat().st_size > 1024]

(here / "index.html").write_text(out)
# preview — с тем же <head>, что оболочка даёт тренажёру (базовые стили и theme.css), чтобы выглядело как в приложении
shell_head = re.search(r"const HEAD = '(.*?)' \+ themeUrl\(\) \+ '(.*?)';", (TOOLS / "shell.html").read_text())
(here / "preview.html").write_text(shell_head.group(1) + "../../site/theme.css" + shell_head.group(2) + "\n" + out + "\n</body></html>")

# в общее приложение: мост к оболочке первой строкой после <title> — до всех скриптов тренажёра
PRELUDE = '<script>(function(){try{var B=window.parent&&window.parent.__eng;if(B&&B.attach)B.attach(%s,window)}catch(e){}})();</script>'
app = out.replace("</title>", "</title>\n" + PRELUDE % json.dumps(KEY), 1)
(SITE / "apps" / f"{KEY}.html").write_text(app)

# звук: записи склеиваются в один пакет, тишина по краям срезается целыми кадрами без пережатия (как tools/deck_sync.py)
spec = importlib.util.spec_from_file_location("deck_sync", TOOLS / "deck_sync.py")
deck_sync = importlib.util.module_from_spec(spec); spec.loader.exec_module(deck_sync)
packs = json.loads((TOOLS / "packs.json").read_text())
buf, idx = bytearray(), {}
for k in have:
    data_, lead = deck_sync.trim_clip((here / "audio" / f"{k}.mp3").read_bytes())
    assert data_[:2] in (b"\xff\xf3", b"\xff\xf2", b"\xff\xfb"), (k, data_[:4])
    idx[k] = [len(buf), len(data_), lead]
    buf += data_
(SITE / "packs" / f"{KEY}.mp3").write_bytes(bytes(buf))
packs[KEY] = idx
(TOOLS / "packs.json").write_text(json.dumps(packs, separators=(",", ":")))

# каталог: после «Вопросов» (q), в группе «Вопросы, связки, пересказ»
cat = json.loads((TOOLS / "catalog.json").read_text())
entry = {"key": KEY, "title": "Косвенные вопросы", "group": "text",
         "desc": "Could you tell me where the lab is: прямой порядок слов, if и whether",
         "ids": [c["id"] for c in CARDS], "ls": f"{KEY}:state",
         "en": "indirect questions embedded questions could you tell me where the lab is do you know if whether I wonder "
               "word order прямой порядок слов косвенный вопрос",
         "kw": " · ".join(t["title"] for t in TOPICS), "voice": "Ryan", "size": len(app.encode())}
apps = [a for a in cat["apps"] if a["key"] != KEY]
pos = next(i for i, a in enumerate(apps) if a["key"] == "q") + 1
cat["apps"] = apps[:pos] + [entry] + apps[pos:]
(TOOLS / "catalog.json").write_text(json.dumps(cat, ensure_ascii=False))
print("ok", len(app), "bytes;", len(TOPICS), "topics;", len(CARDS), "cards; записей", len(have), "из", len(need), ";", len(buf), "bytes of audio")
if len(have) < len(need):
    print("без записей — голос устройства:", len(need) - len(have), "фраз; записать: python3 indq/tts.py, затем снова indq/build.py")
