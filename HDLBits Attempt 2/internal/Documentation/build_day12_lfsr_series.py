"""Build the technical body for the three-problem LFSR study note.

The collection indexer adds the standard cover, bookmarks, navigation footer,
and final page labels. This builder emits eleven technical pages.
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
OUTPUT = ROOT / "HDLBits_Day12_LFSR_Taps_Shifts_and_Old_Value_Timing.pdf"
TEMP_OUTPUT = ROOT / "internal" / "tmp" / "day12_lfsr_series" / "body.pdf"

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


def code(text, font_size=8.15, leading=10.65):
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
    for row_index, row in enumerate(rows):
        formatted.append(
            [value if isinstance(value, Paragraph) else cell(value, row_index == 0) for value in row]
        )
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
        commands.append(
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, HexColor("#F7FAFB")])
        )
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
    canvas.drawString(48, height - 31, "DAY 12  /  LFSR SERIES")
    canvas.drawRightString(width - 48, height - 31, f"TECHNICAL PAGE {doc.page} OF 11")
    canvas.setStrokeColor(GRID)
    canvas.setLineWidth(0.5)
    canvas.line(48, height - 39, width - 48, height - 39)
    canvas.restoreState()


def set_bit(value, index, bit):
    if bit:
        return value | (1 << index)
    return value & ~(1 << index)


def next_lfsr5(value):
    shifted = (value >> 1) | ((value & 1) << 4)
    return set_bit(shifted, 2, ((value >> 3) & 1) ^ (value & 1))


def next_mt2015(value):
    q0 = (value >> 0) & 1
    q1 = (value >> 1) & 1
    q2 = (value >> 2) & 1
    return (q2 << 0) | (q0 << 1) | ((q1 ^ q2) << 2)


def next_lfsr32(value):
    shifted = (value >> 1) | ((value & 1) << 31)
    feedback = value & 1
    for destination, source_index in ((21, 22), (1, 2), (0, 1)):
        shifted = set_bit(
            shifted,
            destination,
            ((value >> source_index) & 1) ^ feedback,
        )
    return shifted


def cycle(step, seed, limit):
    value = seed
    seen = []
    while value not in seen and len(seen) <= limit:
        seen.append(value)
        value = step(value)
    return seen, value


def polynomial_mul_mod(left, right, polynomial, degree):
    result = 0
    while right:
        if right & 1:
            result ^= left
        right >>= 1
        left <<= 1
        if left & (1 << degree):
            left ^= polynomial
    return result


def polynomial_pow_mod(base, exponent, polynomial, degree):
    result = 1
    while exponent:
        if exponent & 1:
            result = polynomial_mul_mod(result, base, polynomial, degree)
        base = polynomial_mul_mod(base, base, polynomial, degree)
        exponent >>= 1
    return result


def verify_models():
    """Check every short cycle and the stated 32-bit primitive polynomial."""

    states5, repeat5 = cycle(next_lfsr5, 1, 40)
    assert len(states5) == 31 and repeat5 == 1 and 0 not in states5
    assert states5[:9] == [0x01, 0x14, 0x0A, 0x05, 0x16, 0x0B, 0x11, 0x1C, 0x0E]

    states3, repeat3 = cycle(next_mt2015, 1, 10)
    assert len(states3) == 7 and repeat3 == 1 and 0 not in states3
    assert states3 == [0b001, 0b010, 0b100, 0b101, 0b111, 0b011, 0b110]

    assert next_lfsr32(1) == 0x80200003

    polynomial = (1 << 32) | (1 << 22) | (1 << 2) | (1 << 1) | 1
    order = (1 << 32) - 1
    assert polynomial_pow_mod(2, order, polynomial, 32) == 1
    for prime_factor in (3, 5, 17, 257, 65537):
        assert polynomial_pow_mod(2, order // prime_factor, polynomial, 32) != 1


LFSR5_RTL = r"""module top_module (
    input clk,
    input reset,              // Active-high synchronous reset
    output reg [4:0] q
);
    always @(posedge clk) begin
        if (reset) begin
            q <= 5'h01;
        end else begin
            q    <= {q[0], q[4:1]};
            q[2] <= q[3] ^ q[0];
        end
    end
endmodule"""


MT2015_RTL = r"""module top_module (
    input  [2:0] SW,          // Parallel-load value R
    input  [1:0] KEY,         // KEY[1] = L, KEY[0] = clock
    output reg [2:0] LEDR     // Register outputs Q
);
    always @(posedge KEY[0]) begin
        if (KEY[1]) begin
            LEDR <= SW;
        end else begin
            LEDR[0] <= LEDR[2];
            LEDR[1] <= LEDR[0];
            LEDR[2] <= LEDR[1] ^ LEDR[2];
        end
    end
endmodule"""


LFSR32_RTL = r"""module top_module (
    input clk,
    input reset,              // Active-high synchronous reset
    output reg [31:0] q
);
    always @(posedge clk) begin
        if (reset) begin
            q <= 32'h00000001;
        end else begin
            q     <= {q[0], q[31:1]};
            q[21] <= q[22] ^ q[0];
            q[1]  <= q[2]  ^ q[0];
            q[0]  <= q[1]  ^ q[0];
        end
    end
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
        title="LFSR taps, shifts and old-value timing",
        author="Kapil Tripathi",
        subject="HDLBits Attempt 2 entries 141, 145 and 151",
    )

    story = []

    # Technical page 1
    story += page_title(
        "SERIES MAP  /  ENTRIES 141, 145, 151",
        "Three LFSRs, one translation method",
        "These exercises move from a drawn five-bit Galois LFSR, through a three-bit mux-and-flip-flop circuit, to a 32-bit Galois LFSR. The reliable workflow is always the same: name the old state, write each next-bit equation, and only then compress the equations into Verilog.",
    )
    story += [
        table(
            [
                ["Entry", "Problem", "Main reasoning task"],
                [141, "Lfsr5", "Translate one-based taps 5 and 3 into a right-shifting Galois update."],
                [145, "Mt2015_lfsr", "Read the mux diagram, distinguish parallel load from feedback, and map board pins."],
                [151, "Lfsr32", "Scale the same Galois pattern to taps 32, 22, 2, and 1 without an index error."],
            ],
            [48, 120, 331],
        ),
        Spacer(1, 8),
        p("Questions this note answers", "H2"),
        q("What does an LFSR actually store, and why can a small register generate a long sequence without using a counter?"),
        q("If the diagram says tap position 3, why does the code override q[2]? Why does tap 22 become q[21] in the 32-bit version?"),
        q("Why is a whole-vector nonblocking assignment followed by a few slice assignments valid? Do the XOR expressions see old q or the partly shifted q?"),
        q("For Mt2015_lfsr: what exactly is the question asking, how do L, R, Clock, Q, SW, KEY, and LEDR correspond, and why does the accepted solution work?"),
        p("All three open HDLBits result panels showed Status: Success! on 9 September 2026. The note also verifies the full 31-state and 7-state cycles locally.", "Small"),
        PageBreak(),
    ]

    # Technical page 2
    story += page_title(
        "SHARED MODEL  /  STATE RECURRENCE",
        "An LFSR is a state machine written as bit equations",
        "An n-bit register stores one state. At each active clock edge, every next bit is a linear XOR expression of the old bits. Repeating that fixed transformation produces a deterministic orbit through the state space.",
    )
    story += [
        p("The three layers", "H2"),
        table(
            [
                ["Layer", "Question to ask", "Example"],
                ["State", "What values exist before this edge?", "old q[4:0] = 00001"],
                ["Next-state equations", "What should each destination bit become?", "next q[2] = old q[3] ^ old q[0]"],
                ["Clocked storage", "When do all those values become visible?", "Together, immediately after posedge clk"],
            ],
            [96, 206, 197],
        ),
        Spacer(1, 8),
        p("Why XOR is called linear", "H2"),
        p("Over one-bit arithmetic, XOR is addition modulo 2: 0^0=0, 0^1=1, 1^0=1, and 1^1=0. Every LFSR next-state bit is a sum of selected old bits with no carries. That is why matrix and polynomial methods can analyze its period."),
        p("Maximum length and the missing state", "H2"),
        p("An n-bit register has 2^n possible bit patterns. A maximum-length XOR-feedback LFSR visits all 2^n - 1 nonzero states before repeating. It cannot include zero because XORs of all zeros are still zero; 000...0 is a separate self-loop called lockup."),
        p("Resetting to 1 is therefore functional, not decorative. It chooses a nonzero seed. Any other nonzero seed on the same maximal cycle changes the starting point but not the cycle length."),
        p("LFSR is not the same as binary count", "H2"),
        p("The output sequence looks irregular and is useful for test patterns, scrambling, CRC-style logic, and compact counters. It is still fully deterministic. Knowing the current state determines every future state."),
        p("Recall test", "Callout"),
        p("If q is all zero and the only feedback operators are XOR, no clock edge can escape zero."),
        PageBreak(),
    ]

    # Technical page 3
    story += page_title(
        "SHARED MODEL  /  TAP NUMBERING",
        "Tap position k maps to Verilog index k-1",
        "HDLBits numbers tap positions from 1, but Verilog vectors use zero-based indices. Write the position and index on separate lines before coding; this single step prevents the most common LFSR error.",
    )
    story += [
        table(
            [
                ["Named position", "Verilog bit", "Five-bit meaning", "Thirty-two-bit meaning"],
                [1, "q[0]", "Output/feedback bit", "Output plus tap stage"],
                [2, "q[1]", "Ordinary shift stage", "Tap stage"],
                [3, "q[2]", "Tap stage", "Ordinary shift stage"],
                [22, "q[21]", "Not present", "Tap stage"],
                [32, "q[31]", "Not present", "Feedback enters here"],
            ],
            [88, 88, 155, 168],
        ),
        Spacer(1, 8),
        p("Start from the ordinary right shift", "H2"),
        code(
            "next_q = {old_q[0], old_q[N-1:1]};\n"
            "// next_q[N-1] = old_q[0]\n"
            "// next_q[i]   = old_q[i+1] for 0 <= i < N-1"
        ),
        p("Then override the tap destinations", "H2"),
        p("For a Galois tap at position k below the top position, the destination q[k-1] receives its ordinary shifted source XORed with the outgoing feedback bit q[0]. Thus position 3 gives next q[2] = old q[3] ^ old q[0]. Position 22 gives next q[21] = old q[22] ^ old q[0]."),
        p("Why the top tap may not need a separate line", "H2"),
        p("The base concatenation already writes old q[0] into the top stage. The diagram often draws the top XOR with a constant-zero second input for consistency. XOR with zero changes nothing, so the whole-vector shift already implements it."),
        p("Mechanical translation", "Callout"),
        p("Diagram position -> subtract 1 -> destination index. Ordinary shifted source -> add 1 -> old source index. XOR the outgoing old q[0] only at tapped destinations."),
        PageBreak(),
    ]

    # Technical page 4
    story += page_title(
        "ENTRY 141  /  LFSR5",
        "The five-bit Galois solution",
        "The circuit shifts right. Position 5 receives the outgoing q[0], while the tap at position 3 receives old q[3] XOR old q[0]. The synchronous reset selects seed 00001.",
    )
    story += [
        code(LFSR5_RTL, 8.0, 10.45),
        p("Line-by-line meaning", "H2"),
        table(
            [
                ["Code", "Next-state equation"],
                ["q <= {q[0], q[4:1]};", "q4'=q0, q3'=q4, q2'=q3, q1'=q2, q0'=q1"],
                ["q[2] <= q[3] ^ q[0];", "Replace the base q2'=q3 with tapped q2'=q3^q0"],
                ["q <= 5'h01;", "Select nonzero seed 00001 when reset is high at the edge"],
            ],
            [210, 289],
        ),
        Spacer(1, 7),
        p("Why q[2] is assigned twice", "H2"),
        p("Both assignments are in the same always block. The whole-vector line supplies the default next value for every bit, then the later slice assignment replaces only q[2]. This is a compact default-plus-exception pattern, not two hardware drivers."),
        p("Why output reg is shown", "H2"),
        p("The always block stores q, so q must be a procedural variable in Verilog. Declaring output reg [4:0] q makes the port itself the register. An internal reg plus assign q = internal_q would also be valid but adds an unnecessary name here."),
        source(
            "HDLBits Lfsr5",
            "https://hdlbits.01xz.net/wiki/Lfsr5",
            "The page specifies taps 5 and 3, reset to 1, and shows Status: Success!",
        ),
        PageBreak(),
    ]

    # Technical page 5
    story += page_title(
        "ENTRY 141  /  LFSR5 TRACE",
        "Old values produce the 31-state cycle",
        "Tracing from reset seed 01 hex exposes both the shift direction and the tap override. It also matches the beginning of HDLBits' displayed reference waveform.",
    )
    story += [
        table(
            [
                ["Step", "old q", "old q0", "base shift", "new q2", "next q"],
                [0, "00001 (01)", 1, "10000", "q3^q0 = 1", "10100 (14)"],
                [1, "10100 (14)", 0, "01010", "q3^q0 = 0", "01010 (0A)"],
                [2, "01010 (0A)", 0, "00101", "q3^q0 = 1", "00101 (05)"],
                [3, "00101 (05)", 1, "10010", "q3^q0 = 1", "10110 (16)"],
                [4, "10110 (16)", 0, "01011", "q3^q0 = 0", "01011 (0B)"],
            ],
            [42, 105, 60, 94, 105, 93],
        ),
        Spacer(1, 8),
        p("The important first edge", "H2"),
        p("Starting at 00001, an ordinary rotate-like right shift would produce 10000. The position-3 tap changes q[2] from old q[3]=0 to 0^1=1, so the real result is 10100. If your first post-reset state is not 10100, the shift direction or tap index is wrong."),
        p("A compact sequence fingerprint", "H2"),
        code("01 -> 14 -> 0A -> 05 -> 16 -> 0B -> 11 -> 1C -> 0E -> ...", 9.0, 12.0),
        p("Local exhaustive check", "H2"),
        p("The builder starts at 00001, records states until the first repeat, and asserts 31 unique states, no zero state, and a return to 00001. That verifies the implemented recurrence, not merely the first few waveform labels."),
        p("Reset timing", "H2"),
        p("Because reset is inside always @(posedge clk), it is synchronous. A high reset between edges does not immediately change q. At the next rising edge, reset wins over the feedback update and q becomes 00001."),
        p("Debug boundary", "Callout"),
        p("Check one edge after reset first. A correct 00001 -> 10100 transition proves the seed, shift direction, feedback bit, and tap destination together."),
        PageBreak(),
    ]

    # Technical page 6
    story += page_title(
        "ENTRY 145  /  MT2015_LFSR",
        "Read the schematic as three D-input equations",
        "Each flip-flop stores one LEDR bit. Its input mux chooses either the parallel R input or the feedback-network value. The load selector L is shared, so all three bits load or advance together.",
    )
    story += [
        table(
            [
                ["Schematic label", "Top-level port", "Role"],
                ["R[2:0]", "SW[2:0]", "Three-bit value loaded in parallel"],
                ["L", "KEY[1]", "Mux selection: 1 loads R, 0 selects feedback"],
                ["Clock", "KEY[0]", "Rising edge stores all three selected D inputs"],
                ["Q[2:0]", "LEDR[2:0]", "Visible stored state"],
            ],
            [105, 110, 284],
        ),
        Spacer(1, 8),
        p("Feedback equations when L=0", "H2"),
        code(
            "next Q[0] = old Q[2]\n"
            "next Q[1] = old Q[0]\n"
            "next Q[2] = old Q[1] ^ old Q[2]"
        ),
        p("Parallel-load equations when L=1", "H2"),
        code(
            "next Q[0] = R[0]\n"
            "next Q[1] = R[1]\n"
            "next Q[2] = R[2]"
        ),
        p("What the question is asking", "H2"),
        p("The task is not asking you to instantiate physical switches, keys, LEDs, muxes, or flip-flop submodules. It asks for behavior equivalent to the shown circuit while using the required board-facing port names. One clocked always block implements all three flip-flops and their shared load selection."),
        p("Do not infer an extra reset", "H2"),
        p("This module has no reset port. KEY[1] and SW supply an explicit load path instead. To establish a known state, set SW to a chosen seed, use L=1 for one active clock edge, then use L=0 to advance the recurrence."),
        source(
            "HDLBits Mt2015_lfsr",
            "https://hdlbits.01xz.net/wiki/Mt2015_lfsr",
            "The page maps R to SW, Clock to KEY[0], L to KEY[1], and Q to LEDR.",
        ),
        PageBreak(),
    ]

    # Technical page 7
    story += page_title(
        "ENTRY 145  /  MT2015_LFSR RTL",
        "Load has explicit priority over feedback",
        "The if branch models the shared mux select. At every rising edge of KEY[0], KEY[1] chooses one complete three-bit next state: SW for load, or the feedback equations for advance.",
    )
    story += [
        code(MT2015_RTL, 7.9, 10.35),
        p("Why LEDR <= SW is the right load", "H2"),
        p("The vector assignment is exactly the three parallel equations LEDR[i] <= SW[i]. No shifting happens in that branch. Since it is the if branch, it has priority whenever KEY[1] is 1 at the sampling edge."),
        p("Why all three feedback assignments read old LEDR", "H2"),
        p("Nonblocking <= evaluates all three right-hand sides from the same old LEDR. The first line does not alter the value read by the second, and neither alters the operands read by the XOR. They represent three flip-flops sampling simultaneously."),
        table(
            [
                ["At posedge KEY[0]", "KEY[1]", "Stored result"],
                ["Load operation", 1, "LEDR_next = SW"],
                ["Sequence operation", 0, "LEDR_next = {LEDR1^LEDR2, LEDR0, LEDR2}"],
            ],
            [170, 75, 254],
        ),
        Spacer(1, 7),
        p("Board polarity versus logic polarity", "H2"),
        p("The exercise connects KEY[1] directly to logical L and the accepted circuit loads when that signal is 1. A physical pushbutton may be electrically active-low on the board; that affects how a person drives the pin, not the Boolean behavior requested by the schematic. Do not silently insert an inversion that the problem does not show."),
        p("Original saved question", "Question"),
        p("The editor comment asked to understand the question before the solution. The mapping table on page 7 and the two equation sets on page 7 are the essential pre-code interpretation; this page is the direct RTL transcription."),
        PageBreak(),
    ]

    # Technical page 8
    story += page_title(
        "ENTRY 145  /  MT2015_LFSR TRACE",
        "Seven nonzero states prove the recurrence",
        "Load seed 001, deassert L, and advance once per rising edge. The circuit visits all seven nonzero three-bit patterns before returning to 001.",
    )
    story += [
        table(
            [
                ["Old Q", "Q0'=old Q2", "Q1'=old Q0", "Q2'=old Q1^old Q2", "Next Q"],
                ["001", 0, 1, "0^0=0", "010"],
                ["010", 0, 0, "1^0=1", "100"],
                ["100", 1, 0, "0^1=1", "101"],
                ["101", 1, 1, "0^1=1", "111"],
                ["111", 1, 1, "1^1=0", "011"],
                ["011", 0, 1, "1^0=1", "110"],
                ["110", 1, 0, "1^1=0", "001"],
            ],
            [60, 95, 95, 155, 94],
        ),
        Spacer(1, 8),
        p("Why 000 never appears", "H2"),
        p("Every listed nonzero state maps to another nonzero state. Separately, 000 maps to 000 because each next bit is either an old bit or XOR of old bits. Loading 000 therefore locks the generator. Load any of the seven nonzero seeds to enter the same seven-state cycle at a different point."),
        p("What would blocking assignments risk?", "H2"),
        p("If the feedback branch used = and the statements executed sequentially, later equations could read values already changed by earlier statements. The simulated recurrence would depend on source order and no longer match three simultaneous D flip-flops. Nonblocking <= preserves the intended old-state snapshot."),
        p("A useful mental rewrite", "H2"),
        code(
            "old = LEDR;\n"
            "LEDR_next[0] = old[2];\n"
            "LEDR_next[1] = old[0];\n"
            "LEDR_next[2] = old[1] ^ old[2];"
        ),
        p("You do not need this temporary variable in the final RTL. It is a reasoning device that makes simultaneous sampling explicit."),
        p("Verification result", "Callout"),
        p("001 -> 010 -> 100 -> 101 -> 111 -> 011 -> 110 -> 001. Period = 7 = 2^3 - 1."),
        PageBreak(),
    ]

    # Technical page 9
    story += page_title(
        "ENTRY 151  /  LFSR32",
        "The 32-bit solution is the five-bit pattern scaled up",
        "Start with the same right-shift default, then override destinations for the lower taps. Positions 22, 2, and 1 become q[21], q[1], and q[0]. Position 32 is already handled by feedback into q[31].",
    )
    story += [
        code(LFSR32_RTL, 7.6, 9.9),
        table(
            [
                ["Tap position", "Destination index", "Ordinary source", "Implemented next value"],
                [32, "q[31]", "constant 0 at drawn XOR", "old q[0]"],
                [22, "q[21]", "old q[22]", "old q[22] ^ old q[0]"],
                [2, "q[1]", "old q[2]", "old q[2] ^ old q[0]"],
                [1, "q[0]", "old q[1]", "old q[1] ^ old q[0]"],
            ],
            [80, 105, 130, 184],
        ),
        Spacer(1, 7),
        p("The off-by-one trap", "H2"),
        p("Writing q[22], q[2], and q[1] treats the one-based tap labels as if they were Verilog indices. That moves every lower XOR one stage too high. The first visible state can expose the error immediately."),
        p("First edge after reset seed 00000001", "H2"),
        code(
            "base shift: q[31]=1, all other bits=0\n"
            "tap overrides: q[21]=1, q[1]=1, q[0]=1\n"
            "next q = 32'h80200003"
        ),
        source(
            "HDLBits Lfsr32",
            "https://hdlbits.01xz.net/wiki/Lfsr32",
            "The page specifies taps 32, 22, 2, and 1 and reset to 32'h1.",
        ),
        PageBreak(),
    ]

    # Technical page 10
    story += page_title(
        "ENTRY 151  /  NONBLOCKING OVERRIDES",
        "The XORs read old q, never a partly shifted q",
        "The accepted compact style relies on two Verilog rules: nonblocking right-hand sides are sampled before updates become visible, and the last assignment to an overlapping destination in one process determines that destination's scheduled value.",
    )
    story += [
        table(
            [
                ["Statement", "RHS snapshot", "Scheduled destination"],
                ["q <= {q[0],q[31:1]}", "Entire old q", "All 32 next bits"],
                ["q[21] <= q[22]^q[0]", "old q[22], old q[0]", "Replace scheduled bit 21"],
                ["q[1] <= q[2]^q[0]", "old q[2], old q[0]", "Replace scheduled bit 1"],
                ["q[0] <= q[1]^q[0]", "old q[1], old q[0]", "Replace scheduled bit 0"],
            ],
            [190, 145, 164],
        ),
        Spacer(1, 8),
        p("This is one owner, not multiple drivers", "H2"),
        p("All four assignments live in one clocked process. Synthesis sees one bank of 32 flip-flops with combinational next-value logic. A separate always block or continuous assign writing q would create another owner and would be a real multiple-driver error."),
        p("Equivalent explicit next-vector style", "H2"),
        code(
            "reg [31:0] next_q;\n"
            "always @(*) begin\n"
            "    next_q     = {q[0], q[31:1]};\n"
            "    next_q[21] = q[22] ^ q[0];\n"
            "    next_q[1]  = q[2]  ^ q[0];\n"
            "    next_q[0]  = q[1]  ^ q[0];\n"
            "end\n"
            "always @(posedge clk)\n"
            "    if (reset) q <= 32'h1; else q <= next_q;",
            7.8,
            10.1,
        ),
        p("Both styles describe the same hardware. The explicit form can be easier to audit because every exception names next_q; the compact form is shorter and safe when all overlapping nonblocking assignments remain in one process."),
        p("Polynomial check", "H2"),
        p("The stated taps correspond to x^32 + x^22 + x^2 + x + 1, up to the reciprocal orientation used by the right-shifting implementation. The builder verifies the primitive-order conditions using the prime factors 3, 5, 17, 257, and 65537 of 2^32 - 1. This supports the maximal nonzero period stated by the exercise."),
        PageBreak(),
    ]

    # Technical page 11
    story += page_title(
        "REFERENCE  /  VERIFICATION AND DEBUGGING",
        "Use equations first, code second",
        "The shortest reliable LFSR solution starts from a paper trace. Treat every HDLBits drawing as a next-state specification, then use one clocked owner to store the result.",
    )
    story += [
        table(
            [
                ["Check", "What to write or test"],
                ["1. Direction", "For each destination, identify the old source before thinking about taps."],
                ["2. Numbering", "Convert one-based position k to zero-based q[k-1]."],
                ["3. Feedback", "Mark the outgoing old bit once; use it only at drawn tap stages."],
                ["4. Storage", "Use <= in one edge-triggered owner. Omitted assignment means hold."],
                ["5. Seed", "Avoid zero for XOR-feedback operation; match the stated reset or load."],
                ["6. First edge", "Predict one post-seed value by hand and compare it exactly."],
                ["7. Period", "For small designs, enumerate until repeat and assert zero is absent."],
            ],
            [105, 394],
        ),
        Spacer(1, 8),
        p("Three reference results", "H2"),
        table(
            [
                ["Problem", "Seed or load", "First result / verified cycle"],
                ["Lfsr5", "00001", "10100; all 31 nonzero states, then 00001"],
                ["Mt2015_lfsr", "001 via SW", "010; seven-state cycle ending 110 -> 001"],
                ["Lfsr32", "00000001", "80200003; primitive-polynomial order check passes"],
            ],
            [115, 115, 269],
        ),
        Spacer(1, 8),
        p("Mistake-to-symptom map", "H2"),
        table(
            [
                ["Symptom", "Likely cause"],
                ["First Lfsr5 result is 10000", "The tap-3 override was omitted."],
                ["Lfsr32 lower XORs appear one stage high", "Tap positions were used directly as indices."],
                ["Mt2015 result changes with statement order", "Blocking = was used for clocked state updates."],
                ["Sequence stays zero", "Zero was reset or loaded into an XOR-feedback LFSR."],
                ["Compiler rejects q as an l-value", "The procedurally assigned output was not declared reg/variable."],
            ],
            [205, 294],
        ),
        Spacer(1, 7),
        p("Verification used for this note", "H2"),
        p("The builder exhaustively verifies the 5-bit period of 31 and the 3-bit period of 7, checks their exact early sequences, checks the 32-bit first transition 00000001 -> 80200003, and proves the stated 32-bit polynomial has full multiplicative order. The three current HDLBits panels independently show accepted submissions."),
    ]

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    TEMP_OUTPUT.replace(OUTPUT)

    import fitz

    pdf = fitz.open(OUTPUT)
    if len(pdf) != 11:
        raise ValueError(f"Expected 11 technical pages, found {len(pdf)}")
    expected_headings = [
        "Three LFSRs, one translation method",
        "An LFSR is a state machine written as bit equations",
        "Tap position k maps to Verilog index k-1",
        "The five-bit Galois solution",
        "Old values produce the 31-state cycle",
        "Read the schematic as three D-input equations",
        "Load has explicit priority over feedback",
        "Seven nonzero states prove the recurrence",
        "The 32-bit solution is the five-bit pattern scaled up",
        "The XORs read old q, never a partly shifted q",
        "Use equations first, code second",
    ]
    for page, heading in zip(pdf, expected_headings):
        page_text = " ".join(page.get_text().split())
        if heading not in page_text:
            raise ValueError(f"Missing heading on technical page {page.number + 1}: {heading}")
        for block in page.get_text("blocks"):
            x0, y0, x1, y1 = block[:4]
            if x0 < -0.5 or y0 < -0.5 or x1 > page.rect.width + 0.5 or y1 > page.rect.height + 0.5:
                raise ValueError(f"Text outside page bounds on technical page {page.number + 1}")

    # Remove ReportLab's unused Helvetica setup resource. Visible text uses
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
            "title": "LFSR taps, shifts and old-value timing",
            "author": "Kapil Tripathi",
            "subject": "HDLBits Attempt 2 entries 141, 145 and 151",
            "keywords": "HDLBits; Verilog; LFSR; Galois; taps; nonblocking assignment; old value; shift register",
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
