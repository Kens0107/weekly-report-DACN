import os
from PIL import Image

fig_dir = r"f:\latex\weekly-report-DACN\reports\week-02-03\figures"
S = 300.0 / 72.0

def crop_pt(page_num, box_pt, out_name):
    img = Image.open(os.path.join(fig_dir, f"page_300-{page_num:02d}.png"))
    box_px = (
        int(round(box_pt[0] * S)),
        int(round(box_pt[1] * S)),
        int(round(box_pt[2] * S)),
        int(round(box_pt[3] * S))
    )
    cropped = img.crop(box_px)
    out_path = os.path.join(fig_dir, out_name)
    cropped.save(out_path)
    print(f"Cropped {out_name}: size={cropped.size}")

# 1. Fig 3: Page 7, col 1
crop_pt(7, (24, 45, 250, 160), "paper_fig03.png")

# 2. Fig 4: Page 8, full width
crop_pt(8, (24, 45, 542, 156), "paper_fig04.png")

# 3. Fig 5 & 6: Page 8, col 1
crop_pt(8, (24, 440, 282, 650), "paper_fig05_06.png")

# 4. Fig 7, 8, 9, 10: Smileface steps
p8 = Image.open(os.path.join(fig_dir, "page_300-08.png"))
def get_box(b):
    return p8.crop((int(b[0]*S), int(b[1]*S), int(b[2]*S), int(b[3]*S)))

f7 = get_box((24, 665, 282, 755))
f8 = get_box((285, 470, 542, 570))
f9 = get_box((285, 570, 542, 660))
f10 = get_box((285, 660, 542, 755))

w_col = max(f7.width, f8.width, f9.width, f10.width)
h_row = max(f7.height, f8.height, f9.height, f10.height)
stitched_7_10 = Image.new("RGB", (w_col * 2 + 20, h_row * 2 + 20), (255, 255, 255))
stitched_7_10.paste(f7, (0, 0))
stitched_7_10.paste(f8, (w_col + 20, 0))
stitched_7_10.paste(f9, (0, h_row + 20))
stitched_7_10.paste(f10, (w_col + 20, h_row + 20))
stitched_7_10.save(os.path.join(fig_dir, "paper_fig07_10.png"))
print(f"Cropped paper_fig07_10.png: size={stitched_7_10.size}")

# 5. Fig 11 & 12: Page 9, col 1 (trimmed trailing text)
crop_pt(9, (24, 45, 282, 372), "paper_fig11_12.png")

# 6. Fig 13: Page 9, col 2 (trimmed Table 1)
crop_pt(9, (285, 45, 542, 215), "paper_fig13.png")

# 7. Fig 14: Page 10, col 1 ONLY
crop_pt(10, (24, 45, 282, 260), "paper_fig14.png")

# 8. Fig 15: Page 10, col 2 ONLY
crop_pt(10, (285, 45, 542, 260), "paper_fig15.png")

# 9. Fig 16: Page 11, col 1
crop_pt(11, (24, 45, 282, 160), "paper_fig16.png")

# 10. Fig 17: Page 11, col 2
crop_pt(11, (285, 45, 542, 235), "paper_fig17.png")

# 11. Fig 18: Page 12, full width
crop_pt(12, (24, 45, 542, 175), "paper_fig18.png")

print("Refined crops saved!")
