import asyncio, json, time, pathlib, subprocess, sys
from playwright.async_api import async_playwright
root = pathlib.Path("kogo").resolve()
srv = subprocess.Popen([sys.executable, "-m", "http.server", "8766", "--bind", "127.0.0.1"], cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
URL = "http://127.0.0.1:8766/preview.html"
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
        out["first_tab"] = await pg.evaluate("document.getElementById('rule').hidden ? 'drill' : 'rule'")
        await pg.screenshot(path=str(root / "s-rule.png"))
        await pg.evaluate("document.getElementById('rule').scrollTop = 620")
        await pg.wait_for_timeout(150)
        await pg.screenshot(path=str(root / "s-rule2.png"))
        # тема 1 раскрыта
        await pg.click(".t-item:nth-child(1) .t-head"); await pg.wait_for_timeout(150)
        await pg.evaluate("document.querySelector('.t-item:nth-child(1)').scrollIntoView()")
        await pg.screenshot(path=str(root / "s-topic.png"))
        # тренировка
        await pg.click("#tabDrill"); await pg.wait_for_timeout(150)
        await pg.screenshot(path=str(root / "s-q.png"))
        wrong = await pg.evaluate("shownOpts.findIndex(o => o !== queue[index].a)")
        btns = await pg.query_selector_all("#opts .opt"); await btns[wrong].click(); await pg.wait_for_timeout(200)
        out["verdict_wrong"] = await pg.inner_text("#verdict")
        out["audio"] = await pg.evaluate("player.getAttribute('src')")
        await pg.screenshot(path=str(root / "s-wrong.png"))
        # пройти всю сессию правильно
        n = 0
        while n < 60:
            await pg.click("#next"); await pg.wait_for_timeout(60)
            has = await pg.evaluate("!!queue[index]")
            if not has: break
            i = await pg.evaluate("shownOpts.indexOf(queue[index].a)")
            btns = await pg.query_selector_all("#opts .opt"); await btns[i].click(); await pg.wait_for_timeout(60)
            n += 1
        out["answered"] = n
        out["done_hint"] = await pg.inner_text("#hint")
        out["cards_in_progress"] = await pg.evaluate("Object.keys(progress).length")
        await ctx.close()
        # iPad альбомная
        ctx, pg = await mk(1180, 760)
        await pg.screenshot(path=str(root / "s-pad-rule.png"))
        await pg.click("#go"); await pg.wait_for_timeout(200)
        await pg.screenshot(path=str(root / "s-pad-q.png"))
        await ctx.close()
        await b.close()
    out["errors"] = errors
    print(json.dumps(out, ensure_ascii=False, indent=1))
try:
    asyncio.run(run())
finally:
    srv.terminate()
