#!/usr/bin/env python3
"""og.png 1200x630 — Man Yaman Bake Shop — 'kakanin layers' poster. v2:
advance-width (anchor) centering + measured clearance asserts. t_5fc04d16 2026-11-24."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "public", "og.png")

UBE = (70, 25, 74); UBE2 = (99, 51, 95); CREAM = (251, 243, 230); GOLD = (210, 154, 47)
JADE = (122, 158, 122); PLUM = (141, 85, 135); LAV = (198, 168, 203); MIST = (214, 192, 214)

def font(paths, size):
    bases = ["/System/Library/Fonts/Supplemental/", "/System/Library/Fonts/"]
    for b in bases:
        for n in paths:
            p = b + n
            if os.path.exists(p):
                try: return ImageFont.truetype(p, size)
                except Exception: pass
    return ImageFont.load_default()

serif = lambda s: font(["Iowan Old Style.ttc", "Palatino.ttc", "Georgia.ttf", "Times New Roman.ttf"], s)
sans = lambda s: font(["Futura.ttc", "HelveticaNeue.ttc", "Arial.ttf"], s)

img = Image.new("RGB", (W, H), UBE)
d = ImageDraw.Draw(img)

d.rectangle([0, 470, W, H], fill=UBE2)          # lower band
d.rectangle([0, 0, W, 6], fill=GOLD)
d.rectangle([0, H-6, W, H], fill=GOLD)

def center(text, f, cy, fill, tracking=0):
    """Anchor-centered; returns (ink_left, ink_right, ink_top, ink_bottom)."""
    if tracking:
        widths = [d.textlength(ch, font=f) for ch in text]
        tw = sum(widths) + tracking * (len(text) - 1)
        x = (W - tw) / 2.0
        tops, bots = [], []
        for ch, w in zip(text, widths):
            bb = d.textbbox((x, cy), ch, font=f, anchor="lm")
            d.text((x, cy), ch, font=f, fill=fill, anchor="lm")
            tops.append(bb[1]); bots.append(bb[3])
            x += w + tracking
        return (int((W - tw) / 2), int((W + tw) / 2), min(tops), max(bots))
    bb = d.textbbox((W / 2, cy), text, font=f, anchor="mm")
    d.text((W / 2, cy), text, font=f, fill=fill, anchor="mm")
    return (bb[0], bb[2], bb[1], bb[3])   # normalize to (left, right, top, bottom)

# kicker
k = center("V E R N O N   ·   C O N N E C T I C U T   —   N O W   O P E N", sans(22), 52, GOLD, tracking=3)
# brand
b1 = center("MAN YAMAN", serif(124), 168, CREAM)
b2 = center("B A K E   S H O P", sans(34), 272, LAV, tracking=8)
# gold double rule under brand
d.rectangle([W/2-140, 316, W/2+140, 319], fill=GOLD)
d.rectangle([W/2-140, 325, W/2+140, 328], fill=GOLD)
# headline lines
l1 = center("Pandesal at dawn.", serif(48), 376, CREAM)
l2 = center("Kakanin to remember.", serif(48), 438, GOLD)
# sapin-sapin stripe (gold / jade / plum)
sx0, sx1 = 150, W-150
third = (sx1-sx0)/3.0
STRIPE_TOP = 484
d.rectangle([sx0, STRIPE_TOP, sx0+third, STRIPE_TOP+12], fill=GOLD)
d.rectangle([sx0+third, STRIPE_TOP, sx0+2*third, STRIPE_TOP+12], fill=JADE)
d.rectangle([sx0+2*third, STRIPE_TOP, sx1, STRIPE_TOP+12], fill=PLUM)
# menu / address / tag lines (all inside the deeper band, clear of stripe)
m = center("Pandesal  ·  Ensaymada  ·  Sapin-Sapin  ·  Bibingka  ·  Ube Cake  ·  Empanadas", sans(24), 524, MIST)
a = center("101 West Street, Unit B  —  Vernon, CT 06066  —  (860) 281-4546", sans(22), 562, CREAM)
t = center("Traditional Filipino baked goods, cakes & kakanin", sans(20), 596, LAV)

# geometry asserts (the model's nit lines, proven by measurement)
assert l2[3] < STRIPE_TOP - 8, f"line2 ink bottom {l2[3]} collides stripe {STRIPE_TOP}"
assert t[3] < H - 8, f"tag line bottom {t[3]} hits bottom bar"
assert a[3] < m[0]*0 + 585, f"address bottom {a[3]}"
for name, box, y in [("kicker", k, 52), ("brand", b1, 168), ("bakeshop", b2, 272),
                     ("l1", l1, 376), ("l2", l2, 438), ("menu", m, 524), ("addr", a, 562), ("tag", t, 596)]:
    off = abs(((box[0] + box[1]) / 2) - W / 2)
    assert off <= 2, f"{name} center off by {off}px"
    assert box[0] >= 24 and box[1] <= W - 24, f"{name} ink near canvas edge {box}"
    print(f"{name:9s} ink x[{box[0]},{box[1]}] y[{box[2]},{box[3]}] center-offset {off:.1f}px")
print(f"line2/stripe clearance {STRIPE_TOP - l2[3]}px  stripe@{STRIPE_TOP}")

img.save(OUT, "PNG", optimize=True)
print("wrote", OUT, os.path.getsize(OUT), "bytes")
