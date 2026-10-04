import asyncio, json, time, pathlib, subprocess, sys
from playwright.async_api import async_playwright
root = pathlib.Path("stative").resolve()
srv = subprocess.Popen([sys.executable, "-m", "http.server", "8769", "--bind", "127.0.0.1"], cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
URL = "http://127.0.0.1:8769/preview.html"
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
        ctx, pg = await mk(390, 800)
        await pg.screenshot(path=str(root / "s-rule.png"))
        await pg.evaluate("document.getElementById('rule').scrollTop = 560"); await pg.wait_for_timeout(120)
        await pg.screenshot(path=str(root / "s-rule2.png"))
        await pg.evaluate("document.getElementById('rule').scrollTop = 1180"); await pg.wait_for_timeout(120)
        await pg.screenshot(path=str(root / "s-rule3.png"))
        await pg.click("#tabDrill"); await pg.wait_for_timeout(150)
        await pg.screenshot(path=str(root / "s-q.png"))
        wrong = await pg.evaluate("shownOpts.findIndex(o => o !== queue[index].a)")
        await (await pg.query_selector_all("#opts .opt"))[wrong].click(); await pg.wait_for_timeout(200)
        out["verdict"] = await pg.inner_text("#verdict")
        out["audio"] = await pg.evaluate("player.getAttribute('src')")
        await pg.screenshot(path=str(root / "s-wrong.png"))
        n = 0
        while n < 70:
            await pg.click("#next"); await pg.wait_for_timeout(50)
            if not await pg.evaluate("!!queue[index]"): break
            i = await pg.evaluate("shownOpts.indexOf(queue[index].a)")
            await (await pg.query_selector_all("#opts .opt"))[i].click(); await pg.wait_for_timeout(50)
            n += 1
        out["answered"] = n
        out["done"] = await pg.inner_text("#hint")
        # тема 11 с «тоже верно»
        await pg.evaluate("buildTopic(11); setTab('drill'); render();"); await pg.wait_for_timeout(100)
        for k in range(4):
            has_also = await pg.evaluate("!!(queue[index] && queue[index].also)")
            if has_also:
                alt = await pg.evaluate("shownOpts.findIndex(o => o !== queue[index].a)")
                await (await pg.query_selector_all("#opts .opt"))[alt].click(); await pg.wait_for_timeout(120)
                out["also_verdict"] = await pg.inner_text("#verdict")
                break
            i = await pg.evaluate("shownOpts.indexOf(queue[index].a)")
            await (await pg.query_selector_all("#opts .opt"))[i].click(); await pg.wait_for_timeout(60)
            await pg.click("#next"); await pg.wait_for_timeout(60)
        await ctx.close()
        ctx, pg = await mk(1180, 760)
        await pg.screenshot(path=str(root / "s-pad-rule.png"))
        await pg.click("#go"); await pg.wait_for_timeout(200)
        await pg.screenshot(path=str(root / "s-pad-q.png"))
        await ctx.close(); await b.close()
    out["errors"] = errors
    print(json.dumps(out, ensure_ascii=False, indent=1))
try:
    asyncio.run(run())
finally:
    srv.terminate()
