"""Build the Attempt 2 reading covers, PDF navigation and Markdown catalogue.

Run from any directory: python index_study_pdfs.py
Dependencies: PyMuPDF, reportlab, openpyxl (tracker read only), Ghostscript.
The existing PDFs supply the original vector pages; no screenshots replace text.
Reruns replace the generated cover instead of repeatedly prepending it.
"""
from __future__ import annotations

import io
import json
import re
import shutil
import subprocess
import sys
import textwrap
from pathlib import Path
from xml.sax.saxutils import escape

BUNDLED_SITE_PACKAGES = (
    Path.home()
    / ".cache"
    / "codex-runtimes"
    / "codex-primary-runtime"
    / "dependencies"
    / "python"
    / "Lib"
    / "site-packages"
)
if BUNDLED_SITE_PACKAGES.exists():
    sys.path.append(str(BUNDLED_SITE_PACKAGES))

import fitz
import openpyxl
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / "internal/tmp/portfolio_index"
MARKER = "attempt2-reading-index-v1"
INDEX_URL = "https://github.com/kapiltrip/hdlBits/blob/main/HDLBits%20Attempt%202/DOCUMENT_INDEX.md"
NAVY, TEAL, INK, MUTED = "#162235", "#087F8C", "#233246", "#566579"
ARIAL = Path(r"C:/Windows/Fonts/arial.ttf")
ARIAL_BOLD = Path(r"C:/Windows/Fonts/arialbd.ttf")
CONSOLAS = Path(r"C:/Windows/Fonts/consola.ttf")
pdfmetrics.registerFont(TTFont("Arial-Cover", str(ARIAL)))
pdfmetrics.registerFont(TTFont("Arial-Cover-Bold", str(ARIAL_BOLD)))


def spec(filename, title, summary, takeaway, groups, pages, entries, prepend=False):
    return dict(filename=filename, title=title, summary=summary, takeaway=takeaway,
                groups=groups, pages=pages, entries=entries, prepend=prepend)


# Page numbers below are the original physical pages, before a new cover.
# Documents with technical content on page 1 get an additional reading cover.
DOCS = [
    spec("HDLBits_Fsm_serialdata_For_Loops_vs_Clock_Cycles.pdf",
         "Serial input needs\nreal clock edges",
         "From the original for-loop mistake to one-bit-per-edge capture, complete frames and odd-parity timing.",
         "A loop without timing control runs within one process activation. A bit counter preserves progress between clock edges.",
         [(2, "The original loop and its simulation", "2-5"), (6, "Two capture patterns and an eight-edge trace", "6-7"),
          (8, "Related exercises and debugging references", "8-9"), (10, "Start, stop and missing-stop recovery", "10"), (11, "Odd parity at the stop edge", "11")],
         ["The original loop and clock sequence", "One edge, seven loop iterations", "Spatial versus temporal repetition", "Local simulation evidence", "Indexed and shift-register capture", "Eight-clock capture trace", "Related serial exercises", "Debugging checklist and references", "Complete frame and recovery", "Odd-parity timing"],
         {2: "2-10", 4: "2-10", 6: "10-11"}),
    spec("HDLBits_Combined_Questions_and_Day2_Review.pdf", "Loops, muxes\nand storage",
         "Connect Verilog statements to the hardware they describe: vector loops, carry chains, mux selection, operators and storage.",
         "First decide whether the task repeats hardware or repeats work across clock edges. Then choose the loop, wiring and storage.",
         [(2, "Question map and linked exercises", "2"), (3, "Generate loops, reversal, carry and population count", "3-6"),
          (7, "Mux masks and two-level selection", "7"), (8, "Lemmings: the 20/21-cycle boundary", "8"),
          (9, "Reset, operator choices and latch behavior", "9-12")],
         ["Question map", "genvar and elaboration", "Vector reversal: two loop styles", "Carry-chain wiring", "Population count and initialization", "Mux operators and selectors", "Lemmings fall counter", "Other takeaways and problem references", "Bitwise versus logical inversion", "Bitwise AND versus logical AND", "Intentional latch storage"],
         {7:"8", 13:"7", 19:"2, 9", 20:"2, 9", 21:"2, 9", 22:"2, 9", 23:"3-4", 24:"2, 9", 25:"2, 9", 26:"3, 6", 27:"2, 9", 28:"2, 9", 29:"7", 30:"5", 31:"10", 36:"11", 38:"12"}),
    spec("HDLBits_Fsm_hdlc_Mealy_to_Moore_Deep_Dive.pdf", "HDLC: get the\noutput cycle right",
         "Follow discard, flag and error detection from the first attempts through a working Moore machine and timing traces.",
         "Recognizing a pattern is only part of the task. The output must also remain valid in the cycle required by the interface.",
         [(2, "Pattern rules, sampling and the first failed approaches", "2-7"), (8, "Ten Moore states and continuous input", "8-9"),
          (10, "Clock traces and Verilog event ordering", "10-11"), (12, "Code review and reference-model checks", "12-13"),
          (14, "Original and working source excerpts", "14-16")],
         ["Pattern rules and run-length reference", "Moore and Mealy output timing", "Why the first Mealy attempt fails", "Flag timing and error behavior", "Why the output became Mealy-style", "Why the first Moore rewrite fails", "Why ten Moore states are useful", "Working Moore FSM", "Discard, flag and error traces", "Event regions and reset", "Code review", "Verification and debugging", "Appendix A: first-attempt blocks", "Appendix B: working source, part 1", "Appendix B: working source, part 2"], {8:"2-16"}),
    spec("HDLBits_Recovered_Code_Questions_54_74_75_77.pdf", "States, sampled edges\nand operators",
         "Four questions from saved submissions: remembered history, sampled edges, asynchronous reset and operator classes.",
         "Inputs describe the present. State preserves history; a sampled edge compares values from consecutive clock samples.",
         [(2, "Entry 54: why the water-level FSM needs history", "2"), (3, "Entry 74: sampled positive-edge detection", "3"),
          (4, "Entry 75: asynchronous-reset event control", "4"), (5, "Entry 77: reduction, bitwise and logical operators", "5"),
          (6, "Revision checklist, checks and references", "6")],
         ["Water-level history", "Sampled positive-edge detection", "Asynchronous-reset event control", "Reduction, bitwise and logical operators", "Checklist and verification"], {54:"2",74:"3",75:"4",77:"5"}),
    spec("HDLBits_Day4_Questions_Vector_DFF_PS2.pdf", "Bytes, flip-flops\nand PS/2 packets",
         "Choose the right bits, capture them at the right edge, and follow a three-byte packet until its data becomes valid.",
         "Separate state decisions from stored data. Check which byte is written at each edge and when done makes the packet valid.",
         [(2, "Entry 67: indexed part-selects and byte reversal", "2-3"), (3, "Entry 66: D flip-flop excitation", "3"),
          (4, "Entry 70: parser states and data ownership", "4"), (5, "Complete parser and datapath implementation", "5"),
          (6, "Three-byte timing trace and checks", "6")],
         ["Indexed part-selects and byte reversal", "Slice checks and DFF excitation", "Parser states and stored data", "Complete parser implementation", "Packet timing trace and checklist"], {66:"3",67:"2-3",70:"4-6"}),
    spec("HDLBits_Entry80_Moore_Serial_Twos_Complement_Deep_Dive.pdf", "Two's complement,\none bit at a time",
         "Understand the LSB-first algorithm, why the Moore machine needs three states, and what each transition remembers.",
         "Copy zeros and the first one, then invert later bits. A Moore state must also identify the output value after sampling.",
         [(2, "The algorithm and a worked eight-bit example", "2"), (3, "Three state meanings and every transition", "3-4"),
          (5, "Clock-by-clock timing and asynchronous reset", "5"), (6, "Source walkthrough and the Mealy comparison", "6-7"),
          (8, "Mistakes, verification and recall questions", "8")],
         ["Serial algorithm and worked example", "Why three Moore states", "Every transition decoded", "Clock-by-clock timing", "Source walkthrough", "Cleaner names and Mealy comparison", "Mistakes, checks and recall"], {80:"2-8"}),
    spec("HDLBits_Day5_Original_Submissions_Review.pdf", "Small RTL mistakes,\nexplained",
         "Day 5 questions and submission notes: operators, concatenation width, sticky edge capture and one-hot Mealy encoding.",
         "Use one counterexample to distinguish similar-looking expressions. Keep the earlier attempt beside its correction.",
         [(1, "Earlier questions and water-level state history", "1-2"), (2, "Sampled edges, reset and operator classes", "2-3"),
          (4, "Entries 80-82: serial complement, OR and padding", "4"), (5, "Entries 83-85: sticky edges, ring and one-hot state", "5-6"),
          (7, "Local verification record", "7"), (8, "Historical submission records (appendix)", "8-11")],
         ["Earlier questions and water-level state history", "Water-level continuation and sampled edges", "Reset and operator classes", "Entries 80-82: complement, OR and padding", "Entries 83-85: sticky edges, ring and one-hot state", "One-hot continuation and September follow-up", "Local verification record", "Historical submission records", "Historical records, continued 1", "Historical records, continued 2", "Historical records, continued 3"],
         {81:"4",82:"4",83:"5",84:"5",85:"5-6"}, True),
    spec("HDLBits_Day6_Non_FSM_QA_Dualedge_and_Circuit5.pdf", "Dual-edge sampling\nand waveform reasoning",
         "Select the newest sample, distinguish simulation from FPGA implementation, and infer Circuit5 from its waveform.",
         "OR cannot select the newest stored bit. Both-edge behavior also needs a deliberate resource and timing choice in hardware.",
         [(2, "Why OR fails and how clock-level selection works", "2-4"), (5, "FPGA resources: fabric, IDDR, ODDR and DDIO", "5-10"),
          (11, "Architecture, half-cycle timing and startup", "11-14"), (15, "Circuit5: infer the selector and write the case", "15-17"),
          (18, "Verification, primary sources and checklist", "18-19")],
         ["Question map and FPGA scope", "Why OR merging fails", "Clock-level selection", "Simulation and FPGA implementation", "Why ordinary fabric is different", "Dedicated DDR I/O resources", "AMD/Xilinx IDDR example", "AMD/Xilinx ODDR example", "Intel DDIO and timing constraints", "Architecture choices", "Half-cycle timing", "Glitches, reset and startup", "XOR-feedback alternative", "Circuit5 waveform inference", "Circuit5 selector and case code", "Waveform-inference method", "Verification and primary sources", "Revision checklist"], {87:"3-14",89:"15-17"}),
    spec("HDLBits_Entry90_Exams_2014_Q3FSM_Three_Sample_Window_Deep_Dive.pdf", "Three samples,\nno wasted cycle",
         "Separate controller state, sample position and accumulated data, then follow adjacent three-sample groups without gaps.",
         "At the third edge, the stored count contains the first two samples. Include the current input before deciding the result.",
         [(2, "Start edge, sample numbering and a 101 trace", "2-3"), (4, "Failed attempts: loop, count and gap-cycle mistakes", "4-8"),
          (9, "Combinational defaults and corrected RTL", "9-10"), (11, "All eight groups and local verification", "11"),
          (12, "Revision checklist and sources", "12")],
         ["Responsibilities and exact clock sequence", "Zero-based sample timing", "Why the loop samples one value", "The incorrect three-state attempt", "Count and gap-cycle errors", "Why count plus w was still wrong", "Why the third sample is current input", "Defaults and sequential holding", "Complete corrected solution", "All eight groups and verification", "Checklist and sources"], {90:"2-12"}),
    spec("HDLBits_Day7_QA_FSM_Warnings_and_Counter_Interface.pdf", "FSM widths and\ncounter connections",
         "Read truncation warnings, derive next-state bits, and trace each control signal through a parent and child counter.",
         "Write down each signal's width, driver and meaning. A next-state bit and a current-state output answer different questions.",
         [(2, "Width warnings and the problem map", "2"), (3, "Entry 102: derive Y0 and z", "3"), (4, "Entry 107: derive Y2", "4"),
          (5, "Entry 109: counter load, enable and data", "5"), (6, "Related examples, checklist and sources", "6-7")],
         ["Width warnings and completion map", "Entry 102: Y0 and z", "Entry 107: next-state Y2", "Entry 109: counter interface", "Related code examples", "Checklist and sources"], {102:"2-3",107:"4",109:"5"}),
    spec("HDLBits_Day8_QA_Wire_Reg_and_Shift_Reset.pdf", "Wire, reg\nand reset behavior",
         "Distinguish a continuous connection from initialization, follow a carry wire, and check shift-register and BCD-clock reset.",
         "The reg keyword permits procedural assignment. The assignment behavior determines whether hardware needs storage.",
         [(1, "Entry 129: declaration assignment versus initialization", "1"), (2, "Entry 129: carry wiring through the adder", "2"),
          (3, "Entry 127: reset belongs with the stored value", "3"), (4, "Entry 123: old values and assignment priority", "4"),
          (5, "Entry 123: complete BCD rollover and boundaries", "5")],
         ["Wire declaration and variable initialization", "Carry wiring", "Shift-register reset", "BCD clock: old values and priority", "Complete BCD rollover"], {123:"4-5",127:"3",129:"1-2"}, True),
    spec("HDLBits_Day9_QA_Latches_and_Sequence_FSM.pdf", "Missing assignments\nand the 1101 FSM",
         "Trace the latch created by a missing assignment, then follow a five-state recognizer with detection held until reset.",
         "Combinational outputs need a value on every path. In a clocked process, an omitted assignment normally means hold the stored value.",
         [(1, "Entry 158: complete combinational assignments", "1"), (2, "The missing else and a latch timing trace", "2"),
          (3, "Defaults, Boolean forms and operator details", "3"), (4, "Entry 155: complete 1101 recognizer RTL", "4"),
          (5, "State meanings, overlap and sticky detection", "5")],
         ["Complete combinational assignments", "Missing else and latch trace", "Defaults and Boolean alternatives", "Complete 1101 recognizer", "Five states, overlap and sticky detection"], {158:"1-3"}, True),
    spec("HDLBits_Day10_Kmaps_Boolean_Forms_and_Rules90_110.pdf", "K-map operators, Boolean\nforms and cellular automata",
         "Connect four Day 10 questions: operator intent in Kmap4, equivalent SOP/POS forms, and simultaneous next-state logic in Rules 90 and 110.",
         "Use | to combine Boolean alternatives, derive SOP from 1-cells and POS from 0-cells, and keep each automaton's current state separate from its next state.",
         [(1, "Entry 161: why Verilog uses | instead of +", "1-2"),
          (3, "Entry 164: SOP, POS and De Morgan's law", "3-4"),
          (5, "Entry 168: Rule 90 and why nextVal is used", "5-6"),
          (7, "Entry 172: Rule 110 expression and boundaries", "7-8")],
         ["Why the K-map expression uses |, not +", "Why + can appear to work here",
          "SOP, POS and De Morgan's law", "Applying SOP and POS to the problem",
          "One whole generation changes at a time", "Why nextVal is used - and whether it is required",
          "Rule 110 uses left, center and right", "Why the Rule 110 expression works"],
         {161:"1-2", 164:"3-4", 168:"5-6", 172:"7-8"}, True),
    spec("HDLBits_Day11_Review2015_Timer_Series_and_Next_State.pdf", "Timer-series FSMs and\nnext-state timing",
         "Build the Review 2015 timer from its counter, shift register and controller, with a precise guide to state, next_state, nonblocking assignments and register ownership.",
         "Use state for work belonging to the current phase. Use next_state only for an intentional reaction to the chosen transition; use both to detect a one-edge entry or exit.",
         [(1, "Series map and questions answered", "1"),
          (2, "Entry 144: the 0-to-999 timing primitive", "2"),
          (3, "Entry 149: MSB-first shift/down datapath", "3-4"),
          (5, "Entry 155: 1101 recognition and transition timing", "5"),
          (6, "Entry 160: four-cycle enable and multiple drivers", "6"),
          (7, "Entry 165: the complete controller", "7-8"),
          (9, "When a clocked block should inspect state or next_state", "9-10"),
          (11, "Entry 170: capture and exact timer duration", "11-14")],
         ["One timer, six connected ideas", "Count 0 through 999, then wrap",
          "MSB-first input still shifts toward the MSB", "Two true enables: the last assignment wins",
          "The repeated question that unlocks the series", "Exactly four cycles, with one owner per register",
          "Search, capture, count, notify, acknowledge", "Yes, the capture counter must be re-armed",
          "state is now; next_state is the chosen destination", "When to use state, next_state, or both",
          "The fourth bit uses old delay plus current data", "Two nested counters implement (delay + 1) x 1000",
          "Controller and next-state logic", "Datapath, outputs and a final audit"],
         {144:"2", 149:"3-4", 155:"5", 160:"6", 165:"7-10", 170:"11-14"}, True),
    spec("HDLBits_Day12_LFSR_Taps_Shifts_and_Old_Value_Timing.pdf", "LFSR taps, shifts and\nold-value timing",
         "Connect the 5-bit, schematic-based 3-bit and 32-bit LFSRs through one method: derive next-bit equations from old state, translate one-based taps, then verify the cycle.",
         "Treat every LFSR as simultaneous next-state equations. Convert tap position k to q[k-1], keep one clocked owner, and never seed an XOR-feedback LFSR with zero.",
         [(1, "Series map and questions answered", "1"),
          (2, "Shared LFSR model and state-space limits", "2"),
          (3, "One-based tap positions versus Verilog indices", "3"),
          (4, "Entry 141: five-bit Galois implementation", "4-5"),
          (6, "Entry 145: schematic, board mapping and RTL", "6-8"),
          (9, "Entry 151: 32-bit taps and nonblocking overrides", "9-10"),
          (11, "Verification and debugging reference", "11")],
         ["Three LFSRs, one translation method",
          "An LFSR is a state machine written as bit equations",
          "Tap position k maps to Verilog index k-1",
          "The five-bit Galois solution", "Old values produce the 31-state cycle",
          "Read the schematic as three D-input equations", "Load has explicit priority over feedback",
          "Seven nonzero states prove the recurrence",
          "The 32-bit solution is the five-bit pattern scaled up",
          "The XORs read old q, never a partly shifted q",
          "Use equations first, code second"],
         {141:"2-5", 145:"6-8", 151:"9-10"}, True),
    spec("HDLBits_Day12_Conway_Grid_Indexing_and_Next_State.pdf", "Conway: grid indexing\nand next-state timing",
         "Derive row * 16 + col, wrap both coordinates, count eight old-state neighbors and advance the complete board on one clock edge.",
         "Calculate every next cell from the same old grid. Wrap row and column separately, and let load override evolution at the rising edge.",
         [(1, "Row/column indexing and inverse mapping", "1"),
          (2, "Toroidal boundaries and eight neighbors", "2"),
          (3, "Rules, old state and next-state timing", "3"),
          (4, "Complete Verilog solution", "4"),
          (5, "Loops, arithmetic width and storage", "5"),
          (6, "Boundary trace and revision checks", "6")],
         ["Why the index is row * 16 + col", "Wrap coordinates before flattening",
          "Every cell reads the same old generation", "The complete two-process solution",
          "What the loops and assignments mean in hardware", "Trace the boundary, then test the whole grid"],
         {177:"1-6"}, True),
]


def shift_range(value, shift):
    return re.sub(r"\d+", lambda m: str(int(m[0]) + shift), value)


def paragraph(c, text, x, y, width, size=11, color=INK, bold=False):
    style = ParagraphStyle("text", fontName="Arial-Cover-Bold" if bold else "Arial-Cover",
                           fontSize=size, leading=size * 1.4, textColor=HexColor(color))
    p = Paragraph(escape(text).replace("\n", "<br/>"), style)
    _, height = p.wrap(width, 1000)
    p.drawOn(c, x, y - height)
    return y - height


def cover(meta, number, total, shift):
    stream = io.BytesIO()
    c = canvas.Canvas(stream, pagesize=(595.276, 841.89), invariant=1)
    w, h = 595.276, 841.89
    c.setFillColor(HexColor("#F7F5F0")); c.rect(0, 0, w, h, stroke=0, fill=1)
    c.setFillColor(HexColor(TEAL)); c.rect(0, h-12, w, 12, stroke=0, fill=1)
    paragraph(c, "HDLBITS  /  ATTEMPT 2", 48, 790, 350, 10, TEAL, True)
    paragraph(c, f"NOTE {number:02d} / {len(DOCS):02d}", 436, 790, 112, 10, TEAL, True)
    y = paragraph(c, meta["title"], 48, 755, 500, 28, NAVY, True)
    y = paragraph(c, meta["summary"], 48, y-14, 492, 11.5)
    y = paragraph(c, f"Kapil Tripathi  |  Verilog & digital design  |  {total} pages", 48, y-15, 500, 9.2, MUTED)
    y -= 23
    c.setStrokeColor(HexColor("#CBD5D7")); c.line(48, y, 547, y)
    y = paragraph(c, "CONTENTS  /  click a row to jump", 48, y-17, 500, 9.5, TEAL, True) - 7
    links = []
    for source_page, label, span in meta["groups"]:
        top = y + 4
        y = paragraph(c, label, 48, y, 428, 10.5)
        paragraph(c, shift_range(span, shift), 492, top-4, 60, 10, TEAL, True)
        bottom = y - 8
        c.setStrokeColor(HexColor("#E0E4E3")); c.line(48, bottom, 547, bottom)
        links.append((fitz.Rect(45, h-top, 550, h-bottom), source_page+shift-1))
        y = bottom-9
    y -= 6
    y = paragraph(c, "KEEP THIS IDEA", 48, y, 500, 9, TEAL, True)
    y = paragraph(c, meta["takeaway"], 48, y-5, 500, 10.5)
    if number == 6:
        y = paragraph(c, 'Original question: "explain me this code in a deep manner, along with need of each state"\n"ik the meaning and need of states s0, s1, s2 ... rest, explain me in doc"', 48, y-10, 499, 8.5, MUTED)
    entry_text = ", ".join(map(str, meta["entries"]))
    y = paragraph(c, f"Tracker entries: {entry_text}", 48, y-14, 499, 8.5, MUTED)
    if y < 135:
        raise ValueError(f"Cover too long: {meta['filename']}, y={y}")
    paragraph(c, "Study notes by Kapil Tripathi, based on HDLBits exercises. Original questions, source references and dated verification records are retained in the notes.", 48, 119, 499, 8.4, MUTED)
    paragraph(c, "ALL NOTES + ENTRY INDEX", 48, 75, 270, 9, TEAL, True)
    c.linkURL(INDEX_URL, (46, 59, 270, 79), relative=0)
    paragraph(c, "HDLBits problem collection", 375, 75, 175, 9, TEAL)
    c.linkURL("https://hdlbits.01xz.net/wiki/Problem_sets", (374, 59, 550, 79), relative=0)
    c.save()
    cover_doc = fitz.open(stream=stream.getvalue(), filetype="pdf")
    # ReportLab emits an unused Helvetica setup command even though all visible
    # cover text uses embedded Arial. Remove only that empty command/resource.
    for page in cover_doc:
        for content_xref in page.get_contents():
            content = cover_doc.xref_stream(content_xref)
            cleaned = re.sub(rb"BT /F1 [0-9.]+ Tf [0-9.]+ TL ET", b"", content)
            if cleaned != content:
                cover_doc.update_stream(content_xref, cleaned)
    for xref in range(1, cover_doc.xref_length()):
        obj = cover_doc.xref_object(xref, compressed=False)
        cleaned = re.sub(r"/F1\s+2\s+0\s+R", "", obj)
        if cleaned != obj:
            cover_doc.update_object(xref, cleaned)
    return cover_doc, links


def tracker_rows():
    # Normal mode exposes native cell hyperlinks. Formula-based hyperlinks in
    # older rows remain supported while new discussion links use native XLSX
    # relationships so preview engines can show their friendly text.
    workbook = openpyxl.load_workbook(ROOT / "HDLBits_Attempt_2_Tracker_Simple.xlsx", read_only=False, data_only=False)
    rows = {}
    for cells in workbook["Tracker"].iter_rows():
        values = [cell.value for cell in cells]
        if not values or not isinstance(values[0], int):
            continue
        n, day, problem, status, discussion = values
        problem_link = cells[2].hyperlink.target if cells[2].hyperlink else None
        if problem_link:
            problem = f'=HYPERLINK("{problem_link}","{problem}")'
        match = re.fullmatch(r'=HYPERLINK\("([^"]+)","([^"]+)"\)', problem)
        if not match:
            raise ValueError(f"Unexpected problem formula for {n}")
        discussion_link = cells[4].hyperlink.target if cells[4].hyperlink else None
        if discussion_link:
            discussion = f'=HYPERLINK("{discussion_link}","{discussion}")'
        rows[n] = dict(day=day, problem=match[2], url=match[1], status=status, discussion=discussion)
    workbook.close()
    return rows


def fix_known_page_references(doc, meta):
    if "Day5_Original" in meta["filename"]:
        pg = doc[1]
        for b in pg.get_text("blocks"):
            if b[6] == 0 and b[4].startswith("The PDF version contains this review"):
                box = fitz.Rect(b[:4])
                pg.add_redact_annot(box, fill=False)
                pg.apply_redactions(images=0, graphics=0)
                replacement = "This PDF contains the review and its historical submission table. The Markdown companion remains available from the collection index and the existing tracker links."
                result = pg.insert_textbox(fitz.Rect(box.x0, box.y0, box.x1, box.y1+4), replacement, fontsize=10.2, fontname="ArialFix", fontfile=str(ARIAL), color=(.09,.14,.20))
                if result < 0:
                    raise ValueError("Day 5 companion reference does not fit")
                break
        pg = doc[7]
        for b in pg.get_text("blocks"):
            if b[6] == 0 and b[4].startswith("PASS: all 8 possible q3fsm") and b[2] > pg.rect.width-48:
                box = fitz.Rect(b[:4])
                lines = b[4].strip().splitlines()
                pg.add_redact_annot(box, fill=False)
                pg.apply_redactions(images=0, graphics=0)
                wrapped = '\n'.join(textwrap.fill(line, width=90, subsequent_indent='  ') for line in lines)
                result = pg.insert_textbox(fitz.Rect(box.x0,box.y0,pg.rect.width-48,box.y0+80),wrapped,fontsize=8.1,fontname='ConsolasFix',fontfile=str(CONSOLAS),color=(.09,.14,.20))
                if result < 0:
                    raise ValueError('Wrapped verification log does not fit')
                break
        pg = doc[-1]
        for b in pg.get_text('blocks'):
            if b[6] == 0 and 'On 7 September, the tracker records 151' in ' '.join(b[4].split()):
                box=fitz.Rect(b[:4])
                pg.add_redact_annot(box,fill=False)
                pg.apply_redactions(images=0,graphics=0)
                replacement = 'At the 3 September checkpoint, entries 1-93 were Done and entries 94-178 had not yet been included in the review. The earlier 7 September document-review checkpoint recorded 151 Done and 27 Pending. These are historical counts; use the tracker for current progress.'
                result=pg.insert_textbox(fitz.Rect(box.x0,box.y0,box.x1,box.y0+85),replacement,fontsize=10.2,fontname='ArialFix',fontfile=str(ARIAL),color=(.09,.14,.20))
                if result < 0:
                    raise ValueError('Historical checkpoint paragraph does not fit')
                break
    # This note has one prose reference to its own original page ranges.
    if "Day9_QA" in meta["filename"]:
        pg = doc[1]
        for b in pg.get_text("blocks"):
            if b[6] == 0 and b[4].startswith("Pages 2"):
                box = fitz.Rect(b[:4])
                pg.add_redact_annot(box, fill=False)
                pg.apply_redactions(images=0, graphics=0)
                replacement = "Pages 3-4 explain the missing paths, timing and alternative coding styles. Pages 5-6 answer the cleanup question in the entry 155 sequence-recognizer code."
                result = pg.insert_textbox(fitz.Rect(box.x0, box.y0, box.x1+2, box.y1+4), replacement, fontsize=8, fontname="ArialFix", fontfile=str(ARIAL), color=(.34,.40,.48))
                if result < 0:
                    raise ValueError("Day 9 cross-reference does not fit")
                break


def build_pdf(meta, number, rows):
    path = ROOT / meta["filename"]
    src = fitz.open(path)
    built = MARKER in src.metadata.get("keywords", "")
    start = 1 if built or not meta["prepend"] else 0
    if len(src)-start != len(meta["pages"]):
        raise ValueError(f"Body page count changed; update the manifest for {path.name}")
    shift = int(meta["prepend"])
    total = len(meta["pages"])+1
    output, links = cover(meta, number, total, shift)
    # Copy body links explicitly. Copying a page subset with links enabled can
    # leave dangling references to the discarded old cover page.
    body_links = []
    for source_number in range(start, len(src)):
        source_page = src[source_number]
        for link in source_page.get_links():
            if fitz.Rect(link["from"]).y0 >= source_page.rect.height - 50:
                continue
            if link["kind"] == fitz.LINK_URI:
                body_links.append((source_number-start, {
                    "kind": fitz.LINK_URI,
                    "from": fitz.Rect(link["from"]),
                    "uri": link["uri"],
                }))
            elif link["kind"] == fitz.LINK_GOTO and link.get("page", -1) >= start:
                body_links.append((source_number-start, {
                    "kind": fitz.LINK_GOTO,
                    "from": fitz.Rect(link["from"]),
                    "page": 1 + link["page"] - start,
                    "to": fitz.Point(link.get("to", fitz.Point(0, 0))),
                    "zoom": link.get("zoom", 0),
                }))
    output.insert_pdf(src, from_page=start, links=False, annots=False)
    src.close()
    for body_number, link in body_links:
        output[body_number + 1].insert_link(link)
    fix_known_page_references(output, meta)
    for rect, target in links:
        output[0].insert_link({"kind":fitz.LINK_GOTO,"from":rect,"page":target,"to":fitz.Point(0,0)})
    outline = [[1, "Contents and reading guide", 1], [1, "Sections", 2]]
    outline += [[2, title, i+2] for i,title in enumerate(meta["pages"])]
    outline += [[1, "Tracker entries", 2]]
    for entry, location in meta["entries"].items():
        outline.append([2, f"Entry {entry}: {rows[entry]['problem']}", int(re.search(r"\d+",location)[0])+shift])
    output.set_toc(outline)
    output.set_page_labels([dict(startpage=0, prefix="", style="D", firstpagenum=1)])
    output.xref_set_key(output.pdf_catalog(), "PageMode", "/UseOutlines")
    output.xref_set_key(output.pdf_catalog(), "Lang", "(en-IN)")
    for i, pg in enumerate(output):
        w,h = pg.rect.width, pg.rect.height
        # Remove navigation annotations from a previous indexed build before
        # drawing the fresh footer. Redaction removes text, not link objects.
        for link in list(pg.get_links()):
            if fitz.Rect(link["from"]).y0 >= h - 50:
                pg.delete_link(link)
        if i:
            # Original footer spans occupy only the final 35 points. Removing text
            # rather than painting over it prevents duplicate extracted page numbers.
            pg.add_redact_annot(fitz.Rect(0,h-37,w,h),fill=(1,1,1))
            pg.apply_redactions(images=0, graphics=0)
        pg.draw_line(fitz.Point(48,h-36),fitz.Point(w-48,h-36), color=(.79,.82,.83), width=.5)
        pg.insert_font(fontname="ArialFooter", fontfile=str(ARIAL), set_simple=True)
        pg.insert_text((48,h-22), f"Kapil Tripathi  |  HDLBits Attempt 2  |  Note {number:02d}",fontname="ArialFooter",fontsize=7.5,color=(.34,.40,.48))
        pg.insert_text((w-215,h-22), "Contents",fontsize=8,fontname="ArialFooter",color=(.03,.50,.55))
        pg.insert_link({"kind":fitz.LINK_GOTO,"from":fitz.Rect(w-217,h-33,w-173,h-14),"page":0,"to":fitz.Point(0,0)})
        pg.insert_text((w-155,h-22), "All notes",fontsize=8,fontname="ArialFooter",color=(.03,.50,.55))
        pg.insert_link({"kind":fitz.LINK_URI,"from":fitz.Rect(w-157,h-33,w-113,h-14),"uri":INDEX_URL})
        pg.insert_text((w-80,h-22),f"{i+1} / {total}",fontname="ArialFooter",fontsize=8,color=(.34,.40,.48))
    output.set_metadata(dict(title=meta["title"].replace("\n"," "),author="Kapil Tripathi",subject=meta["summary"],
                             keywords=f"{MARKER}; HDLBits; Attempt 2; Verilog; RTL; study notes",creator="Kapil Tripathi - HDLBits study notes"))
    temporary = WORK / path.name
    output.subset_fonts()
    output.save(temporary, garbage=4, deflate=True)
    output.close()
    embed_fonts(temporary, path)
    return dict(file=path.name, pages=total, note=number, entries=len(meta["entries"]))


def embed_fonts(source, destination):
    """Avoid viewer-dependent substitution of the standard PDF fonts.

    No PDFSETTINGS preset or image downsampling is used. Verify nonvisual
    navigation and extracted text before accepting the rewritten PDF.
    """
    gs = shutil.which('gs') or shutil.which('gswin64c')
    if not gs:
        with fitz.open(source) as checked:
            missing = []
            for xref in sorted({font[0] for page in checked for font in page.get_fonts()}):
                name, _, _, data = checked.extract_font(xref)
                if not data:
                    missing.append((xref, name))
            if missing:
                raise RuntimeError(
                    f'Ghostscript is unavailable and fonts remain unembedded: '
                    f'{destination.name}: {missing}'
                )
        source.replace(destination)
        return
    embedded = source.with_suffix('.embedded.pdf')
    subprocess.run([gs, '-q', '-dBATCH', '-dNOPAUSE', '-sDEVICE=pdfwrite',
                    '-dCompatibilityLevel=1.7', '-dAutoRotatePages=/None',
                    '-dEmbedAllFonts=true', '-dSubsetFonts=true',
                    '-dDownsampleColorImages=false', '-dDownsampleGrayImages=false',
                    '-dDownsampleMonoImages=false', f'-sOutputFile={embedded}',
                    '-c', '<</NeverEmbed []>> setdistillerparams', '-f', str(source)],
                   check=True, capture_output=True)
    with fitz.open(source) as before, fitz.open(embedded) as after:
        if before.get_toc() != after.get_toc() or len(before) != len(after):
            raise ValueError(f'Font embedding changed the outline: {destination.name}')
        for old,new in zip(before,after):
            if re.sub(r'\s+','',old.get_text()) != re.sub(r'\s+','',new.get_text()):
                raise ValueError(f'Font embedding changed text: {destination.name}, page {old.number+1}')
            targets = lambda page: sorted((l['kind'],l.get('page',-1),l.get('uri','')) for l in page.get_links())
            if targets(old) != targets(new):
                raise ValueError(f'Font embedding changed links: {destination.name}, page {old.number+1}')
    embedded.replace(destination)


def write_index(rows, results):
    # Entry 155 is intentionally discussed in both Note 12 and Note 14.  Count
    # unique tracker destinations while allowing the newer series note to be
    # the primary lookup target below.
    mapping_count = len({n for meta in DOCS for n in meta["entries"]})
    text = f"""# HDLBits Attempt 2 - document index

**Kapil Tripathi | Verilog and digital design**

{len(DOCS)} study PDFs explain the questions behind this second pass through HDLBits. Start with a topic below, browse the collection, or jump to one of the **{mapping_count} tracker entries with discussion links**. These are study notes based on HDLBits exercises; the original problem statements belong to HDLBits.

[Browse all PDFs](#the-complete-collection) · [Find an entry](#find-a-tracker-entry) · [Tracker](HDLBits_Attempt_2_Tracker_Simple.xlsx) · [Review record](DOCUMENT_REVIEW.md) · [LinkedIn plan](../LinkedIn_Attempt_2_Posting_Plan_and_Ideas.md)

## Start with a question

"""
    questions = [
        ("Why does a loop not receive eight serial bits?",0,"2-7"),
        ("When do I use generate rather than a procedural loop?",1,"3-6"),
        ("Why does reg not always mean a physical register?",10,"2-3"),
        ("How does a missing assignment create a latch?",11,"2-4"),
        ("What changes at the Lemmings 20/21-cycle boundary?",1,"8"),
        ("Why does the HDLC output appear in the wrong cycle?",2,"2-11"),
        ("Why does a Moore two's-complement machine need three states?",5,"2-5"),
        ("How do I include the third sample without a gap?",8,"2-3, 7-10"),
        ("When are PS/2 packet data and done valid?",4,"4-6"),
        ("Why can OR not select the newest dual-edge sample?",7,"3-4"),
        ("How do I read FSM width warnings and counter wiring?",9,"2-5"),
        ("How should the 1101 recognizer hold its result?",11,"5-6"),
        ("What is different about reduction, bitwise and logical operators?",3,"5"),
        ("Why does Kmap4 use | instead of +?",12,"2-3"),
        ("What are SOP, POS and De Morgan's law, and why do I need them?",12,"4-5"),
        ("Why did I use nextVal in Rule 90, and is it required?",12,"6-7"),
        ("How does the Rule 110 expression match its truth table?",12,"8-9"),
        ("When should a clocked block inspect state, next_state, or both?",13,"10-11"),
        ("Why does assign plus a clocked assignment create multiple drivers?",13,"7"),
        ("How do four captured bits become an exact (delay + 1) x 1000 timer?",13,"12-15"),
        ("Why does tap position k become Verilog bit q[k-1]?",14,"4-6"),
        ("Why do nonblocking LFSR assignments all read old q?",14,"5-11"),
        ("How do I translate the Mt2015 LFSR schematic into RTL?",14,"7-9"),
        ("Why is Conway's cell index row * 16 + col, and how do boundaries wrap?",15,"2-3"),
        ("Why does Conway calculate next_q before the clocked q update?",15,"4-7"),
        ("Which small mistakes explain sticky capture and one-hot encoding?",6,"5-7"),
    ]
    for question, i, pages in questions:
        text += f"- **{question}** [Note {i+1:02d}, pp. {pages}]({DOCS[i]['filename']}#page={re.search(r'\d+',pages)[0]}).\n"
    text += "\n## The complete collection\n\nNote numbers are catalogue identifiers, separate from tracker entries and posting days. Older day labels remain in filenames so existing links keep working.\n\n| Note | PDF | Pages | What it explains |\n|---|---|---:|---|\n"
    for i, (meta, result) in enumerate(zip(DOCS,results),1):
        title = meta["title"].replace("\n"," ").replace("|", "&#124;")
        summary = meta["summary"].replace("|", "&#124;")
        text += f"| {i:02d} | [{title}]({meta['filename']}) | {result['pages']} | {summary} |\n"
    text += """
Each PDF has a clickable contents page, section and tracker-entry bookmarks, embedded fonts, a consistent page counter, and **Contents / All notes** links in the footer. Text and diagrams remain searchable/vector content where present in the source. Page numbers here match the printed counter and physical PDF page.

Page-fragment links (`#page=N`) work in supporting PDF viewers. If GitHub's preview ignores the fragment, download the PDF and use its contents page, bookmarks or printed page number. The contents labels and page numbers also work as a visual guide in document previews that do not support links.

## Find a tracker entry

Entry numbers below come from the revision tracker, not the HDLBits website's ordering. Shared PDFs answer multiple questions. The workbook is the source for progress; this index does not announce completion.

| Entry | HDLBits problem | Note and answer pages |
|---:|---|---|
"""
    mapping = {}
    for i,meta in enumerate(DOCS,1):
        for n,location in meta["entries"].items():
            mapping[n] = (i,meta,shift_range(location,int(meta["prepend"])))
    linked = {n for n,r in rows.items() if str(r["discussion"]).startswith('=HYPERLINK(')}
    if linked != set(mapping):
        raise ValueError(f"Tracker coverage differs: {linked ^ set(mapping)}")
    for n,(i,meta,pages) in sorted(mapping.items()):
        row=rows[n]
        text += f"| {n} | [{row['problem']}]({row['url']}) | [Note {i:02d}, pp. {pages}]({meta['filename']}#page={re.search(r'\d+',pages)[0]}) |\n"
    text += """
The [Day 5 Markdown review](HDLBits_Day5_Original_Submissions_Review.md) is an alternative to Note 07 and has its own section index. Its historical submission appendix preserves the original evidence and dates.

## Sharing and revision

For a LinkedIn attachment, use the reader-facing title on the PDF cover. For a focused post, choose one question and its trace or counterexample; the full note supplies the surrounding explanation and sources. The [posting plan](../LinkedIn_Attempt_2_Posting_Plan_and_Ideas.md) maps these notes to the proposed series.

For revision, try the linked problem before opening the explanation. Then check the state meaning, sampling edge, bit width, reset and boundary case that mattered. The [review record](DOCUMENT_REVIEW.md) distinguishes earlier RTL checks from this indexing and layout update.
"""
    (ROOT/"DOCUMENT_INDEX.md").write_text(text,encoding="utf-8")


def main():
    WORK.mkdir(parents=True, exist_ok=True)
    rows = tracker_rows()
    expected = {m["filename"] for m in DOCS}
    actual = {p.name for p in ROOT.glob("*.pdf")}
    if expected != actual:
        raise ValueError(f"Update manifest for added/removed PDFs: {expected ^ actual}")
    results = [build_pdf(meta,i,rows) for i,meta in enumerate(DOCS,1)]
    write_index(rows,results)
    (WORK/"build_summary.json").write_text(json.dumps(results,indent=2))
    mapping_count = len({n for meta in DOCS for n in meta["entries"]})
    print(f"Indexed {len(results)} PDFs, {sum(r['pages'] for r in results)} pages and {mapping_count} linked tracker entries.")


if __name__ == "__main__":
    main()
