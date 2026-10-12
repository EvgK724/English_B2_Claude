# Шаблон «I know the feeling» собираю из шаблона «Three, tree, sheep» (sounds): тот же тренажёр с разметкой [фраза|a];
# карточек на слух здесь нет. Вкладка правил — своя: таблица «когда — смысл — фразы», как выбрать фразу, мнемоника.
# Запуск из sources/: python3 encour/mk_template.py   (нужен sounds/template.html — python3 sounds/mk_template.py)
import pathlib
s = pathlib.Path("sounds/template.html").read_text()

def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Three, tree, sheep</title>", "<title>I know the feeling</title>")

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
def W(t, c):
    return f'<span class="{c}">{t.replace(" ", "&nbsp;") if len(t) <= 16 else t}</span>'
D = ' <span class="sep">·</span> '
steps = (step(1, "Боится, что не&nbsp;получится?", W("It might work out fine", "pr") + D + W("I'm sure it'll be fine", "pr"))
         + step(2, "Сейчас начнётся экзамен, собеседование?", W("Good luck!", "pr") + D + W("Don't worry", "pr"))
         + step(3, "Винит себя или уже не&nbsp;повезло?", W("It's not your fault", "pr") + D + W("You're just unlucky", "pr"))
         + step(4, "Устал, тяжело?", W("It's never easy", "pr") + D + W("Never give up hope", "pr"))
         + step(5, "У&nbsp;вас было так&nbsp;же?", W("I know the feeling", "st") + D + W("That's just like when I lost my phone", "st")))

a = s.index('    <div class="r-left">'); b = s.index('    <div class="r-right">')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">I know the feeling</h1>
      <p class="r-sub">Фразы урока, которые нужно знать наизусть: как <b class="pr">поддержать</b> собеседника и&nbsp;как показать, что <b class="st">у&nbsp;вас было так&nbsp;же</b>. Слушайте и&nbsp;повторяйте вслух целиком&nbsp;— фразы запоминаются кусками, вместе с&nbsp;интонацией.</p>
      <div class="algo">
        <p class="algo-h">Главная таблица</p>
        <table class="mt vt">
          <colgroup><col><col></colgroup>
          <thead><tr><th scope="col">Смысл</th><th scope="col">Фразы</th></tr></thead>
<!--__TABLE__-->
        </table>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Как выбрать фразу</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m">Сначала посочувствуй&nbsp;— <b class="st" lang="en">I&nbsp;know the feeling</b>, потом подбодри&nbsp;— <b class="pr" lang="en">It might work out fine</b>.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
''' + s[b:]

rep('const LS_STATE = "sounds:state";\nconst LS_SPEAK = "sounds:autospeak";\nconst LS_TAB = "sounds:tab";\nconst LS_OPEN = "sounds:open";',
    'const LS_STATE = "encour:state";\nconst LS_SPEAK = "encour:autospeak";\nconst LS_TAB = "encour:tab";\nconst LS_OPEN = "encour:open";')
rep('["apple-mobile-web-app-title", "sounds"],', '["apple-mobile-web-app-title", "feeling"],')
assert "sounds:" not in s
rep('<h2 class="lbl">Одна ситуация&nbsp;— разный смысл</h2>', '<h2 class="lbl">Мини-диалоги</h2>')
pathlib.Path("encour/template.html").write_text(s)
print("ok", len(s))
