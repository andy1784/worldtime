#!/usr/bin/env python3
"""Generate earth-clock OG image"""
from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1200, 630
img = Image.new('RGB', (W, H), '#050520')
draw = ImageDraw.Draw(img)

# Background gradient
for y in range(H):
    r = int(5 + (y / H) * 8)
    g = int(5 + (y / H) * 15)
    b = int(32 + (y / H) * 25)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# Stars
import random
random.seed(99)
for _ in range(100):
    x = random.randint(0, W)
    y = random.randint(0, H)
    size = random.choice([1, 1, 1, 2])
    alpha = random.randint(80, 255)
    draw.ellipse([x, y, x+size, y+size], fill=(alpha, alpha, alpha))

# Large globe
globe_cx, globe_cy = W//2, H//2 + 20
globe_r = 180

# Globe glow
for r in range(220, 0, -1):
    alpha = int(50 * (1 - r/220))
    draw.ellipse([globe_cx-r, globe_cy-r, globe_cx+r, globe_cy+r], fill=(96, 165, 250))

# Globe body
draw.ellipse([globe_cx-globe_r, globe_cy-globe_r, globe_cx+globe_r, globe_cy+globe_r], 
             fill=(20, 50, 90), outline=(96, 165, 250, 150), width=3)

# Continents (simplified)
# North America
draw.ellipse([globe_cx-80, globe_cy-100, globe_cx-20, globe_cy-30], fill=(40, 80, 50))
# South America
draw.ellipse([globe_cx-60, globe_cy+10, globe_cx-10, globe_cy+80], fill=(40, 80, 50))
# Europe/Africa
draw.ellipse([globe_cx+10, globe_cy-80, globe_cx+60, globe_cy+60], fill=(40, 80, 50))
# Asia
draw.ellipse([globe_cx+50, globe_cy-100, globe_cx+130, globe_cy-10], fill=(40, 80, 50))
# Australia
draw.ellipse([globe_cx+100, globe_cy+40, globe_cx+140, globe_cy+80], fill=(40, 80, 50))

# Day/night terminator
for x in range(globe_cx-globe_r, globe_cx+globe_r):
    for y in range(globe_cy-globe_r, globe_cy+globe_r):
        dx = x - globe_cx
        dy = y - globe_cy
        if dx*dx + dy*dy <= globe_r*globe_r:
            # Simple day/night based on x position
            if dx > 20:
                # Night side - darker
                r, g, b = img.getpixel((x, y))
                img.putpixel((x, y), (r//2, g//2, b//2))

# City dots with glow
cities = [
    (0.25, 0.32, "New York"),
    (0.48, 0.25, "London"),
    (0.82, 0.35, "Tokyo"),
    (0.85, 0.70, "Sydney"),
    (0.60, 0.40, "Dubai"),
    (0.50, 0.28, "Paris"),
    (0.12, 0.35, "LA"),
    (0.75, 0.50, "Singapore"),
]
for cx, cy, label in cities:
    x = int(cx * W)
    y = int(cy * H)
    for r in range(18, 0, -1):
        alpha = int(100 * (1 - r/18))
        draw.ellipse([x-r, y-r, x+r, y+r], fill=(96, 165, 250))
    draw.ellipse([x-5, y-5, x+5, y+5], fill=(96, 165, 250))
    draw.ellipse([x-2, y-2, x+2, y+2], fill=(255, 255, 255))

# Fonts
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 52)
    font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 26)
    font_logo = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
    font_url = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
except:
    font_title = ImageFont.load_default()
    font_sub = font_title
    font_logo = font_title
    font_url = font_title

# Logo
draw.text((W//2, 50), "WORLD TIME SYNC", fill=(96, 165, 250), font=font_logo, anchor="mt")

# Title
title = "Watch the World Tick"
bbox = draw.textbbox((0, 0), title, font=font_title)
tw = bbox[2] - bbox[0]
draw.text(((W-tw)//2, 120), title, fill=(255, 255, 255), font=font_title)

# Subtitle
sub = "Real-time earth clock — day and night sweep across the globe"
bbox = draw.textbbox((0, 0), sub, font=font_sub)
tw = bbox[2] - bbox[0]
draw.text(((W-tw)//2, 195), sub, fill=(200, 210, 230), font=font_sub)

# URL
bbox = draw.textbbox((0, 0), "worldtimessync.com/earth-clock.html", font=font_url)
tw = bbox[2] - bbox[0]
draw.text(((W-tw)//2, H-45), "worldtimessync.com/earth-clock.html", fill=(150, 160, 180), font=font_url)

img.save('/home/kaliuser/worldtime/og-earth.png', 'PNG', quality=95)
print("Earth clock OG image saved: og-earth.png")
