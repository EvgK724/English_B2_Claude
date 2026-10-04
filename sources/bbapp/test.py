import asyncio, json, time, pathlib, subprocess, sys
from playwright.async_api import async_playwright
root = pathlib.Path("bbapp").resolve()
srv = subprocess.Popen([sys.executable, "-m", "http.server", "8767", "--bind", "127.0.0.1"], cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
URL = "http://127.0.0.1:8767/preview.html"
DAY = 86400000
def seed(now):
    steps = {"better-call-saul":0,"in-the-business":1,"the-one-who-knocks":2,"no-more-half-measures":3,"just-because-doesnt-mean":2,
             "know-who-youre-talking-to":1,"either-or":2,"when-i-say-so":0,"say-my-name":2,"good-at-it":1,"gotta-be-kidding":3,
             "get-away-with-it":0,"whats-the-point-of":1,"let-me-do-it":0,"tread-lightly":2,"a-man-provides":0,"stay-out-of":1,
             "same-as-you":0,"youre-damn-right":1,"committed-enough":2}
    return {k: {"step": v, "due": now - DAY, "ts": now - 2*DAY} for k, v in steps.items()}
async def run():
    out = {"shots": []}
    async with async_playwright() as p:
        b = await p.chromium.launch()
        errors = []
        async def mk(w, h, seeded=True):
            ctx = await b.new_context(viewport={"width": w, "height": h}, device_scale_factor=2)
            pg = await ctx.new_page()
            pg.on("pageerror", lambda e: errors.append(str(e)))
            pg.on("console", lambda m: errors.append("console:" + m.text) if m.type == "error" else None)
            if seeded:
                now = int(time.time() * 1000)
                await pg.add_init_script("localStorage.setItem('bbphrases:state', " + json.dumps(json.dumps({"progress": seed(now)})) + ")")
            await pg.goto(URL); await pg.wait_for_timeout(400)
            return ctx, pg
        ctx, pg = await mk(390, 800)
        out["plan"] = await pg.inner_text("#plan")
        out["kicker"] = await pg.inner_text("#heroKicker")
        await pg.screenshot(path=str(root / "s-home.png"))
        await pg.click("#start"); await pg.wait_for_timeout(250)
        await pg.screenshot(path=str(root / "s-intro.png"))
        await pg.click("#next"); await pg.wait_for_timeout(150)
        shot = {}
        types = []
        wrong_build = False
        for i in range(60):
            item = await pg.evaluate("queue[index] ? [queue[index].type, queue[index].card.id] : null")
            if not item: break
            t, cid = item
            types.append(t)
            if t == "intro":
                await pg.click("#next"); await pg.wait_for_timeout(100); continue
            if t not in shot:
                await pg.screenshot(path=str(root / f"s-{t}.png")); shot[t] = True
            if t == "build":
                # собрать: первый раз — с ошибкой (поменять два первых слова), потом правильно
                order = await pg.evaluate("build.toks.map(t => t.key)")
                seq = list(range(len(order)))
                if not wrong_build and len(seq) > 2:
                    seq[0], seq[1] = seq[1], seq[0]
                for k in seq:
                    key = order[k]
                    pos = await pg.evaluate("(key) => build.pool.findIndex(ti => build.toks[ti].key === key)", key)
                    tiles = await pg.query_selector_all("#opts .tile")
                    await tiles[pos].click(); await pg.wait_for_timeout(40)
                    if k == seq[len(seq)//2] and "build-mid" not in shot:
                        await pg.screenshot(path=str(root / "s-build-mid.png")); shot["build-mid"] = True
                if not wrong_build and len(seq) > 2:
                    wrong_build = True
                    out["build_wrong_verdict"] = await pg.inner_text("#verdict")
                    await pg.screenshot(path=str(root / "s-build-wrong.png"))
            else:
                idx = await pg.evaluate("shownOpts.findIndex(o => o.id === queue[index].card.id)")
                btns = await pg.query_selector_all("#opts .opt")
                await btns[idx].click()
            await pg.wait_for_timeout(80)
            await pg.click("#next"); await pg.wait_for_timeout(80)
        out["types"] = types
        out["result"] = await pg.inner_text("#result")
        await pg.screenshot(path=str(root / "s-done.png"))
        await pg.click("#tabDict"); await pg.wait_for_timeout(150)
        await pg.click(".d-item:nth-child(1) .d-row"); await pg.wait_for_timeout(150)
        await pg.screenshot(path=str(root / "s-dict.png"))
        await pg.fill("#find", "Сол"); await pg.wait_for_timeout(100)
        out["search_sol"] = await pg.evaluate("[...document.querySelectorAll('.d-term')].map(n => n.textContent)")
        await ctx.close()
        ctx, pg = await mk(1180, 760)
        await pg.screenshot(path=str(root / "s-pad-home.png"))
        await pg.click("#start"); await pg.wait_for_timeout(200)
        # дойти до «собери фразу»
        for i in range(40):
            t = await pg.evaluate("queue[index] && queue[index].type")
            if t == "build" or not t: break
            if t == "intro":
                await pg.click("#next"); await pg.wait_for_timeout(80); continue
            idx = await pg.evaluate("shownOpts.findIndex(o => o.id === queue[index].card.id)")
            btns = await pg.query_selector_all("#opts .opt"); await btns[idx].click(); await pg.wait_for_timeout(60)
            await pg.click("#next"); await pg.wait_for_timeout(60)
        await pg.screenshot(path=str(root / "s-pad-build.png"))
        await pg.click("#tabDict"); await pg.wait_for_timeout(150)
        await pg.screenshot(path=str(root / "s-pad-dict.png"))
        await ctx.close()
        await b.close()
    out["errors"] = errors
    print(json.dumps(out, ensure_ascii=False, indent=1))
try:
    asyncio.run(run())
finally:
    srv.terminate()
