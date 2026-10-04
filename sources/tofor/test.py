import asyncio, json, time, pathlib, subprocess, sys
from playwright.async_api import async_playwright
from PIL import Image
root = pathlib.Path("tofor").resolve()
srv = subprocess.Popen([sys.executable, "-m", "http.server", "8775", "--bind", "127.0.0.1"], cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
URL = "http://127.0.0.1:8775/preview.html"
shots = []
async def run():
    out = {}
    async with async_playwright() as p:
        b = await p.chromium.launch()
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
        for k, y in enumerate([700, 1400, 2100, 2800]):
            if y > H - 400: break
            await pg.evaluate(f"document.getElementById('rule').scrollTop = {y}"); await pg.wait_for_timeout(120)
            await shot(pg, f"rule{k+2}")
        # горизонтальная прокрутка страницы
        out["hscroll"] = await pg.evaluate("document.documentElement.scrollWidth > window.innerWidth")
        # состав первой сессии
        out["first_session"] = await pg.evaluate("""(() => { buildMain(); const n = {}; queue.forEach(c => { const k = c.t === SORT_TOPIC ? 'list-' + c.a : 't' + c.t; n[k] = (n[k] || 0) + 1; }); return n; })()""")
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
            i = await pg.evaluate("shownOpts.indexOf(queue[index].a)")
            await (await pg.query_selector_all("#opts .opt"))[i].click(); await pg.wait_for_timeout(40)
            n += 1
        out["answered"] = n
        out["done"] = await pg.inner_text("#hint")
        # списки: кнопка «Проверить себя по спискам»
        await pg.click("#tabRule"); await pg.wait_for_timeout(100)
        await pg.evaluate("document.getElementById('sortGo').scrollIntoView()"); await pg.click("#sortGo"); await pg.wait_for_timeout(150)
        out["sort_kind"] = await pg.inner_text("#kind"); out["sort_hint"] = await pg.inner_text("#hint")
        await shot(pg, "sort")
        i = await pg.evaluate("shownOpts.indexOf(queue[index].a)")
        await (await pg.query_selector_all("#opts .opt"))[i].click(); await pg.wait_for_timeout(150)
        out["sort_why"] = await pg.inner_text("#why")
        await shot(pg, "sort-ok")
        # тема 8 с «тоже верно»
        await pg.evaluate("buildTopic(8); setTab('drill'); render();"); await pg.wait_for_timeout(100)
        for k in range(8):
            has_also = await pg.evaluate("!!(queue[index] && queue[index].also)")
            if has_also:
                alt = await pg.evaluate("shownOpts.findIndex(o => queue[index].also[o])")
                await (await pg.query_selector_all("#opts .opt"))[alt].click(); await pg.wait_for_timeout(120)
                out["also_verdict"] = await pg.inner_text("#verdict")
                break
            i = await pg.evaluate("shownOpts.indexOf(queue[index].a)")
            await (await pg.query_selector_all("#opts .opt"))[i].click(); await pg.wait_for_timeout(60)
            await pg.click("#next"); await pg.wait_for_timeout(60)
        # итог — только предложения
        out["mixed_only_sentences"] = await pg.evaluate("buildTopic(MIXED_TOPIC), queue.every(c => c.t < SORT_TOPIC) && queue.length === MIXED_SIZE")
        # тема в аккордеоне с примерами
        await pg.evaluate("setTab('rule'); openTopic = 7; renderTopics(); document.querySelector('.t-head[aria-expanded=\"true\"]').scrollIntoView()"); await pg.wait_for_timeout(150)
        await shot(pg, "topic7")
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
# контактные листы
def sheet(paths, name, h=560):
    ims = [Image.open(p) for p in paths]
    ims = [im.resize((int(im.width * h / im.height), h)) for im in ims]
    W = sum(im.width for im in ims) + 10 * (len(ims) + 1)
    s = Image.new("RGB", (W, h + 20), (60, 60, 60)); x = 10
    for im in ims: s.paste(im, (x, 10)); x += im.width + 10
    s.save(root / name)
phone = [p for p in shots if "pad" not in p.name]
sheet(phone[:len(phone)//2 + 1], "sheet1.png"); sheet(phone[len(phone)//2 + 1:], "sheet2.png")
sheet([p for p in shots if "pad" in p.name], "sheet3.png", 420)
