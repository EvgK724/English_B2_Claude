import asyncio, pathlib
from playwright.async_api import async_playwright
from PIL import Image
SK = '<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light;box-sizing:border-box}body{margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif;background:#faf9f5;color:#141413}[hidden]:not([hidden=until-found i]){display:none!important}</style></head><body>'
pathlib.Path("countable/preview.html").write_text(SK + pathlib.Path("countable/index.html").read_text(encoding="utf-8") + "</body></html>", encoding="utf-8")
URL = "file://" + str(pathlib.Path("countable/preview.html").resolve())
async def main():
    errs, notes, shots = [], [], []
    async with async_playwright() as p:
        b = await p.chromium.launch(args=["--autoplay-policy=user-gesture-required"])
        async def page(w, h):
            pg = await b.new_page(viewport={"width": w, "height": h})
            pg.on("pageerror", lambda e: errs.append(str(e)))
            pg.on("console", lambda m: errs.append(m.type + ": " + m.text) if m.type == "error" else None)
            await pg.goto(URL); await pg.wait_for_timeout(250); return pg
        # телефон: правила, затем тренировка до и после ответа
        pg = await page(390, 844)
        await pg.screenshot(path="countable/s1.png"); shots.append("countable/s1.png")
        await pg.click("#go"); await pg.wait_for_timeout(120)
        await pg.screenshot(path="countable/s2.png"); shots.append("countable/s2.png")
        wrong = await pg.evaluate("shownOpts.find(o => o !== queue[index].a)")
        await pg.click(f"#opts .opt:nth-child({await pg.evaluate('shownOpts.indexOf(' + repr(wrong).replace(chr(39), chr(34)) + ') + 1')})")
        await pg.wait_for_timeout(400)
        notes.append("audio: " + await pg.evaluate("player.currentSrc.split('/').slice(-2).join('/') + (player.paused ? ' paused' : ' playing')"))
        await pg.screenshot(path="countable/s3.png"); shots.append("countable/s3.png")
        # «ничего»-вариант и also: тема 9 и тема 7
        await pg.click("#tabRule"); await pg.click(".t-item:nth-child(9) .t-head"); await pg.click(".t-item:nth-child(9) .t-train"); await pg.wait_for_timeout(100)
        for _ in range(6):
            cid = await pg.evaluate("queue[index].id")
            if cid == "t9-knowledge":
                i = await pg.evaluate('shownOpts.indexOf("") + 1'); await pg.click(f"#opts .opt:nth-child({i})")
                notes.append("also verdict: " + await pg.inner_text("#verdict")); break
            a = await pg.evaluate("queue[index].a"); i = await pg.evaluate(f"shownOpts.indexOf({a!r}) + 1".replace("'", '"'))
            await pg.click(f"#opts .opt:nth-child({i})"); await pg.click("#next")
        notes.append("topic status: " + await pg.inner_text("#status"))
        await pg.close()
        # iPad альбомная: тренировка
        pg = await page(1180, 760)
        await pg.click("#go"); await pg.wait_for_timeout(150)
        notes.append("ipad landscape k=" + await pg.evaluate("getComputedStyle(document.documentElement).getPropertyValue('--k')"))
        await pg.screenshot(path="countable/s4.png"); shots.append("countable/s4.png"); await pg.close()
        await b.close()
    ims = [Image.open(s) for s in shots]
    ph = [i.resize((int(i.width * 0.6), int(i.height * 0.6)), Image.LANCZOS) for i in ims[:3]]
    pad = ims[3].resize((int(ims[3].width * 0.6), int(ims[3].height * 0.6)), Image.LANCZOS)
    W = max(sum(i.width for i in ph) + 24, pad.width); H = ph[0].height + 12 + pad.height
    out = Image.new("RGB", (W, H), (60, 60, 60)); x = 0
    for i in ph: out.paste(i, (x, 0)); x += i.width + 12
    out.paste(pad, (0, ph[0].height + 12)); out.save("countable/look.png")
    print("errors:", errs or "none"); print("\n".join(notes))
asyncio.run(main())
