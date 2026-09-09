"""Read-only palette inventory for reader-authored vector/text PDF content."""
from collections import Counter
from index_study_pdfs import DOCS, ROOT, fitz

for number, meta in enumerate(DOCS,1):
    doc=fitz.open(ROOT/meta['filename'])
    text_colors=Counter()
    fills=Counter()
    for page in doc:
        for block in page.get_text('dict')['blocks']:
            if block['type']==0:
                for line in block['lines']:
                    for span in line['spans']:
                        text_colors[f'#{span["color"]:06X}']+=len(span['text'])
        for drawing in page.get_drawings():
            rgb=drawing.get('fill')
            if rgb and len(rgb)==3:
                fills['#'+''.join(f'{round(v*255):02X}' for v in rgb)]+=1
    print(number, meta['filename'], 'TEXT',text_colors.most_common(12),'FILLS',fills.most_common(12))
