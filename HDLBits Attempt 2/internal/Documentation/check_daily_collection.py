"""Audit every saved daily page, source-page mapping and navigation target."""
import hashlib
import json
import re
from collections import Counter
from urllib.parse import unquote, urlparse
from index_study_pdfs import ROOT, DOCS, fitz, tracker_rows
from build_daily_collection import MANIFEST, QUESTIONS, INDEX_URL
from build_day12_lfsr_series import verify_models, next_lfsr5, next_lfsr32, next_mt2015


def tokens(s):
    # PyMuPDF's embedded Arial encoding extracts visible inserted hyphens as
    # soft hyphens; normalize only this equivalent punctuation representation.
    return Counter(re.findall(r'\w+|[^\w\s]',s.replace('\xad','-')))


def text(page, day):
    result=[]
    for block in page.get_text('dict')['blocks']:
        if block['type']!=0:
            continue
        for line in block['lines']:
            for span in line['spans']:
                if span['bbox'][1]>=page.rect.height-40:
                    continue
                s=span['text']
                if span['bbox'][1]<45:
                    if 'TECHNICAL PAGE' in s:
                        continue
                    if day==10:
                        s=re.sub(r'DAY 1[12]','DAY 10',s)
                result.append(s)
    return ' '.join(result)


def images(doc,page):
    return Counter(hashlib.sha256(doc.extract_image(x[0])['image']).hexdigest()
                   for x in page.get_images(full=True))


def main():
    manifest=json.loads(MANIFEST.read_text(encoding='utf-8'))
    seen=set(); total=links=bookmarks=0
    sources={n+1:fitz.open(ROOT/m['filename']) for n,m in enumerate(DOCS)}
    sources[0]=fitz.open(ROOT/'internal/tmp/daily_collection/lfsr_reference.pdf')
    for d in manifest['days']:
        doc=fitz.open(ROOT/d['file'])
        assert len(doc)==d['pages']
        total+=len(doc); bookmarks+=len(doc.get_toc())
        for item in d['provenance']:
            key=(item['note'],item['source_page']); assert key not in seen; seen.add(key)
            old=sources[key[0]][key[1]-1]; new=doc[item['page']-1]
            assert old.rect==new.rect
            expected=tokens(text(old,d['day']))
            for change in item['references']:
                expected.subtract(tokens(change['old']))
                expected.update(tokens(change['new']))
            actual=tokens(text(new,d['day']))
            assert +expected==actual, (d['day'],item['page'],expected-actual,actual-expected)
            assert images(sources[key[0]],old)==images(doc,new),(d['day'],item['page'],'image bytes')
        for front in d['front_links']:
            matches=[l for l in doc[front['page']-1].get_links()
                     if l['kind']==fitz.LINK_GOTO and l['page']==front['target']-1
                     and max(abs(a-b) for a,b in zip(l['from'],front['rect']))<.1]
            assert len(matches)==1,(d['day'],front)
        outline=doc.get_toc()
        for p in d['parts']:
            offset=p['first']-(1 if not p['note'] else 2)
            for i,q in enumerate(QUESTIONS[p['note']][offset:offset+p['last']-p['first']+1]):
                assert [2,q,p['start']+i] in outline
        for pg in doc:
            foot=[l for l in pg.get_links() if l['from'].y0>=pg.rect.height-40]
            assert len(foot)==2
            assert any(l['kind']==fitz.LINK_GOTO and l['page']==0 for l in foot)
            assert any(l['kind']==fitz.LINK_URI and l['uri']==INDEX_URL for l in foot)
            assert f'{pg.number+1} / {len(doc)}' in pg.get_text()
            for l in pg.get_links():
                links+=1
                if l['kind']==fitz.LINK_GOTO:
                    assert 0<=l['page']<len(doc)
            for b in pg.get_text('blocks'):
                if b[6]==0:
                    assert b[0]>=-.5 and b[1]>=-.5 and b[2]<=pg.rect.width+.5 and b[3]<=pg.rect.height+.5,(d['day'],pg.number+1,b)
        for xref in {f[0] for pg in doc for f in pg.get_fonts(full=True)}:
            assert doc.extract_font(xref)[3], (d['day'],'unembedded font',xref)
        doc.close()
    assert len(seen)==151 and sum(k[0]!=0 for k in seen)==148
    assert len(manifest['days'])==10 and total==manifest['total_pages']
    # Index local destinations and every exact-page fragment resolve.
    index=(ROOT/'DOCUMENT_INDEX.md').read_text(encoding='utf-8')
    checked=0
    for target in re.findall(r'\]\(([^)]+)\)',index):
        if target.startswith(('http:','https:','#')):
            continue
        name,_,fragment=unquote(target).partition('#')
        path=ROOT/name
        assert path.exists(), target
        if fragment.startswith('page='):
            with fitz.open(path) as doc:
                assert 1<=int(fragment[5:])<=len(doc)
        checked+=1
    rows=tracker_rows()
    assert {str(n) for n,r in rows.items() if str(r['discussion']).startswith('=HYPERLINK(')}==set(manifest['entries'])
    # Current-pass completion is preserved, not re-inferred by this layout job.
    assert len(rows)==178 and all(r['status']=='Done' for r in rows.values())
    verify_models()
    for q in range(32):
        assert next_lfsr5(q)==((q>>1)^(0x14 if q&1 else 0))
        for r in range(32):
            assert next_lfsr5(q^r)==(next_lfsr5(q)^next_lfsr5(r))
    q=1; rotate=[]
    while q not in rotate:
        rotate.append(q); q=(q>>1)^(0x10 if q&1 else 0)
    assert rotate==[1,16,8,4,2] and q==1
    assert next_lfsr32(1)==0x80200003 and next_mt2015(1)==2
    assert 'LFSR' in sources[0][0].get_text()
    for src in sources.values():
        src.close()
    print(f'PASS: 10 PDFs, {total} pages, 148/148 source pages + 3 reference pages; {bookmarks} bookmarks, {links} links; {checked} index links.')
    print('PASS: source text (reviewed reference changes only), image bytes, geometry, embedded fonts, 58 entry mappings and LFSR checks.')


if __name__=='__main__':
    main()
