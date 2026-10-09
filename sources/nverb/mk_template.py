# Шаблон «Advice и advise» собираю из шаблона «Three, tree, sheep» (sounds): тот же тренажёр с полем say
# (ударение REcord и reCORD, вопросы о звуке) и разметкой [слово|a]; карточек на слух здесь нет.
# Вкладка правил — своя: таблица «образец — правило — пары», как отличить, мнемоника.
# Запуск из sources/: python3 nverb/mk_template.py   (нужен sounds/template.html — python3 sounds/mk_template.py)
import pathlib
s = pathlib.Path("sounds/template.html").read_text()

def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Three, tree, sheep</title>", "<title>Advice и advise</title>")

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
def W(t, c):
    return f'<span class="{c}">{t.replace(" ", "&nbsp;") if len(t) <= 16 else t}</span>'
D = ' <span class="sep">·</span> '
steps = (step(1, "Перед словом a, the, my, good или оно подлежащее? Существительное", W("my advice", "pr") + D + W("a deep breath", "pr") + D + W("the loss", "pr"))
         + step(2, "После to, can, will, should или это сказуемое? Глагол", W("to advise", "st") + D + W("can breathe", "st") + D + W("will lose", "st"))
         + step(3, "На слух: существительное глухое, глагол звонкий", W("advice [s]", "pr") + D + W("advise [z]", "st") + D + W("belief [f]", "pr") + D + W("believe [v]", "st"))
         + step(4, "Пишутся одинаково? Существительное — ударение вперёд", W("a REcord", "pr") + D + W("to reCORD", "st")))

a = s.index('    <div class="r-left">'); b = s.index('    <div class="r-right">')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Advice и&nbsp;advise</h1>
      <p class="r-sub">Существительное и&nbsp;глагол часто отличаются одной буквой, звуком или ударением: <b lang="en">advice</b>&nbsp;— совет, <b lang="en">advise</b>&nbsp;— советовать. В&nbsp;примерах <b class="pr">существительное</b> оранжевое, <b class="st">глагол</b> синий.</p>
      <div class="algo">
        <p class="algo-h">Главная таблица</p>
        <table class="mt vt">
          <colgroup><col><col></colgroup>
          <thead><tr><th scope="col">Правило</th><th scope="col">Пары</th></tr></thead>
<!--__TABLE__-->
        </table>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Как отличить</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m"><b class="pr">Существительное</b>&nbsp;— глухое и&nbsp;с&nbsp;ударением вперёд, <b class="st">глагол</b>&nbsp;— звонкий и&nbsp;с&nbsp;ударением назад: <i lang="en">a REcord of advice</i>&nbsp;— <i lang="en">to reCORD and advise</i>.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
''' + s[b:]

rep('const LS_STATE = "sounds:state";\nconst LS_SPEAK = "sounds:autospeak";\nconst LS_TAB = "sounds:tab";\nconst LS_OPEN = "sounds:open";',
    'const LS_STATE = "nverb:state";\nconst LS_SPEAK = "nverb:autospeak";\nconst LS_TAB = "nverb:tab";\nconst LS_OPEN = "nverb:open";')
rep('["apple-mobile-web-app-title", "sounds"],', '["apple-mobile-web-app-title", "advice"],')
assert "sounds:" not in s
pathlib.Path("nverb/template.html").write_text(s)
print("ok", len(s))
