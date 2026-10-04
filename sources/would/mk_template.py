# Шаблон «would» собираю из шаблона «Пары слов»: тренажёр тот же,
# вкладка правил — своя: семь работ would, как звучит, ошибки, темы по группам.
import pathlib
s = pathlib.Path("pairs/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Пары слов</title>", "<title>Would</title>")
rep("  .pw-tip .tl{font-family:var(--serif);font-size:16px;color:var(--soft)}\n",
    "  .snd-ex{margin:4px 0 0;font-family:var(--serif);font-size:18px;line-height:1.35;color:var(--soft)}\n  .algo-m b.pr{color:var(--accent)}\n")

def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
W = lambda t: f'<span class="pr">{t}</span>'
steps = (step(1, "Вежливость", f'{W("Would")} <i>you…?</i> <span class="sep">·</span> <i>I</i>{W("’d")}&nbsp;<i>like…</i>')
         + step(2, "Воображаемое: «бы»", f'<i>If I had time, I</i> {W("would")}&nbsp;<i>go</i>')
         + step(3, "Прошлое, которого не было", f'<i>I</i> {W("would have")}&nbsp;<i>come</i>')
         + step(4, "Будущее в прошлом: will → would", f'<i>He said he</i> {W("would")}&nbsp;<i>call</i>')
         + step(5, "Привычки в прошлом, «бывало»", f'<i>We</i> {W("would")}&nbsp;<i>go fishing</i>')
         + step(6, "Отказ, «ни в какую»", f'<i>The car</i> {W("wouldn’t")}&nbsp;<i>start</i>')
         + step(7, "Хочу, чтобы другой изменился", f'<i>I wish you</i> {W("would")}&nbsp;<i>stop</i>'))

a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Would</h1>
      <p class="r-sub">Одно из самых занятых слов английского. Чаще всего это русское «бы», вежливость и&nbsp;will, перенесённое в&nbsp;прошлое. Вот все <b>семь его работ</b>.</p>
      <div class="algo">
        <p class="algo-h">Семь работ would</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m">После <b class="pr" lang="en">if</b> would не&nbsp;ставят: <i lang="en">If I&nbsp;had time</i>, не&nbsp;<i lang="en">If I&nbsp;would have</i>.</p>
        <p class="algo-note"><i lang="en">’d</i>&nbsp;— это would или had: <i lang="en">I’d&nbsp;go</i>&nbsp;— would, <i lang="en">I’d&nbsp;gone</i>&nbsp;— had.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
    <div class="r-right">
      <h2 class="lbl">Как звучит</h2>
      <div class="mx-wrap">
<!--__SOUNDS__-->
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

rep('const LS_STATE = "pairs:state";\nconst LS_SPEAK = "pairs:autospeak";\nconst LS_TAB = "pairs:tab";\nconst LS_OPEN = "pairs:open";',
    'const LS_STATE = "would:state";\nconst LS_SPEAK = "would:autospeak";\nconst LS_TAB = "would:tab";\nconst LS_OPEN = "would:open";')
rep('["apple-mobile-web-app-title", "Пары слов"],', '["apple-mobile-web-app-title", "would"],')
rep("// ——— Пары: прослушать", "// ——— Как звучит: прослушать")
rep("// Новые карточки идут вперемешку по темам: пары чередуются — выбирать приходится по смыслу и написанию.",
    "// Новые карточки идут вперемешку по темам: значения would чередуются — выбирать приходится по смыслу.")
# варианты из двух слов (would stop, didn't want) — в одну колонку, без переносов
rep("const cols = longest > 11 ? 1 : (n === 3 ? 3 : 2);", "const cols = longest > 9 ? 1 : (n === 3 ? 3 : 2);")
assert "pairs:" not in s and "Пары слов" not in s
pathlib.Path("would/template.html").write_text(s)
print("ok", len(s))
