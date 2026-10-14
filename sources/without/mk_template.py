# Шаблон «Do without и похожие» собираю из шаблона «Three, tree, sheep» (sounds), как «Like и look like» (like):
# тот же тренажёр с разметкой [фраза|a]; карточек на слух здесь нет.
# Вкладка правил — своя: таблица «образец — правило — примеры», как выбрать, мнемоника, мини-диалоги.
# Запуск из sources/: python3 without/mk_template.py   (нужен sounds/template.html — python3 sounds/mk_template.py)
import pathlib
s = pathlib.Path("sounds/template.html").read_text()

def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Three, tree, sheep</title>", "<title>Do without и похожие</title>")

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
def W(t, c):
    return f'<span class="{c}">{t.replace(" ", "&nbsp;") if len(t) <= 16 else t}</span>'
D = ' <span class="sep">·</span> '
steps = (step(1, "Спокойно обходитесь без чего-то?", W("do without", "pr") + D + W("manage without", "pr"))
         + step(2, "Остались без нужного, тяжело?", W("go without sleep", "pr") + D + W("go without food", "pr"))
         + step(3, "Обходитесь тем, что есть? Денег впритык?", W("make do with", "pr") + D + W("get by on", "pr"))
         + step(4, "Наоборот, хочется, нужно?", W("could do with", "st"))
         + step(5, "Убрать насовсем? Связано с чем-то?", W("do away with", "good") + D + W("have to do with", "good")))

a = s.index('    <div class="r-left">'); b = s.index('    <div class="r-right">')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Do without и&nbsp;похожие</h1>
      <p class="r-sub">Как сказать «обойтись без»: <b lang="en">do without</b>&nbsp;— справиться без чего-то, <b lang="en">go without</b>&nbsp;— остаться без нужного, <b lang="en">make do</b>&nbsp;— обойтись тем, что есть, <b lang="en">get by</b>&nbsp;— свести концы с&nbsp;концами. И&nbsp;рядом фразы с&nbsp;do, которые с&nbsp;ними путают. В&nbsp;примерах <b class="pr">обойтись без</b> оранжевое, <b class="st">нужно, хочется</b> синее, <b class="good">другие фразы с&nbsp;do</b> зелёное.</p>
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
        <p class="algo-m"><b class="st" lang="en">with</b>&nbsp;— нужно, <b class="pr" lang="en">without</b>&nbsp;— можно и&nbsp;без: <i lang="en">I could do with a coffee, but I can do without the cake.</i></p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
''' + s[b:]

rep('const LS_STATE = "sounds:state";\nconst LS_SPEAK = "sounds:autospeak";\nconst LS_TAB = "sounds:tab";\nconst LS_OPEN = "sounds:open";',
    'const LS_STATE = "without:state";\nconst LS_SPEAK = "without:autospeak";\nconst LS_TAB = "without:tab";\nconst LS_OPEN = "without:open";')
rep('["apple-mobile-web-app-title", "sounds"],', '["apple-mobile-web-app-title", "do without"],')
assert "sounds:" not in s
rep('<h2 class="lbl">Одна ситуация&nbsp;— разный смысл</h2>', '<h2 class="lbl">Мини-диалоги</h2>')
pathlib.Path("without/template.html").write_text(s)
print("ok", len(s))
