# Проверка тренажёра «Advice и advise» в браузере: nverb/preview.html (сама страница) и site/ (внутри оболочки).
# Запуск из sources/ после nverb/build.py и tools/mk_shell.py: python3 nverb/test.py   (скриншоты — nverb/s-*.png, nverb/sheet*.png)
import asyncio, json, time, pathlib, subprocess, sys
from playwright.async_api import async_playwright
from PIL import Image
root = pathlib.Path("nverb").resolve()
repo = root.parent.parent
srv = subprocess.Popen([sys.executable, "-m", "http.server", "8836", "--bind", "127.0.0.1"], cwd=repo, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
PAGE = "http://127.0.0.1:8836/sources/nverb/preview.html"
SHELL = "http://127.0.0.1:8836/site/"
shots = []
WIDTHS = [(320, 640), (375, 740), (390, 800), (430, 900), (820, 1180), (1180, 820)]

async def run():
    out = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(args=["--autoplay-policy=no-user-gesture-required"])
        errors = []
        async def mk(w, h, url=PAGE):
            ctx = await b.new_context(viewport={"width": w, "height": h}, device_scale_factor=2, service_workers="block")
            pg = await ctx.new_page()
            pg.on("pageerror", lambda e: errors.append(f"{w}: {e}"))
            pg.on("console", lambda m: errors.append(f"{w} console: {m.text}") if m.type == "error" else None)
            await pg.goto(url); await pg.wait_for_timeout(400)
            return ctx, pg
        async def shot(pg, name):
            path = root / f"s-{name}.png"; await pg.screenshot(path=str(path)); shots.append(path)

        # ——— сама страница, телефон 390
        ctx, pg = await mk(390, 800)
        await shot(pg, "rule")
        H = await pg.evaluate("document.getElementById('rule').scrollHeight")
        for k, y in enumerate([700, 1400, 2100, 2800, 3500, 4200]):
            if y > H - 400: break
            await pg.evaluate(f"document.getElementById('rule').scrollTop = {y}"); await pg.wait_for_timeout(120)
            await shot(pg, f"rule{k + 2}")
        out["overflow_rule"] = await pg.evaluate("[...document.querySelectorAll('.md, .err, .algo, .mt, .steps li, .mt th, .mt td')].filter(n => n.scrollWidth > n.clientWidth + 1).map(n => n.className || n.tagName)")
        out["groups"] = await pg.evaluate("[...document.querySelectorAll('.t-group')].map(g => g.textContent)")
        out["marks_t5"] = await pg.evaluate("openTopic = 5, renderTopics(), [...document.querySelectorAll('.t-body .ex-en span')].map(x => x.className + ':' + x.textContent)")
        await pg.evaluate("document.querySelector('.t-head[aria-expanded=\"true\"]').scrollIntoView()"); await pg.wait_for_timeout(150)
        await shot(pg, "topic5")
        # первая сессия — только B1, B2 позже
        out["first_session"] = await pg.evaluate("(() => { buildMain(); const n = {}; queue.forEach(c => n['t' + c.t] = (n['t' + c.t] || 0) + 1); return n; })()")
        out["order_first30"] = await pg.evaluate("FRESH_ORDER.slice(0, 30).map(c => c.t).join(',')")
        out["order_last10"] = await pg.evaluate("FRESH_ORDER.slice(-10).map(c => c.t).join(',')")
        await pg.evaluate("buildMain(); render();")
        await pg.click("#tabDrill"); await pg.wait_for_timeout(150)
        await shot(pg, "q")
        wrong = await pg.evaluate("shownOpts.findIndex(o => o !== queue[index].a && !(queue[index].also && queue[index].also[o]))")
        await (await pg.query_selector_all("#opts .opt"))[wrong].click(); await pg.wait_for_timeout(200)
        out["verdict_wrong"] = await pg.inner_text("#verdict")
        await shot(pg, "wrong")
        n = 0
        while n < 40:
            await pg.click("#next"); await pg.wait_for_timeout(40)
            if not await pg.evaluate("!!queue[index]"): break
            i = await pg.evaluate("shownOpts.indexOf(queue[index].a)")
            await (await pg.query_selector_all("#opts .opt"))[i].click(); await pg.wait_for_timeout(40)
            if n == 3: await shot(pg, "right")
            n += 1
        out["answered"] = n
        out["done"] = await pg.inner_text("#hint")
        out["saved"] = await pg.evaluate("Object.keys(JSON.parse(localStorage.getItem('nverb:state')).progress).length")
        out["mixed_size"] = await pg.evaluate("buildTopic(MIXED_TOPIC), queue.length")
        # «тоже верно»
        await pg.evaluate("queue = [CARDS.find(c => c.id === 'v1-advice')]; index = 0; mode = 'topic'; topicN = 1; render();"); await pg.wait_for_timeout(100)
        si = await pg.evaluate("shownOpts.indexOf(\"advise\")")
        await (await pg.query_selector_all("#opts .opt"))[si].click(); await pg.wait_for_timeout(150)
        out["trap_verdict"] = await pg.inner_text("#verdict")
        await shot(pg, "also")
        # ударение: на экране REcord, озвучка — обычное предложение (поле say)
        await pg.evaluate("queue = [CARDS.find(c => c.id === 'v7-record-n')]; index = 0; mode = 'topic'; topicN = 7; render();"); await pg.wait_for_timeout(100)
        ri = await pg.evaluate("shownOpts.indexOf('REcord')")
        await (await pg.query_selector_all("#opts .opt"))[ri].click(); await pg.wait_for_timeout(200)
        out["say"] = await pg.evaluate("[document.getElementById('q').textContent, fullText(queue[index]), player.getAttribute('src')]")
        await shot(pg, "stress")
        # ни один вариант ответа не вылезает за кнопку — на самом узком экране проверим ниже
        await ctx.close()

        # ——— все ширины: без горизонтального скролла, варианты помещаются
        out["hscroll"], out["opt_overflow"] = {}, {}
        for w, h in WIDTHS:
            ctx, pg = await mk(w, h)
            out["hscroll"][w] = await pg.evaluate("document.documentElement.scrollWidth > window.innerWidth || document.getElementById('rule').scrollWidth > document.getElementById('rule').clientWidth")
            if w in (320, 820, 1180): await shot(pg, f"w{w}-rule")
            await pg.click("#go"); await pg.wait_for_timeout(150)
            out["opt_overflow"][w] = await pg.evaluate("""(() => { const bad = []; CARDS.forEach(c => { queue = [c]; index = 0; mode = 'topic'; topicN = c.t; render();
                if ([...document.querySelectorAll('#opts .opt, #q')].some(b => b.scrollWidth > b.clientWidth + 1)) bad.push(c.id); }); return bad; })()""")
            if w in (320, 1180):
                await pg.evaluate("(() => { const m = c => Math.max(...c.opts.map(o => o.length)); const c = CARDS.reduce((a, c) => m(c) > m(a) ? c : a); queue = [c]; index = 0; render(); })()")
                await shot(pg, f"w{w}-long")
            await ctx.close()

        # ——— внутри оболочки «Английский B2»
        ctx, pg = await mk(390, 800, SHELL)
        await pg.wait_for_timeout(600)
        out["shell_tile"] = await pg.evaluate("[...document.querySelectorAll('button, a')].filter(n => n.textContent.includes('Advice и advise')).length")
        await pg.fill("#q", "advise"); await pg.wait_for_timeout(400)
        out["shell_search"] = await pg.evaluate("[...document.querySelectorAll('#home button')].filter(n => n.offsetParent && n.textContent.includes('Advice и advise')).length")
        await shot(pg, "shell-search")
        await pg.evaluate("openCourse('nverb')"); await pg.wait_for_timeout(1500)
        await shot(pg, "shell-open")
        fr = pg.frame_locator("#frame")
        await fr.locator("#go").click(); await pg.wait_for_timeout(300)
        for _ in range(3):
            i = await fr.locator("body").evaluate("() => shownOpts.indexOf(queue[index].a)")
            await fr.locator("#opts .opt").nth(i).click(); await pg.wait_for_timeout(150)
            await fr.locator("#say").click(); await pg.wait_for_timeout(300)
            await fr.locator("#next").click(); await pg.wait_for_timeout(100)
        await shot(pg, "shell-q")
        out["shell_saved"] = await pg.evaluate("Object.keys(JSON.parse(localStorage.getItem('nverb:state') || '{\"progress\":{}}').progress).length")
        out["shell_note"] = await pg.evaluate("document.getElementById('cnote').hidden ? '' : document.getElementById('cnote').textContent")
        out["shell_audio_log"] = await pg.evaluate("AE.log.slice(-6)")
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
phone = [p for p in shots if not p.name.startswith(("s-w820", "s-w1180"))]
for i in range(0, len(phone), 6):
    sheet(phone[i:i + 6], f"sheet{i // 6 + 1}.png")
sheet([p for p in shots if p.name.startswith(("s-w820", "s-w1180"))], "sheet-pad.png", 420)
