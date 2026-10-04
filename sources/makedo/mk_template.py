# Шаблон «make / do» собираю из шаблона «Предлоги»: тренажёр тот же,
# вкладка правил — своя: таблица make/do, таблица спорта, сочетания с озвучкой, ошибки, темы по группам.
import pathlib
s = pathlib.Path("preps/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Предлоги at, on, in</title>", "<title>Make или do</title>")

# ——— стили
rep("  .aoi col.rh{width:62px}", "  .aoi col.rh{width:74px}")
rep("  .aoi .ic td{padding:2px 4px 0}\n  .aoi .ic svg{width:34px;height:34px}\n", "")
rep("  .md-en{margin:0;font-family:var(--serif);font-size:19px;line-height:1.3}\n  .md-ru{margin:2px 0 0;font-size:14px;line-height:1.35;color:var(--muted)}\n",
    '''  .aoi .what td{padding-top:6px;vertical-align:top}
  .algo-2{margin-top:12px}
  .algo-m b.pr{color:var(--accent)}
  .wd-w{margin:0;line-height:1.3}
  .wd-w .ph{margin-right:6px;font-family:var(--serif);font-size:21px}
  .wd-ru{font-size:15px;color:var(--muted)}
  .wd-p{margin:3px 0 0;font-family:var(--serif);font-size:17px;line-height:1.35;color:var(--soft)}
''')

# ——— разметка вкладки «Правила»
a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Make or do?</h1>
      <p class="r-sub">По-русски и&nbsp;то, и&nbsp;другое&nbsp;— «делать». Правило простое: <b>make&nbsp;— создаёшь, do&nbsp;— действуешь</b>. А&nbsp;в&nbsp;спорте ещё <i lang="en">play</i> и&nbsp;<i lang="en">go</i>.</p>
      <div class="algo">
        <p class="algo-h">Make или do</p>
        <table class="aoi">
          <colgroup><col class="rh"><col><col></colgroup>
          <thead>
            <tr><td></td><th scope="col" class="st" lang="en">make</th><th scope="col" class="pr" lang="en">do</th></tr>
            <tr class="what"><td></td><td>создаёшь: не&nbsp;было&nbsp;— стало</td><td>действуешь: работа, дела, обязанности</td></tr>
          </thead>
          <tbody>
<!--__GRID__-->
          </tbody>
        </table>
        <p class="algo-m">Делать вообще&nbsp;— всегда <b class="pr" lang="en">do</b>: <i lang="en">What&nbsp;are&nbsp;you&nbsp;doing?</i></p>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Спорт</p>
        <table class="aoi">
          <thead>
            <tr><th scope="col" class="good" lang="en">play</th><th scope="col" class="st" lang="en">go</th><th scope="col" class="pr" lang="en">do</th></tr>
            <tr class="what"><td>мяч, игра против кого-то</td><td>занятие на&nbsp;-ing</td><td>всё остальное</td></tr>
          </thead>
          <tbody>
<!--__SPORT__-->
          </tbody>
        </table>
        <p class="algo-note"><i lang="en">go swimming</i>&nbsp;— без <i lang="en">to</i>. С&nbsp;<i lang="en">to</i>&nbsp;— только место: <i lang="en">go&nbsp;to&nbsp;the&nbsp;gym</i>.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
    <div class="r-right">
      <h2 class="lbl">Всегда make</h2>
      <div class="mx-wrap">
<!--__MAKE__-->
      </div>
      <h2 class="lbl">Всегда do</h2>
      <div class="mx-wrap">
<!--__DO__-->
      </div>
      <h2 class="lbl">«Сделать»&nbsp;— не make и не do</h2>
      <div class="mx-wrap">
<!--__NEITHER__-->
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

# ——— скрипт
rep('const LS_STATE = "preps:state";\nconst LS_SPEAK = "preps:autospeak";\nconst LS_TAB = "preps:tab";\nconst LS_OPEN = "preps:open";',
    'const LS_STATE = "makedo:state";\nconst LS_SPEAK = "makedo:autospeak";\nconst LS_TAB = "makedo:tab";\nconst LS_OPEN = "makedo:open";')
rep('["apple-mobile-web-app-title", "at / on / in"],', '["apple-mobile-web-app-title", "make / do"],')
rep("// ——— Медицинские сочетания: прослушать", "// ——— Сочетания: прослушать")
rep("// Новые карточки идут вперемешку по темам: время, место и другие значения чередуются — выбирать приходится по смыслу.",
    "// Новые карточки идут вперемешку по темам: make, do и спорт чередуются — выбирать приходится по смыслу.")
rep('''// […] — предлог: at — синий, on — оранжевый, in — зелёный, остальные подчёркнуты
const PREP_CLS = { at: "st", on: "pr", in: "good" };
''', '''// […] — глагол: make и go — синий, do — оранжевый, play — зелёный, остальные подчёркнуты
const VERB_CLS = {};
[["st", "make makes made making go goes went gone going"], ["pr", "do does did done doing"], ["good", "play plays played playing"]]
  .forEach(([cls, forms]) => forms.split(" ").forEach(w => { VERB_CLS[w] = cls; }));
''')
rep('f.append(el("span", PREP_CLS[m[1].toLowerCase()] || "hl", m[1]));', 'f.append(el("span", VERB_CLS[m[1].toLowerCase()] || "hl", m[1]));')
assert "preps" not in s and "PREP_CLS" not in s
pathlib.Path("makedo/template.html").write_text(s)
print("ok", len(s))
