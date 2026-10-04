import asyncio, json, time, pathlib, subprocess, sys
from playwright.async_api import async_playwright
root = pathlib.Path("phrasal").resolve()
srv = subprocess.Popen([sys.executable, "-m", "http.server", "8765", "--bind", "127.0.0.1"], cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
URL = "http://127.0.0.1:8765/preview.html"
DAY = 86400000
def seed_progress(now_ms):
    # как у пользователя: 11 карточек в работе; для проверки часть из них уже к повтору, разные ступени
    steps = {"wear-off":0,"come-down-with":0,"carry-out":1,"point-out":1,"find-out":2,"set-up":2,"turn-out":3,"come-up-with":0,"look-into":1,"deal-with":2,"end-up":0}
    return {k: {"step": v, "due": now_ms - DAY, "ts": now_ms - 2*DAY} for k, v in steps.items()}
async def run():
    out = {}
    async with async_playwright() as p:
        b = await p.chromium.launch()
        errors = []
        async def mk(w, h, seed=True):
            ctx = await b.new_context(viewport={"width": w, "height": h}, device_scale_factor=2)
            pg = await ctx.new_page()
            pg.on("pageerror", lambda e: errors.append(str(e)))
            pg.on("console", lambda m: errors.append("console:" + m.text) if m.type == "error" else None)
            if seed:
                now = int(time.time() * 1000)
                await pg.add_init_script("localStorage.setItem('flashcards:state', " + json.dumps(json.dumps({"progress": seed_progress(now)})) + ")")
            await pg.goto(URL); await pg.wait_for_timeout(400)
            return ctx, pg
        # ——— телефон
        ctx, pg = await mk(390, 800)
        # где найден глагол в каждом примере
        out["matches"] = await pg.evaluate("""() => CARDS.map(c => { const m = findVerb(c); return [c.id, m ? m.joined : null, m ? m.ranges.map(r => c.ex.slice(r[0], r[1])).join(' … ') : null]; })""")
        out["distractors"] = await pg.evaluate("""() => CARDS.map(c => [c.term, pickDistractors(c,'rec').map(coreRu).join(' | '), pickDistractors(c,'prod').map(x=>x.term).join(' | ')])""")
        out["home_plan"] = await pg.inner_text("#plan")
        await pg.screenshot(path=str(root / "s-phone-home.png"))
        await pg.click("#start"); await pg.wait_for_timeout(300)
        out["first_kind"] = await pg.inner_text("#kind")
        out["audio_src"] = await pg.evaluate("player.getAttribute('src')")
        await pg.screenshot(path=str(root / "s-phone-intro.png"))
        await pg.click("#next"); await pg.wait_for_timeout(200)
        seen_types = []
        shot = {"rec": False, "cloze": False, "prod": False}
        wrong_done = False
        for i in range(40):
            item = await pg.evaluate("queue[index] ? [queue[index].type, queue[index].card.id] : null")
            if not item: break
            t, cid = item
            seen_types.append(t)
            if t == "intro":
                await pg.click("#next"); await pg.wait_for_timeout(120); continue
            if t in shot and not shot[t]:
                await pg.screenshot(path=str(root / f"s-phone-{t}.png")); shot[t] = True
            # один раз отвечаем неверно
            idx = await pg.evaluate("shownOpts.findIndex(o => o.id " + ("!==" if not wrong_done else "===") + " queue[index].card.id)")
            btns = await pg.query_selector_all("#opts .opt")
            await btns[idx].click(); await pg.wait_for_timeout(150)
            if not wrong_done:
                wrong_done = True
                out["wrong_verdict"] = await pg.inner_text("#verdict")
                await pg.screenshot(path=str(root / "s-phone-wrong.png"))
            await pg.click("#next"); await pg.wait_for_timeout(120)
        out["types"] = seen_types
        out["after_home"] = await pg.inner_text("#result")
        await pg.screenshot(path=str(root / "s-phone-done.png"))
        out["progress_after"] = await pg.evaluate("Object.fromEntries(Object.entries(progress).map(([k,v]) => [k, v.step]))")
        # словарь
        await pg.click("#tabDict"); await pg.wait_for_timeout(200)
        await pg.click(".d-item:nth-child(2) .d-row"); await pg.wait_for_timeout(200)
        await pg.screenshot(path=str(root / "s-phone-dict.png"))
        await pg.fill("#find", "исключ"); await pg.wait_for_timeout(150)
        out["search"] = await pg.evaluate("[...document.querySelectorAll('.d-term')].map(n => n.textContent)")
        await ctx.close()
        # ——— iPad, альбомная
        ctx, pg = await mk(1180, 760)
        await pg.screenshot(path=str(root / "s-pad-home.png"))
        await pg.click("#start"); await pg.wait_for_timeout(200)
        await pg.click("#next"); await pg.wait_for_timeout(200)
        await pg.screenshot(path=str(root / "s-pad-drill.png"))
        await pg.click("#tabDict"); await pg.wait_for_timeout(200)
        await pg.screenshot(path=str(root / "s-pad-dict.png"))
        await ctx.close()
        # ——— iPad, книжная, без прогресса (первый запуск на новом устройстве)
        ctx, pg = await mk(820, 1130, seed=False)
        await pg.screenshot(path=str(root / "s-padp-home.png"))
        await ctx.close()
        await b.close()
    out["errors"] = errors
    print(json.dumps(out, ensure_ascii=False, indent=1))
try:
    asyncio.run(run())
finally:
    srv.terminate()
