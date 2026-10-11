# Шаблон «Инфинитив без to» собираю из шаблона «Three, tree, sheep» (sounds): тот же тренажёр с разметкой [слово|a];
# карточек на слух здесь нет. Вкладка правил — своя: таблица «после чего — правило — примеры», как выбрать, мнемоника.
# Запуск из sources/: python3 bare/mk_template.py   (нужен sounds/template.html — python3 sounds/mk_template.py)
import pathlib
s = pathlib.Path("sounds/template.html").read_text()

def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Three, tree, sheep</title>", "<title>Инфинитив без to</title>")

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
def W(t, c):
    return f'<span class="{c}">{t.replace(" ", "&nbsp;") if len(t) <= 16 else t}</span>'
D = ' <span class="sep">·</span> '
steps = (step(1, "Перед глаголом can, must, should, will, might? Без to — кроме ought to и have to", W("must rest", "pr") + D + W("ought to rest", "good"))
         + step(2, "Перед глаголом do, does, did? Начальная форма, без -s и -ed", W("did you take", "pr") + D + W("doesn't smoke", "pr"))
         + step(3, "make или let + кого-то? Без to; allow, tell, ask — с to", W("let me know", "st") + D + W("allow me to", "good"))
         + step(4, "had better, would rather, why not? Без to; prefer — с to", W("'d better call", "st") + D + W("prefer to stay", "good"))
         + step(5, "Пассив от make, see, hear? to возвращается", W("was made to wait", "good")))

a = s.index('    <div class="r-left">'); b = s.index('    <div class="r-right">')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title">Инфинитив без to</h1>
      <p class="r-sub">Обычно перед глаголом стоит to: <b lang="en">want to go</b>. Но после модальных, do и did, make и let, had better и would rather, see и hear to не нужен: <b lang="en">must go</b>, <b lang="en">let me go</b>. В&nbsp;примерах <b class="pr">слово-сигнал</b> оранжевое, <b class="st">глагол без to</b> синий.</p>
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
        <p class="algo-m"><b class="pr" lang="en">Let me make you wait</b>&nbsp;— в&nbsp;активе to не&nbsp;нужен; <b class="good" lang="en">you were made to wait</b>&nbsp;— в&nbsp;пассиве он&nbsp;возвращается.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
''' + s[b:]

rep('const LS_STATE = "sounds:state";\nconst LS_SPEAK = "sounds:autospeak";\nconst LS_TAB = "sounds:tab";\nconst LS_OPEN = "sounds:open";',
    'const LS_STATE = "bare:state";\nconst LS_SPEAK = "bare:autospeak";\nconst LS_TAB = "bare:tab";\nconst LS_OPEN = "bare:open";')
rep('["apple-mobile-web-app-title", "sounds"],', '["apple-mobile-web-app-title", "no to"],')
assert "sounds:" not in s
pathlib.Path("bare/template.html").write_text(s)
print("ok", len(s))
