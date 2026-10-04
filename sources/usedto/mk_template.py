# Шаблон «used to» собираю из шаблона «Погода»: тренажёр тот же, пометки [текст|x] красятся по форме,
# вкладка правил — своя: таблица «что с чем», алгоритм из четырёх вопросов, ситуации, ошибки, темы.
import pathlib
s = pathlib.Path("wthr/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Погода</title>", "<title>Used to и would</title>")
rep("  .vt .w.st{color:var(--blue)}\n", "  .vt .w.st{color:var(--blue)}\n  .vt .w.hl{color:var(--text)}\n")

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
steps = (step(1, "Раньше было, а&nbsp;теперь нет?", '<span class="pr">used&nbsp;to</span> + глагол <span class="sep">·</span> <i>и&nbsp;действия, и&nbsp;состояния</i>')
         + step(2, "Так бывало, повторялось в&nbsp;рассказе?", '<span class="hl">would</span> + глагол <span class="sep">·</span> <i>только действия</i>')
         + step(3, "Уже привычно, «привык»?", '<span class="good">be&nbsp;used&nbsp;to</span> + <i>-ing или сущ.</i>')
         + step(4, "Привыкаешь, это процесс?", '<span class="st">get&nbsp;used&nbsp;to</span> + <i>-ing или сущ.</i>'))

a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Used to</h1>
      <p class="r-sub">Четыре похожие конструкции&nbsp;— четыре разных смысла: <b>used to&nbsp;— раньше, be used to&nbsp;— привык, get used to&nbsp;— привыкаю, would&nbsp;— так бывало</b>.</p>
      <div class="algo">
        <p class="algo-h">Что с&nbsp;чем</p>
        <table class="vt">
          <colgroup><col class="v"><col></colgroup>
          <tbody>
<!--__TABLE__-->
          </tbody>
        </table>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Как выбрать</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m">Перед used to стоит <b class="good" lang="en">be</b> или <b class="st" lang="en">get</b>&nbsp;— дальше <i lang="en">-ing</i>. Нет&nbsp;— обычный глагол.</p>
        <p class="algo-note">Отрицание и&nbsp;вопрос&nbsp;— без d: <i lang="en">didn't use to, Did you use to…?</i> «Обычно» в&nbsp;настоящем&nbsp;— <i lang="en">usually</i>, а&nbsp;не use to.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
    <div class="r-right">
      <h2 class="lbl">Одна ситуация&nbsp;— разный смысл</h2>
      <div class="mx-wrap">
<!--__CONTRAST__-->
      </div>
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

rep('const LS_STATE = "wthr:state";\nconst LS_SPEAK = "wthr:autospeak";\nconst LS_TAB = "wthr:tab";\nconst LS_OPEN = "wthr:open";',
    'const LS_STATE = "usedto:state";\nconst LS_SPEAK = "usedto:autospeak";\nconst LS_TAB = "usedto:tab";\nconst LS_OPEN = "usedto:open";')
rep('["apple-mobile-web-app-title", "Погода"],', '["apple-mobile-web-app-title", "used to"],')
rep("// ——— Шпаргалка и ситуации: прослушать", "// ——— Ситуации: прослушать")
rep("// Новые карточки идут вперемешку по темам: солнце, дождь, туман, ветер и стихия чередуются — выбирать приходится по сочетанию.",
    "// Новые карточки идут вперемешку по темам: раньше, привык, привыкаю и «так бывало» чередуются — выбирать приходится по смыслу.")
rep('''// […] — сочетание в фокусе (оранжевый)
function modalCls(){ return "pr"; }''', '''// [текст|x] — форма в фокусе: без метки used to — оранжевый, |b be used to — зелёный, |g get used to — синий, |w would и |p пассив — подчёркнуты
const MARK_CLS = { b: "good", g: "st", w: "hl", p: "hl" };
function modalCls(t){ const i = t.lastIndexOf("|"); return i > 0 ? (MARK_CLS[t.slice(i + 1)] || "pr") : "pr"; }
function markText(t){ const i = t.lastIndexOf("|"); return i > 0 ? t.slice(0, i) : t; }''')
rep('f.append(el("span", modalCls(m[1]), m[1]));', 'f.append(el("span", modalCls(m[1]), markText(m[1])));')
rep('function exText(en){ return en.replace(/[\\[\\]]/g, ""); }', 'function exText(en){ return en.replace(/\\|\\w\\]/g, "]").replace(/[\\[\\]]/g, ""); }')
assert "wthr:" not in s
pathlib.Path("usedto/template.html").write_text(s)
print("ok", len(s))
