import asyncio, pathlib
from playwright.async_api import async_playwright
from PIL import Image
src = pathlib.Path("index.html").read_text(encoding="utf-8")
pathlib.Path("preview.html").write_text('<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light;box-sizing:border-box}body{margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif;background:#faf9f5;color:#141413}[hidden]:not([hidden=until-found i]){display:none!important}</style></head><body>' + src + '</body></html>', encoding="utf-8")
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=["--autoplay-policy=user-gesture-required"])
        pg = await b.new_page(viewport={"width": 390, "height": 844})
        errs = []
        pg.on("pageerror", lambda e: errs.append("pageerror: " + str(e)))
        pg.on("console", lambda m: errs.append(m.type + ": " + m.text) if m.type == "error" else None)
        await pg.goto("file://" + str(pathlib.Path("preview.html").resolve())); await pg.wait_for_timeout(300)
        shots = []
        await pg.screenshot(path="s1.png"); shots.append("s1.png")
        await pg.click(".t-item:nth-child(7) .t-head"); await pg.wait_for_timeout(150)
        await pg.eval_on_selector(".t-item:nth-child(7)", "e => e.scrollIntoView({block:'start'})"); await pg.wait_for_timeout(100)
        await pg.screenshot(path="s2.png"); shots.append("s2.png")
        await pg.click("#go"); await pg.wait_for_timeout(150)
        await pg.screenshot(path="s3.png"); shots.append("s3.png")
        await pg.click("[data-opt='an']"); await pg.wait_for_timeout(400)
        audio = await pg.evaluate("player.currentSrc.split('/').slice(-2).join('/') + (player.paused ? ' paused' : ' playing')")
        await pg.screenshot(path="s4.png"); shots.append("s4.png")
        # тренировка темы 7: ответ the на «in ___ hospital» должен засчитываться как «тоже верно»
        await pg.click("#tabRule"); await pg.click(".t-item:nth-child(7) .t-train"); await pg.wait_for_timeout(150)
        found = None
        for _ in range(8):
            q = await pg.inner_text("#q")
            if "My father" in q:
                await pg.click("[data-opt='the']"); found = await pg.inner_text("#verdict"); break
            ans = await pg.evaluate("queue[index].a")
            await pg.click(f"[data-opt='{ans}']"); await pg.click("#next")
        status = await pg.inner_text("#status")
        await b.close()
    imgs = [Image.open(s) for s in shots]
    out = Image.new("RGB", (sum(i.width for i in imgs) + 12 * 3, max(i.height for i in imgs)), (60, 60, 60)); x = 0
    for i in imgs: out.paste(i, (x, 0)); x += i.width + 12
    out.save("look.png")
    print("errors:", errs or "none"); print("audio after answer:", audio); print("also-answer verdict:", found); print("topic status:", status)
asyncio.run(main())
