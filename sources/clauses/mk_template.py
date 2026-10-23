# Шаблон «Types of clauses» собираю из шаблона «Three, tree, sheep» (sounds), как «What is it for?» (whatfor):
# тот же тренажёр с разметкой [слово|a]; карточек на слух здесь нет.
# Вкладка правил — своя: таблица «образец — правило — примеры», как выбрать, мнемоника, мини-диалоги.
# Запуск из sources/: python3 clauses/mk_template.py   (нужен sounds/template.html — python3 sounds/mk_template.py)
import pathlib
s = pathlib.Path("sounds/template.html").read_text()

def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Three, tree, sheep</title>", "<title>Types of clauses</title>")

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
def W(t, c):
    return f'<span class="{c}">{t.replace(" ", "&nbsp;") if len(t) <= 16 else t}</span>'
D = ' <span class="sep">·</span> '
steps = (step(1, "Какой вопрос? Когда, почему, что в итоге, зачем, вопреки чему, как", W("when", "pr") + D + W("because", "pr") + D + W("so", "pr") + D + W("to", "good") + D + W("although", "pr") + D + W("as if", "pr"))
         + step(2, "Дальше целое предложение — подлежащее и глагол?", W("because it's risky", "pr") + D + W("although it rained", "pr"))
         + step(3, "Дальше существительное или -ing?", W("because of the risk", "st") + D + W("despite the rain", "st"))
         + step(4, "Дальше глагол — цель?", W("to stay safe", "good") + D + W("so as not to fall", "good"))
         + step(5, "О будущем после when, as soon as, until — без will; придаточное впереди — запятая", W("As soon as I hear, I'll call.", "pr")))

a = s.index('    <div class="r-left">'); b = s.index('    <div class="r-right">')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Types of&nbsp;clauses</h1>
      <p class="r-sub">Придаточное отвечает на&nbsp;один из&nbsp;шести вопросов: когда? почему? что в&nbsp;итоге? зачем? вопреки чему? как? А&nbsp;связку выбирают по&nbsp;тому, что идёт после неё. В&nbsp;примерах <b class="pr">оранжевая</b>&nbsp;— дальше целое предложение (<i lang="en">because it's risky</i>), <b class="st">синяя</b>&nbsp;— существительное или -ing (<i lang="en">because of the risk</i>), <b class="good">зелёная</b>&nbsp;— глагол (<i lang="en">to stay safe</i>), <span class="hl">подчёркнутая</span>&nbsp;— отдельное слово между предложениями (<i lang="en">However,</i>).</p>
      <div class="algo">
        <p class="algo-h">Главная таблица</p>
        <table class="mt vt">
          <colgroup><col><col></colgroup>
          <thead><tr><th scope="col">Правило</th><th scope="col">Примеры</th></tr></thead>
<!--__TABLE__-->
        </table>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Как выбрать</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m"><b class="pr" lang="en">because</b> + предложение, <b class="st" lang="en">because of</b> + слово, <b class="good" lang="en">to</b> + глагол: <i lang="en">because it's risky · because of the risk · to stay safe</i></p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
''' + s[b:]

rep('const LS_STATE = "sounds:state";\nconst LS_SPEAK = "sounds:autospeak";\nconst LS_TAB = "sounds:tab";\nconst LS_OPEN = "sounds:open";',
    'const LS_STATE = "clauses:state";\nconst LS_SPEAK = "clauses:autospeak";\nconst LS_TAB = "clauses:tab";\nconst LS_OPEN = "clauses:open";')
rep('["apple-mobile-web-app-title", "sounds"],', '["apple-mobile-web-app-title", "clauses"],')
assert "sounds:" not in s
rep('<h2 class="lbl">Одна ситуация&nbsp;— разный смысл</h2>', '<h2 class="lbl">Одна мысль&nbsp;— разные связки</h2>')
pathlib.Path("clauses/template.html").write_text(s)
print("ok", len(s))
