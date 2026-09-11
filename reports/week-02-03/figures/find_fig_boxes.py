import subprocess, re

pdftotext = r"C:\Users\trung\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdftotext.exe"
pdf_path = r"F:\DACN\week 3_9\SVStream.pdf"

for p in range(7, 13):
    res = subprocess.run([pdftotext, '-f', str(p), '-l', str(p), '-bbox', pdf_path, '-'], capture_output=True, text=True, encoding='utf-8', errors='ignore')
    lines = res.stdout.split('</line>')
    for l in lines:
        raw = re.sub(r'<[^>]+>', ' ', l).strip()
        m = re.match(r'Fig\.\s*(\d+)\.', raw)
        if m:
            coords = re.findall(r'(xMin|yMin|xMax|yMax)="([0-9.]+)"', l)
            cd = dict(coords)
            if 'yMin' in cd:
                yMin, yMax = float(cd['yMin']), float(cd['yMax'])
                xMin, xMax = float(cd['xMin']), float(cd['xMax'])
                print(f"Page {p:02d} | Fig {m.group(1):>2} | pt y=[{yMin:5.1f}, {yMax:5.1f}] | px(300dpi) y=[{yMin*300/72:4.0f}, {yMax*300/72:4.0f}] | {raw[:50]}")
