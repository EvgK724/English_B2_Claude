# Плитка «Английский»: веер карточек, на передней — Aa (A светлая, a оранжевая), сверху синим english
import asyncio, base64, pathlib, io
from playwright.async_api import async_playwright
from PIL import Image
here = pathlib.Path(__file__).resolve().parent
S = here.parent.parent
font_b64 = base64.b64encode((S / "tile/node_modules/@fontsource/dm-serif-display/files/dm-serif-display-latin-400-normal.woff2").read_bytes()).decode()
JS = r"""
async (b64) => {
  const buf = Uint8Array.from(atob(b64), ch => ch.charCodeAt(0)).buffer;
  const face = new FontFace("DMSD", buf); await face.load(); document.fonts.add(face);
  const S = 1024, c = document.createElement("canvas"); c.width = c.height = S;
  const x = c.getContext("2d");
  x.fillStyle = "#0e1113"; x.fillRect(0, 0, S, S);
  const W = 540, H = 660, R = 64, rad = d => d * Math.PI / 180;
  const card = (cx, cy, rot, fill, stroke, shadow) => {
    x.save(); x.translate(cx, cy); x.rotate(rad(rot));
    x.shadowColor = "rgba(0,0,0,.5)"; x.shadowBlur = shadow; x.shadowOffsetY = shadow * 0.4;
    x.beginPath(); x.roundRect(-W/2, -H/2, W, H, R); x.fillStyle = fill; x.fill();
    x.shadowColor = "transparent"; x.shadowBlur = 0; x.shadowOffsetY = 0;
    x.lineWidth = 4; x.strokeStyle = stroke; x.stroke();
    return () => x.restore();
  };
  // две карточки сзади — колода тем
  card(430, 540, -11, "#13181b", "#232a2e", 36)();
  card(600, 530, 9, "#161c1f", "#283034", 40)();
  // передняя
  const done = card(512, 520, -1.5, "#1b2125", "#313a3f", 48);
  x.textBaseline = "alphabetic"; x.textAlign = "left";
  x.fillStyle = "#7cc0dd"; x.font = "64px DMSD"; x.fillText("english", -W/2 + 48, -H/2 + 104);
  let fs = 360; x.font = fs + "px DMSD";
  while (x.measureText("Aa").width > W - 120){ fs -= 6; x.font = fs + "px DMSD"; }
  const mA = x.measureText("A"), mAa = x.measureText("Aa");
  const left = -mAa.width / 2, base = 150;
  x.fillStyle = "#ececea"; x.fillText("A", left, base);
  x.fillStyle = "#d97757"; x.fillText("a", left + mA.width, base);
  // строка-«прогресс» внизу карточки
  const bw = W - 96, by = H/2 - 78;
  x.fillStyle = "#2a3236"; x.beginPath(); x.roundRect(-bw/2, by, bw, 12, 6); x.fill();
  x.fillStyle = "#d97757"; x.beginPath(); x.roundRect(-bw/2, by, bw * 0.62, 12, 6); x.fill();
  done();
  return c.toDataURL("image/png");
}
"""
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page()
        await pg.goto("about:blank")
        data = await pg.evaluate(JS, font_b64); await b.close()
    big = Image.open(io.BytesIO(base64.b64decode(data.split(",", 1)[1]))).convert("RGB")
    big.save(here / "tile-1024.png", optimize=True)
    big.resize((400, 400), Image.LANCZOS).save(here / "icon-400.png", optimize=True)
    print("ok", (here / "icon-400.png").stat().st_size)
asyncio.run(main())
