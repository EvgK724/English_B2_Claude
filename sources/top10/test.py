import asyncio, json, time, pathlib, subprocess, sys
from playwright.async_api import async_playwright
from PIL import Image
root = pathlib.Path("top10").resolve()
srv = subprocess.Popen([sys.executable, "-m", "http.server", "8794", "--bind", "127.0.0.1"], cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
URL = "http://127.0.0.1:8794/preview.html"
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
        ctx, pg = await mk(390, 800)
        await shot(pg, "rule")
        H = await pg.evaluate("document.getElementById('rule').scrollHeight")
        out["rule_height"] = H
        for k, y in enumerate([700, 1400, 2100, 2800, 3500]):
            if y > H - 400: break
            await pg.evaluate(f"document.getElementById('rule').scrollTop = {y}"); await pg.wait_for_timeout(120)
            await shot(pg, f"rule{k+2}")
        out["hscroll"] = await pg.evaluate("document.documentElement.scrollWidth > window.innerWidth")
        # чек-лист открывает разбор ошибки
        await pg.evaluate("document.getElementById('rule').scrollTop = 0"); await pg.wait_for_timeout(80)
        await pg.click('.ck[data-n="6"]'); await pg.wait_for_timeout(800)
        out["check_open"] = await pg.evaluate("openTopic")
        out["check_top"] = await pg.evaluate("Math.round(document.querySelector('.t-head[data-n=\"6\"]').getBoundingClientRect().top - document.getElementById('rule').getBoundingClientRect().top)")
        await shot(pg, "topic6")
        await pg.evaluate("openAndShow(10)"); await pg.wait_for_timeout(700)
        await shot(pg, "topic10")
        await pg.evaluate("document.getElementById('rule').scrollTop += 700"); await pg.wait_for_timeout(120)
        await shot(pg, "topic10b")
        await pg.click('.pair .ex-play'); await pg.wait_for_timeout(300)
        out["ff_audio"] = await pg.evaluate("player.getAttribute('src')")
        # тема с примерами
        await pg.evaluate("openAndShow(1)"); await pg.wait_for_timeout(700)
        await shot(pg, "topic1")
        await pg.evaluate("document.getElementById('rule').scrollTop += 650"); await pg.wait_for_timeout(120)
        await shot(pg, "topic1b")
        # состав первой сессии
        out["first_session"] = await pg.evaluate("""(() => { buildMain(); const n = {}; queue.forEach(c => n['t' + c.t] = (n['t' + c.t] || 0) + 1); return n; })()""")
        out["order"] = await pg.evaluate("FRESH_ORDER.map(c => c.t).join(',')")
        await pg.evaluate("buildMain(); render();")
        await pg.click("#tabDrill"); await pg.wait_for_timeout(150)
        await shot(pg, "q")
        wrong = await pg.evaluate("shownOpts.findIndex(o => o !== queue[index].a && !(queue[index].also && queue[index].also[o]))")
        await (await pg.query_selector_all("#opts .opt"))[wrong].click(); await pg.wait_for_timeout(200)
        out["verdict"] = await pg.inner_text("#verdict")
        out["audio"] = await pg.evaluate("player.getAttribute('src')")
        await shot(pg, "wrong")
        n = 0
        while n < 60:
            await pg.click("#next"); await pg.wait_for_timeout(40)
            if not await pg.evaluate("!!queue[index]"): break
            if n == 4: await shot(pg, "q2")
            i = await pg.evaluate("shownOpts.indexOf(queue[index].a)")
            await (await pg.query_selector_all("#opts .opt"))[i].click(); await pg.wait_for_timeout(40)
            if n == 4: await shot(pg, "right2")
            n += 1
        out["answered"] = n
        out["done"] = await pg.inner_text("#hint")
        out["mixed_size"] = await pg.evaluate("buildTopic(MIXED_TOPIC), queue.length")
        await pg.evaluate("queue = [CARDS.find(c => c.id === 'wi-soon')]; index = 0; mode = 'topic'; topicN = 4; render();"); await pg.wait_for_timeout(100)
        await shot(pg, "pick")
        wrong = await pg.evaluate("shownOpts.findIndex(o => o !== queue[index].a)")
        await (await pg.query_selector_all("#opts .opt"))[wrong].click(); await pg.wait_for_timeout(150)
        out["pick_verdict"] = await pg.inner_text("#verdict")
        out["pick_q"] = await pg.inner_text("#q")
        await shot(pg, "pick-wrong")
        await pg.evaluate("queue = [CARDS.find(c => c.id === 'a1-smoking')]; index = 0; render();"); await pg.wait_for_timeout(100)
        i = await pg.evaluate("shownOpts.indexOf('')")
        await (await pg.query_selector_all("#opts .opt"))[i].click(); await pg.wait_for_timeout(150)
        out["zero_q"] = await pg.inner_text("#q")
        await shot(pg, "zero")
        await pg.evaluate("queue = [CARDS.find(c => c.id === 'pp-waiting')]; index = 0; render();"); await pg.wait_for_timeout(100)
        out["b2_kind"] = await pg.inner_text("#kind")
        # самые длинные варианты
        await pg.evaluate("queue = [CARDS.find(c => c.id === 'qu-indirect')]; index = 0; mode = 'topic'; topicN = 3; render();"); await pg.wait_for_timeout(100)
        await shot(pg, "long")
        out["long_overflow"] = await pg.evaluate("[...document.querySelectorAll('#opts .opt')].some(b => b.scrollWidth > b.clientWidth + 1)")
        # все карточки: ни один вариант не вылезает за кнопку
        out["any_overflow"] = await pg.evaluate("""(() => { const bad = []; CARDS.forEach(c => { queue = [c]; index = 0; render();
            if ([...document.querySelectorAll('#opts .opt')].some(b => b.scrollWidth > b.clientWidth + 1)) bad.push(c.id); }); return bad; })()""")
        await ctx.close()
        for (w, h, name) in [(1180, 760, "pad-land"), (820, 1130, "pad-port")]:
            ctx, pg = await mk(w, h)
            await shot(pg, name + "-rule")
            await pg.click("#go"); await pg.wait_for_timeout(200)
            await shot(pg, name + "-q")
            out[name + "_hscroll"] = await pg.evaluate("document.documentElement.scrollWidth > window.innerWidth")
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
