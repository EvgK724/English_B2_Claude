# Шаблон «Сокращения» собираю из шаблона «manage to»: оболочка, озвучка, облако, вкладки и темы те же,
# тренировка — карточки для заучивания (english-flashcards): лицевая сторона, оборот, «не знаю / почти / знаю», свайпы.
import pathlib
s = pathlib.Path("manage/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

def cut(a, b, new):
    """Заменить кусок от метки a (включительно) до метки b (не включая)."""
    global s
    i = s.index(a); j = s.index(b, i)
    s = s[:i] + new + s[j:]

PLAY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9.5h3.5L12 5.5v13l-4.5-4H4z"/><path d="M15.5 9a4 4 0 0 1 0 6"/></svg>'
SAY = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9.5h3.5L12 5.5v13l-4.5-4H4z"/><path d="M15.5 9a4 4 0 0 1 0 6"/><path d="M18.2 6.4a7.6 7.6 0 0 1 0 11.2"/></svg>'

# ——— Заголовок и цвета
rep("<title>Manage to и похожие</title>", "<title>Сокращения</title>")
rep("    --yes-text:#9ad0b4;\n", "    --yes-text:#9ad0b4;\n    --almost:#9a7f3d;\n    --almost-text:#dcc38a;\n")

# ——— Стили карточки и правил
rep("  :focus-visible{outline:2px solid var(--accent);outline-offset:2px}\n", '''  /* ——— Карточка */
  [hidden]{display:none!important}
  .fc{cursor:pointer;touch-action:pan-y;-webkit-user-select:none;user-select:none;transition:transform .2s ease,border-color .15s ease}
  .fc.drag{transition:border-color .15s ease}
  .fc.lean-yes{border-color:var(--yes)}
  .fc.lean-no{border-color:var(--no)}
  .front{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;padding-bottom:36px;text-align:center}
  .ab{margin:0;font-family:var(--serif);font-weight:400;font-size:76px;line-height:1.05;letter-spacing:.01em}
  .ab.m{font-size:58px}
  .ab.s{font-size:46px}
  .ctx{margin:0;font-family:var(--serif);font-size:21px;color:var(--soft)}
  .front .hint{max-width:17em;font-size:16px;line-height:1.4}
  .fc .back{flex:1;gap:12px;padding-top:0;border-top:0}
  .say-front{border-radius:50%}
  .b-head{margin:0;display:flex;flex-wrap:wrap;align-items:baseline;column-gap:14px}
  .ab2{font-family:var(--serif);font-size:46px;line-height:1.1}
  .ipa2{font-size:19px;color:var(--blue);white-space:nowrap}
  .gram{margin:-8px 0 0;font-size:15px;line-height:1.35;color:var(--muted)}
  .fl{display:grid;grid-template-columns:minmax(0,1fr) 48px;column-gap:10px;align-items:center}
  .full{margin:0;font-family:var(--serif);font-size:25px;line-height:1.25;text-wrap:pretty}
  .fl .ex-play{grid-column:2;grid-row:1}
  .ru{margin:-4px 0 0;font-size:22px;line-height:1.35}
  .note{margin:0;font-size:16px;line-height:1.45;color:var(--soft)}
  .exb{display:grid;grid-template-columns:minmax(0,1fr) 48px;gap:4px 10px;align-items:start;padding-top:14px;border-top:1px solid var(--line)}
  .swipe{margin:auto 0 0;text-align:center;font-size:13px;color:var(--muted)}
  .done{flex:1;display:flex;flex-direction:column;justify-content:center;gap:12px}
  .done-t{margin:0;font-family:var(--serif);font-size:34px;line-height:1.15}
  .done-p{margin:0;font-size:18px;line-height:1.5;color:var(--soft)}
  .grades{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
  .grades .big{min-height:62px;padding:0 4px}
  .g0{border-color:var(--no);color:var(--no-text)}
  .g1{border-color:var(--almost);color:var(--almost-text)}
  .g2{border-color:var(--yes);color:var(--yes-text)}

  /* ——— Правила: буквы, a/an, списки тем */
  .s-f .ipa{font-family:var(--sans);font-size:14px;color:var(--muted)}
  .lts{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:8px;margin-top:10px}
  .lt{min-height:66px;padding:6px 2px;border:1px solid var(--line-2);border-radius:12px;background:transparent;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;cursor:pointer}
  .lt:active{background:var(--raise)}
  .lt-l{font-family:var(--serif);font-size:27px;line-height:1}
  .lt-i{font-size:13px;line-height:1.2;color:var(--blue);white-space:nowrap}
  .algo-m .ltrs{display:block;margin-top:4px;font-family:var(--serif);font-weight:400;font-size:22px;letter-spacing:.04em;color:var(--accent)}
  .abl{display:flex;flex-direction:column}
  .abl-row{display:grid;grid-template-columns:minmax(0,1fr) 48px;column-gap:10px;align-items:center;padding:9px 0;border-top:1px solid var(--line)}
  .abl-row:first-child{border-top:0}
  .abl-row .ex-play{grid-row:auto}
  .abl-t{margin:0;line-height:1.3}
  .abl-a{margin-right:8px;font-family:var(--serif);font-size:21px;color:var(--text)}
  .abl-f{font-family:var(--serif);font-size:16px;color:var(--soft)}
  .abl-r{display:block;margin-top:2px;font-size:14px;color:var(--muted)}
  .known .abl-a::after{content:"✓";margin-left:6px;font-family:var(--sans);font-size:14px;color:var(--yes-text)}

  @media (max-height:43.7em){
    .card{padding:16px 16px 14px;gap:12px}
    .fc .back{gap:9px}
    .ab{font-size:64px}
    .ab2{font-size:38px}
    .ipa2{font-size:17px}
    .gram{margin-top:-5px}
    .full{font-size:22px}
    .ru{font-size:20px}
    .note{font-size:15px;line-height:1.4}
    .exb{padding-top:10px}
    .exb .ex-en{font-size:18px}
    .swipe{display:none}
  }

  :focus-visible{outline:2px solid var(--accent);outline-offset:2px}
''')
rep("@media (prefers-reduced-motion:reduce){.bar-fill,.t-chev{transition:none}",
    "@media (prefers-reduced-motion:reduce){.bar-fill,.t-chev,.fc{transition:none}")
cut("  body.wide #drill{display:grid;", "  body.wide #rule{",
    "  body.wide #drill,body.wide .meta,body.wide .bar{width:100%;max-width:880px;margin-left:auto;margin-right:auto}\n"
    "  body.wide .fc .back{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);grid-template-rows:auto auto auto auto 1fr auto;column-gap:36px;row-gap:12px}\n"
    "  body.wide .fc .back > *{grid-column:1}\n"
    "  body.wide .fc .exb{grid-column:2;grid-row:1 / span 5;align-self:center;padding:0 0 0 30px;border-top:0;border-left:1px solid var(--line)}\n"
    "  body.wide .fc .swipe{grid-column:1 / -1;grid-row:6}\n")

# ——— Тренировка: карточка
cut('  <section class="view" id="drill"', '  <section class="rule" id="rule"', f'''  <section class="view" id="drill" role="tabpanel" aria-labelledby="tabDrill" hidden>
    <article class="card fc" id="card">
      <span class="kind" id="kind">В больнице</span>
      <div class="front" id="front">
        <p class="ab" id="ab" lang="en"></p>
        <p class="ctx" id="ctx" lang="en" hidden></p>
        <button class="say say-front" id="say" type="button" aria-label="Прослушать сокращение">
          {SAY}
        </button>
        <p class="hint" id="hint">Вспомни расшифровку и&nbsp;перевод, потом открой карточку</p>
      </div>
      <div class="back" id="back" aria-live="polite" hidden>
        <p class="b-head"><span class="ab2" id="ab2" lang="en"></span><span class="ipa2" id="ipa"></span></p>
        <p class="gram" id="gram"></p>
        <div class="fl">
          <p class="full" id="full" lang="en"></p>
          <button class="ex-play" id="playL" type="button" aria-label="Прослушать расшифровку">{PLAY}</button>
        </div>
        <p class="ru" id="ru"></p>
        <p class="note" id="note"></p>
        <div class="exb">
          <p class="ex-en" id="exEn" lang="en"></p>
          <button class="ex-play" id="playE" type="button" aria-label="Прослушать пример">{PLAY}</button>
          <p class="ex-ru" id="exRu"></p>
        </div>
        <p class="swipe" aria-hidden="true">← не&nbsp;знаю · знаю&nbsp;→</p>
      </div>
      <div class="done" id="done" hidden>
        <p class="done-t" id="doneT">На сегодня всё</p>
        <p class="done-p" id="doneP"></p>
      </div>
    </article>
    <div class="actions" id="actShow">
      <button class="big primary" id="show" type="button">Показать</button>
    </div>
    <div class="grades" id="actGrade" hidden>
      <button class="big g0" type="button" data-g="0">Не знаю</button>
      <button class="big g1" type="button" data-g="1">Почти</button>
      <button class="big g2" type="button" data-g="2">Знаю</button>
    </div>
    <div class="actions" id="actDone" hidden>
      <button class="big primary" id="more" type="button">Ещё 10 новых</button>
      <button class="big" id="toRule" type="button">Правила</button>
    </div>
  </section>

''')

# ——— Правила
def step(n, title, formula):
    return f'          <li><span class="sn">{n}</span><div><p class="s-t">{title}</p><p class="s-f" lang="en">{formula}</p></div></li>\n'
D = ' <span class="sep">·</span> '
def ab(t, ipa=None):
    x = f'<span class="pr">{t}</span>'
    if ipa:
        x += f' <span class="ipa">{ipa}</span>'
    return f'<span class="nw">{x}</span>'
def art(a, rest, cls="pr"):
    return f'<span class="nw"><span class="{cls}">{a}</span> {rest}</span>'
def zero(t):
    return f'<span class="nw"><span class="zero">∅</span>{t}</span>'

read = (step(1, "Обычно&nbsp;— по&nbsp;буквам, ударение на&nbsp;последнюю", ab("CT", "/ˌsiː ˈtiː/") + D + ab("FBI", "/ˌef biː ˈaɪ/"))
        + step(2, "Складывается в&nbsp;слово&nbsp;— читают словом", ab("NATO", "/ˈneɪtəʊ/") + D + ab("PIN", "/pɪn/"))
        + step(3, "Латинские вслух заменяют словами",
               '<span class="nw"><span class="pr">e.g.</span> → for example</span>' + D + '<span class="nw"><span class="pr">i.e.</span> → that is</span>'))
aan = (step(1, "Первый звук гласный&nbsp;→ an", art("an", "MRI") + D + art("an", "FBI agent") + D + art("an", "HR manager"))
       + step(2, "Первый звук согласный&nbsp;→ a", art("a", "CT scan", "st") + D + art("a", "UK citizen", "st") + D + art("a", "UNESCO site", "st")))
the = (step(1, "Название по&nbsp;буквам&nbsp;→ the", art("the", "FBI") + D + art("the", "UN") + D + art("the", "USA"))
       + step(2, "Название словом&nbsp;→ без артикля", zero("NATO") + D + zero("NASA") + D + zero("UNESCO"))
       + step(3, "Много&nbsp;→ просто -s", 'two CT<span class="pr">s</span>' + D + 'MRI<span class="pr">s</span>' + D + 'CEO<span class="pr">s</span>'))

cut('    <div class="r-left">', '  </section>\n</div>', '''    <div class="r-left">
      <h1 class="r-title" lang="en">Abbreviations</h1>
      <p class="r-sub">Сокращение читают по&nbsp;буквам или как слово. <b>Артикль выбирают по&nbsp;звуку, а&nbsp;не по&nbsp;букве</b>: <i lang="en">an MRI</i>, но <i lang="en">a UN report</i>.</p>
      <div class="algo">
        <p class="algo-h">Как читать</p>
        <ol class="steps">
''' + read + '''        </ol>
        <p class="algo-note">ASAP и&nbsp;LOL читают и&nbsp;так, и&nbsp;так: по&nbsp;буквам или словом.</p>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">Трудные буквы</p>
        <div class="lts">
<!--__LETTERS__-->
        </div>
        <p class="algo-note">H&nbsp;— /eɪtʃ/, не&nbsp;«аш»; R&nbsp;— /ɑː/, не&nbsp;«эр»; Z&nbsp;— /zed/, в&nbsp;Америке /ziː/. Нажми на&nbsp;букву, чтобы услышать.</p>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">a или an</p>
        <ol class="steps">
''' + aan + '''        </ol>
        <p class="algo-m">an&nbsp;— перед буквами <b class="ltrs" lang="en">A E F H I L M N O R S X</b></p>
        <p class="algo-note">Проверка: произнеси первую букву вслух. F&nbsp;— /ef/, M&nbsp;— /em/, H&nbsp;— /eɪtʃ/: в&nbsp;начале гласный звук&nbsp;— значит <i lang="en">an</i>. U&nbsp;— /juː/: в&nbsp;начале [j]&nbsp;— значит <i lang="en">a</i>.</p>
      </div>
      <div class="algo algo-2">
        <p class="algo-h">the и&nbsp;множественное число</p>
        <ol class="steps">
''' + the + '''        </ol>
        <p class="algo-note">Апостроф не&nbsp;нужен: <i lang="en">CT's</i>&nbsp;— ошибка.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
    <div class="r-right">
      <h2 class="lbl">Частые ошибки</h2>
      <div class="mx-wrap">
        <ul class="errs">
<!--__ERRORS__-->
        </ul>
      </div>
      <h2 class="lbl">Темы</h2>
      <div class="topics" id="topics"></div>
    </div>
''')

# ——— Скрипт: состояние и мелочи
rep('const LS_STATE = "manage:state";\nconst LS_SPEAK = "manage:autospeak";\nconst LS_TAB = "manage:tab";\nconst LS_OPEN = "manage:open";',
    'const LS_STATE = "abbr:state";\nconst LS_SPEAK = "abbr:autospeak";\nconst LS_TAB = "abbr:tab";\nconst LS_OPEN = "abbr:open";')
rep("let answered = false;\n", "let flipped = false;\n")
rep("let shownOpts = [];\n", "")
rep('["apple-mobile-web-app-title", "manage to"],', '["apple-mobile-web-app-title", "Сокращения"],')
rep('function topicLabel(n){ return n === MIXED_TOPIC ? "Всё вместе" : "Тема " + n + " · " + TOPIC_BY[n].title; }\nfunction label(a){ return a === "" ? "ничего" : a; }\n', "")
cut("// ——— Предложение с пропуском", "// ——— Синхронизация прогресса", '''// ——— Разметка: [x] — оранжевым (буквы-источники в расшифровке, сокращение в примере)
function richText(s){
  const f = document.createDocumentFragment();
  f.append(String(s).replace(/ → /g, "\\u00a0→\\u00a0"));
  return f;
}
function marked(s){
  const f = document.createDocumentFragment();
  const re = /\\[([^\\]]+)\\]/g;
  let last = 0, m;
  while ((m = re.exec(s))){
    if (m.index > last) f.append(richText(s.slice(last, m.index)));
    f.append(el("span", "pr", m[1]));
    last = re.lastIndex;
  }
  if (last < s.length) f.append(richText(s.slice(last)));
  return f;
}

''')
rep("if (mode === \"main\" && stats.first === 0 && !answered){ buildMain(); render(); }",
    "if (mode === \"main\" && stats.first === 0 && !flipped){ buildMain(); render(); }")
rep('// ——— Ситуации: прослушать\ndocument.querySelectorAll(".mm-play")',
    '// ——— Буквы в правилах: прослушать\ndocument.querySelectorAll(".lt")')
rep("// Новые карточки идут вперемешку по темам: удалось, справиться и успеть чередуются — выбирать приходится по смыслу и конструкции.",
    "// Новые карточки идут вперемешку по темам: больница, статьи, работа, организации, быт и переписка чередуются.")

# ——— Скрипт: карточка
cut("function renderOpts(card){", "// ——— Правила", '''// ——— Карточка: лицевая сторона — сокращение; оборот — расшифровка, перевод, пример
function sayFront(){
  const c = queue[index];
  if (c && !flipped) playClip(c.id + "-a", c.sa, 0.8);
}
function render(){
  stopAudio();
  flipped = false;
  const card = queue[index];
  const box = $("card");
  box.scrollTop = 0;
  box.style.transform = "";
  box.classList.remove("lean-yes", "lean-no");
  if (!card){ renderDone(); return; }
  show("kind", true);
  $("kind").textContent = TOPIC_BY[card.t].title;
  show("front", true);
  show("back", false);
  show("done", false);
  const ab = $("ab");
  ab.textContent = card.ab;
  ab.className = "ab" + (card.ab.length > 7 ? " s" : card.ab.length > 4 ? " m" : "");
  $("ctx").textContent = card.ctx || "";
  show("ctx", !!card.ctx);
  show("actShow", true);
  show("actGrade", false);
  show("actDone", false);
  const prefix = mode === "topic" ? TOPIC_BY[topicN].title + " · " : mode === "mixed" ? "Всё вместе · " : "";
  $("status").textContent = prefix + "Карточка " + (index + 1) + " из " + queue.length;
  setBar(index, queue.length);
  if (autoSpeak && !$("drill").hidden) sayFront();
  else preloadClip(card.id + "-a");
}

function fillBack(card){
  $("ab2").textContent = card.ab;
  $("ipa").textContent = card.ipa;
  $("gram").textContent = card.gram;
  const full = $("full"); full.textContent = ""; full.append(marked(card.full));
  $("ru").textContent = card.ru;
  const note = $("note"); note.textContent = "";
  if (card.note) note.append(richText(card.note));
  show("note", !!card.note);
  const ex = $("exEn"); ex.textContent = ""; ex.append(marked(card.ex));
  $("exRu").textContent = card.exRu;
}

function flip(){
  const card = queue[index];
  if (!card || flipped) return;
  flipped = true;
  fillBack(card);
  show("front", false);
  show("back", true);
  show("actShow", false);
  show("actGrade", true);
  $("card").scrollTop = 0;
  if (autoSpeak) playClip(card.id + "-l", card.sl, 0.85);
  else stopAudio();
}

// «Не знаю» — завтра и ещё раз в этой же сессии; «почти» — тот же интервал; «знаю» — следующий: 1 → 3 → 7 → 16 дней
function grade(g){
  const card = queue[index];
  if (!card || !flipped) return;
  if (!seen.has(card.id)){
    seen.add(card.id);
    stats.first++;
    if (g === 2) stats.correct++;
  }
  const prev = progress[card.id];
  let step = prev ? prev.step : -1;
  if (g === 0){
    step = 0;
    lapsed[card.id] = true;
    queue.splice(Math.min(queue.length, index + 4), 0, card);   // вернётся через несколько карточек
  } else if (g === 1){
    step = lapsed[card.id] ? 0 : Math.max(0, step);
  } else {
    step = (step < 0 || lapsed[card.id]) ? 0 : Math.min(INTERVALS.length - 1, step + 1);
  }
  progress[card.id] = { step: step, due: dayStart(Date.now()) + INTERVALS[step] * DAY, ts: Date.now() };
  saveLocal();
  schedulePush();
  index++;
  render();
}

function renderDone(){
  show("kind", false);
  show("front", false);
  show("back", false);
  show("done", true);
  $("doneT").textContent = mode === "main" ? "На сегодня всё" : mode === "mixed" ? "Итог пройден" : "Тема «" + TOPIC_BY[topicN].title + "» пройдена";
  const left = unseenCount();
  let text = stats.first ? "Знаю с первого раза: " + stats.correct + " из " + stats.first + ". " : "";
  if (mode === "main") text += left ? "Новых карточек в запасе: " + left + ". " : "Все карточки уже в работе. ";
  text += "Повторы вернутся сами — завтра, через 3, 7 и 16 дней.";
  $("doneP").textContent = text;
  show("actShow", false);
  show("actGrade", false);
  const more = $("more");
  if (mode === "main"){
    more.hidden = !left;
    const k = Math.min(NEW_PER_SESSION, left);
    more.textContent = "Ещё " + k + " " + plural(k, "новая", "новых", "новых");
  } else {
    more.hidden = false;
    more.textContent = "Обычная тренировка";
  }
  show("actDone", true);
  $("status").textContent = "Готово";
  setBar(1, 1);
}

''')

# ——— Скрипт: темы — список сокращений вместо примеров
cut('      const rule = el("p", "t-rule"); rule.append(richText(t.rule)); body.append(rule);', '      const train = el("button", "t-train"', '''      const rule = el("p", "t-rule"); rule.append(richText(t.rule)); body.append(rule);
      const cards = CARDS.filter(c => c.t === t.n);
      if (cards.length){
        const list = el("div", "abl");
        cards.forEach(c => {
          const row = el("div", "abl-row" + (progress[c.id] && progress[c.id].step >= 1 ? " known" : ""));
          const txt = el("p", "abl-t");
          const a = el("span", "abl-a", c.ab); a.lang = "en";
          const f = el("span", "abl-f"); f.lang = "en"; f.append(marked(c.full));
          txt.append(a, f, el("span", "abl-r", c.ru));
          const play = el("button", "ex-play");
          play.type = "button";
          play.setAttribute("aria-label", "Прослушать: " + c.ab);
          play.innerHTML = PLAY_SVG;
          play.addEventListener("click", () => playClip(c.id + "-l", c.sl, 0.85));
          row.append(txt, play);
          list.append(row);
        });
        body.append(list);
      }
''')
rep('  const drill = name === "drill";\n', '  const drill = name === "drill";\n  const was = !$("drill").hidden;\n')
rep("  if (!drill){ stopAudio(); renderTopics(); }\n", "  if (!drill){ stopAudio(); renderTopics(); }\n  else if (!was && autoSpeak) sayFront();\n")

# ——— Скрипт: кнопки, свайпы, клавиатура
cut('$("next").addEventListener("click", next);', "function boot(){", '''$("show").addEventListener("click", flip);
$("say").addEventListener("click", sayFront);
$("playL").addEventListener("click", () => { const c = queue[index]; if (c) playClip(c.id + "-l", c.sl, 0.85); });
$("playE").addEventListener("click", () => { const c = queue[index]; if (c) playClip(c.id + "-e", c.se, 0.85); });
document.querySelectorAll("#actGrade .big").forEach(b => b.addEventListener("click", () => grade(Number(b.dataset.g))));
$("sound").addEventListener("click", () => {
  autoSpeak = !autoSpeak;
  $("sound").setAttribute("aria-pressed", String(autoSpeak));
  lsSet(LS_SPEAK, autoSpeak ? "1" : "0");
  if (!autoSpeak) stopAudio();
});

// Свайп по карточке: на лицевой стороне — открыть; на обороте вправо — «знаю», влево — «не знаю».
// Нажатие на лицевую сторону тоже открывает карточку.
const SWIPE = 70;
const reduceMotion = (function(){ try{ return window.matchMedia("(prefers-reduced-motion: reduce)").matches; }catch(e){ return false; } })();
const cardBox = $("card");
let drag = null, swallowClick = false;
cardBox.addEventListener("pointerdown", e => {
  if (e.pointerType === "mouse" && e.button !== 0) return;
  if (!queue[index] || (e.target.closest && e.target.closest("button"))) return;
  drag = { id: e.pointerId, x: e.clientX, y: e.clientY, dx: 0, on: false };
});
cardBox.addEventListener("pointermove", e => {
  if (!drag || e.pointerId !== drag.id) return;
  const dx = e.clientX - drag.x, dy = e.clientY - drag.y;
  if (!drag.on){
    if (Math.abs(dx) < 12 || Math.abs(dx) < Math.abs(dy) * 1.3) return;
    drag.on = true;
    try{ cardBox.setPointerCapture(e.pointerId); }catch(_){}
    cardBox.classList.add("drag");
  }
  drag.dx = dx;
  if (!reduceMotion) cardBox.style.transform = "translateX(" + dx + "px) rotate(" + (dx / 40).toFixed(2) + "deg)";
  cardBox.classList.toggle("lean-yes", flipped && dx > SWIPE);
  cardBox.classList.toggle("lean-no", flipped && dx < -SWIPE);
});
function endDrag(e, cancel){
  if (!drag || e.pointerId !== drag.id) return;
  const d = drag;
  drag = null;
  cardBox.classList.remove("drag", "lean-yes", "lean-no");
  if (!d.on) return;
  swallowClick = true;
  setTimeout(() => { swallowClick = false; }, 0);
  cardBox.style.transform = "";
  if (cancel || Math.abs(d.dx) < SWIPE) return;
  if (!flipped) flip();
  else grade(d.dx > 0 ? 2 : 0);
}
cardBox.addEventListener("pointerup", e => endDrag(e, false));
cardBox.addEventListener("pointercancel", e => endDrag(e, true));
cardBox.addEventListener("click", e => {
  if (swallowClick){ swallowClick = false; return; }
  if (e.target.closest && e.target.closest("button")) return;
  if (!flipped && queue[index]) flip();
});

// Клавиатура на компьютере: пробел или Enter — открыть; 1, 2, 3 — не знаю, почти, знаю; стрелки ← и → — не знаю и знаю
document.addEventListener("keydown", e => {
  if ($("drill").hidden || e.altKey || e.ctrlKey || e.metaKey) return;
  if (e.target && e.target.closest && e.target.closest("button")) return;
  if (!queue[index]) return;
  if (!flipped){
    if (e.key === " " || e.key === "Enter"){ e.preventDefault(); flip(); }
    return;
  }
  const g = { "1": 0, "2": 1, "3": 2, "ArrowLeft": 0, "ArrowRight": 2 }[e.key];
  if (g !== undefined){ e.preventDefault(); grade(g); }
});

''')

for bad in ("manage:", "answered", "shownOpts", "choose(", "renderOpts", "fullText", "modalCls"):
    assert bad not in s, bad
pathlib.Path("abbr/template.html").write_text(s)
print("ok", len(s))
