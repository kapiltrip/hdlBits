"""Rebuild covers and correct the Attempt 2 study PDFs without discarding figures.

Original PDFs are saved once in internal/tmp/document_review_20260907/originals.
The tracker is read only. Run with the local Python that provides PyMuPDF.
"""
from pathlib import Path
import sys, re, json, shutil, hashlib
sys.path.append(r'C:\Users\kapil\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\Lib\site-packages')
import fitz
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Preformatted, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT/'internal/tmp/document_review_20260907'
ORIG = WORK/'originals'
ORIG.mkdir(parents=True, exist_ok=True)
for p in ROOT.glob('*.pdf'):
    if not (ORIG/p.name).exists(): shutil.copy2(p, ORIG/p.name)
MD = ROOT/'HDLBits_Day5_Original_Submissions_Review.md'
if not (ORIG/MD.name).exists(): shutil.copy2(MD, ORIG/MD.name)
rows = json.loads((WORK/'tracker.json').read_text(encoding='utf-8'))
entries = {r['values'][0]:r['values'] for r in rows if isinstance(r['values'][0], int)}
links = {}
for n,v in entries.items():
    m=re.match(r'=HYPERLINK\("([^"]+)","([^"]+)"\)',str(v[4]))
    if m: links.setdefault(m[1],[]).append(n)
S=getSampleStyleSheet()
S.add(ParagraphStyle(name='Body', fontName='Helvetica', fontSize=10.2, leading=14.5, spaceAfter=8, textColor=colors.HexColor('#172333')))
S.add(ParagraphStyle(name='SmallText', parent=S['Body'], fontSize=8.2, leading=11))
S.add(ParagraphStyle(name='TableText', parent=S['Body'], fontSize=8, leading=10.6, spaceAfter=0))
S.add(ParagraphStyle(name='CodeText', fontName='Courier', fontSize=8.1, leading=10.6, spaceAfter=10, backColor=colors.HexColor('#f1f4f7'), borderPadding=7))
S['Title'].fontName='Helvetica-Bold'; S['Title'].fontSize=25; S['Title'].leading=30; S['Title'].alignment=0
S['Title'].textColor=colors.HexColor('#002060')
S['Heading2'].textColor=colors.HexColor('#002060'); S['Heading2'].spaceBefore=12
S['Heading2'].keepWithNext=True;S['Heading3'].keepWithNext=True
S['Body'].allowWidows=0;S['Body'].allowOrphans=0

def p(t,style='Body'): return Paragraph(escape(t),S[style])
def code(t): return Preformatted(t.strip('\n'),S['CodeText'])
def table(rows,widths=None):
    cells=[[p(str(c),'TableText') for c in row] for row in rows]
    t=Table(cells,colWidths=widths,repeatRows=1,hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#D9E1F2')),('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,0),.6,colors.HexColor('#002060')),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f5f7fa')]),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
    return t
def build(path,story,label='HDLBits Attempt 2',offset=0):
    def footer(c,d):
        c.setFont('Helvetica',8); c.setFillColor(colors.HexColor('#566579'))
        c.drawString(48,25,label); c.drawRightString(A4[0]-48,25,str(d.page+offset))
    SimpleDocTemplate(str(path),pagesize=A4,rightMargin=48,leftMargin=48,topMargin=48,bottomMargin=46).build(story,onFirstPage=footer,onLaterPages=footer)
def page(title,items,path,offset=0):
    build(path,[p(title,'Title'),Spacer(1,10)]+items,offset=offset)
    d=fitz.open(path)
    assert len(d)==1,(title,len(d))
    d.close()

META={
'HDLBits_Combined_Questions_and_Day2_Review.pdf':('Loops, muxes and storage', 'Use these notes to connect the Verilog you wrote to the circuit it describes. The examples cover vector loops, carry wiring, population count, mux selection, operators, falling-time counters and latches.', [('3-6','Generate and procedural loops; vector reversal, carry wiring and population count'),('7','Mux operators and the two levels of a 4-to-1 mux'),('8','Resetting the Lemmings fall counter and handling long falls'),('9-12','Reset types, operator choices and intentional latch storage')]),
'HDLBits_Day4_Questions_Vector_DFF_PS2.pdf':('Bytes, flip-flops and PS/2 packets', 'These three questions are about choosing the right bits and storing them at the right edge. Start with the byte-slice trace, then follow the PS/2 packet through its three writes.', [('2-3','Entry 67: indexed part-selects and byte reversal'),('3','Entry 66: the D input needed for the next Q value'),('4-6','Entry 70: byte capture, register ownership and the done pulse')]),
'HDLBits_Day6_Non_FSM_QA_Dualedge_and_Circuit5.pdf':('Dual-edge sampling and Circuit5', 'Two edge-triggered registers hold samples from different moments. The Dualedge explanation shows how to select the newest one, then explains the timing limits of that circuit in an FPGA. Circuit5 shows how to infer a mux from a waveform.', [('2-4','Why OR loses the newest value; clock-selected mux solution'),('5-14','FPGA DDR resources, half-cycle timing, glitches and XOR startup'),('15-17','Circuit5 selector mapping and case statements'),('18-19','Simulation checks, sources and revision questions')]),
'HDLBits_Day7_QA_FSM_Warnings_and_Counter_Interface.pdf':('FSM widths and counter connections', 'The width warnings come from assigning wide constants to one-bit outputs. The counter question is about following a signal through a parent module and its child instance. Both become easier when you write down each signal\'s width and driver.', [('2-3','Entry 102: Quartus truncation warnings and Y0 decoding'),('4','Entry 107: simplifying Y2 next-state logic'),('5','Entry 109: Q, c_enable, c_load and c_d'),('6-7','Short reviews of entries 99-110 and source links')]),
'HDLBits_Entry80_Moore_Serial_Twos_Complement_Deep_Dive.pdf':("Moore serial two's complement", 'Read the input from the least-significant bit. Copy zeros and the first one, then invert every later bit. The three Moore states remember both where you are in that rule and which output bit should be visible.', [('2','Why copy-through-first-one equals invert-plus-one'),('3-4','Why three states are needed and where every transition goes'),('5-7','Clock timing, complete code and the Mealy comparison'),('8','Mistakes, worked checks and recall questions')]),
'HDLBits_Entry90_Exams_2014_Q3FSM_Three_Sample_Window_Deep_Dive.pdf':('Counting three-sample groups', 'After s starts the controller, take three w samples per group without a gap. At the third edge, add the current w to the two samples already counted. Then reset the group counters whether the result matches or not.', [('2-3','Start edge, sample numbering and a 101 trace'),('4-8','The loop mistake, gap cycle and misplaced resets'),('9-10','Defaults and the corrected two-state controller'),('11-12','All eight groups, back-to-back checks and sources')]),
'HDLBits_Fsm_hdlc_Mealy_to_Moore_Deep_Dive.pdf':('HDLC: getting the output cycle right', 'The first detector recognized the patterns but lost its discard and flag pulses at the sampling edge. The working Moore machine stores each completed event in a separate state, so its output stays high for the following cycle.', [('2-7','Pattern timing and why the first two output approaches fail'),('8-12','The ten states, overlapping input bits and clock-by-clock traces'),('13-16','Reference-model checks and both source excerpts')]),
'HDLBits_Fsm_serialdata_For_Loops_vs_Clock_Cycles.pdf':('Serial input needs real clock edges', 'A for loop runs through its statements when the process wakes up. It cannot wait for the next serial bit by changing its loop index. Use stored state and a bit counter to capture one bit on each data edge.', [('2-5','What the original loop does in one edge and the simulation result'),('6-7','Indexed capture, right shifting and an eight-bit trace'),('8-9','Related exercises and references'),('10-11','Start/stop recovery and odd-parity timing')]),
'HDLBits_Recovered_Code_Questions_54_74_75_77.pdf':('States, sampled edges and operators', 'These notes answer four comments from your earlier submissions. Each question is kept beside its explanation so you can connect the fix to what you were trying to do.', [('2','Entry 54: why the water-level controller needs history'),('3','Entry 74: comparing consecutive rising-edge samples'),('4','Entry 75: making asynchronous reset wake the block'),('5-6','Entry 77: reduction, bitwise and logical operators')])}

def make_cover(name):
    title,intro,contents=META[name]
    nums=links[name]
    days=sorted(set(entries[n][1] for n in nums))
    story=[p('HDLBits Attempt 2','SmallText'),Spacer(1,14),p(title,'Title'),Spacer(1,9),p(intro),Spacer(1,14),p('Where this fits in your sheet','Heading2'),p('Entries '+', '.join(map(str,nums))+'.  '+', '.join(days)+'.'),p('Entry numbers follow the tracker. Day labels in older filenames refer to when the notes were written; use the entry numbers to find the matching problem.','SmallText'),Spacer(1,10),table([['Pages','What to read']]+contents,[48,451])]
    if 'Entry80' in name:
        story += [p('Your question','Heading2'),code('// explain me this code in a deep manner, along with need of each state\n// ik the meaning and need of states s0, s1, s2 ... rest, explain me in doc')]
    story += [Spacer(1,14),p('Reviewed against the saved tracker and available code on 7 September 2026. Earlier submission dates inside these notes are historical records.','SmallText')]
    path=WORK/(Path(name).stem+'_cover.pdf'); build(path,story)
    assert len(fitz.open(path))==1,name
    return path

# Shorter headings and direct wording. Original quoted comments and code stay intact.
PHRASES={
'Core mental model':'Key idea', 'The one-sentence diagnosis':'What went wrong',
'Important refinement':'How the loop runs', 'Binary-address mental model':'Read the selector as an address',
'Evidence boundary':'What was checked', 'Direct answer':'Answer', 'Short answer':'Answer',
'Final answer status':'Questions covered', 'Final answer to the submitted question':'Why the states are needed',
'A semantically named SystemVerilog version makes the proof visible in the code:':'Here is the same SystemVerilog design with names that describe each state:',
'Deep state-partition insight':'Why these states stay separate',
'The central nuance':'Why Moore?',
'Why the outputs are now genuinely Moore':'Why these outputs are Moore',
'A compact mathematical oracle':'A run-length reference model',
'This mental model explains the waveform without blaming the simulator.':'Follow the evaluation order below to see when the output changes.',
'Most valuable rename':'Clearer state names',
'A compact design recipe for similar FSM problems':'How to work through a similar FSM',
'The strongest direct vendor statement':'What the vendor documentation says',
'Important correction to the chat':'Why the XOR version needs initialization',
'Algebraically elegant, but the two registers need known initial values.':'Both registers need known initial values.',
'progress frontier':'completed range', 'genuinely one-hot':'one-hot',
'Q&A;':'Q&A', 'Q&A.;':'Q&A.', 'verified study record':'study notes',
'clock contract':'clock sequence', 'clocked contract':'clock sequence',
'temporal position':'bit position', 'temporal RTL patterns':'RTL capture patterns',
'spatial loop and temporal counter':'single-edge loop and clocked counter',
'Mental-model mismatch':'Why the loop cannot wait',
'A scalable tracker rule':'The three linked exercises',
'Do not collapse completion and verification':'Progress and local checks',
'Reduction NOR':'Two-input NOR',
}

CUSTOM={
('HDLBits_Combined_Questions_and_Day2_Review.pdf',4,'The saved successful solution is a direct structural use'):'Each loop iteration creates one full adder. carry is a wire because it connects continuously driven module outputs to inputs; it stores no clocked value. There are 101 carry nodes: the carry-in plus one output from each of the 100 stages.',
('HDLBits_Fsm_serialdata_For_Loops_vs_Clock_Cycles.pdf',7,'For each solved problem, record four distinct facts:'):'The tracker links entries 2, 4 and 6 to this PDF. They share the same capture sequence: a start bit, eight data edges, and a stop check. Entry 6 adds a parity edge before the stop bit. Pages 10-11 show that timing.',
('HDLBits_Fsm_serialdata_For_Loops_vs_Clock_Cycles.pdf',7,"'Solved' is Kapil's activity record."):'The tracker records your progress. The local tests check the examples saved here. A passing example is useful for understanding the fix, but it does not mean every historical submission was rerun.',
('HDLBits_Fsm_serialdata_For_Loops_vs_Clock_Cycles.pdf',4,'This simulation verifies the language-level behavior'):'This test checks the loop and counter examples shown here. The complete original serial-receiver submission is not saved locally, so this is not a rerun of that submission.',
('HDLBits_Entry90_Exams_2014_Q3FSM_Three_Sample_Window_Deep_Dive.pdf',1,'Minimal-state interpretation'):'Two controller states\nA waits for s; B keeps sampling. The counters and zreg also store state. This is a two-state controller plus a datapath; the complete circuit has more than two possible stored configurations.',
('HDLBits_Entry90_Exams_2014_Q3FSM_Three_Sample_Window_Deep_Dive.pdf',2,"The expression count + {1'b0, w} is not a workaround"):'On the third edge, count contains the ones in the first two samples. Adding the current w gives the total for all three, which is the value the result test needs.',
('HDLBits_Entry90_Exams_2014_Q3FSM_Three_Sample_Window_Deep_Dive.pdf',4,'The next attempt correctly introduced'):'Adding ticks tracks separate edges. Two functional errors remain: count increments for zero inputs, and s2 skips an input. The repeated assignments also make those errors harder to see.',
('HDLBits_Entry90_Exams_2014_Q3FSM_Three_Sample_Window_Deep_Dive.pdf',5,'Bug 2: duplicate ticks assignments do not increment twice'):'Cleanup: duplicate ticks assignments do not increment twice',
('HDLBits_Entry90_Exams_2014_Q3FSM_Three_Sample_Window_Deep_Dive.pdf',5,'Bug 4: duplicated resets hide the real control boundary'):'Cleanup: repeated resets hide where the group ends',
('HDLBits_Recovered_Code_Questions_54_74_75_77.pdf',5,'All four previously missed code-comment questions'):'The four questions are answered on pages 2-5. The water-level snippet shows the state/history idea; it is not a complete solution. The other three examples are covered by the saved Day 5 testbench.',
('HDLBits_Recovered_Code_Questions_54_74_75_77.pdf',1,'If the supplemental-flow output depends'):'In this problem, dfr remembers whether the level last moved down or up while it stays in a middle band. The same sensor pattern can therefore need different dfr values. Separate states preserve that history.',
('HDLBits_Day4_Questions_Vector_DFF_PS2.pdf',1,'The one-line rule'):'Choose one byte on each side',
('HDLBits_Day4_Questions_Vector_DFF_PS2.pdf',2,'Fast debugging cues'):'Check the slice indices and widths',
('HDLBits_Day6_Non_FSM_QA_Dualedge_and_Circuit5.pdf',1,'The eight completed Chrome tabs correspond'):'Entries 87 and 89 are on Day 5 in the tracker. This file kept the Day 6 title from its original review date. Entry 90 has its own FSM PDF; the table below shows the surrounding problems.',
('HDLBits_Day6_Non_FSM_QA_Dualedge_and_Circuit5.pdf',1,'The supplied tab-strip image is completion context'):'For the FPGA question, distinguish what simulates, what synthesizes, which device resources exist, and whether the implemented circuit meets timing.',
('HDLBits_Day7_QA_FSM_Warnings_and_Counter_Interface.pdf',4,'The provided counter gives'):'The provided counter checks load before enable. Reset therefore loads 1 even with enable low. At Q=12, wrapping needs enable=1; otherwise Q holds 12. The next-state equations use the value before the edge.',
('HDLBits_Day8_QA_Wire_Reg_and_Shift_Reset.pdf',0,'Entry 129: why cannot these wires be reg?'):'Entry 129: why can\'t these wires be reg?',
('HDLBits_Day8_QA_Wire_Reg_and_Shift_Reset.pdf',3,'Assigning the same register in two independent branches'):'Keep the seconds update in one place. Within the same clocked process, if two nonblocking assignments to second execute, the later one wins. Across separate processes, conflicting writes can race and create multiple drivers.',
}

changes=[]
def replace_blocks(doc,name):
    for pi,pg in enumerate(doc):
        if pi==0 and name in META: continue
        pending=[]
        dark_rects=[d['rect'] for d in pg.get_drawings() if d.get('fill') and sum(d['fill'][:3])<.7]
        for b in pg.get_text('dict')['blocks']:
            if b['type']!=0: continue
            spans=[s for l in b['lines'] for s in l['spans']]
            flat=' '.join(' '.join(s['text'] for s in l['spans']) for l in b['lines'])
            norm=' '.join(flat.split())
            custom=next((v for (nm,pn,start),v in CUSTOM.items() if nm==name and pn==pi and norm.startswith(start)),None)
            if custom is not None:
                rect=fitz.Rect(b['bbox'])
                if rect.width<350 and len(norm)<110: rect.x1=pg.rect.width-48
                pending.append((rect,spans,custom,norm))
            else:
                for s in spans:
                    old=s['text']; new=old
                    # Do not alter literal evidence/code except the malformed Q&A label.
                    if 'Courier' not in s['font'] and 'Mono' not in s['font']:
                        for a,z in PHRASES.items(): new=new.replace(a,z)
                    if new!=old: pending.append((fitz.Rect(s['bbox']),[s],new,old))
                    elif s['color']!=0xffffff and any(rect.contains(fitz.Rect(s['bbox']).tl+(fitz.Rect(s['bbox']).br-fitz.Rect(s['bbox']).tl)*.5) for rect in dark_rects):
                        white={**s,'color':0xffffff}
                        pending.append((fitz.Rect(s['bbox']),[white],old,old+' [unreadable header color]'))
        if name=='HDLBits_Day8_QA_Wire_Reg_and_Shift_Reset.pdf' and pi==0:
            rect=fitz.Rect(46,77,547,125)
            pending.append((rect,[{'font':'Helvetica','size':9.5,'color':0x34465b}], 'Entries 123, 127 and 129 are Done in the tracker. These notes cover wire and reg, shift-register reset, and BCD clock rollover. Entry 123 is on Day 7; entries 127 and 129 are on Day 8. Reviewed 7 September 2026.', 'old and overlaid status paragraphs'))
        for rect,spans,new,old in pending:
            pg.add_redact_annot(rect,fill=False)
        if not pending: continue
        pg.apply_redactions(images=0,graphics=0)
        for rect,spans,new,old in pending:
            s=spans[0]; font='hebo' if ('Bold' in s['font']) else 'helv'
            rgb=tuple(((s['color']>>shift)&255)/255 for shift in (16,8,0))
            size=s['size']
            # Keep replacements within the original paragraph/cell. Short labels may grow
            # into otherwise empty space only up to the original width plus 2 points.
            box=fitz.Rect(rect.x0,rect.y0,rect.x1+2,rect.y1+2)
            if len(spans)>1: box.x1=min(pg.rect.width-48,max(box.x1,rect.x0+400))
            if len(spans)==1 and 'origin' in s and '\n' not in new:
                while fitz.get_text_length(new,fontname=font,fontsize=size)>box.width and size>s['size']*.77:
                    size-=.15
                if fitz.get_text_length(new,fontname=font,fontsize=size)<=box.width:
                    pg.insert_text(s['origin'],new,fontname=font,fontsize=size,color=rgb)
                    changes.append({'file':name,'page':pi+1,'before':old,'after':new,'font_size':round(size,2)})
                    continue
            while size>=max(6,s['size']*.77):
                shape=pg.new_shape()
                spare=shape.insert_textbox(box,new,fontname=font,fontsize=size,color=rgb,lineheight=1.12)
                if spare>=0:
                    shape.commit(); break
                size-=.2
            else: raise RuntimeError((name,pi+1,new,rect))
            changes.append({'file':name,'page':pi+1,'before':old,'after':new,'font_size':round(size,2)})

def swap_page(doc,index,path):
    with fitz.open(path) as other:
        assert len(other)==1
        doc.delete_page(index); doc.insert_pdf(other,start_at=index)

def combined_mux():
    path=WORK/'mux_page.pdf'
    page('6. Mux operators and selectors',[
        p('Entry 13: keep the whole eight-bit value','Heading2'),
        p('The HDLBits mux selects a when sel=0 and b when sel=1. Repeat sel eight times to make an eight-bit mask. Bitwise AND and OR then select every bit of the chosen bus. Logical operators would reduce each bus to a one-bit truth value.'),
        code("assign out = ({8{~sel}} & a) | ({8{sel}} & b);\n// The conditional form is shorter:\nassign out = sel ? b : a;"),
        table([['sel','a mask result','b mask result','out'],['0','a','0','a'],['1','0','b','b']],[48,155,155,141]),
        p('Entry 29: build the four-way mux in two levels','Heading2'),
        p('Use sel[0] in both first-level muxes. It chooses within the a/b pair and within the c/d pair. Then sel[1] chooses which pair reaches out. The intermediate signals must be eight bits wide.'),
        code('wire [7:0] lower_pair, upper_pair;\nmux2 m0(sel[0], a, b, lower_pair);\nmux2 m1(sel[0], c, d, upper_pair);\nmux2 m2(sel[1], lower_pair, upper_pair, out);'),
        table([['sel[1:0]','00','01','10','11'],['out','a','b','c','d']],[99,100,100,100,100]),
        p('If the pair outputs were single-bit wires, most of each bus would be lost before the final mux. Distinct instance names also avoid the name collisions in the supplied buggy code.'),
        p('Sources: https://hdlbits.01xz.net/wiki/Bugs_mux2 and https://hdlbits.01xz.net/wiki/Bugs_mux4','SmallText')],path,6)
    return path

def lemmings_page():
    path=WORK/'lemmings_page.pdf'
    page('7. Reset the counter when a fall ends',[
        p('Entry 7: why is another reset unnecessary?','Heading2'),
        p('On the landing edge, the current state still describes the fall. The next-state logic can use the old fall count to choose walking or splatter while the clocked block schedules count back to zero. The reset takes effect after the decision, so the measured length is still available when it is needed.'),
        table([['Moment','Count use','Count update'],['Falling','Measure consecutive falling cycles','Increment, with saturation'],['Landing','Use old count to decide survival','Clear for a later fall'],['Reset','Discard the old measurement','Clear immediately'],['Splattered','Count no longer affects behavior','Death remains permanent']],[85,237,177]),
        p('Two details the earlier excerpt left out','Heading2'),
        p('A five-bit counter wraps after 31. A long fall could then look short, so stop incrementing once the counter reaches 21. The task distinguishes falls of at most 20 cycles from falls longer than 20; it does not need the exact length after that threshold.'),
        p('Also decide which edge counts the first falling cycle. The monitor below includes the first edge with ground=0, including the edge that leaves walking or digging. A design that increments only while already in a falling state must account for that different starting point.'),
        code("// Fall-length monitor; combine with the existing movement FSM.\nalways @(posedge clk or posedge areset) begin\n    if (areset)\n        count <= 5'd0;\n    else if (ground)\n        count <= 5'd0;\n    else if (count < 5'd21)\n        count <= count + 5'd1;\nend\n// While in a falling state, on landing:\n// next_state = (count > 5'd20) ? SPLATTER : WALK_SAVED_DIR;"),
        p('SPLATTER must remain terminal until reset. Clearing the counter does not revive the lemming. With this counting convention, 20 low-ground samples followed by landing survive; 21 or more splatter.'),
        p('This is a counter fragment, not a complete Lemmings4 submission. Source: https://hdlbits.01xz.net/wiki/Lemmings4','SmallText')],path,7)
    return path

def serial_appendix():
    a=WORK/'serial_frame.pdf'
    page('9. Follow a complete serial frame',[
        p('Entries 2 and 4: start, data and stop','Heading2'),
        p('While idle, a sampled 0 starts a frame. That edge is the start bit, so it must not also write data bit 0. Capture bit 0 on the next rising edge and bit 7 on the eighth data edge. The following edge checks the stop bit.'),
        table([['Edge','Input meaning','Action'],['Start','0','Enter DATA; set bit index to 0'],['Next 8 edges','b0 through b7, LSB first','Capture one bit per edge'],['Stop','Must be 1','Pulse done if the frame is valid'],['Following edge','Possible next start bit','Return to start detection without losing a back-to-back frame']],[76,150,273]),
        p('What happens when the stop bit is missing?','Heading2'),
        p('If the stop sample is 0, suppress done and wait for a sampled 1. Zeros during this recovery period are still part of the malformed frame; do not treat each one as a new start. Once a 1 has restored idle framing, a later sampled 0 may start a new frame.'),
        p('When can out_byte be read?','Heading2'),
        p('Read it while done is high. The eight writes have finished before the stop edge, so the assembled byte is ready when that edge validates the frame. The exercise does not require out_byte to be meaningful while done=0.'),
        p('The x values on page 7 mark positions that have not yet been captured in that example. With the reset-to-zero code on page 6, those positions would contain zero instead. The bit order and final byte are the same.'),
        p('Sources: https://hdlbits.01xz.net/wiki/Fsm_serial and https://hdlbits.01xz.net/wiki/Fsm_serialdata','SmallText')],a,9)
    b=WORK/'serial_parity.pdf'
    page('10. Add odd parity at the right edge',[
        p('Entry 6: one more sample before the stop bit','Heading2'),
        p('Odd parity means the XOR of the eight data bits and the parity bit is 1. Reset the parity accumulator at the start boundary, include all eight data samples, and include the parity sample. The stop bit must not affect the value used for this check.'),
        code("// Meaning: parity_total contains the XOR accumulated so far.\n// Clear it before data bit 0. During DATA and PARITY:\nparity_total <= parity_total ^ in;\n// At the following STOP edge, the old value includes parity:\n// valid_frame = in && parity_total;"),
        p('The snippet shows the timing rule. In the HDLBits exercise, connect the provided parity module and choose its reset timing to implement that rule. Its accumulator toggles on each sampled 1, so inspect its old output at the stop edge before that edge can include the stop bit.'),
        table([['Stage just completed','What the stored XOR contains'],['Start','0'],['Data bit 0','b0'],['Data bit 7','b0 XOR b1 XOR ... XOR b7'],['Parity bit','All eight data bits XOR parity'],['Stop test','Use the stored nine-bit XOR; require stop=1']],[140,359]),
        p('For byte A6, the data has four ones. A parity bit of 1 makes five, so it is valid. A parity bit of 0 makes four, so done must stay low. In both cases a valid stop bit ends the frame. A zero stop bit uses the framing-error recovery from page 10.'),
        p('If you check parity_total in the same block activation that captures the parity bit, it still contains only the eight data bits. Either test parity_total ^ in at that edge, or wait until the stop edge and test the stored value. Mixing these two conventions causes a one-bit timing error.'),
        p('Source: https://hdlbits.01xz.net/wiki/Fsm_serialdp','SmallText')],b,10)
    return [a,b]

def edit_pdfs():
    for path in sorted(ORIG.glob('*.pdf')):
        name=path.name
        if name not in META and 'Day8_QA' not in name: continue
        doc=fitz.open(path)
        replace_blocks(doc,name)
        if name in META: swap_page(doc,0,make_cover(name))
        if 'Combined_Questions' in name:
            swap_page(doc,6,combined_mux()); swap_page(doc,7,lemmings_page())
        if 'Fsm_serialdata' in name:
            for ap in serial_appendix():
                with fitz.open(ap) as ad: doc.insert_pdf(ad)
        doc.set_metadata({**doc.metadata,'subject':'Attempt 2 study notes reviewed against tracker, 7 September 2026'})
        staging=WORK/name; doc.save(staging,garbage=4,deflate=True);doc.close()
        shutil.copy2(staging,ROOT/name)
    (WORK/'edits.json').write_text(json.dumps(changes,indent=2),encoding='utf-8')

def inline(text):
    text=escape(text)
    text=re.sub(r'`([^`]+)`',r'<font face="Courier">\1</font>',text)
    text=re.sub(r'\*\*([^*]+)\*\*',r'<b>\1</b>',text)
    def link(m):
        label,url=m.groups()
        if url.startswith('https://'): return '<link href="'+url+'" color="#0563C1">'+label+'</link>'
        return label
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,text)

def split_row(line):
    cells=[]; buf=''; quoted=False
    for c in line.strip().strip('|'):
        if c=='`': quoted=not quoted
        if c=='|' and not quoted: cells.append(buf.strip());buf=''
        else: buf+=c
    cells.append(buf.strip());return cells

def markdown_pdf(md,path):
    story=[];lines=md.splitlines();i=0
    while i<len(lines):
        line=lines[i];i+=1
        if not line.strip(): continue
        if line.startswith('```'):
            chunk=[]
            while i<len(lines) and not lines[i].startswith('```'): chunk.append(lines[i]);i+=1
            i+=1;story.append(KeepTogether([code('\n'.join(chunk))]));continue
        if line.startswith('|'):
            group=[split_row(line)]
            while i<len(lines) and lines[i].startswith('|'):
                if not re.match(r'^\|[\s:|\-]+\|$',lines[i]):group.append(split_row(lines[i]))
                i+=1
            count=len(group[0]);assert all(len(r)==count for r in group),group
            widths=([25,94,105,105,43,127] if count==6 else [499/count]*count)
            cells=[[Paragraph(inline(x),S['TableText']) for x in row] for row in group]
            t=Table(cells,colWidths=widths,repeatRows=1,hAlign='LEFT')
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#D9E1F2')),('VALIGN',(0,0),(-1,-1),'TOP'),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f5f7fa')]),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
            story.extend([t,Spacer(1,9)]);continue
        if line.startswith('#'):
            level=len(line)-len(line.lstrip('#'))
            if 'Historical submission records' in line: story.append(PageBreak())
            style='Title' if level==1 else ('Heading2' if level==2 else 'Heading3')
            story.append(Paragraph(inline(line.lstrip('#').strip()),S[style]));continue
        if line.startswith('>'):line=line.lstrip('> ').strip()
        if line.startswith('- '):line='- '+line[2:]
        while i<len(lines) and lines[i].strip() and not re.match(r'^(#|\||>|-|```)',lines[i]):line+=' '+lines[i];i+=1
        story.append(Paragraph(inline(line),S['Body']))
    build(path,story,'Attempt 2 - Day 5 questions and submission notes')

def day5_pdf():
    md=(ORIG/MD.name).read_text(encoding='utf-8')
    end=md.index('## Previously documented questions')
    md='''# Day 5 questions and submission notes

This review explains the saved code for entries 81-85 and keeps the earlier questions for entries 54, 74, 75, 77 and 80 nearby. The submission records at the end were collected on 2-3 September 2026. They describe that checkpoint; the tracker holds the current progress.

Entries 81-85 are all Done in the tracker. The main fixes are Boolean OR, the two padding bits in a concatenation, sticky edge capture, the ring/vibrate condition, and one-hot Mealy state encoding. Entry 80 has its own detailed Moore explanation.

The [PDF version](HDLBits_Day5_Original_Submissions_Review.pdf) contains this review and its historical submission table. The existing tracker links still open this Markdown version.

The saved records show success through entry 93 at the original checkpoint. Entries 86-93 were confirmed by Kapil on 3 September. A matching tab alone does not show that its current editor contents pass; later experiments can differ from an earlier successful submission.

'''+md[end:]
    replaces={
    'Previously documented questions confirmed against the original code':'Earlier questions and where to read them',
    'Newly recovered question 1 -':'Question 1 -', 'Newly recovered question 2 -':'Question 2 -',
    'Newly recovered question 3 -':'Question 3 -', 'Newly recovered question 4 -':'Question 4 -',
    'Current Day 5 original submissions - entries 80 through 85':'Submission notes for entries 80-85',
    'Chrome evidence appendix':'Historical submission records',
    'Day 6 completion follow-up - entries 86 through 93':'The 3 September follow-up: entries 86-93',
    'A genuinely one-hot, fully assigned implementation is:':'Here is a one-hot implementation with every combinational output assigned:',
    'The latest successful code follows this rule, includes a `default` transition for illegal-state recovery, and now has a fresh Attempt 2 success.':'The saved successful code follows this rule and includes a `default` transition for the unused state encoding.',
    'The original problem explicitly says to use one-hot encoding.':'The problem asks for one-hot encoding.',
    'exactly and does not claim unseen success timestamps':'without adding submission timestamps',
    'records the exact evidence available in the follow-up and avoids inventing an unseen timestamp':'records Kapil\'s confirmation rather than a submission time',
    'a safe coding pattern is:':'this fragment shows the idea (it is not a complete submission):',
    'A safe coding pattern is:':'This fragment shows the idea (it is not a complete submission):',
    }
    for a,b in replaces.items():md=md.replace(a,b)
    # Repair stale cross-references: the combined PDF page numbers match sections.
    md=md.replace('[Combined questions PDF](HDLBits_Combined_Questions_and_Day2_Review.pdf), section 7','[Combined questions PDF](HDLBits_Combined_Questions_and_Day2_Review.pdf), page 8')
    md=md.replace('[Day 4 questions PDF](HDLBits_Day4_Questions_Vector_DFF_PS2.pdf), section 1','[Day 4 questions PDF](HDLBits_Day4_Questions_Vector_DFF_PS2.pdf), pages 2-3')
    md=md.replace('Entries 1 through 93 are now Done. Entries 94-178 remain Pending and were not part of this follow-up; no current-window submission claim is made for them.','At the 3 September checkpoint, entries 1-93 were Done and entries 94-178 had not yet been included in the review. Those are historical counts. On 7 September, the tracker records 151 Done and 27 Pending.')
    MD.write_text(md,encoding='utf-8')
    markdown_pdf(md,ROOT/MD.with_suffix('.pdf').name)

if __name__=='__main__':
    edit_pdfs()
    day5_pdf()
    print('Updated ten PDFs; paragraph/label edits:',len(changes))
