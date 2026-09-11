import subprocess
import re

pdftotext = r"C:\Users\trung\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdftotext.exe"
pdf_path = r"F:\DACN\week 3_9\SVStream.pdf"

for p in range(7, 13):
    res = subprocess.run([pdftotext, '-f', str(p), '-l', str(p), '-bbox', pdf_path, '-'], capture_output=True, text=True, encoding='utf-8', errors='ignore')
    for line in res.stdout.splitlines():
        if 'Fig.' in line:
            # extract all words and xMin, yMin, xMax, yMax
            m = re.search(r'xMin="([0-9.]+)" yMin="([0-9.]+)" xMax="([0-9.]+)" yMax="([0-9.]+)"', line)
            # check if the text in line contains 'Fig. <number>'
            txt = re.sub(r'<[^>]+>', ' ', line)
            txt = ' '.join(txt.split())
            if re.search(r'Fig\.\s+\d+', txt):
                xMin, yMin, xMax, yMax = map(float, m.groups())
                print(f"Page {p:02d} | pt: [{xMin:5.1f}, {yMin:5.1f}, {xMax:5.1f}, {yMax:5.1f}] | px(300dpi): [{xMin*300/72:6.1f}, {yMin*300/72:6.1f}, {xMax*300/72:6.1f}, {yMax*300/72:6.1f}] | {txt[:65]}")
