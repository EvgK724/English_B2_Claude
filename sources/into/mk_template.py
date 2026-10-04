# Шаблон «in / into» собираю из шаблона «life / live»: тренажёр тот же,
# вкладка правил — своя: картинка «где или куда», пары-сравнения, значения into, ошибки, темы по группам.
import pathlib
s = pathlib.Path("life/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Life и live</title>", "<title>In или into</title>")
rep("  .s-t .ipa{margin-right:4px}\n", '''  .s-t .ipa{margin-right:4px}
  .algo-m b.st{color:var(--blue)}
  .g4{width:100%;border-collapse:collapse;table-layout:fixed;margin-top:6px}
  .g4 col.rh{width:76px}
  .g4 thead th{padding:4px 4px 8px;font-size:14px;font-weight:600;color:var(--soft);text-align:center;vertical-align:bottom}
  .g4 thead th small{display:block;font-weight:400;font-size:12px;color:var(--muted)}
  .g4 tbody th{padding:12px 0;text-align:left;vertical-align:middle;font-size:13px;font-weight:600;line-height:1.3;color:var(--soft);border-top:1px solid var(--line)}
  .g4 td{padding:12px 4px 10px;text-align:center;vertical-align:top;border-top:1px solid var(--line)}
  .g4 thead td{border-top:0}
  .g4 svg{display:block;width:40px;height:40px;margin:0 auto 4px}
  .g4 .w{display:block;font-family:var(--serif);font-size:28px;line-height:1.1}
  .g4 .e{display:block;margin-top:4px;font-family:var(--serif);font-size:15px;line-height:1.3;color:var(--soft)}
  .cp-en{margin:0;font-family:var(--serif);font-size:19px;line-height:1.3}
  .cp-ru{margin:1px 0 0;font-size:14px;line-height:1.35;color:var(--muted)}
  .cp-ru + .cp-en{margin-top:8px}
''')

I_IN = '<svg viewBox="0 0 40 40" aria-hidden="true"><rect x="7" y="7" width="26" height="26" rx="4" fill="none" stroke="currentColor" stroke-width="2.5"/><circle cx="20" cy="20" r="6" fill="currentColor"/></svg>'
I_INTO = '<svg viewBox="0 0 40 40" aria-hidden="true"><rect x="17" y="7" width="20" height="26" rx="4" fill="none" stroke="currentColor" stroke-width="2.5"/><path d="M3 20h20" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/><path d="M19 14l7 6-7 6" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
I_ON = '<svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="19" r="7" fill="currentColor"/><path d="M5 30h30" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg>'
I_ONTO = '<svg viewBox="0 0 40 40" aria-hidden="true"><path d="M5 33h30" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M20 4v20" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/><path d="M13 18l7 7 7-7" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def cell(cls, icon, word, ex):
    return f'<td class="{cls}">{icon}<span class="w" lang="en">{word}</span><span class="e" lang="en">{ex}</span></td>'

a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + f'''    <div class="r-left">
      <h1 class="r-title" lang="en">In or into? On or onto?</h1>
      <p class="r-sub">По-русски «в» и&nbsp;«на» отвечают на&nbsp;оба вопроса. В&nbsp;английском спроси себя: <b>где?</b>&nbsp;— in, on; <b>куда?</b>&nbsp;— into, onto.</p>
      <div class="algo">
        <p class="algo-h">Где или куда</p>
        <table class="g4">
          <colgroup><col class="rh"><col><col></colgroup>
          <thead><tr><td></td><th scope="col">Где?<small>на месте</small></th><th scope="col">Куда?<small>движение</small></th></tr></thead>
          <tbody>
            <tr><th scope="row">внутри</th>{cell("st", I_IN, "in", "in the room")}{cell("pr", I_INTO, "into", "into the room")}</tr>
            <tr><th scope="row">на поверх&shy;ности</th>{cell("st", I_ON, "on", "on the table")}{cell("pr", I_ONTO, "onto", "onto the table")}</tr>
          </tbody>
        </table>
        <p class="algo-m">Движение&nbsp;— <b class="pr" lang="en">into</b>, <b class="pr" lang="en">onto</b>. На&nbsp;месте&nbsp;— <b class="st" lang="en">in</b>, <b class="st" lang="en">on</b>.</p>
        <p class="algo-note">Без существительного после предлога&nbsp;— только in, on: <i lang="en">Come in!</i> <i lang="en">Hold on!</i> Транспорт: <i lang="en">in the car</i>, но <i lang="en">on the bus</i>.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
    <div class="r-right">
      <h2 class="lbl">Один глагол&nbsp;— разный смысл</h2>
      <div class="mx-wrap">
<!--__CONTRAST__-->
      </div>
      <h2 class="lbl">into&nbsp;— не&nbsp;только «внутрь»</h2>
      <div class="mx-wrap">
<!--__INTO__-->
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

rep('const LS_STATE = "life:state";\nconst LS_SPEAK = "life:autospeak";\nconst LS_TAB = "life:tab";\nconst LS_OPEN = "life:open";',
    'const LS_STATE = "into:state";\nconst LS_SPEAK = "into:autospeak";\nconst LS_TAB = "into:tab";\nconst LS_OPEN = "into:open";')
rep('["apple-mobile-web-app-title", "life / live"],', '["apple-mobile-web-app-title", "in / into"],')
rep("// ——— Как звучит и выражения: прослушать", "// ——— Сравнения и значения into: прослушать")
rep("// Новые карточки идут вперемешку по темам: life, live, alive и lively чередуются — выбирать приходится по смыслу и месту в предложении.",
    "// Новые карточки идут вперемешку по темам: где и куда чередуются — выбирать приходится по смыслу.")
rep("// […] — слово в фокусе (оранжевый)\n", '''// […] — предлог: in и on — синий (где?), into и onto — оранжевый (куда?), остальные подчёркнуты
const PREP_CLS = { in: "st", on: "st", into: "pr", onto: "pr" };
''')
rep('f.append(el("span", "pr", m[1]));', 'f.append(el("span", PREP_CLS[m[1].toLowerCase()] || "hl", m[1]));')
assert "life:" not in s
pathlib.Path("into/template.html").write_text(s)
print("ok", len(s))
