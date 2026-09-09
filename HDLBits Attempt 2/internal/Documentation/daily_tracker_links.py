"""Prepare exact cells; apply native links; verify a minimal workbook change.

Native cell hyperlink authoring is absent from Artifact Tool's documented API.
Only authored label payloads and existing hyperlink targets are transplanted.
All other workbook ZIP parts must be byte-identical to the before snapshot.
"""
import copy
import io
import json
import shutil
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote
from index_study_pdfs import ROOT, openpyxl, fitz
from build_daily_collection import compact

WORK=ROOT/'internal/tmp/daily_collection'
BOOK=ROOT/'HDLBits_Attempt_2_Tracker_Simple.xlsx'
BEFORE=WORK/'tracker_before.xlsx'
CHANGES=WORK/'tracker_changes.json'
NS='http://schemas.openxmlformats.org/spreadsheetml/2006/main'
REL='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
PKG='http://schemas.openxmlformats.org/package/2006/relationships'
ET.register_namespace('',NS); ET.register_namespace('r',REL)
SHEET='xl/worksheets/sheet1.xml'
RELS='xl/worksheets/_rels/sheet1.xml.rels'


def prepare():
    # Preserve the source once; reruns must not silently redefine the baseline.
    if not BEFORE.exists():
        shutil.copy2(BOOK,BEFORE)
    manifest=json.loads((ROOT/'internal/Documentation/daily_collection_manifest.json').read_text())
    wb=openpyxl.load_workbook(BOOK); sh=wb['Tracker']; changes={}
    for cells in sh.iter_rows(min_row=6,max_row=183):
        entry=cells[0].value
        if str(entry) not in manifest['entries']:
            continue
        dests=manifest['entries'][str(entry)]
        assert len({d['day'] for d in dests})==1
        first=dests[0]; pages=compact([d['page'] for d in dests])
        changes[cells[4].coordinate]=dict(entry=entry,
            label=f"Day {first['day']:02d} - answer pp. {pages}",
            target=first['file']+f"#page={first['page']}")
    assert len(changes)==58
    CHANGES.write_text(json.dumps(changes,indent=2))
    wb.close()
    print('Prepared 58 exact discussion-cell changes; saved the before snapshot.')


def apply():
    changes=json.loads(CHANGES.read_text())
    # Read Artifact Tool's saved result without authoring through openpyxl.
    authored=openpyxl.load_workbook(WORK/'tracker_authored.xlsx')
    with zipfile.ZipFile(BEFORE) as src:
        tree=ET.fromstring(src.read(SHEET)); rels=ET.fromstring(src.read(RELS))
        cell_nodes={c.attrib['r']:c for c in tree.findall(f'{{{NS}}}sheetData/{{{NS}}}row/{{{NS}}}c')}
        link_nodes={l.attrib['ref']:l for l in tree.findall(f'{{{NS}}}hyperlinks/{{{NS}}}hyperlink')}
        rel_nodes={r.attrib['Id']:r for r in rels}
        for ref,item in changes.items():
            value=authored['Tracker'][ref].value
            assert value==item['label'],(ref,value,item)
            cell=cell_nodes[ref]
            for node in list(cell):
                if node.tag in {f'{{{NS}}}f',f'{{{NS}}}v',f'{{{NS}}}is'}:
                    cell.remove(node)
            cell.set('t','inlineStr')
            inline=ET.SubElement(cell,f'{{{NS}}}is')
            ET.SubElement(inline,f'{{{NS}}}t').text=value
            link=link_nodes[ref]
            rid=link.attrib[f'{{{REL}}}id']
            rel_nodes[rid].set('Target',item['target'])
            # A display attribute, if supplied by the original producer, must
            # not retain a contradictory old label.
            if 'display' in link.attrib:
                link.set('display',value)
        replacements={SHEET:ET.tostring(tree,encoding='utf-8',xml_declaration=True),
                      RELS:ET.tostring(rels,encoding='utf-8',xml_declaration=True)}
        temp=WORK/'tracker_linked.xlsx'
        with zipfile.ZipFile(temp,'w',zipfile.ZIP_DEFLATED) as out:
            for item in src.infolist():
                out.writestr(item,replacements.get(item.filename,src.read(item.filename)))
    authored.close()
    temp.replace(BOOK)
    # One final workbook is delivered; the identical output-area copy is not
    # another variant and keeps relative PDF links valid in the repository.
    target=ROOT/'outputs/daily_collection/HDLBits_Attempt_2_Tracker_Simple.xlsx'
    target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(BOOK,target)
    verify()


def verify():
    changes=json.loads(CHANGES.read_text())
    with zipfile.ZipFile(BEFORE) as a,zipfile.ZipFile(BOOK) as b:
        assert a.namelist()==b.namelist()
        assert {n for n in a.namelist() if a.read(n)!=b.read(n)}=={SHEET,RELS}
        old_xml=ET.fromstring(a.read(SHEET)); new_xml=ET.fromstring(b.read(SHEET))
        # Drop exactly the 58 authored payloads from both trees; all remaining
        # worksheet content, validation, row heights, panes and styles agree.
        for tree in (old_xml,new_xml):
            for c in tree.findall(f'{{{NS}}}sheetData/{{{NS}}}row/{{{NS}}}c'):
                if c.attrib['r'] in changes:
                    c.attrib.pop('t',None)
                    for child in list(c):
                        if child.tag in {f'{{{NS}}}f',f'{{{NS}}}v',f'{{{NS}}}is'}:
                            c.remove(child)
            for link in tree.findall(f'{{{NS}}}hyperlinks/{{{NS}}}hyperlink'):
                if link.attrib['ref'] in changes:
                    link.attrib.pop('display',None)
        assert ET.tostring(old_xml)==ET.tostring(new_xml)
    old=openpyxl.load_workbook(BEFORE); new=openpyxl.load_workbook(BOOK)
    assert old.sheetnames==new.sheetnames
    for oldsh,newsh in zip(old,new):
        for row in oldsh:
            for a in row:
                b=newsh[a.coordinate]
                change=changes.get(a.coordinate) if oldsh.title=='Tracker' else None
                assert b.value==(change['label'] if change else a.value),(a.coordinate,a.value,b.value)
                assert a._style==b._style
                assert (b.hyperlink.target if b.hyperlink else None)==(change['target'] if change else (a.hyperlink.target if a.hyperlink else None))
    sh=new['Tracker']
    assert sum(bool(c.hyperlink) for row in sh for c in row)==236
    assert sum(sh[f'D{r}'].value=='Done' for r in range(6,184))==178
    assert sh['B3'].value==178 and sh['D3'].value==0
    for ref,item in changes.items():
        name,fragment=item['target'].split('#')
        with fitz.open(ROOT/unquote(name)) as doc:
            assert 1<=int(fragment.split('=')[1])<=len(doc)
        assert sh[ref].font.color.rgb[-6:]=='0563C1'
    old.close();new.close()
    print('PASS: 58 labels/targets updated, 236 native links, 178 Done; every unrelated value, style and workbook package part preserved.')


if __name__=='__main__':
    {'prepare':prepare,'apply':apply,'verify':verify}[sys.argv[1]]()
