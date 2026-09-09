"""Apply a restrained navy/neutral palette without rasterizing PDF content.

Only explicitly inventoried authored vector colors and full-bleed top rules
are changed. Source images, code, text positions, fonts and links are intact.
"""
import hashlib
from pathlib import Path
import re

import fitz
from pypdf.generic import ContentStream, DecodedStreamObject, FloatObject

PALETTE = {
    '087F8C':'002060', '08808C':'002060',
    'F7F5F0':'FFFFFF',
    'FFF59A':'F3F4F6', 'FFFF99':'F3F4F6', 'FFF2CC':'F3F4F6',
    'FFF7CC':'F3F4F6', 'FFFBE5':'F3F4F6', 'FCE4D6':'F3F4F6',
    'EAF3F5':'F3F5F7', 'D8C775':'CBD0D8', 'D79B00':'677384',
    'CCFFCC':'EAF4ED', '198C3A':'2C6B3C',
}


def signature(doc):
    pages=[]
    for page in doc:
        links=sorted((l['kind'],l.get('page',-1),l.get('uri',''),
                      tuple(round(v,2) for v in l['from'])) for l in page.get_links())
        pages.append((re.sub(r'\s+','',page.get_text()),links,tuple(page.rect)))
    image_hashes={xref:hashlib.sha256(doc.xref_stream(xref)).hexdigest()
                  for xref in {im[0] for p in doc for im in p.get_images(full=True)}}
    return pages,doc.get_toc(),image_hashes


def normalize_pdf_palette(path):
    path=Path(path)
    doc=fitz.open(path)
    before=signature(doc)
    streams={xref for page in doc for xref in page.get_contents()}
    streams.update(item[0] for page in doc for item in page.get_xobjects())
    # This caption explicitly names the state colors. Keep the pale-yellow
    # FLAG_PULSE node and its amber outline; color is part of this diagram.
    semantic_streams={xref for page in doc
                      if 'Green and yellow states' in page.get_text()
                      for xref in page.get_contents()}
    changes=0
    for xref in streams:
        raw=doc.xref_stream(xref)
        stream=DecodedStreamObject()
        stream.set_data(raw)
        content=ContentStream(stream,None)
        touched=False
        for index,(operands,op) in enumerate(content.operations):
            if op in (b'rg',b'RG') and len(operands)==3:
                color=''.join(f'{round(float(v)*255):02X}' for v in operands)
                following=content.operations[index+1:index+3]
                semantic_node=(xref in semantic_streams and op==b'rg'
                    and color in ('FFFBE5','F3F4F6') and len(following)==2
                    and following[0][1]==b'RG' and following[1][1]==b'm'
                    and ''.join(f'{round(float(v)*255):02X}'
                                for v in following[0][0])=='A15C00')
                if semantic_node:
                    if color!='FFFBE5':
                        operands[:]=[FloatObject(v/255) for v in (255,251,229)]
                        touched=True
                        changes+=1
                    continue
                if color in PALETTE:
                    new=PALETTE[color]
                    operands[:]=[FloatObject(int(new[i:i+2],16)/255) for i in (0,2,4)]
                    touched=True
                    changes+=1
            elif op==b're' and len(operands)==4:
                x,y,w,h=map(float,operands)
                # Existing A4 full-bleed decorative rules; no technical figure.
                if abs(x)<0.01 and 590<w<600 and 5<h<=12 and 830<y+h<845:
                    operands[1]=FloatObject(y+h-2)
                    operands[3]=FloatObject(2)
                    touched=True
                    changes+=1
        if touched:
            doc.update_stream(xref,content.get_data())
    if not changes:
        doc.close()
        return 0
    temp=path.with_suffix('.palette.tmp.pdf')
    doc.save(temp,garbage=0,deflate=True)
    doc.close()
    with fitz.open(temp) as final:
        assert signature(final)==before, f'Content/navigation changed: {path.name}'
    temp.replace(path)
    return changes


if __name__=='__main__':
    from index_study_pdfs import DOCS,ROOT
    for meta in DOCS:
        print(meta['filename'],normalize_pdf_palette(ROOT/meta['filename']))
