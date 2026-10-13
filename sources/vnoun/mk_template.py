# Шаблон «Recycle → recycling» собираю из шаблона «Three, tree, sheep» (sounds), как «Advice и advise» (nverb):
# тот же тренажёр с разметкой [слово|a]; карточек на слух здесь нет.
# Вкладка правил — своя: таблица «образец — правило — пары», как образовать, мнемоника, пары с карточек урока.
# Запуск из sources/: python3 vnoun/mk_template.py   (нужен sounds/template.html — python3 sounds/mk_template.py)
import pathlib
s = pathlib.Path("sounds/template.html").read_text()

def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Three, tree, sheep</title>", "<title>Recycle → recycling</title>")

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
def W(t, c):
    return f'<span class="{c}">{t.replace(" ", "&nbsp;") if len(t) <= 16 else t}</span>'
D = ' <span class="sep">·</span> '
steps = (step(1, "Перед ним a, the, your, of? Существительное. После to, can, don't — глагол", W("a waste", "pr") + D + W("your support", "pr") + D + W("don't waste", "st"))
         + step(2, "Процесс, занятие? -ing", W("recycling", "pr") + D + W("suffering", "pr") + D + W("screening", "pr"))
         + step(3, "Глагол на -ate, -ct, -ent, -ute? -ion", W("pollution", "pr") + D + W("protection", "pr") + D + W("prevention", "pr"))
         + step(4, "-ence или -ance? Спросите прилагательное", W("existent → existence", "pr") + D + W("resistant → resistance", "pr"))
         + step(5, "Корень меняется? Учите парой", W("solve → solution", "pr") + D + W("destroy → destruction", "pr")))

a = s.index('    <div class="r-left">'); b = s.index('    <div class="r-right">')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Recycle → recycling</h1>
      <p class="r-sub">Как из&nbsp;глагола получается существительное: <b lang="en">recycle</b>&nbsp;— <b lang="en">recycling</b>, <b lang="en">solve</b>&nbsp;— <b lang="en">solution</b>. Сначала&nbsp;— пары с&nbsp;карточек урока, дальше&nbsp;— похожие слова по&nbsp;суффиксам. В&nbsp;примерах <b class="pr">существительное</b> оранжевое, <b class="st">глагол</b> синий.</p>
      <div class="algo">
        <p class="algo-h">Главная таблица</p>
        <table class="mt vt">
          <colgroup><col><col></colgroup>
          <thead><tr><th scope="col">Правило</th><th scope="col">Пары</th></tr></thead>
<!--__TABLE__-->
        </table>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Как образовать</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m">Какая буква в&nbsp;прилагательном, такая и&nbsp;в&nbsp;существительном: <i lang="en">exist<b class="pr">e</b>nt&nbsp;→&nbsp;exist<b class="pr">e</b>nce</i>, <i lang="en">resist<b class="pr">a</b>nt&nbsp;→&nbsp;resist<b class="pr">a</b>nce</i>.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
''' + s[b:]

rep('const LS_STATE = "sounds:state";\nconst LS_SPEAK = "sounds:autospeak";\nconst LS_TAB = "sounds:tab";\nconst LS_OPEN = "sounds:open";',
    'const LS_STATE = "vnoun:state";\nconst LS_SPEAK = "vnoun:autospeak";\nconst LS_TAB = "vnoun:tab";\nconst LS_OPEN = "vnoun:open";')
rep('["apple-mobile-web-app-title", "sounds"],', '["apple-mobile-web-app-title", "recycling"],')
assert "sounds:" not in s
rep('<h2 class="lbl">Одна ситуация&nbsp;— разный смысл</h2>', '<h2 class="lbl">Пары с&nbsp;карточек урока</h2>')
pathlib.Path("vnoun/template.html").write_text(s)
print("ok", len(s))
