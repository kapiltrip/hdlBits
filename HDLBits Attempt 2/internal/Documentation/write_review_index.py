from pathlib import Path
import sys,json,re,hashlib,collections
sys.path.insert(0,str(Path(__file__).parent))
import review_documents as r
ROOT=r.ROOT;WORK=r.WORK
nums=sorted(r.entries)
assert nums==list(range(1,179))
counts=collections.Counter(v[3] for v in r.entries.values())
assert counts=={'Done':151,'Pending':27}
assert sum(map(len,r.links.values()))==43
assert all((ROOT/name).exists() for name in r.links)
assert hashlib.sha256((ROOT/'HDLBits_Attempt_2_Tracker_Simple.xlsx').read_bytes()).hexdigest()=='1d36251348aeb7851478ac0d56c5a4533d8f8cd67b1238b52b2e1fed4f4dad15'
assert sum(v[4]=='No questions asked' for v in r.entries.values())==108
locations={2:'2-9; frame timing 10',4:'2-9; frame timing 10',6:'10-11',7:'8',13:'7',19:'2, 9',20:'2, 9',21:'2, 9',22:'2, 9',23:'3-4',24:'2, 9',25:'2, 9',26:'3, 6',27:'2, 9',28:'2, 9',29:'7',30:'5',31:'10',36:'11',38:'12',54:'2',66:'3',67:'2-3',70:'4-6',74:'3',75:'4',77:'5',80:'2-8',87:'3-14',89:'15-17',90:'2-12',102:'2-3',107:'2, 4',109:'5',123:'4-5',127:'3',129:'1-2'}
audit='''# Attempt 2 document review

Reviewed on 7 September 2026 against the saved tracker, all ten existing PDFs, the Day 5 Markdown review, the available Verilog and testbenches, and the relevant HDLBits problem statements.

The tracker has 178 entries: 151 Done and 27 Pending. All 43 document links resolve to existing files and lead to material for the matching entry. Of these links, 38 open PDFs and five open the Day 5 Markdown review. A PDF version of that review is now available too. The remaining 108 completed entries say `No questions asked`; the 27 pending entries do not require invented question notes.

The workbook was not edited. Its contents and file hash are unchanged from the start of this review.

## Corrections and additions

- Corrected the entry 13 mux polarity: `sel=0` selects `a`, and `sel=1` selects `b`. Updated the code and truth table together.
- Expanded entry 30's explanation of why carry signals are wires, and corrected the Norgate row's description to two-input NOR.
- Replaced the incomplete Lemmings counter excerpt with a clearly labeled monitor that counts the first falling cycle and saturates at 21. The explanation covers 20/21-cycle landing behavior and long falls.
- Added two serial-receiver pages covering start/stop timing, missing-stop recovery, byte validity, odd parity, and the accumulator value seen at the stop edge.
- Removed the hidden obsolete Day 8 paragraph saying entry 123 was unfinished. Clarified that last-assignment priority applies within one process; competing processes can race.
- Explained that entry 90 has two controller states plus counter/output memory. Separated functional errors from redundant assignments.
- Replaced dated progress summaries on PDF covers with entry references and reading guides. Kept historical submission records labeled by date.
- Made introductions, headings and explanations more natural while preserving original quoted questions, useful code, diagrams and timing tables.
- Added the Day 5 PDF, repaired unreadable table headers, and checked page breaks and layout.

## Where each linked entry is answered

Page numbers below refer to the revised PDFs. Day numbers come from the tracker, which may differ from a PDF's older filename.

| Entry | Sheet day | Problem | Document | Pages or section |
|---:|---|---|---|---|
'''
for n,v in sorted(r.entries.items()):
    target=next((f for f,ns in r.links.items() if n in ns),None)
    if not target:continue
    title=re.match(r'=HYPERLINK\("[^"]+","([^"]+)"\)',v[2]).group(1)
    if target.endswith('.md'):
        dest=target.replace('.md','.pdf');label='Day 5 review (PDF; Markdown still linked from sheet)';where=f'Entry {n} section'
    else:
        dest=target;label=r.META.get(target,('Wire, reg and reset',))[0];where=('2-16' if n==8 else locations[n])
    audit+=f'| {n} | {v[1]} | {title} | [{label}]({dest}) | {where} |\n'
audit+='''
## What was tested

The saved Icarus tests passed for entries 74, 75, 77, 80-85, 87, 89 and 90. The HDLC source passed 1,022 post-edge reference checks. The serial-loop test reproduced the original one-edge failure and checked the eight-edge capture. The original Mealy trace reproduced the early discard pulse.

Additional tests used code extracted from the revised PDFs: 131,072 mux selections, 1,000 randomized byte reversals, 100 back-to-back PS/2 packets, a full 86,400-second clock cycle with reset/enable checks, and falls from 19 through 70 cycles. Odd-parity arithmetic was checked for all 256 bytes and both parity choices.

These are local RTL/example checks. Complete historical submissions are not saved for every tracker entry, so this review does not claim to have rerun all 151 completed problems or searched unsaved editor comments. The water-level snippet is conceptual. Vendor DDR examples still require the selected device's libraries and timing constraints for implementation checks.

## Sources for the corrections

- [HDLBits two-input mux](https://hdlbits.01xz.net/wiki/Bugs_mux2) and [four-input mux](https://hdlbits.01xz.net/wiki/Bugs_mux4).
- [Lemmings 4](https://hdlbits.01xz.net/wiki/Lemmings4).
- [Serial receiver](https://hdlbits.01xz.net/wiki/Fsm_serial), [datapath](https://hdlbits.01xz.net/wiki/Fsm_serialdata), and [parity](https://hdlbits.01xz.net/wiki/Fsm_serialdp).
- [BCD clock](https://hdlbits.01xz.net/wiki/Count_clock), [counter 1-12](https://hdlbits.01xz.net/wiki/Exams/ece241_2014_q7a), and [water-level FSM](https://hdlbits.01xz.net/wiki/Exams/ece241_2013_q4).

The edge-detector example was checked against [the official 8-bit interface](https://hdlbits.01xz.net/wiki/Edgedetect) and kept at its correct width.
'''
(ROOT/'DOCUMENT_REVIEW.md').write_text(audit,encoding='utf-8')
old=(ROOT/'README.md').read_text(encoding='utf-8')
backup=WORK/'originals/README.md'
if not backup.exists():backup.write_text(old,encoding='utf-8')
evidence=old.split('## Evidence boundary\n')[-1].strip()
text='''# HDLBits Attempt 2

Use the [tracker](HDLBits_Attempt_2_Tracker_Simple.xlsx) for problem order and progress. The notes below explain the questions and mistakes from this pass.

As of 7 September 2026, the sheet records **151 Done and 27 Pending** out of 178 entries. All 43 document links have matching explanations. The [document review](DOCUMENT_REVIEW.md) maps each entry to its pages and records the corrections and checks.

## Study PDFs

The day labels in older filenames describe the original review sessions. Entry numbers below follow the tracker.

| Entries | Read this | Main topics |
|---|---|---|
'''
for filename,ns in r.links.items():
    dest=filename.replace('.md','.pdf')
    if filename.endswith('.md'):
        title='Day 5 questions and submission notes';topic='OR versus addition, concatenation, sticky edges, ring/vibrate and one-hot Mealy encoding'
    else:
        title=r.META.get(filename,('Wire, reg and shift-register reset',))[0]
        topics={
        'HDLBits_Combined_Questions_and_Day2_Review.pdf':'Loops, carry wiring, muxes, operators, Lemmings fall count and latches',
        'HDLBits_Day4_Questions_Vector_DFF_PS2.pdf':'Part-selects, DFF excitation, packet byte timing and done',
        'HDLBits_Day6_Non_FSM_QA_Dualedge_and_Circuit5.pdf':'Latest-edge selection, DDR resources and waveform-to-mux reasoning',
        'HDLBits_Day7_QA_FSM_Warnings_and_Counter_Interface.pdf':'Width warnings, next-state outputs and the counter hierarchy',
        'HDLBits_Day8_QA_Wire_Reg_and_Shift_Reset.pdf':'Net wiring, reset behavior and BCD clock rollover',
        'HDLBits_Entry80_Moore_Serial_Twos_Complement_Deep_Dive.pdf':'Why three Moore states are needed and when the output changes',
        'HDLBits_Entry90_Exams_2014_Q3FSM_Three_Sample_Window_Deep_Dive.pdf':'Three real samples, old register values and restarting every group',
        'HDLBits_Fsm_hdlc_Mealy_to_Moore_Deep_Dive.pdf':'Moore/Mealy timing, event states and continuous input',
        'HDLBits_Fsm_serialdata_For_Loops_vs_Clock_Cycles.pdf':'Loops, one-bit-per-edge capture, framing recovery and parity',
        'HDLBits_Recovered_Code_Questions_54_74_75_77.pdf':'Water-level history, sampled edges, asynchronous reset and operators'}
        topic=topics[filename]
    text+=f"| {', '.join(map(str,ns))} | [{title}]({dest}) | {topic} |\n"
text+='''
The [Day 5 Markdown review](HDLBits_Day5_Original_Submissions_Review.md) remains available through its existing tracker links. Its PDF includes the same explanations and historical submission table.

## Verification

The PDFs were checked against the sheet and available source, revised for clearer language, rendered, and visually reviewed. Saved simulations and the additional tests described in [DOCUMENT_REVIEW.md](DOCUMENT_REVIEW.md) passed. The tracker was not changed during the document review.

## Completion records

'''+evidence+'\n'
(ROOT/'README.md').write_text(text,encoding='utf-8')
print('Verified 178 entries, 43 linked entries, 11 document targets; workbook unchanged. Wrote review index and README.')
