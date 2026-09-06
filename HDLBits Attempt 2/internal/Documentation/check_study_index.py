"""Check the reader-facing PDF navigation, tracker map and Markdown links."""
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

import fitz
from index_study_pdfs import DOCS, ROOT, INDEX_URL, MARKER, tracker_rows, shift_range


def anchors(text):
    result = set(re.findall(r'<a id="([^"]+)"', text))
    seen = {}
    for heading in re.findall(r'^#{1,6} (.+)$', text, re.M):
        base = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
        count = seen.get(base, 0)
        result.add(base if not count else f'{base}-{count}')
        seen[base] = count+1
    return result


def main():
    rows = tracker_rows()
    mapped, pages, bookmarks, internal_links = set(), 0, 0, 0
    index = (ROOT/'DOCUMENT_INDEX.md').read_text()
    for meta in DOCS:
        path = ROOT/meta['filename']
        with fitz.open(path) as doc:
            assert len(doc) == len(meta['pages'])+1, path.name
            assert MARKER in doc.metadata['keywords'], path.name
            assert doc.metadata['author'] == 'Kapil Tripathi', path.name
            for xref in {font[0] for page in doc for font in page.get_fonts()}:
                assert doc.extract_font(xref)[3], (path.name,'font is not embedded',xref)
            toc = doc.get_toc()
            assert len(toc) == len(meta['pages'])+len(meta['entries'])+3, path.name
            assert all(1 <= item[2] <= len(doc) for item in toc), path.name
            shift = int(meta['prepend'])
            destinations = [l['page'] for l in doc[0].get_links() if l['kind'] == fitz.LINK_GOTO and l['page'] != 0]
            assert destinations == [g[0]+shift-1 for g in meta['groups']], (path.name,destinations)
            for i, pg in enumerate(doc):
                text = pg.get_text()
                assert f'{i+1} / {len(doc)}' in text, (path.name,i+1,'page counter')
                assert len(text.strip()) > 100, (path.name,i+1,'empty page')
                links = pg.get_links()
                assert any(l.get('uri') == INDEX_URL for l in links), (path.name,i+1,'all-notes link')
                assert any(l['kind']==fitz.LINK_GOTO and l['page']==0 for l in links), (path.name,i+1,'contents link')
                for link in links:
                    if link['kind'] == fitz.LINK_GOTO:
                        assert 0 <= link['page'] < len(doc), (path.name,link)
                        internal_links += 1
                for b in pg.get_text('dict')['blocks']:
                    if b['type'] != 0:
                        continue
                    for line in b['lines']:
                        for span in line['spans']:
                            box = fitz.Rect(span['bbox'])
                            assert pg.rect.contains(box), (path.name,i+1,'text outside page',span['text'])
            for n, location in meta['entries'].items():
                assert n not in mapped, n
                mapped.add(n)
                target = int(re.search(r'\d+',location)[0])+shift
                expected = f"[Note {DOCS.index(meta)+1:02d}, pp. {shift_range(location,shift)}]({path.name}#page={target})"
                assert expected in index, (n,expected)
                formula = rows[n]['discussion']
                target_file = re.match(r'=HYPERLINK\("([^"]+)"',formula)[1]
                assert target_file.replace('.md','.pdf') == path.name, n
                assert (ROOT/target_file).exists(), target_file
            pages += len(doc)
            bookmarks += len(toc)
    assert mapped == {n for n,r in rows.items() if str(r['discussion']).startswith('=HYPERLINK(')}
    # The only tracker labels with explicit page ranges must match their PDFs.
    assert '(pp. 5-6)' in rows[155]['discussion']
    assert '(pp. 2-4)' in rows[158]['discussion']
    markdown = list(ROOT.glob('*.md')) + [ROOT/'internal/Documentation/README.md', ROOT.parent/'LinkedIn_Attempt_2_Posting_Plan_and_Ideas.md']
    checked = 0
    for file in markdown:
        text = file.read_text()
        in_code = False
        widths = []
        for line in text.splitlines():
            if line.startswith('```'):
                in_code = not in_code
            if in_code:
                continue
            if line.startswith('|'):
                widths.append(len(re.split(r'(?<!\\)\|',line)))
                assert len(set(widths)) == 1, (file.name,'unequal table columns',line)
            else:
                widths = []
        for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',text):
            url = urlsplit(target)
            if url.scheme or url.netloc:
                continue
            dest = (file.parent/unquote(url.path)).resolve() if url.path else file
            assert dest.exists(), (file.name,target)
            if url.fragment and dest.suffix == '.md':
                assert unquote(url.fragment) in anchors(dest.read_text()), (file.name,target,'missing anchor')
            if url.fragment.startswith('page=') and dest.suffix == '.pdf':
                with fitz.open(dest) as pdf:
                    assert 1 <= int(url.fragment[5:]) <= len(pdf), (file.name,target)
            checked += 1
    print(f'PASS: {len(DOCS)} PDFs, {pages} pages, {bookmarks} bookmarks, {internal_links} internal PDF links, {len(mapped)} tracker mappings, {checked} local Markdown links.')


if __name__ == '__main__':
    main()
