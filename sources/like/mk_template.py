# Шаблон «Like и look like» собираю из шаблона «Three, tree, sheep» (sounds), как «Recycle → recycling» (vnoun):
# тот же тренажёр с разметкой [слово|a]; карточек на слух здесь нет.
# Вкладка правил — своя: таблица «образец — правило — примеры», как выбрать, мнемоника, мини-диалоги.
# Запуск из sources/: python3 like/mk_template.py   (нужен sounds/template.html — python3 sounds/mk_template.py)
import pathlib
s = pathlib.Path("sounds/template.html").read_text()

def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Three, tree, sheep</title>", "<title>Like и look like</title>")

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
def W(t, c):
    return f'<span class="{c}">{t.replace(" ", "&nbsp;") if len(t) <= 16 else t}</span>'
D = ' <span class="sep">·</span> '
steps = (step(1, "Спрашиваете о характере или впечатлении?", W("What's she like?", "pr") + D + W("What was it like?", "pr"))
         + step(2, "О внешности, о сходстве?", W("What does she look like?", "pr") + D + W("looks like her mum", "pr"))
         + step(3, "После look, sound, feel — прилагательное без like; перед существительным — like", W("looks tired", "good") + D + W("looks like a doctor", "pr"))
         + step(4, "Хотите сейчас?", W("I'd like a coffee", "st") + D + W("I feel like a walk", "pr"))
         + step(5, "Роль, профессия — as; просто похоже — like", W("works as a nurse", "good") + D + W("talks like a doctor", "pr")))

a = s.index('    <div class="r-left">'); b = s.index('    <div class="r-right">')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Like и&nbsp;look like</h1>
      <p class="r-sub">Три вопроса, которые путают: <b lang="en">What's she like?</b>&nbsp;— какая она, <b lang="en">What does she look like?</b>&nbsp;— как выглядит, <b lang="en">What does she like?</b>&nbsp;— что любит. В&nbsp;примерах <b class="pr">like «как, похож»</b> оранжевый, <b class="st">like «нравится»</b> синий, <b class="good">прилагательное или as</b> зелёный.</p>
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
        <p class="algo-m"><b class="pr" lang="en">like</b>&nbsp;— характер, <b class="pr" lang="en">look like</b>&nbsp;— внешность, <b class="st" lang="en">like</b>-глагол&nbsp;— вкусы: <i lang="en">What's she like? · What does she look like? · What does she like?</i></p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
''' + s[b:]

rep('const LS_STATE = "sounds:state";\nconst LS_SPEAK = "sounds:autospeak";\nconst LS_TAB = "sounds:tab";\nconst LS_OPEN = "sounds:open";',
    'const LS_STATE = "like:state";\nconst LS_SPEAK = "like:autospeak";\nconst LS_TAB = "like:tab";\nconst LS_OPEN = "like:open";')
rep('["apple-mobile-web-app-title", "sounds"],', '["apple-mobile-web-app-title", "like"],')
assert "sounds:" not in s
rep('<h2 class="lbl">Одна ситуация&nbsp;— разный смысл</h2>', '<h2 class="lbl">Мини-диалоги</h2>')
pathlib.Path("like/template.html").write_text(s)
print("ok", len(s))
