import subprocess, re
from PIL import Image

pdftotext = r"C:\Users\trung\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdftotext.exe"
pdf_path = r"F:\DACN\week 3_9\SVStream.pdf"

captions = {}
for p in range(7, 13):
    res = subprocess.run([pdftotext, '-f', str(p), '-l', str(p), '-bbox', pdf_path, '-'], capture_output=True, text=True, encoding='utf-8', errors='ignore')
    # find all words
    words = []
    for m in re.finditer(r'<word xMin="([0-9.]+)" yMin="([0-9.]+)" xMax="([0-9.]+)" yMax="([0-9.]+)">([^<]+)</word>', res.stdout):
        xMin, yMin, xMax, yMax, w = m.groups()
        words.append((float(xMin), float(yMin), float(xMax), float(yMax), w))
    
    # search for 'Fig.' followed by number
    for i, w in enumerate(words):
        if w[4] == 'Fig.' and i + 1 < len(words):
            num = words[i+1][4].rstrip('.')
            if num.isdigit():
                # collect caption line words
                cap_words = [w]
                j = i + 1
                while j < len(words) and abs(words[j][1] - w[1]) < 8:
                    cap_words.append(words[j])
                    j += 1
                xmin = min(cw[0] for cw in cap_words)
                ymin = min(cw[1] for cw in cap_words)
                xmax = max(cw[2] for cw in cap_words)
                ymax = max(cw[3] for cw in cap_words)
                txt = ' '.join(cw[4] for cw in cap_words)
                captions[int(num)] = (p, xmin, ymin, xmax, ymax, txt)

for num in sorted(captions.keys()):
    p, xmin, ymin, xmax, ymax, txt = captions[num]
    print(f"Fig {num:2d} on Page {p:2d}: pt y=[{ymin:5.1f}, {ymax:5.1f}], x=[{xmin:5.1f}, {xmax:5.1f}] -> {txt[:50]}")
