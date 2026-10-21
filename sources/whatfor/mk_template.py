# Шаблон «What is it for?» собираю из шаблона «Three, tree, sheep» (sounds), как «Like и look like» (like):
# тот же тренажёр с разметкой [слово|a]; карточек на слух здесь нет.
# Вкладка правил — своя: таблица «образец — правило — примеры», как выбрать, мнемоника, мини-диалоги.
# Запуск из sources/: python3 whatfor/mk_template.py   (нужен sounds/template.html — python3 sounds/mk_template.py)
import pathlib
s = pathlib.Path("sounds/template.html").read_text()

def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Three, tree, sheep</title>", "<title>What is it for?</title>")

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
def W(t, c):
    return f'<span class="{c}">{t.replace(" ", "&nbsp;") if len(t) <= 16 else t}</span>'
D = ' <span class="sep">·</span> '
steps = (step(1, "Постройте утверждение, предлог возьмите из сочетания", W("waiting for someone", "pr") + D + W("allergic to something", "pr"))
         + step(2, "Неизвестное — who или what, вперёд; перед подлежащим — do, are, did", W("Who are you waiting…", "st"))
         + step(3, "Предлог остаётся на месте — в конце", W("Who are you waiting for?", "pr") + D + W("What are you allergic to?", "pr"))
         + step(4, "Переспрашиваете коротко? Слово и предлог", W("Who with?", "pr") + D + W("What about?", "pr"))
         + step(5, "Официальное письмо? Предлог можно вперёд, после него whom, which", W("To whom…?", "good") + D + W("On which data…?", "good")))

a = s.index('    <div class="r-left">'); b = s.index('    <div class="r-right">')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">What is it&nbsp;for?</h1>
      <p class="r-sub">Предлог в&nbsp;конце вопроса. Вопросительное слово уходит вперёд, а&nbsp;предлог остаётся при своём глаголе: <b lang="en">What is it for?</b>&nbsp;— для чего, <b lang="en">Who are you waiting for?</b>&nbsp;— кого вы ждёте, <b lang="en">Where are you from?</b>&nbsp;— откуда. В&nbsp;примерах <b class="pr">предлог в&nbsp;конце</b> оранжевый, <b class="st">вопросительное слово</b> синее, <b class="good">официальный вариант</b> зелёный.</p>
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
        <p class="algo-m"><b class="st">Кто, что</b>&nbsp;— вперёд, <b class="pr">предлог</b>&nbsp;— остаётся дома, у&nbsp;своего глагола: <i lang="en">wait for → Who are you waiting for?</i></p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
''' + s[b:]

rep('const LS_STATE = "sounds:state";\nconst LS_SPEAK = "sounds:autospeak";\nconst LS_TAB = "sounds:tab";\nconst LS_OPEN = "sounds:open";',
    'const LS_STATE = "whatfor:state";\nconst LS_SPEAK = "whatfor:autospeak";\nconst LS_TAB = "whatfor:tab";\nconst LS_OPEN = "whatfor:open";')
rep('["apple-mobile-web-app-title", "sounds"],', '["apple-mobile-web-app-title", "what for"],')
assert "sounds:" not in s
rep('<h2 class="lbl">Одна ситуация&nbsp;— разный смысл</h2>', '<h2 class="lbl">Мини-диалоги</h2>')
pathlib.Path("whatfor/template.html").write_text(s)
print("ok", len(s))
