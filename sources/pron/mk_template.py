# Шаблон «my / mine» собираю из шаблона «in / into»: тренажёр тот же,
# вкладка правил — своя: таблица I · me · my · mine, все формы вслух, чего нет в русском, ошибки, темы.
import pathlib
s = pathlib.Path("into/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>In или into</title>", "<title>My или mine</title>")
rep("  .algo-m b.st{color:var(--blue)}\n", '''  .algo-m b.st{color:var(--blue)}
  .algo-m b.good{color:var(--yes-text)}
  .ptab{width:100%;border-collapse:collapse;table-layout:fixed;margin-top:6px}
  .ptab thead th{padding:2px 2px 8px;font-size:14px;font-weight:600;line-height:1.2;color:var(--soft);text-align:center;vertical-align:bottom}
  .ptab thead th small{display:block;margin-top:2px;font-weight:400;font-size:11px;line-height:1.25;color:var(--muted)}
  .ptab td{padding:7px 2px;text-align:center;border-top:1px solid var(--line);font-family:var(--serif);font-size:21px;line-height:1.2}
  .fm-w{margin:0 0 4px;font-family:var(--serif);font-size:22px;line-height:1.3}
  .fm-w .sep{color:var(--muted)}
  .rs{margin:0;font-size:15px;line-height:1.35;color:var(--soft)}
  .re{margin:2px 0 0;font-family:var(--serif);font-size:20px;line-height:1.3}
  .rn{margin:2px 0 0;font-size:13px;line-height:1.35;color:var(--muted)}
''')

a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">I · me · my · mine</h1>
      <p class="r-sub">У&nbsp;каждого лица четыре формы. Спроси себя: <b>кто? кого? чей?</b>&nbsp;— и&nbsp;есть&nbsp;ли после «чей» существительное.</p>
      <div class="algo">
        <p class="algo-h">Четыре формы</p>
        <table class="ptab">
          <thead><tr>
            <th scope="col">Кто?<small>делает</small></th>
            <th scope="col" class="st">Кого?<small>после глагола, предлога</small></th>
            <th scope="col" class="pr">Чей?<small>+&nbsp;сущ.</small></th>
            <th scope="col" class="good">Чей?<small>без сущ.</small></th>
          </tr></thead>
          <tbody>
<!--__TABLE__-->
          </tbody>
        </table>
        <p class="algo-m">Есть существительное&nbsp;— <b class="pr" lang="en">my</b> <i lang="en">car</i>. Нет&nbsp;— <b class="good" lang="en">mine</b>: <i lang="en">The car is&nbsp;mine.</i></p>
        <p class="algo-note">Апострофа нет: <i lang="en">yours, hers, its, ours, theirs</i>. <i lang="en">It’s</i>&nbsp;= it is. Слова «свой» нет&nbsp;— берём по&nbsp;лицу: <i lang="en">she took her bag</i>.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
    <div class="r-right">
      <h2 class="lbl">Все формы вслух</h2>
      <div class="mx-wrap">
<!--__FORMS__-->
      </div>
      <h2 class="lbl">Чего нет в русском</h2>
      <div class="mx-wrap">
<!--__RUEN__-->
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

rep('const LS_STATE = "into:state";\nconst LS_SPEAK = "into:autospeak";\nconst LS_TAB = "into:tab";\nconst LS_OPEN = "into:open";',
    'const LS_STATE = "pron:state";\nconst LS_SPEAK = "pron:autospeak";\nconst LS_TAB = "pron:tab";\nconst LS_OPEN = "pron:open";')
rep('["apple-mobile-web-app-title", "in / into"],', '["apple-mobile-web-app-title", "my / mine"],')
rep("// ——— Сравнения и значения into: прослушать", "// ——— Формы и примеры: прослушать")
rep("// Новые карточки идут вперемешку по темам: где и куда чередуются — выбирать приходится по смыслу.",
    "// Новые карточки идут вперемешку по темам: кто, кого и чей чередуются — выбирать приходится по смыслу.")
rep('function exText(en){ return en.replace(/[\\[\\]]/g, ""); }',
    'function exText(en){ return en.replace(/\\[([^\\]|]+)(?:\\|[soapr])?\\]/g, "$1"); }')
rep('''// […] — предлог: in и on — синий (где?), into и onto — оранжевый (куда?), остальные подчёркнуты
const PREP_CLS = { in: "st", on: "st", into: "pr", onto: "pr" };
function marked(s){
  const f = document.createDocumentFragment();
  const re = /\\[([^\\]]+)\\]/g;''', '''// [слово|x] — форма: s — кто? и r — возвратное (подчёркнуто), o — кого? (синий), a — чей? + сущ. (оранжевый), p — чей? без сущ. (зелёный)
const FORM_CLS = { s: "hl", o: "st", a: "pr", p: "good", r: "hl" };
function marked(s){
  const f = document.createDocumentFragment();
  const re = /\\[([^\\]|]+)(?:\\|([soapr]))?\\]/g;''')
rep('f.append(el("span", PREP_CLS[m[1].toLowerCase()] || "hl", m[1]));', 'f.append(el("span", FORM_CLS[m[2]] || "pr", m[1]));')
assert "into:" not in s and "PREP_CLS" not in s
pathlib.Path("pron/template.html").write_text(s)
print("ok", len(s))
