# Шаблон «For, during, within» собираю из шаблона «Three, tree, sheep» (sounds): тот же тренажёр с разметкой [слово|a];
# карточек на слух здесь нет. Вкладка правил — своя: таблица «слово — смысл — примеры», как выбрать, мнемоника.
# Запуск из sources/: python3 during/mk_template.py   (нужен sounds/template.html — python3 sounds/mk_template.py)
import pathlib
s = pathlib.Path("sounds/template.html").read_text()

def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Three, tree, sheep</title>", "<title>For, during, within</title>")

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
def W(t, c):
    return f'<span class="{c}">{t.replace(" ", "&nbsp;") if len(t) <= 16 else t}</span>'
D = ' <span class="sep">·</span> '
steps = (step(1, "Спрашиваете «сколько?» — for", W("for two hours", "pr") + D + W("for a week", "pr"))
         + step(2, "«Когда, во время чего?» — during, дальше существительное", W("during the night", "st") + D + W("during surgery", "st"))
         + step(3, "Уложиться в срок — within; «через» — in", W("within 24 hours", "good") + D + W("in ten minutes", "hl"))
         + step(4, "Всё время, от начала до конца — throughout; за период, с изменением — over", W("throughout the night", "good") + D + W("over the past year", "hl"))
         + step(5, "Дальше подлежащее и глагол — while", W("while he was asleep", "hl") + D + W("while driving", "hl")))

a = s.index('    <div class="r-left">'); b = s.index('    <div class="r-right">')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">For, during, within</h1>
      <p class="r-sub">По-русски всё это&nbsp;— «в&nbsp;течение». По-английски слово зависит от&nbsp;вопроса: <b lang="en">for</b>&nbsp;— сколько, <b lang="en">during</b>&nbsp;— когда, <b lang="en">within</b>&nbsp;— не&nbsp;позднее, <b lang="en">throughout</b>&nbsp;— всё время, <b lang="en">over</b>&nbsp;— за период.</p>
      <div class="algo">
        <p class="algo-h">Главная таблица</p>
        <table class="mt vt">
          <colgroup><col><col></colgroup>
          <thead><tr><th scope="col">Смысл</th><th scope="col">Примеры</th></tr></thead>
<!--__TABLE__-->
        </table>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Как выбрать</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m"><b class="pr" lang="en">for</b>&nbsp;— сколько, <b class="st" lang="en">during</b>&nbsp;— когда, <b class="good" lang="en">within</b>&nbsp;— успеть, <b class="good" lang="en">throughout</b>&nbsp;— без перерыва, <b class="hl" lang="en">over</b>&nbsp;— что изменилось.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
''' + s[b:]

rep('const LS_STATE = "sounds:state";\nconst LS_SPEAK = "sounds:autospeak";\nconst LS_TAB = "sounds:tab";\nconst LS_OPEN = "sounds:open";',
    'const LS_STATE = "during:state";\nconst LS_SPEAK = "during:autospeak";\nconst LS_TAB = "during:tab";\nconst LS_OPEN = "during:open";')
rep('["apple-mobile-web-app-title", "sounds"],', '["apple-mobile-web-app-title", "during"],')
assert "sounds:" not in s
pathlib.Path("during/template.html").write_text(s)
print("ok", len(s))
