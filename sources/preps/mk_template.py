# Шаблон «Предлоги» собираю из шаблона «two, too или to»: тренажёр тот же (с вариантом «ничего»),
# вкладка правил — своя: картинка at / on / in, медицинские сочетания, темы по группам.
import pathlib
s = pathlib.Path("twotoo/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Two, too или to</title>", "<title>Предлоги at, on, in</title>")

# ——— стили
rep("  .legend{margin:0 2px 10px;font-size:15px;line-height:1.45;color:var(--soft)}",
    '''  .legend{margin:0 2px 10px;font-size:15px;line-height:1.45;color:var(--soft)}
  .hl{color:var(--text);text-decoration:underline;text-decoration-thickness:1.5px;text-underline-offset:3px}
  .aoi{width:100%;border-collapse:collapse;table-layout:fixed;margin-top:4px}
  .aoi col.rh{width:62px}
  .aoi th,.aoi td{padding:6px 4px;text-align:center;vertical-align:middle}
  .aoi thead th{font-family:var(--serif);font-weight:400;font-size:30px;line-height:1}
  .aoi .ic td{padding:2px 4px 0}
  .aoi .ic svg{width:34px;height:34px}
  .aoi .what td{padding:2px 2px 8px;font-size:12px;line-height:1.3;color:var(--muted)}
  .aoi tbody th{padding-left:0;text-align:left;font-size:13px;font-weight:600;color:var(--soft)}
  .aoi tbody td{border-top:1px solid var(--line);font-family:var(--serif);font-size:16px;line-height:1.25}
  .algo-m .hl{font-family:var(--serif);font-size:20px}
  .algo-m i{font-family:var(--serif);font-style:normal;font-size:18px}
  .md{display:grid;grid-template-columns:minmax(0,1fr) 48px;column-gap:10px;align-items:center;padding:8px 10px 8px 14px;border-top:1px solid var(--line)}
  .md:first-child{border-top:0}
  .md-en{margin:0;font-family:var(--serif);font-size:19px;line-height:1.3}
  .md-ru{margin:2px 0 0;font-size:14px;line-height:1.35;color:var(--muted)}
  .md .ex-play{grid-row:1}
  .t-group{margin:22px 0 0;padding:0 2px 7px;border-bottom:1px solid var(--line);font-size:14px;font-weight:600;color:var(--soft)}
  .t-group:first-child{margin-top:4px}''')
rep("  .topics{border-top:1px solid var(--line)}", "  .topics{border-top:0}")

# ——— разметка вкладки «Правила»
ICON_AT = '<svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="5" fill="currentColor"/><circle cx="20" cy="20" r="13" fill="none" stroke="currentColor" stroke-width="2.5"/></svg>'
ICON_ON = '<svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="17" r="7" fill="currentColor"/><path d="M6 27h28" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg>'
ICON_IN = '<svg viewBox="0 0 40 40" aria-hidden="true"><rect x="7" y="7" width="26" height="26" rx="4" fill="none" stroke="currentColor" stroke-width="2.5"/><circle cx="20" cy="20" r="6" fill="currentColor"/></svg>'
a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + f'''    <div class="r-left">
      <h1 class="r-title" lang="en">Prepositions</h1>
      <p class="r-sub">Предлоги at, on, in и&nbsp;другие. В&nbsp;русском «в» и&nbsp;«на» делят мир иначе, поэтому переводить дословно не&nbsp;получится. Опирайся на&nbsp;картинку: <b>точка&nbsp;— поверхность&nbsp;— внутри</b>.</p>
      <div class="algo">
        <p class="algo-h">Главная картинка</p>
        <table class="aoi">
          <colgroup><col class="rh"><col><col><col></colgroup>
          <thead>
            <tr><td></td><th scope="col" class="st" lang="en">at</th><th scope="col" class="pr" lang="en">on</th><th scope="col" class="good" lang="en">in</th></tr>
            <tr class="ic"><td></td><td class="st">{ICON_AT}</td><td class="pr">{ICON_ON}</td><td class="good">{ICON_IN}</td></tr>
            <tr class="what"><td></td><td>точка</td><td>поверхность · день</td><td>внутри · долгий период</td></tr>
          </thead>
          <tbody>
<!--__GRID__-->
          </tbody>
        </table>
        <p class="algo-m"><span class="hl" lang="en">to</span>&nbsp;— движение: быть <i lang="en">at work</i>, идти <i lang="en">to work</i>.</p>
        <p class="algo-note">С&nbsp;next, last, this, every предлог не&nbsp;нужен: <i lang="en">next Monday</i>, <i lang="en">this morning</i>.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
    <div class="r-right">
      <h2 class="lbl">В больнице и в медицине</h2>
      <div class="mx-wrap">
<!--__MED__-->
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
rep('const LS_STATE = "twotoo:state";\nconst LS_SPEAK = "twotoo:autospeak";\nconst LS_TAB = "twotoo:tab";\nconst LS_OPEN = "twotoo:open";',
    'const LS_STATE = "preps:state";\nconst LS_SPEAK = "preps:autospeak";\nconst LS_TAB = "preps:tab";\nconst LS_OPEN = "preps:open";')
rep('["apple-mobile-web-app-title", "two/too/to"],', '["apple-mobile-web-app-title", "at / on / in"],')
rep("// ——— Три слова: прослушать примеры", "// ——— Медицинские сочетания: прослушать")
rep("// Новые карточки идут вперемешку по темам: каждый раз решаешь заново — two, too или to.",
    "// Новые карточки идут вперемешку по темам: время, место и другие значения чередуются — выбирать приходится по смыслу.")
rep('function exText(en){ return en.replace(/[{}|_]/g, ""); }', 'function exText(en){ return en.replace(/[\\[\\]]/g, ""); }')
a = s.index("// {…} — two (синий)"); b = s.index("\n}\n", a) + 3
s = s[:a] + '''// […] — предлог: at — синий, on — оранжевый, in — зелёный, остальные подчёркнуты
const PREP_CLS = { at: "st", on: "pr", in: "good" };
function marked(s){
  const f = document.createDocumentFragment();
  const re = /\\[([^\\]]+)\\]/g;
  let last = 0, m;
  while ((m = re.exec(s))){
    if (m.index > last) f.append(richText(s.slice(last, m.index)));
    f.append(el("span", PREP_CLS[m[1].toLowerCase()] || "hl", m[1]));
    last = re.lastIndex;
  }
  if (last < s.length) f.append(richText(s.slice(last)));
  return f;
}
''' + s[b:]
# темы по группам: время, место, другие значения
rep('''  TOPICS.forEach(t => {
    const item = el("div", "t-item");''', '''  let group = null;
  TOPICS.forEach(t => {
    if (t.group !== group){
      group = t.group;
      box.append(el("p", "t-group", GROUPS[group]));
    }
    const item = el("div", "t-item");''')
pathlib.Path("preps/template.html").write_text(s)
print("ok", len(s))
