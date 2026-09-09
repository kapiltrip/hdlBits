"""Compare reader content/navigation with a named local Git baseline.

Usage: python verify_pdf_preservation.py bc5bc09
The only intended text edit in this presentation audit is the Day 9 FSM page
reference, 4 -> 5. All screenshot bytes, technical text and links must survive.
"""
import hashlib
import re
import subprocess
import sys

from index_study_pdfs import DOCS, ROOT
import fitz


def text(page):
    return re.sub(r'\s+', '', page.get_text(sort=True))


def images(doc):
    return sorted(hashlib.sha256(doc.xref_stream(x)).hexdigest()
                  for x in {im[0] for p in doc for im in p.get_images(full=True)})


def links(page):
    return sorted((l['kind'], l.get('page',-1), l.get('uri',''),
                   tuple(round(v,2) for v in l['from'])) for l in page.get_links())


def main():
    baseline=sys.argv[1]
    for meta in DOCS:
        name=meta['filename']
        raw=subprocess.run(['git','show',f'{baseline}:HDLBits Attempt 2/{name}'],
                           cwd=ROOT.parent,check=True,capture_output=True).stdout
        with fitz.open(stream=raw,filetype='pdf') as old, fitz.open(ROOT/name) as new:
            assert len(old)==len(new), name
            assert old.get_toc()==new.get_toc(), (name,'bookmarks')
            assert images(old)==images(new), (name,'source images')
            for i,(a,b) in enumerate(zip(old,new)):
                expected=text(a)
                if 'Day9_QA' in name and i==3:
                    expected=expected.replace('clockedFSMonpage4','clockedFSMonpage5')
                assert expected==text(b), (name,i+1,'text')
                assert a.rect==b.rect, (name,i+1,'page geometry')
                assert links(a)==links(b), (name,i+1,'navigation')
    print(f'PASS: {len(DOCS)} PDFs preserve text, images, page geometry and navigation against {baseline}; only the documented page-reference correction is permitted.')


if __name__=='__main__':
    main()
