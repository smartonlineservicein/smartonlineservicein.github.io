# -*- coding: utf-8 -*-
"""Watermark the resume template previews with "Smart Online Service".

One clean diagonal watermark across the middle of the page, plus a small
branded footer strip. Clean originals live in assets/samples/_original/ and are
never overwritten, so this script can be re-run any time the wording changes.

Run from the site folder:   python tools-watermark-templates.py
"""
import os, glob, shutil
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SAMPLES = os.path.join(HERE, "assets", "samples")
ORIG = os.path.join(SAMPLES, "_original")
TEXT = "Smart Online Service"
FOOTER = "SMART ONLINE SERVICE   ·   smartonlineservice.in"

os.makedirs(ORIG, exist_ok=True)


def font(size, bold=True):
    names = ["segoeuib.ttf", "arialbd.ttf"] if bold else ["segoeui.ttf", "arial.ttf"]
    for n in names:
        try:
            return ImageFont.truetype(os.path.join(r"C:\Windows\Fonts", n), size)
        except Exception:
            continue
    return ImageFont.load_default()


def watermark(path):
    name = os.path.basename(path)
    backup = os.path.join(ORIG, name)
    if not os.path.exists(backup):            # first run: stash the clean file
        shutil.copy2(path, backup)
    im = Image.open(backup).convert("RGB")
    w, h = im.size

    # --- one diagonal watermark across the centre -----------------------
    f = font(max(20, int(w / 11)))
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    bbox = d.textbbox((0, 0), TEXT, font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text(((w - tw) / 2 - bbox[0], (h - th) / 2 - bbox[1]), TEXT, font=f,
           fill=(15, 15, 15, 54))
    layer = layer.rotate(30, resample=Image.BICUBIC, center=(w / 2, h / 2))
    im = Image.alpha_composite(im.convert("RGBA"), layer).convert("RGB")

    # --- branded footer strip -------------------------------------------
    strip_h = max(18, int(h * 0.036))
    strip = Image.new("RGB", (w, strip_h), (13, 13, 13))
    sd = ImageDraw.Draw(strip)
    sf = font(max(9, int(strip_h * 0.46)))
    lb = sd.textbbox((0, 0), FOOTER, font=sf)
    sd.text(((w - (lb[2] - lb[0])) / 2 - lb[0], (strip_h - (lb[3] - lb[1])) / 2 - lb[1]),
            FOOTER, font=sf, fill=(244, 180, 0))
    im.paste(strip, (0, h - strip_h))

    if os.path.splitext(path)[1].lower() in (".jpg", ".jpeg"):
        im.save(path, "JPEG", quality=86, optimize=True)
    else:
        im.save(path, "PNG", optimize=True)


files = sorted(f for f in glob.glob(os.path.join(SAMPLES, "*"))
               if os.path.isfile(f) and f.lower().endswith((".jpg", ".jpeg", ".png")))
print("watermarking %d template previews..." % len(files))
for i, p in enumerate(files, 1):
    try:
        watermark(p)
    except Exception as e:
        print("  FAILED", os.path.basename(p), e)
print("done — clean originals kept in assets/samples/_original/")
