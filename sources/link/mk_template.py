# Шаблон «Связки» собираю из шаблона «Пересказ»: тренажёр тот же,
# вкладка правил — своя: что идёт после связки (таблица), связки в начале предложения, ситуации, ошибки, темы.
import pathlib
s = pathlib.Path("rep/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Пересказ</title>", "<title>Связки</title>")
rep("  .vt .r{display:block;margin-top:2px;font-size:13px;line-height:1.35;color:var(--muted)}\n",
    "  .vt .r{display:block;margin-top:2px;font-size:13px;line-height:1.35;color:var(--muted)}\n"
    "  .mt.af thead th{padding:2px 8px 8px 0}\n"
    "  .mt.af td{padding:12px 8px 12px 0}\n"
    "  .mt.af td .f{font-size:20px}\n"
    "  .mt.af td small{margin-top:4px}\n"
    "  .vt.sv col.v{width:40%}\n"
    "  .mt.af .sep{color:var(--muted)}\n")

a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Linking words</h1>
      <p class="r-sub">Связки склеивают мысли в&nbsp;текст. Главное&nbsp;— что идёт после: целое предложение (<i lang="en">although he was tired</i>) или существительное (<i lang="en">despite his age</i>).</p>
      <div class="algo">
        <p class="algo-h">Что после связки</p>
        <table class="mt af">
          <colgroup><col><col></colgroup>
          <thead><tr><th scope="col">+&nbsp;предложение</th><th scope="col">+&nbsp;сущ. или -ing</th></tr></thead>
          <tbody>
<!--__AFTER__-->
          </tbody>
        </table>
        <p class="algo-note"><i lang="en">despite</i>&nbsp;— без <i lang="en">of</i>, <i lang="en">in spite of</i>&nbsp;— с&nbsp;<i lang="en">of</i>. Нужно предложение&nbsp;— добавь <i lang="en">the fact that</i>: <i lang="en">despite the fact that he was young</i>.</p>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">В начале нового предложения</p>
        <table class="vt sv">
          <colgroup><col class="v"><col></colgroup>
          <tbody>
<!--__START__-->
          </tbody>
        </table>
        <p class="algo-m"><b class="pr" lang="en">but</b> внутри предложения, <b class="st" lang="en">However,</b> в&nbsp;начале нового: <i lang="en">He is 85, but he drives. He is 85. However, he drives.</i></p>
        <p class="algo-note">После <i lang="en">However, Therefore, In addition</i> ставят запятую.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
    <div class="r-right">
      <h2 class="lbl">Одна мысль&nbsp;— разные связки</h2>
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

rep('const LS_STATE = "rep:state";\nconst LS_SPEAK = "rep:autospeak";\nconst LS_TAB = "rep:tab";\nconst LS_OPEN = "rep:open";',
    'const LS_STATE = "link:state";\nconst LS_SPEAK = "link:autospeak";\nconst LS_TAB = "link:tab";\nconst LS_OPEN = "link:open";')
rep('["apple-mobile-web-app-title", "Пересказ"],', '["apple-mobile-web-app-title", "Связки"],')
rep("// Новые карточки идут вперемешку по темам: say и tell, сдвиг времён, вопросы, просьбы и глаголы пересказа чередуются.",
    "// Новые карточки идут вперемешку по темам: хотя и несмотря на, причина и следствие, цель и условие чередуются.")
assert "rep:state" not in s and "Пересказ" not in s
pathlib.Path("link/template.html").write_text(s)
print("ok", len(s))
