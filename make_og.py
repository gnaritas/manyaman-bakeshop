#!/usr/bin/env python3
"""og.png 1200x630 — Man Yaman Bake Shop — 'kakanin layers' poster.
Ube-ink ground, cream serif brand, sapin-sapin stripe (gold/jade/plum),
pandesal-gold rules. Shop identity only, no third-party marks."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public", "og.png")

UBE = (70, 25, 74); UBE2 = (99, 51, 95); CREAM = (251, 243, 230); GOLD = (210, 154, 47)
JADE = (63, 112, 80); PLUM = (141, 85, 135); LAV = (198, 168, 203); MIST = (214, 192, 214)

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
sans = lambda s: font(["Futura.ttc", "HelveticaNeue.ttc", "HelveticaNeue.ttc", "Arial.ttf"], s)

img = Image.new("RGB", (W, H), UBE)
d = ImageDraw.Draw(img)

# lower third band (deeper ube) like a counter shadow
d.rectangle([0, 470, W, H], fill=UBE2)
# gold rules top and bottom edges
d.rectangle([0, 0, W, 6], fill=GOLD)
d.rectangle([0, H-6, W, H], fill=GOLD)

def center(text, f, y, fill, tracking=0):
    if tracking:
        widths = [d.textbbox((0,0), ch, font=f)[2]-d.textbbox((0,0), ch, font=f)[0] for ch in text]
        tw = sum(widths) + tracking*(len(text)-1)
        x = (W-tw)/2
        for ch,w in zip(text,widths):
            bb = d.textbbox((0,0), ch, font=f)
            d.text((x - bb[0], y), ch, font=f, fill=fill)
            x += w + tracking
        return tw
    bb = d.textbbox((0,0), text, font=f)
    d.text(((W-(bb[2]-bb[0]))/2 - bb[0], y), text, font=f, fill=fill)
    return bb[2]-bb[0]

# kicker
center("V E R N O N   ·   C O N N E C T I C U T   —   N O W   O P E N", sans(22), 44, GOLD, tracking=3)

# brand
center("MAN YAMAN", serif(124), 100, CREAM)
center("B A K E   S H O P", sans(34), 248, LAV, tracking=8)

# double rule under brand
d.rectangle([W/2-140, 320, W/2+140, 323], fill=GOLD)
d.rectangle([W/2-140, 329, W/2+140, 332], fill=GOLD)

# line
center("Pandesal at dawn.", serif(48), 352, CREAM)
center("Kakanin to remember.", serif(48), 412, GOLD)

# sapin-sapin stripe (gold / jade / plum) across the band edge
sx0, sx1 = 150, W-150
third = (sx1-sx0)/3.0
d.rectangle([sx0, 482, sx0+third, 494], fill=GOLD)
d.rectangle([sx0+third, 482, sx0+2*third, 494], fill=(122, 158, 122))
d.rectangle([sx0+2*third, 482, sx1, 494], fill=PLUM)

# menu + address strips (clear of the stripe: stripe ends y494, text starts y512)
center("Pandesal  ·  Ensaymada  ·  Sapin-Sapin  ·  Bibingka  ·  Ube Cake  ·  Empanadas", sans(24), 512, MIST)
center("101 West Street, Unit B  —  Vernon, CT 06066  —  (860) 281-4546", sans(22), 556, CREAM)
center("Traditional Filipino baked goods, cakes & kakanin", sans(20), 592, LAV)

img.save(OUT, "PNG", optimize=True)
print("wrote", OUT, os.path.getsize(OUT), "bytes")
