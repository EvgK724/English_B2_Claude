import asyncio, json, time, pathlib, subprocess, sys
from playwright.async_api import async_playwright
from PIL import Image
root = pathlib.Path("tenses").resolve()
srv = subprocess.Popen([sys.executable, "-m", "http.server", "8788", "--bind", "127.0.0.1"], cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
URL = "http://127.0.0.1:8788/preview.html"
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
        await shot(pg, "grid")
        out["hscroll"] = await pg.evaluate("document.documentElement.scrollWidth > window.innerWidth")
        for cid in ("pres-perf", "past-cont", "pres-pc"):
            await pg.click(f'.tc[data-id="{cid}"]'); await pg.wait_for_timeout(500)
            await shot(pg, "cell-" + cid)
        out["detail_name"] = await pg.inner_text(".td-name")
        await pg.click(".td .ex-play"); await pg.wait_for_timeout(200)
        out["audio"] = await pg.evaluate("player.getAttribute('src')")
        # все 12 схем на одном листе
        await pg.evaluate("""(() => {
          const w = document.createElement('div'); w.id = 'allsvg';
          w.style.cssText = 'position:fixed;inset:0;z-index:99;background:#171c1f;overflow:auto;padding:8px;display:grid;grid-template-columns:1fr 1fr;gap:6px';
          TENSES.forEach(t => { const d = document.createElement('div'); d.style.cssText='color:#e8e8e8;font:12px sans-serif'; d.innerHTML = '<div>' + t.name + '</div>' + t.svg; w.append(d); });
          document.body.append(w);
        })()""")
        await pg.set_viewport_size({"width": 700, "height": 820}); await pg.wait_for_timeout(300)
        await pg.screenshot(path=str(root / "s-alltl.png"))
        await pg.evaluate("document.getElementById('allsvg').remove()")
        await pg.set_viewport_size({"width": 390, "height": 800}); await pg.wait_for_timeout(200)
        # правила ниже
        await pg.evaluate("document.querySelector('.r-right').scrollIntoView()"); await pg.wait_for_timeout(150)
        await shot(pg, "right")
        H = await pg.evaluate("document.getElementById('rule').scrollHeight")
        await pg.evaluate(f"document.getElementById('rule').scrollTop = {H} - 1800"); await pg.wait_for_timeout(150)
        await shot(pg, "right2")
        # тренировка
        out["first_session"] = await pg.evaluate("""(() => { buildMain(); const n = {}; queue.forEach(c => n['t' + c.t] = (n['t' + c.t] || 0) + 1); return n; })()""")
        await pg.evaluate("buildMain(); render();")
        await pg.click("#tabDrill"); await pg.wait_for_timeout(150)
        await shot(pg, "q")
        wrong = await pg.evaluate("shownOpts.findIndex(o => o !== queue[index].a && !(queue[index].also && queue[index].also[o]))")
        await (await pg.query_selector_all("#opts .opt"))[wrong].click(); await pg.wait_for_timeout(200)
        out["verdict"] = await pg.inner_text("#verdict")
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
        # узнай время
        await pg.evaluate("buildTopic(11); setTab('drill'); render();"); await pg.wait_for_timeout(150)
        await shot(pg, "recognize")
        # кнопка «Потренировать» из карточки времени
        await pg.click("#tabRule"); await pg.wait_for_timeout(150)
        await pg.click('.tc[data-id="past-perf"]'); await pg.wait_for_timeout(400)
        await pg.click(".td .t-train"); await pg.wait_for_timeout(200)
        out["train_from_cell"] = await pg.inner_text("#kind")
        # восстановление выбранной клетки
        await pg.reload(); await pg.wait_for_timeout(500)
        await pg.click("#tabRule"); await pg.wait_for_timeout(150)
        out["restored"] = await pg.evaluate("document.querySelector('.tc[aria-pressed=\"true\"]') && document.querySelector('.tc[aria-pressed=\"true\"]').dataset.id")
        await ctx.close()
        for (w, h, name) in [(1180, 760, "pad-land"), (820, 1130, "pad-port")]:
            ctx, pg = await mk(w, h)
            await pg.click('.tc[data-id="pres-perf"]'); await pg.wait_for_timeout(400)
            await pg.evaluate("document.getElementById('rule').scrollTop = 0"); await pg.wait_for_timeout(150)
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
sheet(phone[:5], "sheet1.png"); sheet(phone[5:], "sheet2.png")
sheet([p for p in shots if "pad" in p.name], "sheet3.png", 420)
