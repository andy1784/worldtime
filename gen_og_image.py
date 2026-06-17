#!/usr/bin/env python3
"""Generate OG image for worldtimessync.com using Pillow"""
from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1200, 630
img = Image.new('RGB', (W, H), '#0a0a2e')
draw = ImageDraw.Draw(img)

# Background gradient
for y in range(H):
    r = int(10 + (y / H) * 10)
    g = int(10 + (y / H) * 20)
    b = int(46 + (y / H) * 30)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# Stars
import random
random.seed(42)
for _ in range(80):
    x = random.randint(0, W)
    y = random.randint(0, H)
    size = random.choice([1, 1, 1, 2])
    alpha = random.randint(100, 255)
    draw.ellipse([x, y, x+size, y+size], fill=(alpha, alpha, alpha))

# Glow
for r in range(300, 0, -1):
    alpha = int(40 * (1 - r/300))
    draw.ellipse([W//2-r, H//2-r, W//2+r, H//2+r], fill=(96, 165, 250), outline=None)

# Globe
globe_cx, globe_cy = W//2, H//2
globe_r = 140
draw.ellipse([globe_cx-globe_r, globe_cy-globe_r, globe_cx+globe_r, globe_cy+globe_r], 
             fill=(30, 58, 95), outline=(96, 165, 250, 120), width=2)

# Globe grid lines
for i in range(-3, 4):
    y_off = int(i * globe_r / 4)
    draw.arc([globe_cx-globe_r, globe_cy-globe_r, globe_cx+globe_r, globe_cy+globe_r], 
             start=0, end=360, fill=(96, 165, 250, 30), width=1)

# City dots
cities = [
    (0.28, 0.35, "NY"),
    (0.48, 0.28, "LON"),
    (0.82, 0.38, "TKY"),
    (0.85, 0.72, "SYD"),
    (0.62, 0.42, "DXB"),
    (0.50, 0.30, "PAR"),
    (0.15, 0.38, "LA"),
    (0.75, 0.52, "SIN"),
]
for cx, cy, label in cities:
    x = int(cx * W)
    y = int(cy * H)
    # Glow
    for r in range(15, 0, -1):
        alpha = int(80 * (1 - r/15))
        draw.ellipse([x-r, y-r, x+r, y+r], fill=(96, 165, 250))
    # Dot
    draw.ellipse([x-4, y-4, x+4, y+4], fill=(96, 165, 250))
    draw.ellipse([x-2, y-2, x+2, y+2], fill=(255, 255, 255))

# Try to load fonts
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 56)
    font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    font_logo = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
    font_feat = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    font_url = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
except:
    font_title = ImageFont.load_default()
    font_sub = font_title
    font_logo = font_title
    font_feat = font_title
    font_url = font_title

# Logo
draw.text((W//2, 60), "WORLD TIME SYNC", fill=(96, 165, 250), font=font_logo, anchor="mt")

# Title
title = "What Time Is It Right Now?"
bbox = draw.textbbox((0, 0), title, font=font_title)
tw = bbox[2] - bbox[0]
draw.text(((W-tw)//2, 140), title, fill=(255, 255, 255), font=font_title)

# Subtitle
sub = "Real-time world clock for 700+ cities worldwide"
bbox = draw.textbbox((0, 0), sub, font=font_sub)
tw = bbox[2] - bbox[0]
draw.text(((W-tw)//2, 220), sub, fill=(200, 210, 230), font=font_sub)

# Features
features = ["🌍 700+ Cities", "⏰ Live Time Zones", "🔄 DST Aware", "📱 Mobile Friendly"]
feat_w = 220
start_x = (W - len(features) * feat_w) // 2 + feat_w // 2
for i, feat in enumerate(features):
    x = start_x + i * feat_w
    # Background box
    draw.rounded_rectangle([x-90, 290, x+90, 340], radius=12, 
                           fill=(255, 255, 255, 15), outline=(255, 255, 255, 30))
    bbox = draw.textbbox((0, 0), feat, font=font_feat)
    fw = bbox[2] - bbox[0]
    draw.text((x - fw//2, 300), feat, fill=(220, 230, 245), font=font_feat)

# URL
bbox = draw.textbbox((0, 0), "worldtimessync.com", font=font_url)
tw = bbox[2] - bbox[0]
draw.text(((W-tw)//2, H-50), "worldtimessync.com", fill=(150, 160, 180), font=font_url)

img.save('/home/kaliuser/worldtime/og-image.png', 'PNG', quality=95)
print("OG image saved: og-image.png")
