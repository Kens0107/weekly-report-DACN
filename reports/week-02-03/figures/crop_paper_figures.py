import os
from PIL import Image

# Page size at 300 DPI is (2363, 3225)
# Let's define the bounding box coordinates (left, top, right, bottom) for each figure.
# In IEEE TKDE, page margins:
# Left margin: ~140 px, Right margin: ~2220 px
# Col 1: ~140 to 1140 px, Col 2: ~1220 to 2220 px
# Top margin: ~160 px, Bottom margin: ~3050 px

crops = {
    # Page 7: Fig 3 is at the bottom of the page or where? Let's check page 7.
    # Page 8:
    # Fig 4: Top of page 8, spanning both columns (~140 to 2220, top ~160 to ~590)
    # Fig 5: Col 1, below Fig 4 (~140 to 1140, top ~1650 to ~2150)
    # Fig 6: Col 1, below Fig 5 (~140 to 1140, top ~2200 to ~2600)
    # Figs 7, 8, 9, 10: Col 2 (and lower col 1/2)
}

# Let's inspect page 7, 8, 9, 10, 11, 12 by saving slices or checking non-white bounding boxes.
print("Script template ready")
