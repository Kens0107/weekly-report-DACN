"""Re-crop the SVStream paper figures from the 300 dpi page renders, in pixels.

Boxes are (left, top, right, bottom) on page_300-XX.png (2363 x 3225 px). They
replace the point-based boxes of crop_exact.py for the five figures whose crops
had cut panels or stray text (7-10, 11-12, 13, 14, 15).
"""
import os
from PIL import Image

FIG_DIR = os.path.dirname(os.path.abspath(__file__))


def page(n):
    return Image.open(os.path.join(FIG_DIR, f"page_300-{n:02d}.png")).convert("RGB")


def save(img, name):
    img.save(os.path.join(FIG_DIR, name))
    print(f"{name}: {img.size}")


p8 = page(8)
fig7 = p8.crop((95, 2742, 1175, 3118))
fig8 = p8.crop((1180, 1970, 2262, 2350))
fig9 = p8.crop((1180, 2355, 2262, 2733))
fig10 = p8.crop((1180, 2738, 2262, 3120))
width = max(im.width for im in (fig7, fig8, fig9, fig10))
height = max(im.height for im in (fig7, fig8, fig9, fig10))
sheet = Image.new("RGB", (2 * width + 30, 2 * height + 30), (255, 255, 255))
sheet.paste(fig7, (0, 0))
sheet.paste(fig8, (width + 30, 0))
sheet.paste(fig9, (0, height + 30))
sheet.paste(fig10, (width + 30, height + 30))
save(sheet, "paper_fig07_10.png")

p9 = page(9)
save(p9.crop((95, 195, 1175, 1405)), "paper_fig11_12.png")
save(p9.crop((1180, 195, 2262, 828)), "paper_fig13.png")

p10 = page(10)
save(p10.crop((95, 195, 1175, 1128)), "paper_fig14.png")
save(p10.crop((1180, 195, 2262, 1005)), "paper_fig15.png")

# Figures 5-6 (the point-based crop cut the last line of Figure 6's caption).
save(p8.crop((95, 1850, 1175, 2728)), "paper_fig05_06.png")
