"""Render every collection page with Poppler and make numbered review sheets."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json
import shutil
import subprocess

from index_study_pdfs import DOCS,ROOT
from PIL import Image,ImageDraw,ImageFont

OUT=ROOT/'internal/tmp/collection_review_20260909'
OUT.mkdir(parents=True,exist_ok=True)

def render(item):
    i,meta=item
    folder=OUT/f'note{i:02d}'
    folder.mkdir(exist_ok=True)
    subprocess.run([shutil.which('pdftoppm'),'-r','100','-png',str(ROOT/meta['filename']),str(folder/'page')],check=True,capture_output=True)
    return [(i,int(f.stem.split('-')[-1]),f) for f in sorted(folder.glob('page-*.png'),key=lambda f:int(f.stem.split('-')[-1]))]

with ThreadPoolExecutor(max_workers=4) as pool:
    pages=[p for group in pool.map(render,enumerate(DOCS,1)) for p in group]
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',17)
manifest=[]
for batch in range(0,len(pages),4):
    items=pages[batch:batch+4]
    tile_w=830
    tile_h=1205
    canvas=Image.new('RGB',(tile_w*2,tile_h*2),'#D8DDE3')
    draw=ImageDraw.Draw(canvas)
    labels=[]
    for j,(note,page,path) in enumerate(items):
        img=Image.open(path).convert('RGB')
        x=(j%2)*tile_w
        y=(j//2)*tile_h
        draw.text((x+10,y+4),f'Note {note:02d} - page {page}',fill='#172333',font=font)
        canvas.paste(img,(x,y+27))
        labels.append({'note':note,'page':page,'path':str(path)})
    target=OUT/f'review{batch//4+1:02d}.png'
    canvas.save(target)
    manifest.append({'sheet':str(target),'pages':labels})
(OUT/'manifest.json').write_text(json.dumps(manifest,indent=2))
assert len(pages)==164
print(f'Rendered {len(pages)} pages into {len(manifest)} review sheets: {OUT}')
