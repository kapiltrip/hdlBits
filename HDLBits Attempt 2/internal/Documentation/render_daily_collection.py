"""Render the actual daily PDFs and assemble complete, uncropped QA sheets."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json
import shutil
import subprocess
from index_study_pdfs import ROOT
from PIL import Image, ImageDraw, ImageFont

manifest=json.loads((ROOT/'internal/Documentation/daily_collection_manifest.json').read_text())
out=ROOT/'internal/tmp/daily_collection/rendered'
out.mkdir(parents=True,exist_ok=True)

def render(d):
    folder=out/f"day{d['day']:02d}"; folder.mkdir(exist_ok=True)
    subprocess.run([shutil.which('pdftoppm'),'-r','100','-png',str(ROOT/d['file']),str(folder/'page')],check=True,capture_output=True)
    files=sorted(folder.glob('page-*.png'),key=lambda p:int(p.stem.split('-')[-1]))
    assert len(files)==d['pages']
    return [(d['day'],i+1,p) for i,p in enumerate(files)]

with ThreadPoolExecutor(max_workers=4) as pool:
    pages=[p for part in pool.map(render,manifest['days']) for p in part]
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',18)
review=[]
for start in range(0,len(pages),4):
    batch=pages[start:start+4]
    canvas=Image.new('RGB',(1740,2460),'#DDE1E6'); draw=ImageDraw.Draw(canvas)
    for j,(day,page,path) in enumerate(batch):
        im=Image.open(path).convert('RGB')
        assert im.width<=860 and im.height<=1195,(path,im.size)
        x=(j%2)*870; y=(j//2)*1230
        draw.text((x+10,y+4),f'Day {day:02d} - page {page}',font=font,fill='#172333')
        canvas.paste(im,(x+(870-im.width)//2,y+29))
    target=out/f'review{start//4+1:02d}.png'
    canvas.save(target)
    review.append(dict(sheet=str(target),pages=[dict(day=d,page=p,path=str(f)) for d,p,f in batch]))
(out/'review_manifest.json').write_text(json.dumps(review,indent=2))
print(f'{len(pages)} rendered pages, {len(review)} complete review sheets: {out}')
