# Схемы на оси времени для 12 времён: inline SVG, цвета — классами из стилей страницы.
import math, html

REF = {"present": 175, "past": 130, "future": 215}
NOW2 = {"past": 268, "future": 64}
AXY = 42

def _line(x1, y1, x2, y2, cls, w=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line class="{cls}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke-width="{w}"{d}/>'

def _text(x, y, s, cls, size=12):
    return f'<text class="{cls}" x="{x}" y="{y}" font-size="{size}" text-anchor="middle">{html.escape(s)}</text>'

def _dot(x, r=6):
    return f'<circle class="dot" cx="{x}" cy="{AXY}" r="{r}"/>'

def _bar(a, b):
    return f'<rect class="bar" x="{a}" y="{AXY - 7}" width="{b - a}" height="14" rx="7" stroke-width="2"/>'

def _arc(d, r):
    sx, sy = d, AXY - 8
    cx, cy = (d + r) / 2, 4
    ex, ey = r - 5, AXY - 12
    dx, dy = ex - cx, ey - cy
    n = math.hypot(dx, dy); dx, dy = dx / n, dy / n
    px, py = -dy, dx
    tip = (ex + dx * 7, ey + dy * 7)
    b1 = (ex - dx * 3 + px * 5, ey - dy * 3 + py * 5)
    b2 = (ex - dx * 3 - px * 5, ey - dy * 3 - py * 5)
    pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in (tip, b1, b2))
    return (f'<path class="arc" d="M{sx},{sy} Q{cx:.1f},{cy} {ex},{ey}" stroke-width="2"/>'
            f'<polygon class="arh" points="{pts}"/>')

def _brace(a, b, label):
    return (f'<path class="br" d="M{a},{AXY - 14} V{AXY - 20} H{b} V{AXY - 14}" stroke-width="1.5"/>'
            + _text((a + b) / 2, AXY - 25, label, "lb", 12))

def svg(t):
    time, asp = t["time"], t["aspect"]
    R = REF[time]
    parts = [_line(12, AXY, 300, AXY, "ax"), f'<polygon class="axh" points="300,{AXY - 6} 310,{AXY} 300,{AXY + 6}"/>']
    ref_label = "сейчас" if time == "present" else ("к сроку" if t["id"] == "fut-perf" else "тогда")
    if time in NOW2:
        n = NOW2[time]
        parts.append(_line(n, AXY - 18, n, AXY + 12, "now2", 1.5, "2 3"))
        parts.append(_text(n, 70, "сейчас", "lm", 12))
    show_ref = True
    if asp == "simple":
        if time == "present":
            parts += [_dot(x, 5) for x in (40, 95, 148, 205, 262)]
        else:
            parts.append(_dot(R))
            parts.append(_text(R, 70, "когда", "lr", 12))
            show_ref = False
    elif asp == "cont":
        parts.append(_bar(R - 55, R + 55))
    elif asp == "perf":
        parts.append(_dot(R - 85))
        parts.append(_arc(R - 85, R))
    elif asp == "pc":
        start = {"present": 62, "past": 24, "future": 36}[time]
        parts.append(_bar(start, R))
        parts.append(_brace(start, R, "сколько"))
    if show_ref:
        parts.append(_line(R, 12 if asp != "pc" else 30, R, AXY + 14, "ref", 2, "4 3"))
        parts.append(_text(R, 70, ref_label, "lr", 12))
    label = html.escape(t["name"] + ": " + t["mean"])
    return (f'<svg class="tl" viewBox="0 0 320 80" role="img" aria-label="{label}">' + "".join(parts) + "</svg>")
