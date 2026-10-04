# Шаблон «10 ошибок» собираю из шаблона «Пассива»: общая часть (озвучка, повторы, облако) та же.
import pathlib
s = pathlib.Path("passive/template.html").read_text()

def rep(a, b):
    global s
    assert a in s, a[:70]
    s = s.replace(a, b, 1)

rep("<title>Пассивный залог</title>", "<title>Топ-10 ошибок</title>")

# ——— стили: вместо таблицы форм — чек-лист, пары «неверно → верно», ложные друзья, шаг к B2
a = s.index("  .steps{list-style:none"); b = s.index("  .go-wrap{")
s = s[:a] + '''  .ck-list{list-style:none;margin:0;padding:0}
  .ck-list li{border-top:1px solid var(--line)}
  .ck-list li:first-child{border-top:0}
  .ck{width:100%;min-height:52px;display:grid;grid-template-columns:30px minmax(0,1fr);column-gap:8px;align-items:baseline;padding:8px 0;border:0;background:transparent;text-align:left;cursor:pointer}
  .ck-n{font-family:var(--serif);font-size:20px;line-height:1;color:var(--accent);font-variant-numeric:tabular-nums}
  .ck-t{font-size:16px;line-height:1.35}
  .ck-ex{grid-column:2;margin-top:2px;font-family:var(--serif);font-size:17px;line-height:1.3;color:var(--blue)}
  .algo-note{margin:8px 0 0;font-size:15px;line-height:1.45;color:var(--muted)}
''' + s[b:]
a = s.index("  .chain{display:flex"); b = s.index("  .errs{list-style:none")
s = s[:a] + '''  .pairs{display:flex;flex-direction:column;gap:12px}
  .pair{display:grid;grid-template-columns:minmax(0,1fr) 48px;column-gap:10px;align-items:start}
  .p-bad{margin:0;grid-column:1;font-family:var(--serif);font-size:17px;line-height:1.35;color:var(--no-text);text-decoration:line-through;text-decoration-thickness:1.5px}
  .p-top{margin:0;grid-column:1;font-size:15px;line-height:1.35;color:var(--soft)}
  .p-good{margin:2px 0 0;grid-column:1;font-family:var(--serif);font-size:20px;line-height:1.35}
  .p-good .good{text-decoration:underline;text-decoration-thickness:1.5px;text-underline-offset:3px}
  .p-ru{margin:2px 0 0;grid-column:1;font-size:14px;line-height:1.35;color:var(--muted)}
  .p-ru s{color:var(--no-text);text-decoration-thickness:1.5px}
  .pair .ex-play{grid-column:2;grid-row:1 / span 3}
  .b2{margin:0;padding:10px 12px;border-radius:12px;background:var(--blue-soft);font-size:16px;line-height:1.5;color:var(--text)}
  .b2 b{display:block;margin-bottom:2px;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--blue)}
  .t-lab{margin:0 0 -8px;font-size:13px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--blue)}
  .more{margin:-2px 0 0;font-size:14px;line-height:1.4;color:var(--muted)}
''' + s[b:]
# номера ошибок — крупно, как в рейтинге; во второй строке заголовка — ошибка и исправление
rep("  .t-n{font-size:15px;color:var(--blue);font-variant-numeric:tabular-nums}",
    "  .t-n{font-family:var(--serif);font-size:26px;line-height:1;color:var(--accent);font-variant-numeric:tabular-nums}")
rep("  .t-sub{font-size:14px;line-height:1.3;color:var(--muted)}",
    "  .t-sub{font-family:var(--serif);font-size:16px;line-height:1.3;color:var(--soft)}\n  .t-sub s{color:var(--no-text);text-decoration-thickness:1.5px}\n  .t-sub .arr{font-family:var(--sans);color:var(--muted)}")
rep("  .t-head{width:100%;min-height:60px;", "  .t-head{width:100%;min-height:64px;")
# карточка «выбери фразу»: вопрос — русская фраза; ответ «ничего»
rep("  .gap{display:inline-block;",
    "  .q.ruq{font-family:var(--sans);font-size:24px;line-height:1.35}\n"
    "  .zero{font-family:var(--sans);font-size:.55em;line-height:1;color:var(--yes-text);border:1px solid rgba(78,135,103,.65);border-radius:999px;padding:.12em .45em;margin:0 .35em 0 .05em;vertical-align:.25em}\n"
    "  .gap{display:inline-block;")
rep("  .opt.long{font-size:22px}",
    "  .opt.long{font-size:22px}\n  .opt.xl{font-size:19px;line-height:1.25;padding:8px 14px;text-wrap:balance}\n"
    "  .opt small{font-family:var(--sans);font-size:13px;color:var(--muted)}\n"
    "  .verdict s{font-family:var(--serif);font-size:19px;text-decoration-thickness:1.5px}")
# в альбомной ориентации левая колонка длинная — пусть прокручивается вместе с правой
rep("  body.wide .r-left{position:sticky;top:0}", "  body.wide .r-left{position:static}")

# ——— разметка вкладки «Правила»
a = s.index('    <div class="r-left">'); b = s.index('  </section>\n</div>')
s = s[:a] + '''    <div class="r-left">
      <h1 class="r-title" lang="en">Top 10 mistakes</h1>
      <p class="r-sub">Десять ошибок, которые почти всегда выдают русскоговорящего и&nbsp;держат речь на&nbsp;<b>B1</b>. Все они приходят из&nbsp;русского языка. Исправишь их&nbsp;— и&nbsp;английский сразу звучит на&nbsp;уровень выше, ближе к&nbsp;<b>B2</b>.</p>
      <div class="algo">
        <p class="algo-h">Чек-лист перед фразой</p>
        <ol class="ck-list">
<!--__CHECK__-->
        </ol>
        <p class="algo-note">Нажми на пункт&nbsp;— откроется разбор этой ошибки.</p>
      </div>
      <div class="go-wrap"><button class="big primary" id="go" type="button">Начать тренировку</button></div>
    </div>
    <div class="r-right">
      <h2 class="lbl">10 ошибок</h2>
      <div class="topics" id="topics"></div>
      <h2 class="lbl">Ещё 8 ошибок на пути к B2</h2>
      <div class="mx-wrap">
        <ul class="errs">
<!--__BONUS__-->
        </ul>
      </div>
    </div>
''' + s[b:]
rep('<span class="kind" id="kind">Тема 1</span>', '<span class="kind" id="kind">Ошибка 1</span>')

# ——— скрипт
rep('const LS_STATE = "passive:state";\nconst LS_SPEAK = "passive:autospeak";\nconst LS_TAB = "passive:tab";\nconst LS_OPEN = "passive:open";',
    'const LS_STATE = "top10:state";\nconst LS_SPEAK = "top10:autospeak";\nconst LS_TAB = "top10:tab";\nconst LS_OPEN = "top10:open";')
rep('["apple-mobile-web-app-title", "Passive"],', '["apple-mobile-web-app-title", "10 ошибок"],')
rep('function topicLabel(n){ return n === MIXED_TOPIC ? "Всё вместе" : "Тема " + n + " · " + TOPIC_BY[n].title; }',
    'function topicLabel(n){ return n === MIXED_TOPIC ? "Всё вместе" : "Ошибка " + n + " · " + TOPIC_BY[n].title; }\nfunction label(a){ return a === "" ? "ничего" : a; }')
rep('''function split(card, word){
  const i = card.q.indexOf("___");
  const start = isStart(card.q, i);
  return { pre: card.q.slice(0, i), word: start ? cap(word) : word, post: card.q.slice(i + 3) };
}''', '''function split(card, word){
  const i = card.q.indexOf("___");
  const start = isStart(card.q, i);
  const pre = card.q.slice(0, i);
  let post = card.q.slice(i + 3);
  if (word) return { pre: pre, word: start ? cap(word) : word, post: post };
  post = post.replace(/^\\s+/, "");                  // ответ «ничего»: слово после пропуска встаёт на его место
  return { pre: pre, word: "", post: start ? cap(post) : post };
}''')
rep("// {…} — be (синий), _…_ — третья форма (оранжевый), |…| — зелёный", "// |…| — то, что исправили (зелёный); {…} — синий; _…_ — оранжевый")

# «все формы подряд» здесь не нужны
a = s.index("// ——— «Все формы подряд»"); b = s.index("// ——— Очередь")
s = s[:a] + s[b:]
rep("let chainOn = false;        // играют «все формы подряд»\n", "")
rep("  if (chainOn){ chainOn = false; chainUI(); }\n}", "}")
rep("  if (chainOn){ chainOn = false; chainUI(); }     // без записи подсветка строк не работает\n", "")
rep("// Новые карточки идут вперемешку по темам: время и залог чередуются, чтобы выбирать по смыслу, а не угадывать по теме.",
    "// Новые карточки идут вперемешку: за сессию встречаются все десять ошибок, шаги к B2 — ближе к концу каждой темы.")

# варианты: «ничего» и длинные фразы
rep('''  shownOpts.forEach(o => {
    const b = el("button", "opt" + (longest > 9 ? " long" : ""));
    b.type = "button";
    b.lang = "en";
    b.textContent = o;''', '''  shownOpts.forEach(o => {
    const b = el("button", "opt" + (longest > 26 ? " xl" : longest > 9 ? " long" : ""));
    b.type = "button";
    if (o === ""){
      b.setAttribute("aria-label", "Ничего не нужно");
      b.append(el("span", null, "—"), el("small", null, "ничего"));
    } else {
      b.lang = "en";
      b.textContent = o;
    }''')

# показ карточки: «выбери фразу» — русская фраза вместо пропуска
rep('''  $("kind").textContent = topicLabel(card.t);
  const q = $("q");
  q.textContent = "";
  const i = card.q.indexOf("___");''', '''  $("kind").textContent = topicLabel(card.t) + (card.b2 ? " · шаг к B2" : "");
  const q = $("q");
  q.textContent = "";
  q.className = "q";
  q.lang = "en";
  if (card.pick){
    q.className = "q ruq";
    q.lang = "ru";
    q.textContent = "«" + card.ru + "»";
    q.removeAttribute("aria-label");
    $("hint").textContent = "Как это сказать по-английски?";
    show("hint", true);
    show("back", false);
    renderOpts(card);
    show("opts", true);
    show("actNext", false);
    show("actDone", false);
    renderStatus();
    preloadClip(card.id);
    return;
  }
  const i = card.q.indexOf("___");''')
rep('''  const prefix = mode === "topic" ? "Тема " + topicN + " · " : mode === "mixed" ? "Всё вместе · " : "";
  $("status").textContent = prefix + "Карточка " + (index + 1) + " из " + queue.length;
  setBar(index, queue.length);
  preloadClip(card.id);
}''', '''  renderStatus();
  preloadClip(card.id);
}
function renderStatus(){
  const prefix = mode === "topic" ? "Ошибка " + topicN + " · " : mode === "mixed" ? "Всё вместе · " : "";
  $("status").textContent = prefix + "Карточка " + (index + 1) + " из " + queue.length;
  setBar(index, queue.length);
}''')
rep('''  q.removeAttribute("aria-label");
  q.textContent = mode === "main" ? "На сегодня всё" : mode === "mixed" ? "Итог пройден" : "Тема " + topicN + " пройдена";''',
    '''  q.removeAttribute("aria-label");
  q.className = "q";
  q.lang = "ru";
  q.textContent = mode === "main" ? "На сегодня всё" : mode === "mixed" ? "Итог пройден" : "Ошибка " + topicN + " — разобрана";''')

# ответ
rep('''  const p = split(card, card.a);
  q.append(p.pre, el("span", "good", p.word), p.post);

  const v = $("verdict");''', '''  q.className = "q";
  q.lang = "en";
  const p = split(card, card.a);
  if (p.word) q.append(p.pre, el("span", "good", p.word), p.post);
  else q.append(p.pre, el("span", "zero", "∅"), p.post);

  const v = $("verdict");''')
rep('''  } else {
    v.className = "verdict bad";
    v.append("Нужно ", el("b", "good", card.a), " · твой ответ: ", el("b", null, opt));
  }''', '''  } else if (card.pick){
    v.className = "verdict bad";
    const w = el("s", null, opt); w.lang = "en";
    v.append("Правильно — как выше. Твой вариант: ", w);
  } else {
    v.className = "verdict bad";
    v.append("Нужно ", el("b", "good", label(card.a)), " · твой ответ: ", el("b", null, label(opt)));
  }''')
rep('''  const why = $("why"); why.textContent = ""; why.append(richText(card.why));
  show("hint", false);''', '''  const why = $("why"); why.textContent = ""; why.append(richText(card.why));
  if (card.pick) $("hint").textContent = card.ru;
  show("hint", !!card.pick);''')

# ——— правила: разбор каждой ошибки
a = s.index("let openTopic = null;\nfunction renderTopics(){"); b = s.index("function setTab(name){")
s = s[:a] + r'''let openTopic = null;
function playButton(label, fn){
  const b = el("button", "ex-play");
  b.type = "button";
  b.setAttribute("aria-label", label);
  b.innerHTML = PLAY_SVG;
  b.addEventListener("click", fn);
  return b;
}
function headSub(t){
  const s = el("span", "t-sub");
  const bad = el("s", null, t.bad); bad.lang = "en";
  const good = el("span", "good", t.good); good.lang = "en";
  s.append(el("span", "sr", "Неверно: "), bad, el("span", "arr", " → "), el("span", "sr", "верно: "), good);
  return s;
}
function renderTopics(){
  const box = $("topics");
  box.textContent = "";
  TOPICS.forEach(t => {
    const item = el("div", "t-item");
    const head = el("button", "t-head");
    head.type = "button";
    head.dataset.n = String(t.n);
    head.setAttribute("aria-expanded", String(openTopic === t.n));
    const txt = el("span", "t-txt");
    txt.append(el("span", "t-title", t.title));
    if (t.bad) txt.append(headSub(t));
    head.append(el("span", "t-n", String(t.n)), txt,
                el("span", "t-count", t.n === MIXED_TOPIC ? "" : learnedIn(t.n)), el("span", "t-chev", "›"));
    head.addEventListener("click", () => {
      openTopic = openTopic === t.n ? null : t.n;
      lsSet(LS_OPEN, openTopic ? String(openTopic) : "");
      stopAudio();
      renderTopics();
    });
    item.append(head);
    if (openTopic === t.n){
      const body = el("div", "t-body");
      if (t.why){
        body.append(el("p", "t-lab", "Откуда ошибка"));
        const w = el("p", "t-rule"); w.append(richText(t.why)); body.append(w);
        body.append(el("p", "t-lab", "Как правильно"));
      }
      const rule = el("p", "t-rule"); rule.append(richText(t.rule)); body.append(rule);
      if (t.pairs || t.ff){
        const list = el("div", "pairs");
        (t.pairs || []).forEach((pr, i) => {
          const row = el("div", "pair");
          const bad = el("p", "p-bad", pr.bad); bad.lang = "en";
          const good = el("p", "p-good"); good.lang = "en"; good.append(marked(pr.good));
          row.append(el("span", "sr", "Неверно: "), bad, playButton("Прослушать правильный вариант", () => playClip("r" + t.n + "-" + (i + 1), pr.good.replace(/\|/g, ""), 0.9)), good, el("p", "p-ru", pr.ru));
          list.append(row);
        });
        (t.ff || []).forEach((f, i) => {
          const row = el("div", "pair");
          const en = el("p", "p-good"); en.lang = "en"; en.append(el("span", "good", f.en));
          const no = el("p", "p-ru"); const s = el("s", null, f.no); s.lang = "en";
          no.append(el("span", "sr", "не "), s, " — " + f.means);
          row.append(el("p", "p-top", f.ru), playButton("Прослушать: " + f.en, () => playClip("fw-" + (i + 1), f.en, 0.85)), en, no);
          list.append(row);
        });
        body.append(list);
      }
      if (t.b2){
        const b2 = el("p", "b2");
        b2.append(el("b", null, "Шаг к B2"), richText(t.b2));
        body.append(b2);
      }
      if (t.more) body.append(el("p", "more", t.more));
      const train = el("button", "t-train", t.n === MIXED_TOPIC ? "Начать итоговую тренировку" : "Потренировать эту ошибку");
      train.type = "button";
      train.addEventListener("click", () => { buildTopic(t.n); setTab("drill"); render(); });
      body.append(train);
      item.append(body);
    }
    box.append(item);
  });
}
function openAndShow(n){
  openTopic = n;
  lsSet(LS_OPEN, String(n));
  stopAudio();
  renderTopics();
  const head = document.querySelector('.t-head[data-n="' + n + '"]');
  if (!head) return;
  const rule = $("rule");
  const y = rule.scrollTop + head.getBoundingClientRect().top - rule.getBoundingClientRect().top - 6;
  let reduce = false;
  try{ reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches; }catch(e){}
  try{ rule.scrollTo({ top: y, behavior: reduce ? "auto" : "smooth" }); }catch(e){ rule.scrollTop = y; }
}
document.querySelectorAll(".ck").forEach(b => b.addEventListener("click", () => openAndShow(+b.dataset.n)));

''' + s[b:]
assert "chainOn" not in s and "formsPlay" not in s and "FORMS" not in s, [w for w in ("chainOn", "formsPlay", "FORMS") if w in s]
pathlib.Path("top10/template.html").write_text(s)
print("ok", len(s))
