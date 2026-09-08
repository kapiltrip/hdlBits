"""Build the six technical pages for the combined Day 10 study note.

The collection indexer adds the standard collection cover, navigation footer,
bookmarks, and final page labels.  Keeping this builder focused on the body
also makes the note safe to rebuild without accumulating old cover pages.
"""

from pathlib import Path
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
    Image,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "HDLBits_Day10_Kmaps_Boolean_Forms_and_Rules90_110.pdf"
TEMP_OUTPUT = ROOT / "internal" / "tmp" / "day10_combined" / "body.pdf"
SCREENSHOT_161 = (
    ROOT
    / "internal"
    / "Evidence"
    / "Day 9"
    / "Entry 161 - Kmap4 - bitwise OR versus addition.png"
)

NAVY = HexColor("#162235")
TEAL = HexColor("#087F8C")
INK = HexColor("#233246")
MUTED = HexColor("#566579")
PALE_BLUE = HexColor("#EAF3F5")
PALE_YELLOW = HexColor("#FFF7CC")
PALE_GREEN = HexColor("#EAF6EF")
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
        fontSize=10.15,
        leading=14.25,
        textColor=INK,
        spaceAfter=7,
    ),
    "Small": ParagraphStyle(
        "Small",
        fontName="Arial",
        fontSize=8.2,
        leading=10.8,
        textColor=MUTED,
        spaceAfter=4,
    ),
    "Title": ParagraphStyle(
        "Title",
        fontName="Arial-Bold",
        fontSize=22,
        leading=26,
        textColor=NAVY,
        spaceAfter=9,
    ),
    "H2": ParagraphStyle(
        "H2",
        fontName="Arial-Bold",
        fontSize=13.2,
        leading=16,
        textColor=TEAL,
        spaceBefore=5,
        spaceAfter=5,
    ),
    "Label": ParagraphStyle(
        "Label",
        fontName="Arial-Bold",
        fontSize=8.5,
        leading=11,
        textColor=TEAL,
        spaceAfter=4,
    ),
    "Callout": ParagraphStyle(
        "Callout",
        fontName="Arial-Bold",
        fontSize=10.6,
        leading=14.5,
        textColor=NAVY,
        alignment=TA_CENTER,
        borderColor=TEAL,
        borderWidth=1,
        borderPadding=8,
        backColor=PALE_BLUE,
        spaceBefore=8,
        spaceAfter=9,
    ),
    "Cell": ParagraphStyle(
        "Cell", fontName="Arial", fontSize=8.55, leading=11.2, textColor=INK
    ),
    "CellHead": ParagraphStyle(
        "CellHead",
        fontName="Arial-Bold",
        fontSize=8.55,
        leading=11.2,
        textColor=colors.white,
    ),
}


def p(text, style="Body"):
    return Paragraph(text, styles[style])


def code(text, font_size=8.5, leading=11.3):
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


def table(rows, widths, align=None):
    result = Table(rows, colWidths=widths, repeatRows=1)
    commands = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, HexColor("#F7FAFB")]),
        ("GRID", (0, 0), (-1, -1), 0.5, GRID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]
    if align:
        commands.append(("ALIGN", (0, 1), (-1, -1), align))
    result.setStyle(TableStyle(commands))
    return result


def on_page(canvas, doc):
    width, height = A4
    canvas.saveState()
    canvas.setFillColor(TEAL)
    canvas.rect(0, height - 9, width, 9, stroke=0, fill=1)
    canvas.setFont("Arial-Bold", 7.7)
    canvas.setFillColor(MUTED)
    canvas.drawString(48, height - 31, "DAY 10  /  K-MAPS, BOOLEAN FORMS, RULES 90 + 110")
    canvas.drawRightString(width - 48, height - 31, f"TECHNICAL PAGE {doc.page} OF 8")
    canvas.setStrokeColor(GRID)
    canvas.setLineWidth(0.5)
    canvas.line(48, height - 39, width - 48, height - 39)
    canvas.restoreState()


def page_title(kicker, title, intro):
    return [
        p(kicker, "Label"),
        p(title, "Title"),
        p(intro),
    ]


def verify_logic():
    """Exhaustively verify every Boolean claim used in the note."""
    for value in range(16):
        a, b, c, d = ((value >> shift) & 1 for shift in (3, 2, 1, 0))
        w1 = c ^ d
        w2 = a ^ b
        terms = [
            (not a) and (not b) and w1,
            (not c) and (not d) and w2,
            a and b and w1,
            c and d and w2,
        ]
        assert sum(bool(term) for term in terms) <= 1
        assert bool(any(terms)) == bool(a ^ b ^ c ^ d)

        sop = (c and d) or ((not a) and (not b) and c)
        pos = c and (d or (not a)) and (d or (not b))
        assert bool(sop) == bool(pos)

        ones = {2, 7, 15}
        zeros = {0, 1, 4, 5, 6, 9, 10, 13, 14}
        if value in ones:
            assert sop
        if value in zeros:
            assert not sop

    mask = (1 << 512) - 1
    patterns = [
        0,
        mask,
        1,
        1 << 511,
        int("10" * 256, 2),
        int("0123456789abcdef" * 8, 16),
    ]
    for state in patterns:
        loop_result = 0
        for i in range(512):
            left = (state >> (i - 1)) & 1 if i > 0 else 0
            right = (state >> (i + 1)) & 1 if i < 511 else 0
            loop_result |= (left ^ right) << i
        vector_result = ((state << 1) & mask) ^ (state >> 1)
        assert loop_result == vector_result

    for neighborhood in range(8):
        left = (neighborhood >> 2) & 1
        right = neighborhood & 1
        assert (left ^ right) == ((0b01011010 >> neighborhood) & 1)

    # Rule 110 is asymmetric. In the accepted packed-vector solution, the
    # displayed left neighbour is q[i+1] and the right neighbour is q[i-1].
    def rule110(left, center, right):
        return (right ^ center) | (right & (not left))

    for neighborhood in range(8):
        left = (neighborhood >> 2) & 1
        center = (neighborhood >> 1) & 1
        right = neighborhood & 1
        assert int(bool(rule110(left, center, right))) == ((0b01101110 >> neighborhood) & 1)
    for left in (0, 1):
        for center in (0, 1):
            assert int(bool(rule110(left, center, 0))) == center
    for center in (0, 1):
        for right in (0, 1):
            assert int(bool(rule110(0, center, right))) == (center | right)

    state = 1
    observed = [state]
    for _ in range(9):
        next_state = 0
        for i in range(512):
            left = (state >> (i + 1)) & 1 if i < 511 else 0
            center = (state >> i) & 1
            right = (state >> (i - 1)) & 1 if i > 0 else 0
            next_state |= int(bool(rule110(left, center, right))) << i
        state = next_state
        observed.append(state)
    assert observed == [1, 3, 7, 0xD, 0x1F, 0x31, 0x73, 0xD7, 0x1FD, 0x307]


def build():
    verify_logic()
    if not SCREENSHOT_161.exists():
        raise FileNotFoundError(SCREENSHOT_161)
    TEMP_OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(TEMP_OUTPUT),
        pagesize=A4,
        rightMargin=48,
        leftMargin=48,
        topMargin=50,
        bottomMargin=50,
        title="K-map operators, Boolean forms and Rules 90/110",
        author="Kapil Tripathi",
        subject="HDLBits Attempt 2 entries 161, 164, 168 and 172",
    )

    submitted = Image(str(SCREENSHOT_161))
    submitted.drawWidth = 499
    submitted.drawHeight = 499 * 661 / 1566

    story = []
    story += page_title(
        "ENTRY 161  /  KMAP4",
        "Why the K-map expression uses |, not +",
        "The four bracketed expressions are alternative one-bit conditions. The output must be 1 when any condition is true, so the combining operation is OR.",
    )
    story += [
        p(
            "On paper, Boolean algebra often writes <font name='Consolas'>+</font> for OR. "
            "In Verilog, the symbols have programming-language meanings: "
            "<font name='Consolas'>|</font> is bitwise OR, while "
            "<font name='Consolas'>+</font> is arithmetic addition.",
            "Callout",
        ),
        p("Your accepted construction", "H2"),
        submitted,
        Spacer(1, 5),
        code(
            "wire w1, w2;\n"
            "xor g1 (w1, c, d);\n"
            "xor g2 (w2, a, b);\n"
            "assign out = (~a & ~b) & w1 | (~c & ~d) & w2\n"
            "           | ( a &  b) & w1 | ( c &  d) & w2;"
        ),
        p(
            "Read it aloud as: first condition <b>OR</b> second condition <b>OR</b> "
            "third condition <b>OR</b> fourth condition. Parentheses would make the grouping "
            "easier to scan, although Verilog already evaluates <font name='Consolas'>&amp;</font> "
            "before <font name='Consolas'>|</font>.",
        ),
        p(
            "Source: <link href='https://hdlbits.01xz.net/wiki/Kmap4' color='#087F8C'>HDLBits Kmap4</link>. "
            "The saved submission evidence shows <b>Status: Success!</b>.",
            "Small",
        ),
        PageBreak(),
    ]

    comparison_rows = [
        [p("Inputs", "CellHead"), p("Bitwise OR", "CellHead"), p("Arithmetic addition", "CellHead")],
        [p("0 and 0", "Cell"), p("0 | 0 = 0", "Cell"), p("0 + 0 = 0", "Cell")],
        [p("0 and 1", "Cell"), p("0 | 1 = 1", "Cell"), p("0 + 1 = 1", "Cell")],
        [p("1 and 1", "Cell"), p("1 | 1 = 1", "Cell"), p("1 + 1 = binary 10", "Cell")],
    ]
    story += page_title(
        "ENTRY 161  /  OPERATOR CHECK",
        "Why + can appear to work here",
        "Arithmetic and OR differ as soon as two true terms overlap. This particular expression hides that difference because its four product terms are mutually exclusive.",
    )
    story += [
        table(comparison_rows, [100, 180, 219], "CENTER"),
        Spacer(1, 8),
        p("The carry is the warning", "H2"),
        code(
            "wire term1 = 1'b1;\n"
            "wire term2 = 1'b1;\n"
            "wire       out_or = term1 | term2;                 // 1\n"
            "wire [1:0] sum    = {1'b0,term1} + {1'b0,term2};  // 2'b10"
        ),
        p(
            "If an arithmetic result is kept in only one bit, its carry can be discarded. "
            "That can turn <font name='Consolas'>1 + 1</font> into a stored 0, while OR must remain 1. "
            "The explicit two-bit operands above expose the carry instead of relying on expression-size rules.",
        ),
        p("Why the submitted terms never overlap", "H2"),
        p(
            "<font name='Consolas'>w1 = c ^ d</font> is 1 only when <font name='Consolas'>c,d</font> differ. "
            "Its two terms then select either <font name='Consolas'>a,b = 00</font> or "
            "<font name='Consolas'>a,b = 11</font>. Similarly, <font name='Consolas'>w2 = a ^ b</font> "
            "is 1 only when <font name='Consolas'>a,b</font> differ, and its terms require "
            "<font name='Consolas'>c,d = 00</font> or <font name='Consolas'>c,d = 11</font>. "
            "Those cases cannot be true together, so at most one product term is 1.",
        ),
        p("What the exhaustive check proves", "H2"),
        p(
            "All 16 input combinations were checked. The submitted expression equals "
            "<font name='Consolas'>a ^ b ^ c ^ d</font>, and never has two active product terms. "
            "Therefore <font name='Consolas'>+</font> could accidentally match for this exact expression - "
            "but <font name='Consolas'>|</font> is still the correct, intention-revealing operator.",
            "Callout",
        ),
        PageBreak(),
    ]

    form_rows = [
        [p("Form", "CellHead"), p("Structure", "CellHead"), p("K-map route", "CellHead")],
        [
            p("SOP", "Cell"),
            p("OR of product terms; each product term is an AND of literals.", "Cell"),
            p("Group output-1 cells, write one product term per group, then OR the terms.", "Cell"),
        ],
        [
            p("POS", "Cell"),
            p("AND of sum terms; each sum term is an OR of literals.", "Cell"),
            p("Group output-0 cells, write one sum term per group, then AND the terms.", "Cell"),
        ],
    ]
    story += page_title(
        "ENTRY 164  /  BOOLEAN FORMS",
        "SOP, POS and De Morgan's law",
        "SOP and POS are two ways to implement the same Boolean function. The difference is the form used to describe it, not a different output.",
    )
    story += [
        table(form_rows, [58, 220, 221]),
        Spacer(1, 8),
        p("A precise way to remember them", "H2"),
        p(
            "For SOP, each 1-group creates a condition that makes the function true. For POS, each "
            "0-group creates a sum term that becomes false on that group; ANDing the sum terms blocks "
            "the zero cases. Both final expressions still calculate the same output.",
        ),
        p(
            "Correction to the earlier short note: saying 'SOP describes when the output is 1 and POS "
            "describes when it is 0' was too loose. The accurate statement is that the <b>derivation</b> "
            "starts from 1-cells for SOP and 0-cells for POS.",
            "Callout",
        ),
        p("De Morgan's law", "H2"),
        code("~(A & B) = (~A) | (~B)\n~(A | B) = (~A) & (~B)"),
        p(
            "When a NOT moves through a bracket, AND and OR swap, and every literal inside is "
            "complemented. This is needed when complementing grouped logic or converting a design into "
            "NAND/NOR-friendly form. It is different from factoring or distributing terms.",
        ),
        p("Why both forms are useful", "H2"),
        p(
            "A truth table may produce fewer gates in one form than the other. The exercise requests "
            "both so that you can simplify from the 1-cells and independently from the 0-cells, then "
            "recognize that the resulting circuits satisfy the same specified rows.",
        ),
        PageBreak(),
    ]

    row_sets = [
        [p("Required output", "CellHead"), p("abcd row numbers", "CellHead"), p("Meaning", "CellHead")],
        [p("1", "Cell"), p("2, 7, 15", "Cell"), p("The expression must be true.", "Cell")],
        [p("0", "Cell"), p("0, 1, 4, 5, 6, 9, 10, 13, 14", "Cell"), p("The expression must be false.", "Cell")],
        [p("Don't care", "Cell"), p("3, 8, 11, 12", "Cell"), p("Either value is allowed and may aid simplification.", "Cell")],
    ]
    story += page_title(
        "ENTRY 164  /  ACCEPTED SOLUTION",
        "Applying SOP and POS to the problem",
        "The two accepted assignments are equivalent for every input, and they meet all of the problem's specified truth-table rows.",
    )
    story += [
        code(
            "assign out_sop = (c & d) | (~a & ~b & c);\n"
            "assign out_pos = c & (d | ~a) & (d | ~b);"
        ),
        p("Read the names from the outside inward", "H2"),
        p(
            "The SOP has two ANDed product terms joined by OR. The POS has the literal "
            "<font name='Consolas'>c</font> and two ORed sum terms joined by AND. A single literal may "
            "act as a one-literal product or sum term.",
        ),
        p("Why these two lines are equivalent", "H2"),
        code(
            "(c & d) | (~a & ~b & c)\n"
            "= c & (d | (~a & ~b))             // factor c\n"
            "= c & (d | ~a) & (d | ~b)         // distribute OR over AND"
        ),
        p(
            "That conversion uses the Boolean distributive identity "
            "<font name='Consolas'>X | (Y &amp; Z) = (X | Y) &amp; (X | Z)</font>. It is <b>not</b> "
            "a De Morgan step because no NOT covers the bracket.",
        ),
        table(row_sets, [100, 185, 214]),
        Spacer(1, 7),
        p(
            "The four don't-care rows can be chosen as 0 or 1 during minimization. Because of that "
            "freedom, more than one equally small POS may be valid; the accepted pair above deliberately "
            "implements one consistent value even on the don't-care rows.",
            "Callout",
        ),
        p(
            "Source: <link href='https://hdlbits.01xz.net/wiki/Exams/ece241_2013_q2' color='#087F8C'>HDLBits Exams/ece241_2013_q2</link>.",
            "Small",
        ),
        PageBreak(),
    ]

    rule_rows = [
        [p("Left", "CellHead"), p("Center", "CellHead"), p("Right", "CellHead"), p("Next center", "CellHead")],
        *[
            [p(str(l), "Cell"), p(str(c), "Cell"), p(str(r), "Cell"), p(str(l ^ r), "Cell")]
            for l, c, r in (
                (1, 1, 1),
                (1, 1, 0),
                (1, 0, 1),
                (1, 0, 0),
                (0, 1, 1),
                (0, 1, 0),
                (0, 0, 1),
                (0, 0, 0),
            )
        ],
    ]
    story += page_title(
        "ENTRY 168  /  RULE 90",
        "One whole generation changes at a time",
        "For every cell i, Rule 90 ignores the current center bit and XORs the current left and right neighbours.",
    )
    story += [
        code("next_q[i] = q[i-1] ^ q[i+1]"),
        p(
            "The eight next-state results, read from neighbourhood 111 down to 000, are "
            "<font name='Consolas'>01011010</font>. Interpreted as a binary number, that is decimal 90 - "
            "hence the rule's name.",
        ),
        table(rule_rows, [90, 100, 90, 219], "CENTER"),
        Spacer(1, 7),
        p("Boundary cells", "H2"),
        p(
            "The imaginary neighbours outside the 512-cell vector are zero: "
            "<font name='Consolas'>q[-1] = 0</font> and <font name='Consolas'>q[512] = 0</font>. Therefore "
            "<font name='Consolas'>next_q[0] = q[1]</font> and "
            "<font name='Consolas'>next_q[511] = q[510]</font>.",
        ),
        p("The same rule as one vector expression", "H2"),
        code("{q[510:0], 1'b0} ^ {1'b0, q[511:1]}"),
        p(
            "The first shifted vector places <font name='Consolas'>q[i-1]</font> at bit i; the second "
            "places <font name='Consolas'>q[i+1]</font> at bit i. The inserted zeros implement the two "
            "outside boundaries.",
        ),
        p(
            "All cells must use the <b>same old generation</b>. They are not updated one by one in time. "
            "The design computes all 512 next bits as combinational logic, then the clock stores them together.",
            "Callout",
        ),
        PageBreak(),
    ]

    story += page_title(
        "ENTRY 168  /  YOUR ACCEPTED STRUCTURE",
        "Why nextVal is used - and whether it is required",
        "nextVal is a 512-bit combinational candidate for the next generation; q is the 512-bit register holding the current generation.",
    )
    story += [
        code(
            "integer i;\n"
            "reg [511:0] nextVal;\n"
            "\n"
            "always @(posedge clk) begin\n"
            "    if (load)\n"
            "        q <= data;\n"
            "    else\n"
            "        q <= nextVal;\n"
            "end\n"
            "\n"
            "always @(*) begin\n"
            "    nextVal[0]   = q[1];\n"
            "    nextVal[511] = q[510];\n"
            "    for (i = 1; i < 511; i = i + 1)\n"
            "        nextVal[i] = q[i-1] ^ q[i+1];\n"
            "end",
            font_size=7.45,
            leading=9.25,
        ),
        p("Why you used it", "H2"),
        p(
            "The combinational block calculates every bit of the upcoming state from the unchanged current "
            "<font name='Consolas'>q</font>. At the rising edge, the clocked block either loads "
            "<font name='Consolas'>data</font> or captures that complete candidate with the nonblocking "
            "assignment <font name='Consolas'>q &lt;= nextVal</font>. This cleanly separates "
            "<b>current state</b> from <b>next-state logic</b>.",
        ),
        p("Is nextVal actually required?", "H2"),
        p(
            "No. It is required by <i>this two-process organization</i>, but Rule 90 does not require a "
            "separate named signal. The same next-state network can be written directly:",
        ),
        code(
            "always @(posedge clk) begin\n"
            "    if (load) q <= data;\n"
            "    else      q <= {q[510:0], 1'b0} ^ {1'b0, q[511:1]};\n"
            "end",
            font_size=7.8,
            leading=9.7,
        ),
        p(
            "Both styles describe essentially the same XOR wiring and 512 state bits. "
            "<font name='Consolas'>nextVal</font> improves readability and is convenient in a waveform; it "
            "does not add another clock cycle or another bank of registers. The synthesis loop is unrolled "
            "into hardware rather than executing 510 times over time.",
        ),
        p("Two important safety points", "H2"),
        p(
            "Every bit of <font name='Consolas'>nextVal</font> is assigned (two boundaries plus indices "
            "1 through 510), so the combinational block does not infer a latch. Also avoid updating "
            "<font name='Consolas'>q</font> in place with blocking assignments inside a loop: later iterations "
            "could read already-changed neighbours and would no longer represent a simultaneous generation.",
        ),
        p(
            "Source: <link href='https://hdlbits.01xz.net/wiki/Rule90' color='#087F8C'>HDLBits Rule90</link>. "
            "The current submission panel was rechecked and shows <b>Status: Success!</b>.",
            "Small",
        ),
        PageBreak(),
    ]

    rule110_rows = [
        [p("Left", "CellHead"), p("Center", "CellHead"), p("Right", "CellHead"), p("Next center", "CellHead")],
        *[
            [p(str(l), "Cell"), p(str(c), "Cell"), p(str(r), "Cell"), p(str(value), "Cell")]
            for l, c, r, value in (
                (1, 1, 1, 0),
                (1, 1, 0, 1),
                (1, 0, 1, 1),
                (1, 0, 0, 0),
                (0, 1, 1, 1),
                (0, 1, 0, 1),
                (0, 0, 1, 1),
                (0, 0, 0, 0),
            )
        ],
    ]
    story += page_title(
        "ENTRY 172  /  RULE 110",
        "Rule 110 uses left, center and right",
        "Unlike Rule 90, Rule 110 is asymmetric: swapping the left and right neighbours can change the answer. Keep the vector direction fixed while translating the table.",
    )
    story += [
        table(rule110_rows, [90, 100, 90, 219], "CENTER"),
        Spacer(1, 7),
        p(
            "Read from neighbourhood 111 down to 000, the next-state column is "
            "<font name='Consolas'>01101110</font>, which is decimal 110.",
        ),
        p("A compact Boolean form", "H2"),
        code(
            "next = (~L & C) | (C & ~R) | (~C & R)\n"
            "     = (R ^ C) | (R & ~L)"
        ),
        p(
            "The XOR term handles the rows where center and right differ. The extra "
            "<font name='Consolas'>R &amp; ~L</font> term adds neighbourhood 011, the remaining row "
            "whose output is 1.",
        ),
        p("Vector direction in your accepted code", "H2"),
        code("L = q[i+1]     C = q[i]     R = q[i-1]"),
        p(
            "With that mapping, <font name='Consolas'>(R ^ C) | (R &amp; ~L)</font> becomes exactly "
            "the interior expression you submitted. This direction also explains the successful trace "
            "from a loaded value of 1: "
            "<font name='Consolas'>1, 3, 7, d, 1f, 31, 73, d7, 1fd, 307</font>.",
        ),
        p(
            "Direction is the important difference from Rule 90. Rule 90 XORs left and right, so "
            "mirroring them changes nothing. Rule 110 gives them different roles.",
            "Callout",
        ),
        PageBreak(),
    ]

    story += page_title(
        "ENTRY 172  /  YOUR ACCEPTED STRUCTURE",
        "Why the Rule 110 expression works",
        "The structure again separates the registered current generation q from the combinational next generation nextval.",
    )
    story += [
        code(
            "reg [511:0] nextval;\n"
            "integer i;\n"
            "\n"
            "always @(posedge clk) begin\n"
            "    if (load)\n"
            "        q <= data;\n"
            "    else\n"
            "        q <= nextval;\n"
            "end\n"
            "\n"
            "always @(*) begin\n"
            "    nextval[511] = q[511] | q[510];\n"
            "    nextval[0]   = q[0];\n"
            "    for (i = 1; i < 511; i = i + 1)\n"
            "        nextval[i] = q[i-1] ^ q[i] | ~q[i+1] & q[i-1];\n"
            "end",
            font_size=7.35,
            leading=9.1,
        ),
        p("How Verilog groups the interior expression", "H2"),
        code(
            "nextval[i] = (q[i-1] ^ q[i])\n"
            "           | ((~q[i+1]) & q[i-1]);"
        ),
        p(
            "Unary <font name='Consolas'>~</font> binds first, then "
            "<font name='Consolas'>&amp;</font>, then <font name='Consolas'>^</font>, and finally "
            "<font name='Consolas'>|</font>. The added parentheses do not change the hardware; they make "
            "the intended <font name='Consolas'>(R ^ C) | (R &amp; ~L)</font> form obvious.",
        ),
        p("Why the two boundary assignments are different", "H2"),
        p(
            "At bit 0, the outside right neighbour is 0, so the rule reduces to "
            "<font name='Consolas'>nextval[0] = q[0]</font>. At bit 511, the outside left neighbour is 0, "
            "so the rule reduces to <font name='Consolas'>nextval[511] = q[511] | q[510]</font>. "
            "These are simplifications of the same rule, not special exceptions.",
        ),
        p("Why nextval is still useful", "H2"),
        p(
            "As in Rule 90, <font name='Consolas'>nextval</font> lets all 512 cells be calculated from the "
            "unchanged current <font name='Consolas'>q</font> before one clock edge stores the whole result. "
            "Every bit is assigned, so no latch is inferred. The name is convenient, not mandatory; a "
            "direct clocked implementation with nonblocking assignments could describe the same state update.",
        ),
        p(
            "Source: <link href='https://hdlbits.01xz.net/wiki/Rule110' color='#087F8C'>HDLBits Rule110</link>. "
            "The current compile-and-simulate panel was rechecked and shows <b>Status: Success!</b>.",
            "Small",
        ),
    ]

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    TEMP_OUTPUT.replace(OUTPUT)

    import fitz

    pdf = fitz.open(OUTPUT)
    if len(pdf) != 8:
        raise ValueError(f"Expected 8 technical pages, found {len(pdf)}")
    # ReportLab emits an unused Helvetica setup command even though every
    # visible glyph uses embedded Arial or Consolas. Remove that empty command
    # and its resource so the PDF contains no viewer-dependent font.
    for page in pdf:
        for xref in page.get_contents():
            stream = pdf.xref_stream(xref)
            cleaned = re.sub(rb"BT /F1 [0-9.]+ Tf [0-9.]+ TL ET", b"", stream)
            if cleaned != stream:
                pdf.update_stream(xref, cleaned)
    font_resources = pdf.xref_object(1)
    if "/F1 2 0 R" in font_resources:
        pdf.update_object(1, font_resources.replace("/F1 2 0 R", ""))
    expected_headings = [
        "Why the K-map expression uses |, not +",
        "Why + can appear to work here",
        "SOP, POS and De Morgan's law",
        "Applying SOP and POS to the problem",
        "One whole generation changes at a time",
        "Why nextVal is used - and whether it is required",
        "Rule 110 uses left, center and right",
        "Why the Rule 110 expression works",
    ]
    for page, heading in zip(pdf, expected_headings):
        page_text = " ".join(page.get_text().split())
        if heading not in page_text:
            raise ValueError(f"Missing heading on technical page {page.number + 1}: {heading}")
    metadata = pdf.metadata
    metadata.update(
        {
            "title": "K-map operators, Boolean forms and Rules 90/110",
            "author": "Kapil Tripathi",
            "subject": "HDLBits Attempt 2 entries 161, 164, 168 and 172",
            "keywords": "HDLBits; K-map; SOP; POS; De Morgan; Rule 90; Rule 110; next state",
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
