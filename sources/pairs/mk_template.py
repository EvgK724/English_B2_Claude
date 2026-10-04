# Шаблон «Пары слов» собираю из шаблона «Похожие слова»: тренажёр тот же,
# вкладка правил — своя: как не путать, 40 пар с транскрипцией и подсказками, ошибки, темы по группам.
import pathlib
s = pathlib.Path("similar/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Похожие слова</title>", "<title>Пары слов</title>")

# ——— стили: вместо слов с сочетаниями — пары с транскрипцией
a = s.index("  .kv{display:grid"); b = s.index("  .wd-p{"); b = s.index("\n", b) + 1
s = s[:a] + '''  .s-f .sep{color:var(--muted)}
  .pw{margin:0;line-height:1.35}
  .pw + .pw{margin-top:3px}
  .pw-w{margin-right:6px;font-family:var(--serif);font-size:22px}
  .ipa{margin-right:6px;font-size:14px;color:var(--muted);white-space:nowrap}
  .pw-ru{font-size:15px;color:var(--soft)}
  .pw-tip{margin:8px 0 0;font-size:14px;line-height:1.45;color:var(--muted)}
  .pw-tip .tl{font-family:var(--serif);font-size:16px;color:var(--soft)}
''' + s[b:]

# ——— разметка вкладки «Правила»
a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Word pairs</h1>
      <p class="r-sub">40 пар, которые путают даже на&nbsp;B2: одни похожи на&nbsp;вид и&nbsp;на&nbsp;слух, другие&nbsp;— по&nbsp;смыслу. У&nbsp;каждой пары&nbsp;— транскрипция, озвучка и&nbsp;<b>подсказка, как запомнить</b>.</p>
      <div class="algo">
        <p class="algo-h">Как не путать</p>
        <ol class="steps">
          <li><span class="sn">1</span><div><p class="s-t">Какая это часть речи?</p><p class="s-f"><span class="st" lang="en">affect</span>&nbsp;<i>глагол</i> <span class="sep">·</span> <span class="pr" lang="en">effect</span>&nbsp;<i>сущ.</i></p></div></li>
          <li><span class="sn">2</span><div><p class="s-t">Прислушайся: звук [s] или [z]</p><p class="s-f"><span class="st" lang="en">loose</span>&nbsp;<i>[s]</i> <span class="sep">·</span> <span class="pr" lang="en">lose</span>&nbsp;<i>[z]</i> <span class="sep">·</span> <span class="st" lang="en">price</span>&nbsp;<i>[s]</i> <span class="sep">·</span> <span class="pr" lang="en">prize</span>&nbsp;<i>[z]</i></p></div></li>
          <li><span class="sn">3</span><div><p class="s-t">На конце c&nbsp;— существительное, s&nbsp;— глагол</p><p class="s-f"><span class="st" lang="en">device</span> <span class="sep">·</span> <span class="pr" lang="en">devise</span> <i>как</i> <span lang="en">advice&nbsp;· advise</span></p></div></li>
          <li><span class="sn">4</span><div><p class="s-t">Звучат одинаково&nbsp;— выбирай по&nbsp;смыслу</p><p class="s-f"><span class="st" lang="en">principal</span> <span class="sep">·</span> <span class="pr" lang="en">principle</span> <span class="sep">·</span> <span class="st" lang="en">fair</span> <span class="sep">·</span> <span class="pr" lang="en">fare</span></p></div></li>
          <li><span class="sn">5</span><div><p class="s-t">Берегись ложных друзей</p><p class="s-f"><span class="pr" lang="en">sensible</span>&nbsp;<i>разумный</i> <span class="sep">·</span> <span class="pr" lang="en">cooker</span>&nbsp;<i>плита</i></p></div></li>
        </ol>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
    <div class="r-right">
<!--__PAIRS__-->
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
rep('const LS_STATE = "similar:state";\nconst LS_SPEAK = "similar:autospeak";\nconst LS_TAB = "similar:tab";\nconst LS_OPEN = "similar:open";',
    'const LS_STATE = "pairs:state";\nconst LS_SPEAK = "pairs:autospeak";\nconst LS_TAB = "pairs:tab";\nconst LS_OPEN = "pairs:open";')
rep('["apple-mobile-web-app-title", "Похожие"],', '["apple-mobile-web-app-title", "Пары слов"],')
rep("// ——— Слова: прослушать", "// ——— Пары: прослушать")
rep("// Новые карточки идут вперемешку по темам: группы слов чередуются — выбирать приходится по смыслу, а не по переводу.",
    "// Новые карточки идут вперемешку по темам: пары чередуются — выбирать приходится по смыслу и написанию.")
assert "similar" not in s
pathlib.Path("pairs/template.html").write_text(s)
print("ok", len(s))
