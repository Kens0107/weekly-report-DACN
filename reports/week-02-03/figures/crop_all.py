import os
from PIL import Image

# Page size at 300 DPI is 2363 x 3225.
# Margin left: ~135, right: ~2228.
# Column 1: ~135 to 1145, Column 2: ~1218 to 2228.
# Let's define the bounding box crops for each figure:

fig_dir = r"f:\latex\weekly-report-DACN\reports\week-02-03\figures"

def crop_and_save(page_num, box, out_name):
    page_path = os.path.join(fig_dir, f"page_300-{page_num:02d}.png")
    img = Image.open(page_path)
    cropped = img.crop(box)
    out_path = os.path.join(fig_dir, out_name)
    cropped.save(out_path)
    print(f"Saved {out_name}: size {cropped.size}")

# Page 7: Fig 3 (synthetic streams)
# In page 7: Fig 3 is in col 1 and 2 at the top
# (a) Ring-Ball and (b) Smileface-Twomoons
crop_and_save(7, (135, 230, 2228, 760), "paper_fig03.png")

# Page 8:
# Fig 4: Top across full width: (a) through (e)
crop_and_save(8, (135, 210, 2228, 670), "paper_fig04.png")

# Fig 5 & 6: Col 1 below Fig 4
# Fig 5: Rand index on Ring-Ball
# Fig 6: The two erroneously clustered chunks
crop_and_save(8, (135, 1720, 1150, 2690), "paper_fig05_06.png")

# Fig 7, 8, 9, 10: Smileface steps 10, 12, 51, 70
# Let's crop Fig 7, 8, 9, 10 together or as a combined panel
# Fig 8, 9, 10 are in col 2, Fig 7 is at the bottom of col 1
# Let's create paper_fig07_10.png by combining Fig 7 and Figs 8-10, or cropping them
# On page 8:
# Fig 7: (135, 2690, 1150, 3030)
# Fig 8: (1218, 1730, 2228, 2150)
# Fig 9: (1218, 2160, 2228, 2590)
# Fig 10: (1218, 2600, 2228, 3030)
p8 = Image.open(os.path.join(fig_dir, "page_300-08.png"))
f7 = p8.crop((135, 2700, 1150, 3020))
f8 = p8.crop((1218, 1750, 2228, 2160))
f9 = p8.crop((1218, 2170, 2228, 2580))
f10 = p8.crop((1218, 2590, 2228, 3020))

# Let's stitch them into a 2x2 grid to match user's fig7_10_smileface_steps.png
w_panel = max(f7.width, f8.width, f9.width, f10.width)
h_panel = max(f7.height, f8.height, f9.height, f10.height)
stitched = Image.new("RGB", (w_panel * 2 + 30, h_panel * 2 + 30), (255, 255, 255))
stitched.paste(f7, (0, 0))
stitched.paste(f8, (w_panel + 30, 0))
stitched.paste(f9, (0, h_panel + 30))
stitched.paste(f10, (w_panel + 30, h_panel + 30))
stitched.save(os.path.join(fig_dir, "paper_fig07_10.png"))
print(f"Saved paper_fig07_10.png: size {stitched.size}")

# Page 9:
# Fig 11 & 12: Col 1
# Fig 11: (135, 210, 1150, 770)
# Fig 12: (135, 780, 1150, 1370)
crop_and_save(9, (135, 210, 1150, 1370), "paper_fig11_12.png")

# Fig 13: Col 2 top
# (1218, 210, 2228, 930)
crop_and_save(9, (1218, 210, 2228, 930), "paper_fig13.png")

# Page 10:
# Fig 14: Full width top (a)-(d)
crop_and_save(10, (135, 210, 2228, 1070), "paper_fig14.png")

# Fig 15: Full width middle/lower (a)-(d)
crop_and_save(10, (1218, 1080, 2228, 2180), "paper_fig15.png") # wait, let's verify if Fig 15 is col 2 or full width

# Page 11:
# Fig 16: Col 1 (135, 210, 1150, 830)
crop_and_save(11, (135, 210, 1150, 830), "paper_fig16.png")

# Fig 17: Col 2 (1218, 210, 2228, 1130)
crop_and_save(11, (1218, 210, 2228, 1130), "paper_fig17.png")

# Page 12:
# Fig 18: Full width top (a)-(c)
crop_and_save(12, (135, 210, 2228, 770), "paper_fig18.png")

print("All crops saved successfully!")
