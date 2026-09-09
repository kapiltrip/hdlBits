"""Build ten canonical reading-day PDFs without changing the source PDFs.

Every original technical page occurs exactly once. Old front matter is replaced,
not concatenated. The manifest drives contents, bookmarks, index and link maps.
"""
from __future__ import annotations

import io
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import quote, unquote

from index_study_pdfs import (
    DOCS, ROOT, INDEX_URL, ARIAL, ARIAL_BOLD, CONSOLAS, tracker_rows,
    fitz, canvas, HexColor, ParagraphStyle, Paragraph, pdfmetrics, TTFont,
)
from reportlab.platypus import SimpleDocTemplate, PageBreak, Spacer, Table, TableStyle, Preformatted
from reportlab.lib.pagesizes import A4
from xml.sax.saxutils import escape
from daily_questions import QUESTIONS, CHAPTER_QUESTIONS

OUT = ROOT / 'output/pdf'
WORK = ROOT / 'internal/tmp/daily_collection'
MANIFEST = ROOT / 'internal/Documentation/daily_collection_manifest.json'
NAVY, INK, MUTED, BLUE = '#002060', '#233246', '#566579', '#0563C1'
pdfmetrics.registerFont(TTFont('DailyArial', str(ARIAL)))
pdfmetrics.registerFont(TTFont('DailyBold', str(ARIAL_BOLD)))
pdfmetrics.registerFont(TTFont('DailyMono', str(CONSOLAS)))


def part(note, first=2, last=None, title=None):
    m = DOCS[note-1]
    last = last or len(m['pages'])+1
    return dict(note=note, first=first, last=last,
                title=title or m['title'].replace('\n', ' '))


# Reading-day labels follow the existing review sequence. They are not fresh
# dates or claims that every discussed entry belongs to that tracker day.
# Kapil explicitly requested all later series together in Day 10.
DAYS = [
    dict(day=1, title='Serial reception and HDLC timing',
         summary='Capture bits on real edges, assemble complete frames, and place pattern outputs in the required cycle.',
         parts=[part(1), part(3)]),
    dict(day=2, title='Loops, muxes and Verilog operators',
         summary='Procedural and generate loops, carry wiring, population count, mux selection and the Lemmings boundary.',
         parts=[part(2, 2, 11)]),
    dict(day=3, title='Latch storage and state history',
         summary='Two small explanations together: intentional latch storage and why current water-level inputs cannot replace state history.',
         parts=[part(2, 12, 12, 'Intentional latch storage'), part(4, 2, 2, 'Water-level state history')]),
    dict(day=4, title='Vectors, flip-flops and PS/2 packets',
         summary='Indexed byte slices, D-input equations and packet data ownership, with complete code and clock traces.',
         parts=[part(5)]),
    dict(day=5, title='Sampled edges, serial complement and RTL questions',
         summary='Keep the recovered questions, detailed Moore complementer, small RTL mistakes and dated submission evidence together.',
         parts=[part(4, 3, 6, 'Recovered questions: edges, reset and operators'), part(6), part(7)]),
    dict(day=6, title='Dual-edge sampling and three-sample FSMs',
         summary='Read waveforms, distinguish FPGA resources from simulation behavior, and include the third sample without losing a cycle.',
         parts=[part(8), part(9)]),
    dict(day=7, title='FSM widths and counter connections',
         summary='Interpret width warnings, derive next-state bits and trace load, enable and data through a counter interface.',
         parts=[part(10)]),
    dict(day=8, title='Wire, reg and reset behavior',
         summary='Separate wiring from initialization, understand stored values and check shift-register and BCD-clock reset behavior.',
         parts=[part(11)]),
    dict(day=9, title='Missing assignments and the 1101 FSM',
         summary='Trace accidental latch behavior and review the five-state recognizer before its later use in the timer series.',
         parts=[part(12)]),
    dict(day=10, title='Boolean forms, timers, LFSRs and Conway',
         summary='The final connected series: K-maps, Rules 90 and 110, timer control, three LFSRs and Conway. End with an LFSR definitions and revision reference.',
         parts=[part(13), part(14), part(15), part(16),
                dict(note=0, first=1, last=3, title='LFSR definitions and revision reference')]),
]

REF_HEADINGS = [
    'LFSR: definition and essential vocabulary',
    'Taps, feedback forms and maximum period',
    'Applications, limits and clocked-state revision',
]


def paragraph(c, text, x, top, width=499, size=11, bold=False, color=INK):
    s = ParagraphStyle('p', fontName='DailyBold' if bold else 'DailyArial',
                       fontSize=size, leading=size*1.32, textColor=HexColor(color))
    p = Paragraph(escape(text).replace('\n', '<br/>'), s)
    _, height = p.wrap(width, 1000)
    p.drawOn(c, x, top-height)
    return top-height


def clean_unused_font(doc):
    for page in doc:
        for xref in page.get_contents():
            stream = doc.xref_stream(xref)
            doc.update_stream(xref, re.sub(rb'BT /F1 [0-9.]+ Tf [0-9.]+ TL ET', b'', stream))
    for xref in range(1, doc.xref_length()):
        obj = doc.xref_object(xref)
        cleaned = re.sub(r'/F1\s+\d+\s+0\s+R', '', obj)
        if cleaned != obj:
            doc.update_object(xref, cleaned)


def build_lfsr_reference():
    """Three new reader pages; all worked recurrences are independently checked."""
    styles = {
        'body': ParagraphStyle('body', fontName='DailyArial', fontSize=10.5, leading=14.4,
                               textColor=HexColor(INK), spaceAfter=7),
        'title': ParagraphStyle('title', fontName='DailyBold', fontSize=21, leading=25,
                                textColor=HexColor(NAVY), spaceAfter=10),
        'h': ParagraphStyle('h', fontName='DailyBold', fontSize=12.5, leading=16,
                            textColor=HexColor(NAVY), spaceBefore=6, spaceAfter=5),
        'small': ParagraphStyle('small', fontName='DailyArial', fontSize=8.5, leading=11.4,
                                textColor=HexColor(MUTED), spaceAfter=5),
        'cell': ParagraphStyle('cell', fontName='DailyArial', fontSize=9.2, leading=12.2,
                               textColor=HexColor(INK)),
        'code': ParagraphStyle('code', fontName='DailyMono', fontSize=9.2, leading=12.5,
                               textColor=HexColor(INK), spaceAfter=9),
    }
    def p(text, kind='body'):
        return Paragraph(text, styles[kind])
    def table(rows, widths):
        t = Table([[p(escape(a), 'cell') for a in row] for row in rows], colWidths=widths)
        t.setStyle(TableStyle([
            ('VALIGN',(0,0),(-1,-1),'TOP'), ('BACKGROUND',(0,0),(-1,0),HexColor('#E8EDF3')),
            ('LINEBELOW',(0,0),(-1,-1),.4,HexColor('#CDD3DB')),
            ('LEFTPADDING',(0,0),(-1,-1),6), ('RIGHTPADDING',(0,0),(-1,-1),6),
            ('TOPPADDING',(0,0),(-1,-1),6), ('BOTTOMPADDING',(0,0),(-1,-1),6),
        ]))
        return t
    story = [p(REF_HEADINGS[0], 'title'),
        p('<b>LFSR</b> means <b>linear-feedback shift register</b>: a bank of clocked bits whose next state is formed by shifting and feeding selected old bits back through XOR logic. In the autonomous binary XOR designs studied here, each next bit is a linear combination of old bits over GF(2), the two-element field.'),
        p('What each word means', 'h'),
        table([
            ['Term', 'Meaning in these exercises'],
            ['Register / state', 'The n stored bits q[n-1:0]. A state is the complete bit pattern, not only the output bit.'],
            ['Shift', 'Old values move to specified neighboring destinations on the active edge. The diagram determines direction.'],
            ['Feedback / tap', 'A selected old bit participates in the next-state network. In HDLBits Galois drawings, numbered taps identify stages where feedback is injected.'],
            ['Linear / GF(2)', 'XOR is addition modulo two: 1 XOR 1 = 0, with no carry. A copied bit is also a linear expression.'],
            ['Seed', 'The starting state established by reset or parallel load. It selects where a deterministic trajectory begins.'],
            ['Period', 'The number of updates before the sequence repeats. An n-bit maximal XOR LFSR has a nonzero-state period of 2^n - 1.'],
            ['Lockup', 'A state that maps to itself. With only XOR/copy feedback, all-zero state remains all zero.'],
        ], [112, 387]), Spacer(1,8),
        p('A clock edge computes a new state', 'h'),
        p('For Lfsr5, q=00001 gives outgoing old q[0]=1. The base shift is 10000; the tap changes destination q[2] to old q[3] XOR old q[0] = 1. The next state is 10100. Both steps describe one edge, not two clock cycles.'),
        p('Do not interpret the 5-bit word as a binary count. It progresses 01, 14, 0A, 05, ... in hexadecimal, not 01, 02, 03, 04. Reapplying the same seed and inputs reproduces the same sequence.'),
        p('Source convention: <link href="https://users.ece.cmu.edu/~koopman/lfsr/index.html" color="#0563C1">Philip Koopman, Maximal Length LFSR Feedback Terms</link>, right-shift recurrence. The worked five-bit calculation is derived from the saved HDLBits solution.', 'small'),
        PageBreak(), p(REF_HEADINGS[1], 'title'),
        p('Fibonacci and Galois describe different placements of the feedback XORs. In the Fibonacci form, selected stages combine into feedback entering one end. In the Galois form, the outgoing bit is distributed into selected internal stage updates. Equivalent polynomials can require a state/phase mapping; copying the same seed bits does not guarantee identical cycle-by-cycle register words.'),
        p('Translate the convention before copying a tap list', 'h'),
        p('For the HDLBits right-shifting five-bit Galois circuit, tap positions 5 and 3 correspond to destinations q[4] and q[2]. Position k becomes index k-1. The lower tap uses the ordinary shifted source q[k] XOR outgoing q[0]; the top destination receives q[0]. This rule belongs to this drawing convention, not every published LFSR diagram.'),
        Preformatted("next_q = (q >> 1) ^ (q[0] ? 5'b10100 : 5'b00000);\n// mask 10100 injects feedback into destinations 4 and 2", styles['code']),
        p('Why not every tap choice gives maximum length', 'h'),
        p('A nonzero seed alone is insufficient. If the five-bit mask is 10000, the update merely rotates: 00001 -> 10000 -> 01000 -> 00100 -> 00010 -> 00001. Its period from this seed is only five. The exercise mask 10100 instead visits all 31 nonzero states before returning to 00001.'),
        p('A feedback polynomial records the recurrence algebraically; its coefficients are bits and arithmetic is over GF(2). A degree-n primitive polynomial is irreducible and gives multiplicative order 2^n - 1. The implementation must use the matching orientation and feedback convention. Reversing bit direction can introduce the reciprocal polynomial.'),
        table([
            ['Design', 'Nonzero period', 'Reference transition'],
            ['Mt2015 three-bit circuit', '7', '001 -> 010'],
            ['HDLBits five-bit Galois', '31', '00001 -> 10100'],
            ['HDLBits 32-bit Galois', '4,294,967,295', '00000001 -> 80200003 (hex)'],
        ], [186, 112, 201]), Spacer(1,8),
        p('The short periods were exhaustively enumerated. The 32-bit period is supported by the primitive-order calculation, not by simulating over four billion clock edges. Loading zero into these XOR circuits gives period one instead.'),
        p('XOR and XNOR lockup rules differ', 'h'),
        p('The conventional XNOR-feedback construction in XAPP052 excludes the all-ones state; these XOR exercises exclude zero. Do not swap operators or reset values based only on a tap table.'),
        p('References: <link href="https://docs.amd.com/v/u/en-US/xapp052" color="#0563C1">Peter Alfke, Xilinx XAPP052, pp. 5-6</link> (tap-numbering and XNOR convention); <link href="https://users.ece.cmu.edu/~koopman/lfsr/index.html" color="#0563C1">Koopman</link> (right-shift masks). Equations and the five-state counterexample are derived here.', 'small'),
        PageBreak(), p(REF_HEADINGS[2], 'title'),
        p('What it is useful for', 'h'),
        p('An LFSR provides repeatable test patterns and long periodic bit sequences with simple XOR-and-register logic. It can act as a sequence counter when the numerical binary order is irrelevant. A compact state generator is not a substitute for a binary counter when downstream logic needs the actual arithmetic count.'),
        p('PRBS means pseudo-random binary sequence. The word pseudo matters: a fixed recurrence is predictable from its state. A long period does not make a bare LFSR a secure random-number generator. Its equations are linear, so it should not be used by itself to generate secret keys or security tokens.'),
        p('Scramblers and CRC circuits use related shift/XOR structures, but commonly mix incoming data into the recurrence. A CRC register stores a remainder under a specified polynomial and bit-order convention. An autonomous HDLBits LFSR advancing without message data is not, by itself, a complete CRC implementation.'),
        p('Current state and next state: the shared coding rule', 'h'),
        table([
            ['Question', 'Decision'],
            ['What is q / state?', 'The value stored before the active edge. Use it to perform work belonging to the current phase or generation.'],
            ['What is next_q / next_state?', 'The combinationally computed candidate for storage. It is a signal, not a function call and not an extra clock cycle.'],
            ['Must I declare next_q?', 'No. A single clocked block can write q <= expression_of_old_q. A separate complete combinational block can instead calculate next_q, then store q <= next_q.'],
            ['When inspect next_state in a clocked FSM block?', 'Only for an intended response to the chosen destination. To act once on entry, test state != TARGET && next_state == TARGET.'],
            ['How avoid a partly updated state?', 'Use nonblocking <= for clocked registers. All right-hand sides in the shown process read old state; a later overlapping assignment replaces the scheduled destination, not the old source.'],
        ], [177, 322]), Spacer(1,8),
        p('Quick checks before trusting a new LFSR', 'h'),
        p('Name the shift direction and feedback bit; translate numbered taps; match reset/load priority; predict the first post-seed transition; test zero lockup deliberately; then check the period with a method appropriate to the width. An unknown simulation state is not a random seed: establish a known nonzero state first.'),
        p('Reference: <link href="https://docs.amd.com/v/u/en-US/xapp052" color="#0563C1">XAPP052, pp. 4 and 6</link>, deterministic sequences and LFSR counters. The security warning follows from the explicit linear recurrence; the coding recap applies the old-value rules already traced in the timer, LFSR and Conway chapters.', 'small'),
    ]
    buf = io.BytesIO()
    SimpleDocTemplate(buf, pagesize=A4, leftMargin=48, rightMargin=48,
                      topMargin=49, bottomMargin=48).build(story)
    doc = fitz.open(stream=buf.getvalue(), filetype='pdf')
    assert len(doc) == 3, f'LFSR reference reflowed to {len(doc)} pages'
    for pg, title in zip(doc, REF_HEADINGS):
        assert title in ' '.join(pg.get_text().split())
    clean_unused_font(doc)
    return doc


def headings(p):
    return REF_HEADINGS[p['first']-1:p['last']] if not p['note'] else DOCS[p['note']-1]['pages'][p['first']-2:p['last']-1]


def questions(p):
    start=p['first']-(1 if not p['note'] else 2)
    return QUESTIONS[p['note']][start:start+p['last']-p['first']+1]


def toc_chunks(parts):
    """Plan detailed contents without depending on the eventual page numbers."""
    chunks, chunk, y = [], [], 735
    for idx, p in enumerate(parts):
        for offset, label in enumerate(questions(p)):
            if offset == 0:
                if y < 125:
                    chunks.append(chunk); chunk=[]; y=735
                chunk.append(('part', idx, None, CHAPTER_QUESTIONS[p['note']])); y -= 28
            if y < 85:
                chunks.append(chunk); chunk=[]; y=735
                chunk.append(('part', idx, None, 'Questions continued')); y -= 28
            chunk.append(('section', idx, offset, label)); y -= 17
    if chunk:
        chunks.append(chunk)
    return chunks


def prepare():
    sources = {i+1: fitz.open(ROOT/m['filename']) for i,m in enumerate(DOCS)}
    sources[0] = build_lfsr_reference()
    for n in range(1,17):
        assert len(QUESTIONS[n])==len(DOCS[n-1]['pages'])
    mapping = {}
    for d in DAYS:
        count = sum(p['last']-p['first']+1 for p in d['parts'])
        d['toc_chunks'] = toc_chunks(d['parts']) if count > 11 else []
        d['front'] = 1 + len(d['toc_chunks'])
        d['total'] = d['front'] + count
        d['filename'] = f"HDLBits_Day_{d['day']:02d}.pdf"
        at = d['front'] + 1
        for p in d['parts']:
            p['start'] = at
            p['end'] = at + p['last']-p['first']
            for old in range(p['first'], p['last']+1):
                assert (p['note'],old) not in mapping
                mapping[p['note'],old] = dict(day=d['day'], page=at,
                                               file='output/pdf/'+d['filename'])
                at += 1
    expected = {(n,pg) for n in range(1,17) for pg in range(2,len(sources[n])+1)}
    assert expected == {k for k in mapping if k[0]}, 'Every original body page must occur once'
    return sources, mapping


def front_matter(d):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4, invariant=1)
    links=[]
    w,h=A4
    def header(label):
        c.setFillColor(HexColor(NAVY)); c.rect(0,h-2,w,2,fill=1,stroke=0)
        paragraph(c, 'HDLBITS / ATTEMPT 2',48,794,300,10,True,NAVY)
        paragraph(c,label,427,794,120,10,True,NAVY)
    def row(label, target, top, page=0, size=10.5):
        c.setFillColor(HexColor(BLUE)); c.setFont('DailyArial',size)
        assert pdfmetrics.stringWidth(label,'DailyArial',size) < 463, label
        c.drawString(48,top,label)
        c.setFont('DailyBold',size); c.drawRightString(547,top,str(target))
        links.append((page,fitz.Rect(45,h-top-12,551,h-top+6),target-1))
    header(f"DAY {d['day']:02d} / 10")
    y=paragraph(c,d['title'],48,751,499,26,True,NAVY)
    y=paragraph(c,d['summary'],48,y-17,499,11.5)
    y=paragraph(c,f"Kapil Tripathi | Verilog and digital design | {d['total']} pages",48,y-16,499,9.3,False,MUTED)-29
    y=paragraph(c,'CONTENTS / click a topic to jump',48,y,499,10,True,NAVY)-18
    if d['toc_chunks']:
        for p in d['parts']:
            label=CHAPTER_QUESTIONS[p['note']]
            # Compact labels fit on the cover; full headings appear in the outline.
            if pdfmetrics.stringWidth(label,'DailyArial',10.5)>455:
                label=label.replace('K-map operators, Boolean forms and cellular automata','K-maps and cellular automata')
            row(label,p['start'],y); y-=29
        row('Which specific questions does this PDF answer?',2,y); y-=32
    else:
        for p in d['parts']:
            for offset,label in enumerate(questions(p)):
                row(label,p['start']+offset,y); y-=24
    if d['day']==5:
        y=paragraph(c,'Original entry 80 request: "explain me this code in a deep manner, along with need of each state"; "ik the meaning and need of states s0, s1, s2 ... rest, explain me in doc".',48,y-12,499,9.5,False,MUTED)-10
    if d['day']==10:
        row('What is an LFSR? What do seed, tap and lockup mean?',d['parts'][-1]['start'],y); y-=27
        row('When should the clocked block use next_state?',d['parts'][1]['start']+9,y); y-=27
    assert y>155, (d['day'],y)
    paragraph(c,'Reading days group the explanations, including later revisits. Tracker day labels and original dated submission evidence remain unchanged.',48,135,499,9,False,MUTED)
    paragraph(c,'Use the linked contents or PDF bookmarks. Page numbers match the PDF viewer. Source questions and technical evidence remain beside their explanations.',48,99,499,9,False,MUTED)
    c.showPage()
    for page_index, chunk in enumerate(d['toc_chunks'],1):
        header(f"DAY {d['day']:02d}")
        paragraph(c,'Questions answered'+(' (continued)' if page_index>1 else ''),48,762,499,20,True,NAVY)
        y=723
        for kind,part_index,offset,label in chunk:
            p=d['parts'][part_index]
            if kind=='part':
                y-=7
                row(label,p['start'],y,page_index,10.2); y-=21
            else:
                row(label,p['start']+offset,y,page_index,9.3); y-=17
        assert y>58,(d['day'],y)
        c.showPage()
    c.save()
    doc=fitz.open(stream=buf.getvalue(),filetype='pdf')
    assert len(doc)==d['front']
    clean_unused_font(doc)
    return doc,links


def replace_text(pg, old, new, records, reason):
    """Replace a complete literal span, retaining the original baseline/style."""
    if old==new:
        return
    hits=pg.search_for(old)
    assert hits, (pg.number,old)
    for box in hits:
        spans=[s for b in pg.get_text('dict')['blocks'] if b['type']==0 for line in b['lines']
               for s in line['spans'] if old in s['text'] and fitz.Rect(s['bbox']).intersects(box)]
        assert len(spans)==1,(old,spans)
        span=spans[0]
        # Only accept replacements that fit within the original phrase or its
        # immediately trailing whitespace. Full paragraphs use replace_block.
        font=fitz.Font(fontfile=str(ARIAL))
        width=font.text_length(new,fontsize=span['size'])
        assert width <= box.width+3,(old,new,width,box.width)
        pg.add_redact_annot(box,fill=False); pg.apply_redactions(images=0,graphics=0)
        color=span['color']; rgb=tuple(((color>>s)&255)/255 for s in (16,8,0))
        pg.insert_font(fontname='DailyFix',fontfile=str(ARIAL),set_simple=True)
        pg.insert_text((box.x0,span['origin'][1]),new,fontname='DailyFix',fontfile=str(ARIAL),fontsize=span['size'],color=rgb)
    records.append(dict(old=old,new=new,reason=reason))


def replace_block(pg, contains, new, records):
    blocks=[b for b in pg.get_text('blocks') if b[6]==0 and contains in ' '.join(b[4].split())]
    assert len(blocks)==1,(pg.number,contains,blocks)
    block=blocks[0]; box=fitz.Rect(block[:4])
    # Font ascender/descender metrics need a few points beyond an extracted
    # glyph box. Extend only into proven whitespace below the paragraph.
    following=[b[1] for b in pg.get_text('blocks') if b[6]==0 and b[1]>=box.y1 and b[0]<box.x1 and b[2]>box.x0]
    box.y1=min(box.y1+5,min(following,default=pg.rect.height-45)-2)
    pg.add_redact_annot(box,fill=False); pg.apply_redactions(images=0,graphics=0)
    for size in (10.2,9.7,9.2,8.7):
        font=fitz.Font(fontfile=str(ARIAL))
        # Measure by inserting into a disposable page before touching the real one.
        test=fitz.open(); tp=test.new_page(width=pg.rect.width,height=pg.rect.height)
        result=tp.insert_textbox(box,new,fontsize=size,fontname='f',fontfile=str(ARIAL))
        test.close()
        if result>=0:
            pg.insert_font(fontname='DailyFix',fontfile=str(ARIAL),set_simple=True)
            assert pg.insert_textbox(box,new,fontsize=size,fontname='DailyFix',fontfile=str(ARIAL),color=(.137,.196,.275))>=0
            break
    else:
        raise ValueError(f'Replacement paragraph does not fit: {contains}')
    records.append(dict(old=' '.join(block[4].split()),new=new,reason='Merged-volume reference'))


def remap_references(pg,note,old,mapping,records):
    if note==1:
        pairs={8:[('Pages 10-11','Pages 11-12')],10:[('page 7','page 8'),('page 6','page 7')],11:[('page 10','page 11')]}
        for a,b in pairs.get(old,[]):
            replace_text(pg,a,b,records,'Daily pagination')
    if note==4 and old==6:
        replace_block(pg,'The Attempt 2 tracker links these four entries',
            '- The tracker links each question to its page in Day 3 or Day 5.',records)
        replace_block(pg,'The four questions are answered',
            'Water-level history: Day 3, page 3. The other three answers: pages 3-5 here. The water-level snippet is not a full solution; the saved Day 5 testbench checks the other examples.',records)
    if note==8 and old==2:
        blocks=[' '.join(b[4].split()) for b in pg.get_text('blocks') if b[6]==0 and 'Entries 87 and 89 are on Day 5' in ' '.join(b[4].split())]
        assert len(blocks)==1
        replace_block(pg,'Entries 87 and 89 are on Day 5',
            'Entries 87 and 89 are on Day 5 in the tracker; they were reviewed with the Day 6 material. Entry 90 follows as the three-sample FSM chapter in this same PDF.',records)
        # PDF extraction groups this entire table row as one block. Replace
        # only the destination-cell phrase, preserving the other three cells.
        replace_text(pg,'Dedicated Entry 90 PDF',
            f"FSM chapter, p. {mapping[9,2]['page']}",records,'Merged-volume table reference')
    if note==7 and old==2:
        replace_block(pg,'This PDF contains the review and its historical submission table.',
            'This chapter preserves the review and its historical submission table. The Markdown companion remains available from the collection index; tracker links open the combined day-wise PDFs.',records)
    if note==14 and old==5:
        target=mapping[14,7]['page']
        replace_block(pg,'Several nonblocking assignments to q',
            'Several nonblocking assignments to q inside one clocked block are competing assignments from one owner, '
            'resolved by source order. Assigning q from another always block or continuous assign creates another owner. '
            f'That is the multiple-driver problem addressed on page {target}.',records)
    if note==15 and old==8:
        target=mapping[15,7]['page']
        # Two longer references need the whole paragraph to reflow safely.
        replace_block(pg,'The editor comment asked',
            f'The editor comment asked to understand the question before the solution. The mapping table and the two equation sets on page {target} provide that pre-code interpretation; this page is the direct RTL transcription.',records)


def normalize_body(pg,day):
    w,h=pg.rect.width,pg.rect.height
    for link in list(pg.get_links()):
        pg.delete_link(link)
    pg.add_redact_annot(fitz.Rect(0,h-37,w,h),fill=(1,1,1))
    # Remove independent technical-page numbering, keeping the chapter heading.
    for b in pg.get_text('blocks'):
        if b[6]==0 and b[1]<45 and 'TECHNICAL PAGE' in b[4]:
            # Shared text blocks can hold both left header and right counter.
            for s in b[4].splitlines():
                if 'TECHNICAL PAGE' in s:
                    for rect in pg.search_for(s):
                        pg.add_redact_annot(rect,fill=False)
    pg.apply_redactions(images=0,graphics=0)
    # The later source notes retain old Day 11/12 headers; rename only the
    # running header because Kapil placed all later material into Day 10.
    if day==10:
        for old in ('DAY 11','DAY 12'):
            for box in pg.search_for(old):
                if box.y0<45:
                    spans=[s for b in pg.get_text('dict')['blocks'] if b['type']==0
                           for line in b['lines'] for s in line['spans']
                           if old in s['text'] and s['bbox'][1]<45]
                    span=spans[0]
                    pg.add_redact_annot(box,fill=False); pg.apply_redactions(images=0,graphics=0)
                    pg.insert_font(fontname='DailyHeader',fontfile=str(ARIAL_BOLD),set_simple=True)
                    pg.insert_text((box.x0,span['origin'][1]),'DAY 10',fontname='DailyHeader',
                                   fontfile=str(ARIAL_BOLD),fontsize=span['size'],color=(.337,.396,.475))


def footer(pg,day,total):
    w,h=pg.rect.width,pg.rect.height
    pg.draw_line((48,h-36),(w-48,h-36),color=(.79,.82,.86),width=.5)
    pg.insert_font(fontname='DailyFooter',fontfile=str(ARIAL),set_simple=True)
    pg.insert_text((48,h-22),f'Kapil Tripathi | HDLBits Attempt 2 | Day {day:02d}',fontname='DailyFooter',fontsize=7.5,color=(.34,.40,.48))
    for text,x,kind,target in [('Contents',w-213,fitz.LINK_GOTO,0),('All days',w-151,fitz.LINK_URI,INDEX_URL)]:
        pg.insert_text((x,h-22),text,fontname='DailyFooter',fontsize=8,color=(.02,.388,.757))
        link=dict(kind=kind,from_=None)
        link={'kind':kind,'from':fitz.Rect(x-2,h-33,x+45,h-14)}
        if kind==fitz.LINK_GOTO:
            link.update(page=target,to=fitz.Point(0,0))
        else:
            link['uri']=target
        pg.insert_link(link)
    pg.insert_text((w-80,h-22),f'{pg.number+1} / {total}',fontname='DailyFooter',fontsize=8,color=(.34,.40,.48))


def entry_mapping(mapping,rows):
    locations={}
    for n,m in enumerate(DOCS,1):
        for entry,span in m['entries'].items():
            span=re.sub(r'\d+',lambda x:str(int(x[0])+int(m['prepend'])),span)
            old_pages=[]
            for term in span.split(','):
                nums=[int(x) for x in re.findall(r'\d+',term)]
                old_pages.extend(range(nums[0],nums[-1]+1))
            dests=[mapping[n,p] for p in old_pages]
            locations[entry]=dests
    assert len(locations)==58
    return locations


def rewrite_uri(uri,mapping):
    # Known links to an original reader PDF now target the canonical day page.
    decoded=unquote(uri)
    for note,m in enumerate(DOCS,1):
        if m['filename'] not in decoded:
            continue
        page_match=re.search(r'#page=(\d+)',decoded)
        old=int(page_match[1]) if page_match else 2
        old=max(2,old)
        if (note,old) not in mapping:
            continue
        dest=mapping[note,old]
        return 'https://github.com/kapiltrip/hdlBits/blob/main/HDLBits%20Attempt%202/'+quote(dest['file'],safe='/')+f"#page={dest['page']}"
    return uri


def build_day(d,sources,mapping,entries,rows):
    doc,front_links=front_matter(d)
    provenance=[]
    pending=[]
    for p in d['parts']:
        src=sources[p['note']]
        for old in range(p['first'],p['last']+1):
            new=len(doc)
            srcpg=src[old-1]
            rawlinks=srcpg.get_links()
            doc.insert_pdf(src,from_page=old-1,to_page=old-1,links=False,annots=False)
            pg=doc[new]
            normalize_body(pg,d['day'])
            records=[]
            remap_references(pg,p['note'],old,mapping,records)
            for l in rawlinks:
                if l['from'].y0>=srcpg.rect.height-50:
                    continue
                nl={'kind':l['kind'],'from':l['from']}
                if l['kind']==fitz.LINK_URI:
                    nl['uri']=rewrite_uri(l['uri'],mapping)
                elif l['kind']==fitz.LINK_GOTO:
                    key=(p['note'],l['page']+1)
                    if l['page']==0 and p['note']:
                        nl.update(page=0,to=fitz.Point(0,0))
                    else:
                        target=mapping[key]
                        if target['day']==d['day']:
                            nl.update(page=target['page']-1,to=l.get('to',fitz.Point(0,0)))
                        else:
                            nl={'kind':fitz.LINK_URI,'from':l['from'],
                                'uri':'https://github.com/kapiltrip/hdlBits/blob/main/HDLBits%20Attempt%202/'+quote(target['file'],safe='/')+f"#page={target['page']}"}
                else:
                    raise ValueError(f'Unexpected body link: {l}')
                pending.append((new,nl))
            provenance.append(dict(note=p['note'],source_page=old,page=new+1,references=records))
    assert len(doc)==d['total']
    for page,link in pending:
        doc[page].insert_link(link)
    for page,rect,target in front_links:
        doc[page].insert_link({'kind':fitz.LINK_GOTO,'from':rect,'page':target,'to':fitz.Point(0,0)})
    toc=[[1,'Contents and reading guide',1]]
    if d['front']>1:
        toc.append([1,'Questions answered',2])
    for p in d['parts']:
        toc.append([1,p['title'],p['start']])
        toc.extend([2,label,p['start']+i] for i,label in enumerate(questions(p)))
    day_entries={n:sorted({x['page'] for x in loc if x['day']==d['day']}) for n,loc in entries.items()}
    day_entries={n:pages for n,pages in day_entries.items() if pages}
    # The repeated 1101 question remains accessible in Day 9 and Day 10.
    if d['day']==9:
        day_entries[155]=[mapping[12,5]['page'],mapping[12,6]['page']]
    if day_entries:
        toc.append([1,'Tracker entry lookup',min(min(v) for v in day_entries.values())])
        for n,pages in sorted(day_entries.items()):
            toc.append([2,f"Entry {n}: {rows[n]['problem']}",pages[0]])
    doc.set_toc(toc)
    doc.set_page_labels([dict(startpage=0,prefix='',style='D',firstpagenum=1)])
    doc.xref_set_key(doc.pdf_catalog(),'PageMode','/UseOutlines')
    doc.xref_set_key(doc.pdf_catalog(),'Lang','(en-IN)')
    for pg in doc:
        footer(pg,d['day'],d['total'])
    doc.set_metadata(dict(title=f"Day {d['day']:02d} - {d['title']}",author='Kapil Tripathi',
        subject=d['summary'],keywords='HDLBits; Attempt 2; daily-collection-v1',creator='Kapil Tripathi - HDLBits study notes'))
    doc.subset_fonts()
    dest=OUT/d['filename']
    doc.save(dest,garbage=4,deflate=True)
    doc.close()
    return dict(day=d['day'],title=d['title'],summary=d['summary'],file='output/pdf/'+d['filename'],
        pages=d['total'],front=d['front'],parts=d['parts'],provenance=provenance,
        front_links=[dict(page=pg+1,target=t+1,rect=list(r)) for pg,r,t in front_links],entries=day_entries)


def compact(pages):
    pages=sorted(set(pages)); groups=[]
    start=last=pages[0]
    for p in pages[1:]:
        if p==last+1:
            last=p; continue
        groups.append(str(start) if start==last else f'{start}-{last}'); start=last=p
    groups.append(str(start) if start==last else f'{start}-{last}')
    return ', '.join(groups)


def link_label(dest,label=None):
    return f"[{label or ('Day '+str(dest['day'])+', p. '+str(dest['page']))}]({dest['file']}#page={dest['page']})"


def write_index(results,mapping,entries,rows):
    text='''# HDLBits Attempt 2 - day-wise reading index

**Kapil Tripathi | Verilog and digital design**

One reading PDF per day, across **10 days**. Related short notes are combined; original questions, complete code, diagrams, traces and historical evidence stay with their explanations. Day 10 holds all the later series and ends with an LFSR definition/reference section.

[Find a question](#find-a-question) · [Choose a day](#choose-a-day) · [Find an entry](#find-a-tracker-entry) · [Tracker](HDLBits_Attempt_2_Tracker_Simple.xlsx)

## Choose a day

Reading days follow the review sequence, not a new completion calendar. The tracker retains its original day labels: an exercise can be revisited in a later reading day. Earlier mixed notes were grouped by topic; the Day 2-3 latch page is now with state history on Day 3. All later K-map, timer, LFSR and Conway material is together on Day 10, as requested.

| Day | Open the combined PDF | Pages | Contents |
|---:|---|---:|---|
'''
    for r in results:
        text+=f"| {r['day']} | [{r['title']}]({r['file']}) | {r['pages']} | {r['summary']} |\n"
    text+='''
Each PDF has one reading cover, clickable contents, hierarchical bookmarks, continuous page numbering and **Contents / All days** footer links. Larger days also have a detailed section index. The displayed page numbers match physical PDF pages.

For reliable page jumps, download a PDF and use its built-in contents or bookmarks. Links ending in `#page=N` work in supporting PDF viewers; GitHub previews may ignore the page fragment.

## Find a question

'''
    questions=[
        ('Serial bits and clock edges',1,2),('Generate versus procedural loops',2,3),
        ('Mux operators and selector bits',2,7),('Lemmings: the 20/21-cycle boundary',2,8),
        ('Latch storage',2,12),('Why an FSM must remember water-level history',4,2),
        ('HDLC: Moore/Mealy output timing',3,2),('Indexed part-selects',5,2),('PS/2 data and done timing',5,4),
        ("Why the Moore two\'s-complement machine needs three states",6,3),
        ('Sampled-edge detection',4,3),('Reduction, bitwise and logical operators',4,5),
        ('Sticky edge capture and one-hot encoding',7,6),('Dual-edge logic and FPGA resources',8,3),
        ('Including the third sample without a gap',9,8),('FSM width warnings',10,2),
        ('Counter load, enable and data',10,5),('Wire versus reg',11,2),
        ('Shift-register reset',11,4),('Missing assignments and unintended latches',12,2),
        ('1101 recognizer: original explanation',12,5),('K-map OR versus arithmetic addition',13,2),
        ('SOP, POS and De Morgan',13,4),('Rule 90: do I need nextVal?',13,7),
        ('Rule 110 truth table and boundaries',13,9),('Timer: state, next_state or both?',14,11),
        ('Timer: one owner per register',14,7),('Complete timer and exact duration',14,12),
        ('LFSR tap positions versus bit indices',15,4),('LFSR nonblocking assignments and old q',15,11),
        ('Mt2015 schematic and board-port mapping',15,7),('Conway indexing and wrapped neighbors',16,2),
        ('Conway: old versus next generation',16,4),('LFSR definition, seed, taps, period and lockup',0,1),
        ('LFSR feedback forms and maximum-length conditions',0,2),('LFSR applications and clocked-state recap',0,3),
    ]
    previous_day=None
    for _,n,p in sorted(questions,key=lambda x:(mapping[x[1],x[2]]['day'],mapping[x[1],x[2]]['page'])):
        dest=mapping[n,p]
        label=QUESTIONS[n][p-(1 if n==0 else 2)]
        if dest['day']!=previous_day:
            text+=f"\n### Day {dest['day']}\n\n"
            previous_day=dest['day']
        text+=f"- {link_label(dest,label)} - p. {dest['page']}.\n"
    text+='\n## Find a tracker entry\n\n58 entries have discussion links. The 1101 explanation is intentionally revisited in the timer series; both locations are listed. Entries without a question remain in the tracker, without invented notes.\n\n| Entry | Problem | Tracker day | Answer location |\n|---:|---|---|---|\n'
    for n,loc in sorted(entries.items()):
        labels=[]
        for day in sorted({x['day'] for x in loc}):
            points=[x for x in loc if x['day']==day]; dest=points[0]
            labels.append(link_label(dest,f"Day {day}, pp. {compact([x['page'] for x in points])}"))
        if n==155:
            labels.insert(0,link_label(mapping[12,5],'Day 9, pp. 5-6 (earlier question)'))
        r=rows[n]
        text+=f"| {n} | [{r['problem']}]({r['url']}) | {r['day']} | {'; '.join(labels)} |\n"
    text+='''
## Sources and review records

The original 16 PDFs remain unchanged at their existing paths for compatibility and reproducibility; the ten day-wise files above are the primary reading set. No technical source page was discarded. Original PDF page references in historical appendices identify those retained sources unless explicitly updated to a day-wise destination.

The [Day 5 Markdown companion](HDLBits_Day5_Original_Submissions_Review.md) preserves the original discussion and dated submission appendix. The [review record](DOCUMENT_REVIEW.md) separates technical tests, platform evidence and document/navigation checks. The [posting plan](../LinkedIn_Attempt_2_Posting_Plan_and_Ideas.md) is a separate editorial proposal, not this reading-day index.
'''
    # Lead with the user's questions; the catalogue table is secondary.
    intro,rest=text.split('## Choose a day\n',1)
    days,rest=rest.split('## Find a question\n',1)
    qs,tail=rest.split('## Find a tracker entry\n',1)
    text=intro+'## Find a question\n'+qs+'\n## Choose a day\n'+days+'\n## Find a tracker entry\n'+tail
    (ROOT/'DOCUMENT_INDEX.md').write_text(text,encoding='utf-8')


def main():
    OUT.mkdir(parents=True,exist_ok=True); WORK.mkdir(parents=True,exist_ok=True)
    rows=tracker_rows()
    sources,mapping=prepare()
    entries=entry_mapping(mapping,rows)
    results=[build_day(d,sources,mapping,entries,rows) for d in DAYS]
    sources[0].save(WORK/'lfsr_reference.pdf',garbage=4,deflate=True)
    for src in sources.values():
        src.close()
    write_index(results,mapping,entries,rows)
    manifest=dict(version=1,source_baseline='64c6e8a',days=results,
        entries={str(n):loc for n,loc in entries.items()},
        body_pages=sum(len(r['provenance']) for r in results),
        original_body_pages=sum(len(m['pages']) for m in DOCS),
        total_pages=sum(r['pages'] for r in results))
    MANIFEST.write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in manifest.items() if k not in ('days','entries')},indent=2))
    print([(r['day'],r['pages'],r['front']) for r in results])


if __name__=='__main__':
    main()
