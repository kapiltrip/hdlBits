from pathlib import Path
import subprocess,concurrent.futures,json
import fitz
from PIL import Image,ImageOps,ImageDraw
ROOT=Path(__file__).resolve().parents[2]
WORK=ROOT/'internal/tmp/document_review_20260907'
RENDER=WORK/'renders';RENDER.mkdir(exist_ok=True)
def render(path):
    folder=RENDER/path.stem;folder.mkdir(exist_ok=True)
    subprocess.run(['pdftoppm','-r','75','-png',str(path),str(folder/'page')],check=True,capture_output=True)
    imgs=sorted(folder.glob('page-*.png'))
    contacts=[]
    for start in range(0,len(imgs),6):
        canvas=Image.new('RGB',(1260,1830),'#d9e1e9');draw=ImageDraw.Draw(canvas)
        for j,ip in enumerate(imgs[start:start+6]):
            im=Image.open(ip).convert('RGB');im.thumbnail((610,575))
            x=(j%2)*630+(630-im.width)//2;y=(j//2)*610+25
            canvas.paste(im,(x,y));draw.text(((j%2)*630+10,(j//2)*610+5),path.stem[:65]+' / '+ip.stem,fill='black')
        dest=folder/f'contact-{start//6+1}.jpg';canvas.save(dest,quality=90);contacts.append(str(dest))
    return contacts
paths=sorted(ROOT.glob('*.pdf'))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    contacts=[x for group in pool.map(render,paths) for x in group]
issues=[];counts={}
for path in paths:
    doc=fitz.open(path);counts[path.name]=len(doc)
    for n,pg in enumerate(doc,1):
        for b in pg.get_text('dict')['blocks']:
            if b['type']!=0:continue
            if not fitz.Rect(b['bbox']).intersects(pg.rect):issues.append((path.name,n,'outside page'))
        if len(pg.get_text().strip())<50:issues.append((path.name,n,'little text'))
    text='\n'.join(pg.get_text() for pg in doc)
    for phrase in ['Entry 123 remains unfinished','Day 1 Log','Q&A;','it is not treated as an instruction']:
        if phrase in text:issues.append((path.name,phrase))
(WORK/'layout_checks.json').write_text(json.dumps({'pages':counts,'issues':issues,'contact_sheets':contacts},indent=2),encoding='utf-8')
print(json.dumps({'pages':sum(counts.values()),'issues':issues,'contact_sheets':contacts},indent=2))
