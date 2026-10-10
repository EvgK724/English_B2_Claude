# Шаблон «Косвенные вопросы» собираю из шаблона «Three, tree, sheep» (sounds): тот же тренажёр с разметкой [слово|a];
# карточек на слух здесь нет. Вкладка правил — своя: таблица «прямой вопрос — что меняется — косвенный», как построить, мнемоника.
# Запуск из sources/: python3 indq/mk_template.py   (нужен sounds/template.html — python3 sounds/mk_template.py)
import pathlib
s = pathlib.Path("sounds/template.html").read_text()

def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Three, tree, sheep</title>", "<title>Косвенные вопросы</title>")

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
def W(t, c):
    return f'<span class="{c}">{t.replace(" ", "&nbsp;") if len(t) <= 16 else t}</span>'
D = ' <span class="sep">·</span> '
steps = (step(1, "Уберите do, does, did — время перейдёт в глагол", W("did it start", "hl") + " → " + W("it started", "st") + D + W("does he take", "hl") + " → " + W("he takes", "st"))
         + step(2, "Подлежащее вперёд, is, can, have — после него", W("is the lab", "hl") + " → " + W("the lab is", "st") + D + W("can I park", "hl") + " → " + W("I can park", "st"))
         + step(3, "Вопрос «да или нет»? Добавьте if или whether", W("Do you know if he smokes?", "pr"))
         + step(4, "Знак вопроса — только если вопросом начинается всё предложение", W("Do you know …?", "pr") + D + W("I wonder … .", "st")))

a = s.index('    <div class="r-left">'); b = s.index('    <div class="r-right">')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title">Косвенные вопросы</h1>
      <p class="r-sub">Вопрос внутри предложения уже не вопрос: порядок как в&nbsp;утверждении. <b lang="en">Where is the lab?</b> → <b lang="en">Could you tell me where the lab is?</b> В&nbsp;примерах <b class="pr">вопросительное слово</b> оранжевое, <b class="st">подлежащее и&nbsp;глагол</b> синие.</p>
      <div class="algo">
        <p class="algo-h">Главная таблица</p>
        <table class="mt vt">
          <colgroup><col><col></colgroup>
          <thead><tr><th scope="col">Что меняется</th><th scope="col">Косвенный</th></tr></thead>
<!--__TABLE__-->
        </table>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Как построить</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m">Спросили один раз&nbsp;— в&nbsp;начале: <b class="pr" lang="en">Could you tell me</b>. Второй раз переворачивать не&nbsp;нужно: <b class="st" lang="en">where the lab is</b>.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
''' + s[b:]

rep('const LS_STATE = "sounds:state";\nconst LS_SPEAK = "sounds:autospeak";\nconst LS_TAB = "sounds:tab";\nconst LS_OPEN = "sounds:open";',
    'const LS_STATE = "indq:state";\nconst LS_SPEAK = "indq:autospeak";\nconst LS_TAB = "indq:tab";\nconst LS_OPEN = "indq:open";')
rep('["apple-mobile-web-app-title", "sounds"],', '["apple-mobile-web-app-title", "questions"],')
assert "sounds:" not in s
pathlib.Path("indq/template.html").write_text(s)
print("ok", len(s))
