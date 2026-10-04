# Шаблон «life / live» собираю из шаблона «would»: тренажёр тот же,
# вкладка правил — своя: пять слов семьи, как звучит, выражения, ошибки, темы по группам.
import pathlib
s = pathlib.Path("would/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Would</title>", "<title>Life и live</title>")
rep("  .algo-m b.pr{color:var(--accent)}\n",
    "  .algo-m b.pr{color:var(--accent)}\n  .s-t b{margin-right:4px;font-family:var(--serif);font-weight:400;font-size:21px;color:var(--accent)}\n  .s-t .ipa{margin-right:4px}\n")

def step(n, word, ipa, meaning, formula):
    return (f'          <li><span class="sn">{n}</span><div><p class="s-t"><b lang="en">{word}</b> <span class="ipa">{ipa}</span> {meaning}</p>'
            f'<p class="s-f" lang="en">{formula}</p></div></li>\n')
O = lambda t: f'<span class="pr">{t}</span>'
steps = (step(1, "life", "/laɪf/", "жизнь, существительное", f'{O("Life")} <i>is short.</i> <span class="sep">·</span> <i>save</i> {O("lives")}')
         + step(2, "live", "/lɪv/", "жить, глагол", f'<i>I</i> {O("live")} <i>here.</i> <span class="sep">·</span> <i>She</i> {O("lives")} <i>alone.</i>')
         + step(3, "alive", "/əˈlaɪv/", "жив&nbsp;— после глагола", f'<i>He’s still</i> {O("alive")}<i>.</i>')
         + step(4, "live", "/laɪv/", "и&nbsp;<b lang=\"en\">living</b>&nbsp;— живой, перед существительным", f'{O("live")} <i>music</i> <span class="sep">·</span> {O("living")} <i>things</i>')
         + step(5, "lively", "/ˈlaɪvli/", "оживлённый, бойкий", f'<i>a</i> {O("lively")} <i>discussion</i>'))

a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Life, live, alive, lively</h1>
      <p class="r-sub">Одна семья&nbsp;— пять слов и&nbsp;два произношения <i lang="en">live</i>. Главное&nbsp;— <b>какая это часть речи и&nbsp;где стоит слово</b>.</p>
      <div class="algo">
        <p class="algo-h">Кто есть кто</p>
        <ol class="steps">
''' + steps + '''        </ol>
        <p class="algo-m">Перед существительным&nbsp;— <b class="pr" lang="en">live</b>, после глагола&nbsp;— <b class="pr" lang="en">alive</b>: <i lang="en">a&nbsp;live fish</i>, но <i lang="en">the fish is&nbsp;alive</i>.</p>
        <p class="algo-note"><i lang="en">lively</i>&nbsp;— прилагательное, хоть и&nbsp;на&nbsp;-ly: наречия от&nbsp;него нет. И&nbsp;не&nbsp;путай <i lang="en">live</i> [lɪv]&nbsp;— жить с&nbsp;<i lang="en">leave</i> [liːv]&nbsp;— уходить.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
    <div class="r-right">
      <h2 class="lbl">Как звучит</h2>
      <div class="mx-wrap">
<!--__SOUNDS__-->
      </div>
      <h2 class="lbl">Выражения</h2>
      <div class="mx-wrap">
<!--__EXPR__-->
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

rep('const LS_STATE = "would:state";\nconst LS_SPEAK = "would:autospeak";\nconst LS_TAB = "would:tab";\nconst LS_OPEN = "would:open";',
    'const LS_STATE = "life:state";\nconst LS_SPEAK = "life:autospeak";\nconst LS_TAB = "life:tab";\nconst LS_OPEN = "life:open";')
rep('["apple-mobile-web-app-title", "would"],', '["apple-mobile-web-app-title", "life / live"],')
rep("// ——— Как звучит: прослушать", "// ——— Как звучит и выражения: прослушать")
rep("// Новые карточки идут вперемешку по темам: значения would чередуются — выбирать приходится по смыслу.",
    "// Новые карточки идут вперемешку по темам: life, live, alive и lively чередуются — выбирать приходится по смыслу и месту в предложении.")
assert "would:" not in s
pathlib.Path("life/template.html").write_text(s)
print("ok", len(s))
