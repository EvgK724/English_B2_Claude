import asyncio, json, time, pathlib, subprocess, sys
from playwright.async_api import async_playwright
from PIL import Image
root = pathlib.Path("abbr").resolve()
srv = subprocess.Popen([sys.executable, "-m", "http.server", "8827", "--bind", "127.0.0.1"], cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
URL = "http://127.0.0.1:8827/preview.html"
shots = []

async def run():
    out = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(args=["--autoplay-policy=no-user-gesture-required"])
        errors = []
        async def mk(w, h):
            ctx = await b.new_context(viewport={"width": w, "height": h}, device_scale_factor=2)
            pg = await ctx.new_page()
            pg.on("pageerror", lambda e: errors.append(str(e)))
            pg.on("console", lambda m: errors.append("console:" + m.text) if m.type == "error" else None)
            pg.on("requestfailed", lambda r: errors.append("reqfail:" + r.url))
            await pg.goto(URL); await pg.wait_for_timeout(400)
            return ctx, pg
        async def shot(pg, name):
            path = root / f"s-{name}.png"; await pg.screenshot(path=str(path)); shots.append(path)
        src = "player.getAttribute('src')"

        # ——— Правила (телефон)
        ctx, pg = await mk(390, 800)
        await shot(pg, "rule")
        H = await pg.evaluate("document.getElementById('rule').scrollHeight")
        out["rule_height"] = H
        for k, y in enumerate([700, 1400, 2100, 2800]):
            if y > H - 400: break
            await pg.evaluate(f"document.getElementById('rule').scrollTop = {y}"); await pg.wait_for_timeout(120)
            await shot(pg, f"rule{k + 2}")
        out["hscroll"] = await pg.evaluate("document.documentElement.scrollWidth > window.innerWidth")
        out["rule_overflow"] = await pg.evaluate("[...document.querySelectorAll('.err, .algo, .steps li, .lts, .lt, .s-f, .algo-m')].filter(n => n.scrollWidth > n.clientWidth + 1).map(n => n.className + ':' + n.textContent.slice(0, 30))")
        out["ltrs_lines"] = await pg.evaluate("(() => { const b = document.querySelector('.ltrs'); return Math.round(b.getBoundingClientRect().height / parseFloat(getComputedStyle(b).lineHeight || 30)); })()")
        await pg.click('.lt[data-key="lt-h"]'); await pg.wait_for_timeout(300)
        out["letter_audio"] = await pg.evaluate(src)
        await pg.evaluate("openTopic = 1; renderTopics(); document.querySelector('.t-head[aria-expanded=\"true\"]').scrollIntoView()"); await pg.wait_for_timeout(150)
        await shot(pg, "topic1")
        out["topic1_rows"] = await pg.evaluate("document.querySelectorAll('.abl-row').length")
        out["topic_overflow"] = await pg.evaluate("[...document.querySelectorAll('.abl-row, .abl-t')].some(n => n.scrollWidth > n.clientWidth + 1)")
        await pg.click(".abl-row .ex-play"); await pg.wait_for_timeout(300)
        out["topic_audio"] = await pg.evaluate(src)
        await pg.evaluate("openTopic = 4; renderTopics(); document.querySelector('.t-head[aria-expanded=\"true\"]').scrollIntoView()"); await pg.wait_for_timeout(150)
        await shot(pg, "topic4")
        out["groups"] = await pg.evaluate("[...document.querySelectorAll('.t-group')].map(g => g.textContent)")
        out["first_session"] = await pg.evaluate("""(() => { buildMain(); const n = {}; queue.forEach(c => n['t' + c.t] = (n['t' + c.t] || 0) + 1); return n; })()""")

        # ——— Тренировка
        await pg.evaluate("buildMain(); render();")
        await pg.click("#tabDrill"); await pg.wait_for_timeout(300)
        out["front_audio"] = await pg.evaluate(src)
        await shot(pg, "front")
        await pg.click("#card", position={"x": 60, "y": 150}); await pg.wait_for_timeout(250)   # нажатие на карточку (не на кнопку) открывает её
        out["flipped_by_tap"] = await pg.evaluate("flipped")
        out["back_audio"] = await pg.evaluate(src)
        await shot(pg, "back")
        await pg.click("#playE"); await pg.wait_for_timeout(250)
        out["ex_audio"] = await pg.evaluate(src)
        n0 = await pg.evaluate("queue.length")
        cid = await pg.evaluate("queue[index].id")
        await pg.click("#actGrade .g0"); await pg.wait_for_timeout(150)     # «не знаю» — вернётся в эту же сессию
        out["requeue"] = await pg.evaluate(f"[queue.length - {n0}, queue.findIndex((c, i) => i > 0 && c.id === '{cid}'), index]")
        out["dont_know_due_days"] = await pg.evaluate(f"Math.round((progress['{cid}'].due - dayStart(Date.now())) / DAY)")
        # свайп мышью: на лицевой стороне вправо — открыть, на обороте вправо — «знаю»
        box = await (await pg.query_selector("#card")).bounding_box()
        cx, cy = box["x"] + box["width"] / 2, box["y"] + box["height"] * 0.22
        async def swipe(dx):
            await pg.mouse.move(cx, cy); await pg.mouse.down()
            for k in range(1, 9):
                await pg.mouse.move(cx + dx * k / 8, cy + 3); await pg.wait_for_timeout(16)
            await pg.mouse.up(); await pg.wait_for_timeout(250)
        i0 = await pg.evaluate("index")
        await swipe(160)
        out["swipe_flip"] = await pg.evaluate("flipped")
        await pg.mouse.move(cx, cy); await pg.mouse.down(); await pg.mouse.move(cx + 60, cy); await pg.mouse.move(cx + 120, cy)
        await pg.wait_for_timeout(60)
        await shot(pg, "drag")
        out["lean"] = await pg.evaluate("document.getElementById('card').className")
        await pg.mouse.move(cx + 160, cy); await pg.mouse.up(); await pg.wait_for_timeout(250)
        out["swipe_grade"] = await pg.evaluate(f"[index - {i0}, flipped]")
        await swipe(30)                                                   # короткий — ничего не происходит
        out["short_swipe"] = await pg.evaluate("flipped")
        # клавиатура: пробел — открыть, 3 — знаю
        await pg.keyboard.press("Space"); await pg.wait_for_timeout(100)
        k1 = await pg.evaluate("flipped")
        await pg.keyboard.press("3"); await pg.wait_for_timeout(100)
        out["keyboard"] = [k1, await pg.evaluate("flipped")]
        # до конца сессии
        n = 0
        while n < 60 and await pg.evaluate("!!queue[index]"):
            await pg.click("#show"); await pg.wait_for_timeout(30)
            await pg.click("#actGrade .g2"); await pg.wait_for_timeout(30)
            n += 1
        out["graded"] = n
        out["done"] = await pg.inner_text("#doneP")
        await shot(pg, "done")
        out["mixed_size"] = await pg.evaluate("buildTopic(MIXED_TOPIC), queue.length")
        # все карточки: лицевая и оборотная стороны без горизонтального переполнения; где нужна прокрутка
        out["overflow"] = await pg.evaluate("""(() => { autoSpeak = false; const bad = [], tall = []; const box = document.getElementById('card');
            autoSpeak = false; CARDS.forEach(c => { queue = [c]; index = 0; mode = 'topic'; topicN = c.t; render();
              const ab = document.getElementById('ab');
              if (ab.scrollWidth > ab.clientWidth + 1 || ab.getBoundingClientRect().width > box.clientWidth) bad.push(c.id + ':front');
              flip();
              if ([...document.querySelectorAll('#back, #back *')].some(n => n.clientWidth && n.scrollWidth > n.clientWidth + 1)) bad.push(c.id + ':back');
              if (box.scrollHeight > box.clientHeight + 1) tall.push(c.id + '+' + (box.scrollHeight - box.clientHeight)); });
            return { bad: bad, scroll: tall }; })()""")
        # самая длинная карточка на телефоне
        await pg.evaluate("(() => { const c = CARDS.find(c => c.id === 'o-unesco'); queue = [c]; index = 0; render(); flip(); })()"); await pg.wait_for_timeout(100)
        await shot(pg, "long")
        await pg.evaluate("(() => { const c = CARDS.find(c => c.id === 'd-ampm'); queue = [c]; index = 0; render(); })()"); await pg.wait_for_timeout(100)
        await shot(pg, "front-long")
        await ctx.close()

        # маленький телефон
        ctx, pg = await mk(375, 667)
        await pg.evaluate("(() => { autoSpeak = false; buildMain(); render(); setTab('drill'); flip(); })()"); await pg.wait_for_timeout(150)
        await shot(pg, "se-back")
        out["se_scroll"] = await pg.evaluate("""(() => { const box = document.getElementById('card'); const t = [];
            autoSpeak = false; CARDS.forEach(c => { queue = [c]; index = 0; render(); flip(); if (box.scrollHeight > box.clientHeight + 1) t.push(c.id); }); return t.length; })()""")
        await ctx.close()

        for (w, h, name) in [(1180, 760, "pad-land"), (820, 1130, "pad-port")]:
            ctx, pg = await mk(w, h)
            await shot(pg, name + "-rule")
            await pg.click("#go"); await pg.wait_for_timeout(200)
            await shot(pg, name + "-front")
            await pg.click("#show"); await pg.wait_for_timeout(150)
            await shot(pg, name + "-back")
            out[name + "_hscroll"] = await pg.evaluate("document.documentElement.scrollWidth > window.innerWidth")
            out[name + "_scroll"] = await pg.evaluate("""(() => { const box = document.getElementById('card'); const t = [];
                autoSpeak = false; CARDS.forEach(c => { queue = [c]; index = 0; render(); flip(); if (box.scrollHeight > box.clientHeight + 1) t.push(c.id); }); return t; })()""")
            await ctx.close()
        await b.close()
    out["errors"] = errors
    print(json.dumps(out, ensure_ascii=False, indent=1))
try:
    asyncio.run(run())
finally:
    srv.terminate()

def sheet(paths, name, h=560):
    ims = [Image.open(p) for p in paths]
    ims = [im.resize((int(im.width * h / im.height), h)) for im in ims]
    W = sum(im.width for im in ims) + 10 * (len(ims) + 1)
    s = Image.new("RGB", (W, h + 20), (60, 60, 60)); x = 10
    for im in ims: s.paste(im, (x, 10)); x += im.width + 10
    s.save(root / name)
phone = [p for p in shots if "pad" not in p.name]
half = (len(phone) + 1) // 2
sheet(phone[:half], "sheet1.png"); sheet(phone[half:], "sheet2.png")
sheet([p for p in shots if "pad" in p.name], "sheet3.png", 420)
