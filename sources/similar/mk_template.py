# Шаблон «Похожие слова» собираю из шаблона «Предлоги»: тренажёр тот же,
# вкладка правил — своя: главное по группам, слова с озвучкой, ошибки, темы по группам.
import pathlib, re
s = pathlib.Path("preps/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Предлоги at, on, in</title>", "<title>Похожие слова</title>")

# ——— стили: таблица at/on/in не нужна, нужны пары «слово — подсказка» и строки слов
s, n = re.subn(r"  \.aoi[^\n]*\n", "", s); assert n == 9
rep("  .algo-m .hl{font-family:var(--serif);font-size:20px}\n", "")
rep("  .md-en{margin:0;font-family:var(--serif);font-size:19px;line-height:1.3}\n  .md-ru{margin:2px 0 0;font-size:14px;line-height:1.35;color:var(--muted)}\n",
    '''  .kv{display:grid;grid-template-columns:auto minmax(0,1fr);column-gap:12px;row-gap:4px;align-items:baseline;margin:6px 0 0}
  .kv dt{font-family:var(--serif);font-size:20px;line-height:1.3;color:var(--accent);white-space:nowrap}
  .kv dd{margin:0;font-size:15px;line-height:1.35;color:var(--soft)}
  .s-t b{font-weight:600}
  .algo-m b{color:var(--accent)}
  .wd-w{margin:0;line-height:1.3}
  .wd-w .pr{margin-right:6px;font-family:var(--serif);font-size:22px}
  .wd-ru{font-size:15px;color:var(--muted)}
  .wd-p{margin:3px 0 0;font-family:var(--serif);font-size:17px;line-height:1.35;color:var(--soft)}
''')

# ——— разметка вкладки «Правила»
a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Confusing words</h1>
      <p class="r-sub">По-русски одно слово&nbsp;— «смотреть», «сказать», «поездка», «учить»,&nbsp;— а&nbsp;по-английски несколько. Выбирай не&nbsp;по переводу, а&nbsp;по&nbsp;смыслу: <b>как, кому, зачем</b>.</p>
      <div class="algo">
        <p class="algo-h">Главное</p>
        <ol class="steps">
<!--__KEYS__-->
        </ol>
        <p class="algo-m"><b lang="en">tell</b> и&nbsp;<b lang="en">teach</b>&nbsp;— всегда кому-то: <i lang="en">tell&nbsp;me, teach&nbsp;me</i>.</p>
        <p class="algo-note">А&nbsp;<i lang="en">say</i> и&nbsp;<i lang="en">learn</i>&nbsp;— без человека: <i lang="en">say&nbsp;hello</i>, <i lang="en">learn&nbsp;to&nbsp;drive</i>.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
    <div class="r-right">
<!--__WORDS__-->
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
    'const LS_STATE = "similar:state";\nconst LS_SPEAK = "similar:autospeak";\nconst LS_TAB = "similar:tab";\nconst LS_OPEN = "similar:open";')
rep('["apple-mobile-web-app-title", "at / on / in"],', '["apple-mobile-web-app-title", "Похожие"],')
rep("// ——— Медицинские сочетания: прослушать", "// ——— Слова: прослушать")
rep("// Новые карточки идут вперемешку по темам: время, место и другие значения чередуются — выбирать приходится по смыслу.",
    "// Новые карточки идут вперемешку по темам: группы слов чередуются — выбирать приходится по смыслу, а не по переводу.")
rep('''// […] — предлог: at — синий, on — оранжевый, in — зелёный, остальные подчёркнуты
const PREP_CLS = { at: "st", on: "pr", in: "good" };
''', "// […] — слово в фокусе (оранжевый)\n")
rep('f.append(el("span", PREP_CLS[m[1].toLowerCase()] || "hl", m[1]));', 'f.append(el("span", "pr", m[1]));')
assert "preps" not in s and "PREP_CLS" not in s and "aoi" not in s
pathlib.Path("similar/template.html").write_text(s)
print("ok", len(s))
