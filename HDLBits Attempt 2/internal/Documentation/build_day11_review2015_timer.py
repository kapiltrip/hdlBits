"""Build the technical body for the Review 2015 timer-series study note.

The collection indexer adds the standard cover, bookmarks, navigation footer,
and final page labels.  This builder therefore emits only the fourteen
technical pages.
"""

from pathlib import Path
import html
import re
import sys


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

from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "HDLBits_Day11_Review2015_Timer_Series_and_Next_State.pdf"
TEMP_OUTPUT = ROOT / "internal" / "tmp" / "day11_review2015_timer" / "body.pdf"

NAVY = HexColor("#162235")
TEAL = HexColor("#087F8C")
INK = HexColor("#233246")
MUTED = HexColor("#566579")
PALE_BLUE = HexColor("#EAF3F5")
PALE_YELLOW = HexColor("#FFF7CC")
PALE_GREEN = HexColor("#EAF6EF")
PALE_RED = HexColor("#FCEDEC")
GRID = HexColor("#CBD5D7")
CODE_BG = HexColor("#F3F5F7")

pdfmetrics.registerFont(TTFont("Arial", r"C:/Windows/Fonts/arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", r"C:/Windows/Fonts/arialbd.ttf"))
pdfmetrics.registerFont(TTFont("Consolas", r"C:/Windows/Fonts/consola.ttf"))
pdfmetrics.registerFontFamily(
    "Arial",
    normal="Arial",
    bold="Arial-Bold",
    italic="Arial",
    boldItalic="Arial-Bold",
)

styles = {
    "Body": ParagraphStyle(
        "Body",
        fontName="Arial",
        fontSize=10.05,
        leading=14.15,
        textColor=INK,
        spaceAfter=7,
    ),
    "Small": ParagraphStyle(
        "Small",
        fontName="Arial",
        fontSize=8.15,
        leading=10.7,
        textColor=MUTED,
        spaceAfter=4,
    ),
    "Title": ParagraphStyle(
        "Title",
        fontName="Arial-Bold",
        fontSize=21.5,
        leading=25.5,
        textColor=NAVY,
        spaceAfter=9,
    ),
    "H2": ParagraphStyle(
        "H2",
        fontName="Arial-Bold",
        fontSize=13.1,
        leading=15.8,
        textColor=TEAL,
        spaceBefore=5,
        spaceAfter=5,
    ),
    "H3": ParagraphStyle(
        "H3",
        fontName="Arial-Bold",
        fontSize=10.4,
        leading=13.5,
        textColor=NAVY,
        spaceBefore=3,
        spaceAfter=3,
    ),
    "Label": ParagraphStyle(
        "Label",
        fontName="Arial-Bold",
        fontSize=8.45,
        leading=10.8,
        textColor=TEAL,
        spaceAfter=4,
    ),
    "Callout": ParagraphStyle(
        "Callout",
        fontName="Arial-Bold",
        fontSize=10.45,
        leading=14.2,
        textColor=NAVY,
        alignment=TA_CENTER,
        borderColor=TEAL,
        borderWidth=1,
        borderPadding=8,
        backColor=PALE_BLUE,
        spaceBefore=7,
        spaceAfter=9,
    ),
    "Question": ParagraphStyle(
        "Question",
        fontName="Arial",
        fontSize=9.6,
        leading=13.6,
        textColor=NAVY,
        borderColor=HexColor("#D8C775"),
        borderWidth=0.7,
        borderPadding=7,
        backColor=PALE_YELLOW,
        spaceBefore=4,
        spaceAfter=7,
    ),
    "Cell": ParagraphStyle(
        "Cell", fontName="Arial", fontSize=8.35, leading=10.8, textColor=INK
    ),
    "CellHead": ParagraphStyle(
        "CellHead",
        fontName="Arial-Bold",
        fontSize=8.35,
        leading=10.8,
        textColor=colors.white,
    ),
}


def p(text, style="Body"):
    return Paragraph(text, styles[style])


def q(text):
    return Paragraph(text, styles["Question"])


def code(text, font_size=8.25, leading=10.75):
    return Preformatted(
        text,
        ParagraphStyle(
            "Code",
            fontName="Consolas",
            fontSize=font_size,
            leading=leading,
            textColor=NAVY,
            backColor=CODE_BG,
            borderColor=GRID,
            borderWidth=0.5,
            borderPadding=7,
            spaceBefore=3,
            spaceAfter=8,
        ),
    )


def cell(text, head=False):
    safe = html.escape(str(text)).replace("\n", "<br/>")
    return p(safe, "CellHead" if head else "Cell")


def table(rows, widths, align=None, row_backgrounds=True):
    formatted = []
    for r_index, row in enumerate(rows):
        formatted.append([v if isinstance(v, Paragraph) else cell(v, r_index == 0) for v in row])
    result = Table(formatted, colWidths=widths, repeatRows=1)
    commands = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("GRID", (0, 0), (-1, -1), 0.5, GRID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]
    if row_backgrounds:
        commands.append(("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, HexColor("#F7FAFB")]))
    if align:
        commands.append(("ALIGN", (0, 1), (-1, -1), align))
    result.setStyle(TableStyle(commands))
    return result


def page_title(kicker, title, intro):
    return [p(kicker, "Label"), p(title, "Title"), p(intro)]


def source(label, url, evidence=None):
    suffix = f" {evidence}" if evidence else ""
    return p(
        f"Source: <link href='{url}' color='#087F8C'>{label}</link>.{suffix}",
        "Small",
    )


def on_page(canvas, doc):
    width, height = A4
    canvas.saveState()
    canvas.setFillColor(TEAL)
    canvas.rect(0, height - 9, width, 9, stroke=0, fill=1)
    canvas.setFont("Arial-Bold", 7.6)
    canvas.setFillColor(MUTED)
    canvas.drawString(48, height - 31, "DAY 11  /  REVIEW 2015 TIMER SERIES")
    canvas.drawRightString(width - 48, height - 31, f"TECHNICAL PAGE {doc.page} OF 14")
    canvas.setStrokeColor(GRID)
    canvas.setLineWidth(0.5)
    canvas.line(48, height - 39, width - 48, height - 39)
    canvas.restoreState()


def verify_models():
    """Check the counter boundaries, capture order, and timer duration used below."""

    count = 0
    observed = []
    for _ in range(1002):
        observed.append(count)
        count = 0 if count == 999 else count + 1
    assert observed[:3] == [0, 1, 2]
    assert observed[998:1002] == [998, 999, 0, 1]

    shifted = 0
    for bit in (1, 0, 0, 1):
        shifted = ((shifted << 1) | bit) & 0xF
    assert shifted == 0b1001
    assert ((0 - 1) & 0xF) == 15

    SEARCH0, SEARCH1, SEARCH11, SEARCH110, CAPTURE, COUNT, DONE = range(7)

    def advance(state, bit, tick=0, remaining=0, thousand=0, ack=0):
        if state == SEARCH0:
            return SEARCH1 if bit else SEARCH0
        if state == SEARCH1:
            return SEARCH11 if bit else SEARCH0
        if state == SEARCH11:
            return SEARCH11 if bit else SEARCH110
        if state == SEARCH110:
            return CAPTURE if bit else SEARCH0
        if state == CAPTURE:
            return COUNT if tick == 3 else CAPTURE
        if state == COUNT:
            return DONE if remaining == 0 and thousand == 999 else COUNT
        return SEARCH0 if ack else DONE

    state = SEARCH0
    for bit in (1, 1, 0, 1):
        state = advance(state, bit)
    assert state == CAPTURE

    delay = 0
    tick = 0
    for bit in (0, 0, 0, 1):
        assert state == CAPTURE
        candidate = ((delay << 1) | bit) & 0xF
        next_state = advance(state, bit, tick)
        delay = candidate
        tick = 0 if tick == 3 else tick + 1
        state = next_state
    assert delay == 1 and state == COUNT

    wrong = 0
    # Testing next_state == CAPTURE on the final 1101 edge consumes that final 1.
    for bit in (1, 0, 0, 0):
        wrong = ((wrong << 1) | bit) & 0xF
    assert wrong == 8

    for initial in range(16):
        remaining = initial
        thousand = 0
        cycles = 0
        displayed = []
        while True:
            displayed.append(remaining)
            cycles += 1
            if remaining == 0 and thousand == 999:
                break
            if thousand == 999:
                thousand = 0
                remaining -= 1
            else:
                thousand += 1
        assert cycles == (initial + 1) * 1000
        for value in range(initial, -1, -1):
            start = (initial - value) * 1000
            assert displayed[start : start + 1000] == [value] * 1000


REFERENCE_RTL_PART_1 = r"""module top_module (
    input clk,
    input reset,          // Synchronous reset
    input data,
    output [3:0] count,
    output counting,
    output done,
    input ack
);
    localparam SEARCH0   = 3'd0,
               SEARCH1   = 3'd1,
               SEARCH11  = 3'd2,
               SEARCH110 = 3'd3,
               CAPTURE   = 3'd4,
               COUNTING  = 3'd5,
               WAIT_ACK  = 3'd6;

    reg [2:0] state, next_state;
    reg [2:0] bit_index;
    reg [3:0] delay_shift;
    reg [3:0] remaining;
    reg [9:0] subcount;

    always @(*) begin
        case (state)
            SEARCH0:   next_state = data ? SEARCH1 : SEARCH0;
            SEARCH1:   next_state = data ? SEARCH11 : SEARCH0;
            SEARCH11:  next_state = data ? SEARCH11 : SEARCH110;
            SEARCH110: next_state = data ? CAPTURE : SEARCH0;
            CAPTURE:   next_state = (bit_index == 3) ? COUNTING : CAPTURE;
            COUNTING:  next_state = (remaining == 0 && subcount == 999)
                                      ? WAIT_ACK : COUNTING;
            WAIT_ACK:  next_state = ack ? SEARCH0 : WAIT_ACK;
            default:   next_state = SEARCH0;
        endcase
    end"""


REFERENCE_RTL_PART_2 = r"""    always @(posedge clk) begin
        if (reset) begin
            state       <= SEARCH0;
            bit_index   <= 0;
            delay_shift <= 0;
            remaining   <= 0;
            subcount    <= 0;
        end else begin
            state <= next_state;

            if (state == CAPTURE) begin
                delay_shift <= {delay_shift[2:0], data};
                if (bit_index == 3) begin
                    remaining <= {delay_shift[2:0], data};
                    bit_index <= 0;
                    subcount  <= 0;
                end else begin
                    bit_index <= bit_index + 1'b1;
                end
            end else begin
                bit_index <= 0;
            end

            if (state == COUNTING) begin
                if (subcount == 10'd999) begin
                    subcount <= 0;
                    if (remaining != 0)
                        remaining <= remaining - 1'b1;
                end else begin
                    subcount <= subcount + 1'b1;
                end
            end
        end
    end

    assign count    = remaining;
    assign counting = (state == COUNTING);
    assign done     = (state == WAIT_ACK);
endmodule"""


def build():
    verify_models()
    TEMP_OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(TEMP_OUTPUT),
        pagesize=A4,
        rightMargin=48,
        leftMargin=48,
        topMargin=50,
        bottomMargin=50,
        title="Review 2015 timer series and next-state timing",
        author="Kapil Tripathi",
        subject="HDLBits Attempt 2 entries 144, 149, 155, 160, 165 and 170",
    )

    story = []

    # Technical page 1
    story += page_title(
        "SERIES MAP  /  ENTRIES 144, 149, 155, 160, 165, 170",
        "One timer, six connected ideas",
        "The counter is the timing primitive. The next five exercises progressively add a shift/down register, a 1101 recognizer, a four-cycle capture controller, the complete controller, and finally the datapath.",
    )
    story += [
        table(
            [
                ["Entry", "Problem", "What it contributes"],
                [144, "Counter with period 1000", "A precise 0...999 timebase."],
                [149, "Shift register + down counter", "One register with mutually exclusive shift/count modes."],
                [155, "1101 recognizer", "Find the start word and remember that it was found."],
                [160, "Enable shifting for four cycles", "Turn a one-cycle event into a four-edge capture window."],
                [165, "Complete FSM", "Sequence search -> capture -> count -> acknowledge."],
                [170, "Complete timer", "Combine controller and datapath with exact boundaries."],
            ],
            [42, 182, 275],
        ),
        Spacer(1, 7),
        p("Questions preserved from the work", "H2"),
        q("Why can a clocked block test next_state? Is next_state one clock late? When should the block test state instead? Is the synchronous-reset structure correct?"),
        q("Why can I not write assign count = 0 as well as count <= ...? What exactly are multiple drivers, and why can different tools report them differently?"),
        q("Do I need to clear the four-cycle counter? Why is the fourth-bit test 3 rather than 4? How does (delay + 1) x 1000 arise without multiplication, and what does count represent?"),
        p("Entry 155 appears in an earlier note too. It is repeated here deliberately because its transition into the capture phase is the timing hinge for the whole series.", "Small"),
        PageBreak(),
    ]

    # Technical page 2
    story += page_title(
        "ENTRY 144  /  PERIOD-1000 COUNTER",
        "Count 0 through 999, then wrap",
        "A 10-bit register can represent 0 through 1023, so width alone does not create a modulo-1000 counter. The terminal-value comparison supplies the missing wrap rule.",
    )
    story += [
        code(
            "always @(posedge clk) begin\n"
            "    if (reset)\n"
            "        q <= 10'd0;\n"
            "    else if (q == 10'd999)\n"
            "        q <= 10'd0;\n"
            "    else\n"
            "        q <= q + 10'd1;\n"
            "end"
        ),
        p("Why compare with 999, not 1000?", "H2"),
        p("The value visible during a cycle is the value stored after the preceding rising edge. When that stored value is 999, the next edge must write 0. Testing 1000 would expose an unwanted 1000 cycle and create a period of 1001."),
        table(
            [
                ["Before edge", "reset", "Value written at edge", "Visible after edge"],
                [998, 0, "998 + 1", 999],
                [999, 0, "0 (explicit wrap)", 0],
                ["anything", 1, "0 (reset wins)", 0],
            ],
            [95, 55, 220, 129],
        ),
        Spacer(1, 7),
        p("Synchronous reset and register ownership", "H2"),
        p("Synchronous means reset is sampled only on a rising edge. Between edges, changing reset does not immediately change q. Declaring q as output reg lets the clocked process own it directly. Using an internal reg count plus assign q = count is equivalent; that continuous assignment drives q, not count."),
        p("The reset branch does not need a separate count=0 declaration elsewhere. One clocked process gives the stored value one owner, and every non-reset edge either wraps or increments it."),
        source(
            "HDLBits Exams/review2015_count1k",
            "https://hdlbits.01xz.net/wiki/Exams/review2015_count1k",
            "The open submission shows Status: Success!",
        ),
        PageBreak(),
    ]

    # Technical page 3
    story += page_title(
        "ENTRY 149  /  SHIFT + COUNT DATAPATH",
        "MSB-first input still shifts toward the MSB",
        "The first serial bit must eventually become q[3]. Appending each new bit at q[0] moves every older bit one place toward q[3].",
    )
    story += [
        code(
            "always @(posedge clk) begin\n"
            "    if (shift_ena)\n"
            "        q <= {q[2:0], data};\n"
            "    else if (count_ena)\n"
            "        q <= q - 4'd1;\n"
            "end"
        ),
        table(
            [
                ["Capture edge", "data", "q after edge", "Meaning"],
                [1, 1, "0001", "First bit is newest at q[0]."],
                [2, 0, "0010", "First bit moves to q[1]."],
                [3, 0, "0100", "First bit moves to q[2]."],
                [4, 1, "1001", "Serial 1001 is now q[3:0]."],
            ],
            [80, 55, 105, 259],
        ),
        Spacer(1, 7),
        p("Why the rightmost item is data", "H2"),
        p("Concatenation writes q[3:1] from the old q[2:0] and writes q[0] from the current serial input. Calling the stream MSB-first describes the order in which the four-bit number arrives; it does not mean each new bit is inserted directly into q[3]."),
        p("Why q <= q - 1 wraps from 0 to 15", "H2"),
        p("The destination is four bits. The mathematical result -1 is represented modulo 16, so its low four bits are 1111. An explicit 0-to-15 branch is correct and readable, but it is not required for a four-bit decrement."),
        p("There is no reset in this component's interface. Simulation may therefore show X until an enabled edge establishes a known value. The final system guarantees four shift edges before it counts, so that behavior is intentional."),
        source(
            "HDLBits Exams/review2015_shiftcount",
            "https://hdlbits.01xz.net/wiki/Exams/review2015_shiftcount",
            "The open submission shows Status: Success!",
        ),
        PageBreak(),
    ]

    # Technical page 4
    story += page_title(
        "ENTRY 149  /  PRIORITY AND OLD VALUES",
        "Two true enables: the last assignment wins",
        "The exercise promises that shift_ena and count_ena are not used together. Your two-if version is therefore accepted, but it still has a definite simulation meaning.",
    )
    story += [
        code(
            "if (shift_ena)\n"
            "    q <= {q[2:0], data};\n"
            "else\n"
            "    q <= q;                 // unnecessary self-assignment\n"
            "\n"
            "if (count_ena)\n"
            "    q <= q - 4'd1;          // later assignment in same process"
        ),
        p("All right-hand sides use the old q", "H2"),
        p("Nonblocking assignments sample their right-hand sides during the active clock event and update the destination later. If both enables are 1, both calculations use the same pre-edge q, and the later scheduled write wins. The result is old q minus one; it is not the shifted value minus one."),
        table(
            [
                ["shift_ena", "count_ena", "Two-if result", "Explicit if/else-if result"],
                [0, 0, "hold", "hold"],
                [1, 0, "shift", "shift"],
                [0, 1, "decrement", "decrement"],
                [1, 1, "decrement (last NBA)", "shift (declared priority)"],
            ],
            [80, 80, 170, 169],
        ),
        Spacer(1, 7),
        p("Three cleanup rules", "H2"),
        p("1. Omit q <= q in a clocked process: no assignment already means hold. 2. Use if/else if when you want a visible priority. 3. Give a stored signal one procedural owner; assignment order is predictable only within that one process."),
        p("Why this is different from multiple drivers", "H2"),
        p("Several nonblocking assignments to q inside one clocked block are competing assignments from one owner, resolved by source order. Assigning q from another always block or continuous assign creates another owner. That is the multiple-driver problem addressed on page 7."),
        PageBreak(),
    ]

    # Technical page 5
    story += page_title(
        "ENTRY 155  /  1101 RECOGNIZER",
        "The repeated question that unlocks the series",
        "Five states record the longest useful suffix seen so far. The final state is sticky in this component because later exercises replace that self-loop with the four-bit capture phase.",
    )
    story += [
        table(
            [
                ["State", "Remembered suffix", "Next on 0", "Next on 1"],
                ["SEARCH0", "none", "SEARCH0", "SEARCH1"],
                ["SEARCH1", "1", "SEARCH0", "SEARCH11"],
                ["SEARCH11", "11", "SEARCH110", "SEARCH11"],
                ["SEARCH110", "110", "SEARCH0", "FOUND"],
                ["FOUND", "1101 found", "FOUND", "FOUND"],
            ],
            [95, 155, 120, 129],
        ),
        Spacer(1, 7),
        q("“Why next_state? next_state is a clock late ... is reset right?”"),
        p("next_state is not another stored register here. It is combinational logic calculated from the current state and current data. On the edge that samples the final 1, next_state is FOUND before the nonblocking updates; state becomes FOUND after that edge."),
        code(
            "always @(posedge clk) begin\n"
            "    if (reset) begin\n"
            "        state          <= SEARCH0;\n"
            "        start_shifting <= 1'b0;\n"
            "    end else begin\n"
            "        state <= next_state;\n"
            "        if (next_state == FOUND)\n"
            "            start_shifting <= 1'b1;  // intentional sticky register\n"
            "    end\n"
            "end"
        ),
        p("This raises the registered output on the same edge that state enters FOUND. Testing state == FOUND in that clocked block would raise it one edge later. The cleaner Moore form is assign start_shifting = (state == FOUND): after the state update, the decode rises in the FOUND cycle without a separate output register."),
        p("The synchronous reset is correct: when reset is 1 at a rising edge, its branch wins and the next_state calculation is ignored for that state update."),
        source(
            "HDLBits Exams/review2015_fsmseq",
            "https://hdlbits.01xz.net/wiki/Exams/review2015_fsmseq",
            "The open submission shows Status: Success!",
        ),
        PageBreak(),
    ]

    # Technical page 6
    story += page_title(
        "ENTRY 160  /  FOUR-CYCLE ENABLE",
        "Exactly four cycles, with one owner per register",
        "The accepted counter starts at one on the reset edge while shift_ena becomes 1. Three more enabled edges advance the stored count to four; the following cycle is disabled.",
    )
    story += [
        table(
            [
                ["Edge", "Cause", "count after edge", "shift_ena after edge"],
                ["R", "reset=1", 1, 1],
                ["R+1", "count < 4", 2, 1],
                ["R+2", "count < 4", 3, 1],
                ["R+3", "count < 4", 4, 1],
                ["R+4", "count is 4", "holds 4", 0],
            ],
            [70, 160, 130, 139],
        ),
        Spacer(1, 7),
        q("“Why can’t I add assign count = 3'd0? What does multiple drivers mean, and does it behave differently in each simulator?”"),
        p("A continuous assign drives its left side all the time. The clocked block also tries to drive count after clock edges. Those are two hardware sources connected to one signal. In Verilog, a procedural destination is a variable/reg while a continuous-assignment destination is a net; mixing the two is normally illegal. If a resolved net does have two drivers, conflicting 0 and 1 values resolve to X in simulation and do not describe an ordinary FPGA register."),
        table(
            [
                ["Pattern", "Meaning", "Use it?"],
                ["count <= ... in one clocked block", "One flip-flop bank owns count.", "Yes"],
                ["assign q = count", "Internal count drives a separate output net q.", "Yes"],
                ["assign count = 0 plus count <= ...", "Constant driver fights the clocked driver.", "No"],
                ["count <= ... in two always blocks", "Two procedural owners; ordering is not a priority rule.", "No"],
            ],
            [165, 230, 104],
        ),
        Spacer(1, 7),
        p("Tool messages vary—illegal reg drive, multiple drivers, unresolved signal, or synthesis failure—but the design rule does not: one signal, one owner. Initialization belongs in the reset branch of that owner."),
        source(
            "HDLBits Exams/review2015_fsmshift",
            "https://hdlbits.01xz.net/wiki/Exams/review2015_fsmshift",
            "The open submission shows Status: Success!",
        ),
        PageBreak(),
    ]

    # Technical page 7
    story += page_title(
        "ENTRY 165  /  COMPLETE CONTROLLER",
        "Search, capture, count, notify, acknowledge",
        "The controller combines the previous state machines but still treats the counters as an external datapath. Its outputs describe phases; done_counting returns the datapath result.",
    )
    story += [
        table(
            [
                ["Phase", "State meaning", "Output/action", "Exit condition"],
                ["Search", "Remember suffixes of 1101", "All controls 0", "Final 1 arrives"],
                ["Capture", "Receive four following bits", "shift_ena=1", "Four capture cycles complete"],
                ["Count", "Wait for external counters", "counting=1", "done_counting=1"],
                ["Notify", "Timeout is visible", "done=1", "ack=1"],
            ],
            [72, 184, 120, 123],
        ),
        Spacer(1, 8),
        p("A state-per-cycle controller", "H2"),
        code(
            "SEARCH110: next_state = data ? BIT0 : SEARCH0;\n"
            "BIT0:      next_state = BIT1;\n"
            "BIT1:      next_state = BIT2;\n"
            "BIT2:      next_state = BIT3;\n"
            "BIT3:      next_state = COUNTING;\n"
            "COUNTING:  next_state = done_counting ? WAIT_ACK : COUNTING;\n"
            "WAIT_ACK:  next_state = ack ? SEARCH0 : WAIT_ACK;\n"
            "\n"
            "assign shift_ena = (state == BIT0) || (state == BIT1) ||\n"
            "                   (state == BIT2) || (state == BIT3);\n"
            "assign counting  = (state == COUNTING);\n"
            "assign done      = (state == WAIT_ACK);"
        ),
        p("This version needs more states but no separate four-cycle counter. A compressed CAPTURE state plus a two- or three-bit counter is equally valid. State count and datapath count are two representations of the same four-cycle history."),
        p("Why Moore-style output decoding is useful", "H2"),
        p("Outputs are determined from the current phase, so there is one obvious cycle definition: shift_ena is high for every cycle spent in BIT0 through BIT3; counting is high while waiting; done stays high until acknowledgement. No extra output register can drift away from the state."),
        source(
            "HDLBits Exams/review2015_fsm",
            "https://hdlbits.01xz.net/wiki/Exams/review2015_fsm",
            "The open result panel shows Status: Success!",
        ),
        PageBreak(),
    ]

    # Technical page 8
    story += page_title(
        "ENTRY 165  /  COUNTER-COMPRESSED VERSION",
        "Yes, the capture counter must be re-armed",
        "Your accepted controller uses one CAPTURE state and count to remember which of the four capture cycles is active. That register must be ready at zero before every new timer transaction.",
    )
    story += [
        q("“Do I need to make count 0 or not?”"),
        p("For a controller that can return from WAIT_ACK to searching and start again, yes. If count remains 4, the next arrival in CAPTURE immediately appears complete and shift_ena never supplies four fresh cycles. Resetting count outside CAPTURE, resetting it when CAPTURE finishes, or setting it on entry are all valid—choose one clear owner and one convention."),
        code(
            "always @(posedge clk) begin\n"
            "    if (reset) begin\n"
            "        state <= SEARCH0;\n"
            "        count <= 0;\n"
            "    end else begin\n"
            "        state <= next_state;\n"
            "        if (state == CAPTURE) begin\n"
            "            if (count == 3)\n"
            "                count <= 0;        // fourth cycle completed\n"
            "            else\n"
            "                count <= count + 1'b1;\n"
            "        end else begin\n"
            "            count <= 0;            // armed before next entry\n"
            "        end\n"
            "    end\n"
            "end\n"
            "assign shift_ena = (state == CAPTURE);"
        ),
        p("Why the terminal value is 3", "H2"),
        p("With zero-based numbering, the four capture cycles are 0, 1, 2, and 3. During the cycle with count=3, shift_ena is still high and the fourth bit is sampled at its ending edge. That same edge may move state to COUNTING. Waiting for count=4 would create a fifth CAPTURE cycle."),
        table(
            [
                ["CAPTURE cycle", "count before edge", "Bit sampled", "state after edge"],
                [1, 0, "delay[3]", "CAPTURE"],
                [2, 1, "delay[2]", "CAPTURE"],
                [3, 2, "delay[1]", "CAPTURE"],
                [4, 3, "delay[0]", "COUNTING"],
            ],
            [105, 120, 130, 144],
        ),
        PageBreak(),
    ]

    # Technical page 9
    story += page_title(
        "CLOCKED LOGIC  /  THE CENTRAL CONFUSION",
        "state is now; next_state is the chosen destination",
        "Both names are evaluated before the nonblocking update at a rising edge. They answer different questions, so neither is universally the correct test.",
    )
    story += [
        table(
            [
                ["Before the edge", "At the edge", "After NBA updates"],
                ["state stores Q\ninput has D\nnext_state = F(Q,D)", "Clocked blocks read Q, D, and F(Q,D). Every <= RHS is sampled.", "state stores F(Q,D). Registered outputs receive their scheduled values."],
            ],
            [165, 177, 157],
        ),
        Spacer(1, 9),
        code(
            "always @(posedge clk) begin\n"
            "    state <= next_state;\n"
            "\n"
            "    if (state == CAPTURE)\n"
            "        delay <= {delay[2:0], data};   // action of current cycle\n"
            "\n"
            "    if (next_state == FOUND)\n"
            "        found_reg <= 1'b1;             // react to chosen transition\n"
            "end"
        ),
        p("Testing state", "H2"),
        p("Use state when the action belongs to the phase the machine is already in: sample a delay bit during CAPTURE, advance a subcounter during COUNTING, or clear phase-local storage while outside that phase. This reads the pre-edge current state."),
        p("Testing next_state", "H2"),
        p("Use next_state only when you intentionally want a registered reaction to the transition decision made from this edge's inputs. In the standalone recognizer, next_state==FOUND sets a sticky output on the edge that consumes the final 1. It is not a universal shortcut for avoiding a delay."),
        p("A decoded Moore output needs neither test in the sequential block: assign done = (state == WAIT_ACK). The state update itself makes the output change in the new state."),
        p("next_state is usually combinational—not a second clocked register and not inherently one cycle late.", "Callout"),
        PageBreak(),
    ]

    # Technical page 10
    story += page_title(
        "CLOCKED LOGIC  /  DECISION GUIDE",
        "When to use state, next_state, or both",
        "Start by naming the event you mean. Then choose the expression that identifies that event exactly.",
    )
    story += [
        table(
            [
                ["Intent", "Recommended condition", "Reason"],
                ["Do work throughout phase X", "state == X", "X is the current cycle."],
                ["Decode a Moore output", "assign out = (state == X)", "Keeps output aligned with state."],
                ["React on transition into X", "state != X && next_state == X", "A true one-edge entry event."],
                ["React on transition out of X", "state == X && next_state != X", "A true one-edge exit event."],
                ["Register an output high whenever destination is X", "next_state == X", "Includes entry and any X self-loop."],
                ["Preserve a sticky event", "set on entry; omit assignment otherwise", "Clocked omission intentionally holds."],
            ],
            [165, 165, 169],
        ),
        Spacer(1, 8),
        p("Why next_state == X is not an entry detector", "H2"),
        p("If X self-loops, next_state remains X every cycle inside X. The condition is therefore true on entry and during the stay. Use state != X && next_state == X when exactly one entering edge matters."),
        p("Why delay capture must use state == CAPTURE", "H2"),
        p("On the edge that completes 1101, current state is SEARCH110 and next_state is CAPTURE. Testing next_state would shift that final recognizer bit into delay. Four such tests would capture 1000 for an intended following delay 0001. Testing state starts on the next edge, when the first actual delay bit is present."),
        p("Reset and ownership checklist", "H2"),
        p("In a synchronous-reset block, reset wins only at a rising edge. Reset state and every independently stored datapath register that must begin known. next_state can still toggle combinationally while reset is high; the reset branch ignores it. Assign next_state in the combinational block only, and state in the clocked block only."),
        p("Do not assign next_state from both blocks. Do not register next_state unless you deliberately want another pipeline stage.", "Callout"),
        PageBreak(),
    ]

    # Technical page 11
    story += page_title(
        "ENTRY 170  /  CAPTURE THE DELAY",
        "The fourth bit uses old delay plus current data",
        "Nonblocking assignment means delay still contains the first three captured bits while the fourth edge is being evaluated. The concatenation supplies the missing current bit immediately.",
    )
    story += [
        code(
            "if (state == CAPTURE) begin\n"
            "    delay <= {delay[2:0], data};\n"
            "    if (bit_index == 3) begin\n"
            "        bit_index <= 0;\n"
            "        remaining <= {delay[2:0], data};\n"
            "        subcount <= 0;\n"
            "    end else begin\n"
            "        bit_index <= bit_index + 1'b1;\n"
            "    end\n"
            "end"
        ),
        table(
            [
                ["Before edge", "Current data", "Candidate {delay[2:0],data}", "After edge"],
                ["delay=0000, index=0", 0, "0000", "delay=0000"],
                ["delay=0000, index=1", 0, "0000", "delay=0000"],
                ["delay=0000, index=2", 0, "0000", "delay=0000"],
                ["delay=0000, index=3", 1, "0001", "delay=0001; remaining=0001"],
            ],
            [125, 85, 180, 109],
        ),
        Spacer(1, 7),
        q("“At the third tick, if I put the completed value in countreg, do I still need next_state?”"),
        p("The bit index and the state answer separate questions. bit_index==3 says this edge has the fourth delay bit, so it constructs the completed value. state==CAPTURE says the current data belongs to the delay field at all. next_state is not needed for the datapath write; combinational FSM logic independently uses bit_index==3 to leave CAPTURE on that edge."),
        p("Why the if test is == 3, not != 3", "H2"),
        p("The special work—copying the completed four-bit candidate into remaining—belongs only to the fourth capture edge. Using != 3 would perform it on the first three edges and skip it precisely when the final bit arrives."),
        source(
            "HDLBits Exams/review2015_fancytimer",
            "https://hdlbits.01xz.net/wiki/Exams/review2015_fancytimer",
            "The open result panel shows Status: Success!",
        ),
        PageBreak(),
    ]

    # Technical page 12
    story += page_title(
        "ENTRY 170  /  EXACT TIMER LENGTH",
        "Two nested counters implement (delay + 1) x 1000",
        "remaining is not the raw clock-cycle count. It is the value displayed for a block of 1000 cycles. subcount selects the cycle within that block.",
    )
    story += [
        code(
            "if (state == COUNTING) begin\n"
            "    if (subcount == 10'd999) begin\n"
            "        subcount <= 0;\n"
            "        if (remaining != 0)\n"
            "            remaining <= remaining - 1'b1;\n"
            "    end else begin\n"
            "        subcount <= subcount + 1'b1;\n"
            "    end\n"
            "end\n"
            "\n"
            "// Leave after the final cycle of the final block.\n"
            "COUNTING: next_state = (remaining == 0 && subcount == 999)\n"
            "                       ? WAIT_ACK : COUNTING;"
        ),
        table(
            [
                ["Loaded delay", "remaining shown", "Cycles per value", "Total COUNTING cycles"],
                [0, "0", 1000, 1000],
                [1, "1, then 0", "1000 each", 2000],
                [5, "5,4,3,2,1,0", "1000 each", 6000],
                [15, "15 down to 0", "1000 each", 16000],
            ],
            [100, 150, 120, 129],
        ),
        Spacer(1, 7),
        q("“How is this block making (delay + 1) x 1000? What is count? Am I putting delay in countreg?”"),
        p("Yes: remaining/countreg starts as the captured delay. Values delay, delay-1, ..., 0 form delay+1 display blocks. subcount visits 0 through 999 inside every block, giving 1000 cycles per value. Multiplication is unnecessary because the two counters express the product structurally."),
        p("The terminal comparison is made from the old pre-edge values. When remaining=0 and subcount=999, that cycle is still the thousandth cycle displaying 0; the ending edge moves to WAIT_ACK. This avoids the two common off-by-one failures: leaving at 998 or creating an extra cycle at 1000."),
        p("A 10-bit subcount is sufficient because 999 fits. A nine-bit register is not: its maximum is 511. A separate product register would need 14 bits for the maximum 16000, but this architecture never stores that product."),
        PageBreak(),
    ]

    # Technical page 13
    story += page_title(
        "ENTRY 170  /  REFERENCE RTL, PART 1",
        "Controller and next-state logic",
        "This complete version keeps the successful seven-state structure, uses one owner per stored signal, and makes every next-state path explicit.",
    )
    story += [
        code(REFERENCE_RTL_PART_1, font_size=6.8, leading=8.45),
        p("Why the default branch matters", "H2"),
        p("Every legal state assigns next_state, and default recovers from an unused or unknown encoding. This is complete combinational logic: it does not intentionally remember an earlier next_state value and therefore does not infer a latch."),
        p("The SEARCH11 self-loop preserves overlap. After 111, the most useful suffix is still 11, so a following 01 can complete the pattern."),
        PageBreak(),
    ]

    # Technical page 14
    story += page_title(
        "ENTRY 170  /  REFERENCE RTL, PART 2",
        "Datapath, outputs and a final audit",
        "The sequential block performs work for the current phase; continuous Moore decodes expose the phase after each state update.",
    )
    story += [
        code(REFERENCE_RTL_PART_2, font_size=6.75, leading=8.3),
        p("Final audit", "H2"),
        table(
            [
                ["Check", "What to confirm"],
                ["Sampling", "The final 1 of 1101 is not the first delay bit."],
                ["Capture", "Exactly four edges shift MSB-first; index 3 completes the value."],
                ["Timing", "subcount spans 0...999 for every remaining value, including 0."],
                ["Outputs", "counting and done decode current state; done holds until ack."],
                ["Reset", "State and all independently stored datapath values reset on the edge."],
                ["Ownership", "Each register is written by one clocked block; next_state by one combinational block."],
            ],
            [100, 399],
        ),
        Spacer(1, 6),
        p("Verification used for this note", "H2"),
        p("The builder checks the 998,999,0,1 wrap; MSB-first capture of 1001; four-bit underflow; entry to CAPTURE after 1101; the wrong 1000 value produced by consuming the recognizer's final 1; and every delay value 0 through 15 for exact duration and 1000-cycle count plateaus."),
        p("The six open HDLBits pages showed successful submissions. That platform evidence establishes acceptance; the local model above independently checks the timing claims printed in this note.", "Small"),
    ]

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    TEMP_OUTPUT.replace(OUTPUT)

    import fitz

    pdf = fitz.open(OUTPUT)
    if len(pdf) != 14:
        raise ValueError(f"Expected 14 technical pages, found {len(pdf)}")
    expected_headings = [
        "One timer, six connected ideas",
        "Count 0 through 999, then wrap",
        "MSB-first input still shifts toward the MSB",
        "Two true enables: the last assignment wins",
        "The repeated question that unlocks the series",
        "Exactly four cycles, with one owner per register",
        "Search, capture, count, notify, acknowledge",
        "Yes, the capture counter must be re-armed",
        "state is now; next_state is the chosen destination",
        "When to use state, next_state, or both",
        "The fourth bit uses old delay plus current data",
        "Two nested counters implement (delay + 1) x 1000",
        "Controller and next-state logic",
        "Datapath, outputs and a final audit",
    ]
    for page, heading in zip(pdf, expected_headings):
        page_text = " ".join(page.get_text().split())
        if heading not in page_text:
            raise ValueError(f"Missing heading on technical page {page.number + 1}: {heading}")

    # Remove ReportLab's unused Helvetica setup resource. All visible text uses
    # the embedded Arial or Consolas fonts registered above.
    for page in pdf:
        for xref in page.get_contents():
            stream = pdf.xref_stream(xref)
            cleaned = re.sub(rb"BT /F1 [0-9.]+ Tf [0-9.]+ TL ET", b"", stream)
            if cleaned != stream:
                pdf.update_stream(xref, cleaned)
    for xref in range(1, pdf.xref_length()):
        obj = pdf.xref_object(xref, compressed=False)
        cleaned = re.sub(r"/F1\s+\d+\s+0\s+R", "", obj)
        if cleaned != obj:
            pdf.update_object(xref, cleaned)

    metadata = pdf.metadata
    metadata.update(
        {
            "title": "Review 2015 timer series and next-state timing",
            "author": "Kapil Tripathi",
            "subject": "HDLBits Attempt 2 entries 144, 149, 155, 160, 165 and 170",
            "keywords": "HDLBits; Verilog; FSM; timer; state; next_state; nonblocking assignment; multiple drivers",
            "creator": "Kapil Tripathi - HDLBits study notes",
        }
    )
    pdf.set_metadata(metadata)
    verified = TEMP_OUTPUT.with_name("verified.pdf")
    pdf.save(verified, garbage=4, deflate=True)
    pdf.close()
    verified.replace(OUTPUT)
    print(OUTPUT)


if __name__ == "__main__":
    build()
