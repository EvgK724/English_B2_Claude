# Шаблон «Прилагательное или наречие» собираю из шаблона «Пассива»: тренажёр тот же, вкладка правил — своя.
import pathlib
s = pathlib.Path("passive/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Пассивный залог</title>", "<title>Прилагательные и наречия</title>")

# ——— стили: вместо таблицы форм — памятка из четырёх групп
a = s.index("  .chain{display:flex"); b = s.index("  .errs{list-style:none")
s = s[:a] + '''  .mm{margin-top:10px;padding:12px 14px 12px;background:var(--surface);border:1px solid var(--line);border-radius:16px}
  .mm:first-of-type{margin-top:0}
  .mm-h{margin:0 0 6px;font-size:13px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--blue)}
  .mm-n{display:inline-block;min-width:1.6em;color:var(--accent)}
  .mm-grid{display:grid;grid-template-columns:1fr 1fr;gap:2px 12px}
  .mm-w{margin:0;padding:5px 0}
  .mm-w span{display:block;font-family:var(--serif);font-size:20px;line-height:1.2}
  .mm-w small{display:block;font-size:13px;line-height:1.3;color:var(--muted)}
  .mm-pair{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr) 44px;column-gap:10px;align-items:center;padding:6px 0;border-top:1px solid var(--line)}
  .mm-pair:first-of-type{border-top:0}
  .mm-pair p{margin:0}
  .mm-pair span{display:block;font-family:var(--serif);font-size:20px;line-height:1.2}
  .mm-pair small{display:block;font-size:13px;line-height:1.3;color:var(--muted)}
  .mm-play{width:44px;height:44px;border-radius:50%;border:1px solid var(--line-2);background:transparent;color:var(--accent);display:grid;place-items:center;cursor:pointer}
  .mm-play svg{width:18px;height:18px}
  .mm-note{margin:8px 0 0;padding-top:8px;border-top:1px solid var(--line);font-size:14px;line-height:1.45;color:var(--soft)}
  .legend{margin:0 2px 10px;font-size:15px;line-height:1.45;color:var(--soft)}
''' + s[b:]
rep("  .s-f{margin:3px 0 0;font-family:var(--serif);font-size:20px;line-height:1.3}",
    "  .s-f{margin:3px 0 0;font-family:var(--serif);font-size:20px;line-height:1.3}\n  .s-f i{font-style:normal;color:var(--soft)}")

# ——— разметка вкладки «Правила»
a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Adjective or adverb?</h1>
      <p class="r-sub">Прилагательное или наречие. Главный вопрос&nbsp;— <b>какой?</b> или <b>как?</b> Всё остальное&nbsp;— четыре группы исключений, они собраны в&nbsp;памятке.</p>
      <div class="algo">
        <p class="algo-h">Проверка за секунду</p>
        <ol class="steps">
          <li><span class="sn">1</span><div><p class="s-t">Какой? Описывает существительное</p><p class="s-f" lang="en"><i>a</i> <span class="st">careful</span> <i>doctor</i></p></div></li>
          <li><span class="sn">2</span><div><p class="s-t">Как? Описывает действие</p><p class="s-f" lang="en"><i>examines</i> <span class="pr">carefully</span></p></div></li>
          <li><span class="sn">3</span><div><p class="s-t">После be, look, feel, sound, seem, get&nbsp;— прилагательное</p><p class="s-f" lang="en"><i>You look</i> <span class="st">tired</span></p></div></li>
        </ol>
        <p class="algo-m">Наречие&nbsp;= прилагательное + -ly: <b class="st" lang="en">careful</b> → <b class="pr" lang="en">carefully</b></p>
        <p class="algo-note">Особое слово: <i lang="en">good</i> → <i lang="en">well</i>. A good doctor, но she works well.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
    <div class="r-right">
      <h2 class="lbl">Памятка: четыре группы исключений</h2>
      <p class="legend"><span class="st">Синим</span>&nbsp;— прилагательное (какой?), <span class="pr">оранжевым</span>&nbsp;— наречие (как?).</p>
<!--__MEMO__-->
      <h2 class="lbl">Частые ошибки</h2>
      <div class="mx-wrap">
        <ul class="errs">
<!--__ERRORS__-->
        </ul>
      </div>
      <h2 class="lbl">Темы</h2>
      <div class="topics" id="topics"></div>
    </div>
''' + s[b:]

# ——— скрипт
rep('const LS_STATE = "passive:state";\nconst LS_SPEAK = "passive:autospeak";\nconst LS_TAB = "passive:tab";\nconst LS_OPEN = "passive:open";',
    'const LS_STATE = "adjadv:state";\nconst LS_SPEAK = "adjadv:autospeak";\nconst LS_TAB = "adjadv:tab";\nconst LS_OPEN = "adjadv:open";')
rep('["apple-mobile-web-app-title", "Passive"],', '["apple-mobile-web-app-title", "adj / adv"],')
rep("// {…} — be (синий), _…_ — третья форма (оранжевый), |…| — зелёный", "// {…} — прилагательное (синий), _…_ — наречие (оранжевый), |…| — зелёный")
# «все формы подряд» здесь не нужны; вместо них — кнопки прослушивания пар в памятке
a = s.index("// ——— «Все формы подряд»"); b = s.index("// ——— Очередь")
s = s[:a] + '''// ——— Памятка: прослушать пару (hard — hardly…)
document.querySelectorAll(".mm-play").forEach(b => b.addEventListener("click", () => playClip(b.dataset.key, b.dataset.text, 0.85)));

''' + s[b:]
rep("let chainOn = false;        // играют «все формы подряд»\n", "")
rep("  if (chainOn){ chainOn = false; chainUI(); }\n}", "}")
rep("  if (chainOn){ chainOn = false; chainUI(); }     // без записи подсветка строк не работает\n", "")
rep("// Новые карточки идут вперемешку по темам: время и залог чередуются, чтобы выбирать по смыслу, а не угадывать по теме.",
    "// Новые карточки идут вперемешку по темам: каждый раз решаешь заново — какой? или как?")
# в альбомной ориентации левая колонка выше экрана — пусть прокручивается вместе с правой
rep("  body.wide .r-left{position:sticky;top:0}", "  body.wide .r-left{position:static}")
# стрелка «→» держится за оба слова: easy → easily не разрывается
rep("  String(s).split(/(-[a-z]+)/).forEach(", "  String(s).replace(/ → /g, \"\\u00a0→\\u00a0\").split(/(-[a-z]+)/).forEach(")
assert "chainOn" not in s and "formsPlay" not in s and "FORMS" not in s, [w for w in ("chainOn", "formsPlay", "FORMS") if w in s]
pathlib.Path("adjadv/template.html").write_text(s)
print("ok", len(s))
