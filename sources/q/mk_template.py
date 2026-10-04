# Шаблон «Вопросы» собираю из шаблона «Сравнения»: тренажёр тот же,
# вкладка правил — своя: как построить вопрос (шаги и схема), «сколько, как давно» (таблица), ситуации, ошибки, темы.
import pathlib
s = pathlib.Path("cmp/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Сравнения</title>", "<title>Вопросы</title>")
rep("  .vt col.v{width:40%}\n", "  .vt col.v{width:46%}\n")

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
P = lambda t: f'<span class="pr">{t}</span>'
D = ' <span class="sep">·</span> '
nw = lambda t: f'<span class="nw">{t}</span>'
steps = (step(1, "Есть be, can, will или have в&nbsp;Perfect?", nw(P("Are") + " you in pain?") + D + nw(P("Can") + " you lift it?"))
         + step(2, "Обычный глагол?", nw(P("Do") + " you smoke?") + D + nw("When " + P("did") + " it start?"))
         + step(3, "Кто или что&nbsp;— сам исполнитель?", nw("Who " + P("called") + "?") + D + nw("What " + P("happened") + "?") + ' <i>без do</i>')
         + step(4, "Вежливо: Could you tell me…?", nw("…when " + P("it started")) + ' <i>порядок как в&nbsp;утверждении</i>'))

a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Questions</h1>
      <p class="r-sub">По-русски вопрос делают интонацией: «Вы курите?» По-английски нужен <b>помощник перед подлежащим</b>: <i lang="en">Do you smoke? Are you in pain?</i> Тренируемся на&nbsp;том, что спрашивают у&nbsp;пациента.</p>
      <div class="algo">
        <p class="algo-h">Как построить вопрос</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m">Схема: вопрос&nbsp;— помощник&nbsp;— кто&nbsp;— действие<br><b lang="en"><span class="st">When</span> <span class="pr">did</span> <span class="good">it</span> start?</b></p>
        <p class="algo-note">После do, does, did глагол без окончаний: <i lang="en">Does it hurt? Did it start?</i></p>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Сколько, как давно</p>
        <table class="vt">
          <colgroup><col class="v"><col></colgroup>
          <tbody>
<!--__TABLE__-->
          </tbody>
        </table>
        <p class="algo-note">«Как давно у&nbsp;вас…» с&nbsp;болью, которая есть и&nbsp;сейчас,&nbsp;— <i lang="en">How long have you had…?</i>, не&nbsp;<i lang="en">How long do you have</i>.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
    <div class="r-right">
      <h2 class="lbl">Одна ситуация&nbsp;— разный смысл</h2>
      <div class="mx-wrap">
<!--__CONTRAST__-->
      </div>
      <h2 class="lbl">Частые ошибки</h2>
      <div class="mx-wrap">
        <ul class="errs">
<!--__ERRORS__-->
        </ul>
      </div>
      <h2 class="lbl">Темы</h2>
      <div class="topics" id="topics"></div>
    </div>
''' + s[b:]

rep('const LS_STATE = "cmp:state";\nconst LS_SPEAK = "cmp:autospeak";\nconst LS_TAB = "cmp:tab";\nconst LS_OPEN = "cmp:open";',
    'const LS_STATE = "q:state";\nconst LS_SPEAK = "q:autospeak";\nconst LS_TAB = "q:tab";\nconst LS_OPEN = "q:open";')
rep('["apple-mobile-web-app-title", "Сравнения"],', '["apple-mobile-web-app-title", "Вопросы"],')
rep("// Новые карточки идут вперемешку по темам: формы, than и as, «насколько», «во сколько раз» и язык статей чередуются.",
    "// Новые карточки идут вперемешку по темам: do и did, вопросы без do, вежливые вопросы и расспрос пациента чередуются.")
assert "cmp:" not in s
pathlib.Path("q/template.html").write_text(s)
print("ok", len(s))
