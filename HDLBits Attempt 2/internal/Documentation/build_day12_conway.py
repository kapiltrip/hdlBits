"""Six technical Conway pages; the collection indexer adds the reading cover."""
from pathlib import Path
import re

from build_day12_lfsr_series import (
    p, q, code, table, page_title, source, A4, SimpleDocTemplate,
    PageBreak, NAVY, TEAL, MUTED, GRID,
)
import fitz

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "HDLBits_Day12_Conway_Grid_Indexing_and_Next_State.pdf"
RTL = Path(__file__).with_name("conway_reference.v")
HEADINGS = [
    "Why the index is row * 16 + col",
    "Wrap coordinates before flattening",
    "Every cell reads the same old generation",
    "The complete two-process solution",
    "What the loops and assignments mean in hardware",
    "Trace the boundary, then test the whole grid",
]


def on_page(canvas, doc):
    w, h = A4
    canvas.saveState()
    canvas.setFillColor(TEAL)
    canvas.rect(0, h-9, w, 9, stroke=0, fill=1)
    canvas.setFont("Arial-Bold", 7.6)
    canvas.setFillColor(MUTED)
    canvas.drawString(48, h-31, "DAY 12  /  CONWAY'S GAME OF LIFE")
    canvas.drawRightString(w-48, h-31, f"TECHNICAL PAGE {doc.page} OF 6")
    canvas.setStrokeColor(GRID)
    canvas.line(48, h-39, w-48, h-39)
    canvas.restoreState()


def build():
    story = page_title("ENTRY 177  /  GRID REPRESENTATION", HEADINGS[0],
        "The circuit stores 256 cells in q[255:0]. A row has 16 cells, so the start of row r is bit 16r. Column c selects the c-th bit after that start.")
    story += [
        q('Your editor question: "why and how to calc the row and col index, discuss."'),
        p("Derive the address from rows already skipped", "H2"),
        p("Before row 3 there are three complete rows: 3 x 16 = 48 cells. Moving to column 5 adds five more positions. Therefore cell (3,5) is q[53]. Both coordinates start at zero. Multiplication by 16 supplies the row offset; addition supplies the position inside that row."),
        table([["Coordinate or row", "Vector location", "Reason"],
               ["(0,0)", "q[0]", "0 x 16 + 0"],
               ["Row 0", "q[15:0]", "Indices 0 through 15"],
               ["Row 1", "q[31:16]", "Indices 16 through 31"],
               ["(3,5)", "q[53]", "48 + 5"],
               ["(15,15)", "q[255]", "240 + 15"]], [130,130,239]),
        p("Recover the coordinates", "H2"),
        code("index = row * 16 + col;\nrow   = index / 16;  // integer quotient\ncol   = index % 16;  // remainder"),
        p("For index 53, integer division gives row 3 and the remainder gives column 5. For a nonnegative 8-bit index, the upper four bits identify the row and the lower four identify the column. This is the binary meaning of dividing a 16-column grid into rows."),
        p("Vector print order versus coordinate order", "H2"),
        p("The notation q[15:0] prints bit 15 on the left, but our coordinate convention calls q[0] column 0. Keep that convention consistent in neighbors and traces. Reversing how a row is drawn does not change the recurrence if every coordinate mapping is reversed consistently."),
        source("HDLBits Conwaylife", "https://hdlbits.01xz.net/wiki/Conwaylife", "The problem specifies the row-to-vector mapping and a 16 x 16 grid."),
        PageBreak(),
    ]
    story += page_title("BOUNDARIES  /  TOROIDAL NEIGHBORS", HEADINGS[1],
        "A toroid connects top to bottom and left to right. Wrap the row and column independently, then turn each coordinate pair into a bit index.")
    story += [
        code("up    = (row == 0)  ? 15 : row - 1;\ndown  = (row == 15) ? 0  : row + 1;\nleft  = (col == 0)  ? 15 : col - 1;\nright = (col == 15) ? 0  : col + 1;"),
        p("The eight neighbors of cell (0,0)", "H2"),
        table([["Direction", "Wrapped coordinate", "Read from old q"],
               ["Up-left", "(15,15)", "q[255]"], ["Up", "(15,0)", "q[240]"],
               ["Up-right", "(15,1)", "q[241]"], ["Left", "(0,15)", "q[15]"],
               ["Right", "(0,1)", "q[1]"], ["Down-left", "(1,15)", "q[31]"],
               ["Down", "(1,0)", "q[16]"], ["Down-right", "(1,1)", "q[17]"]], [130,180,189]),
        p("Why flat index + 1 can be wrong", "H2"),
        p("At (0,15), the right neighbor is (0,0), index 0. Incrementing flat index 15 gives 16, which is (1,0), a different row. Even taking (index + 1) % 256 does not fix that row-boundary error. Wrap col within 0..15 first, while preserving row."),
        p("Do not count the center", "H2"),
        p("The surrounding 3 x 3 square contains nine positions. The sum uses its eight outer positions and excludes q[row*16+col]. The center matters only for the two-neighbor survival rule. Every cell, including a corner, has eight distinct neighbors on this 16 x 16 toroid."),
        source("HDLBits Conwaylife", "https://hdlbits.01xz.net/wiki/Conwaylife", "The listed corner neighbors require wrapping on both axes."), PageBreak(),
    ]
    story += page_title("RULES  /  PRESENT AND NEXT VALUES", HEADINGS[2],
        "q is the registered current grid. next_q is the combinational result of applying one generation of rules to that grid. All neighbor reads come from q.")
    story += [
        table([["Live neighbors", "Current cell 0", "Current cell 1", "Assignment"],
               ["0 or 1", "0", "0", "next cell = 0"],
               ["2", "0", "1", "next cell = old cell"],
               ["3", "1", "1", "next cell = 1"],
               ["4 through 8", "0", "0", "next cell = 0"]], [100,100,100,199]),
        p("Why copy q when count is two?", "H2"),
        p("Two neighbors preserve the center's existing state: a dead center stays dead and a live center stays live. Setting it unconditionally to 1 would incorrectly create a new cell. Copying q[row*16+col] expresses precisely that conditional survival."),
        p("A generation must use one consistent snapshot", "H2"),
        p("Suppose an earlier loop iteration kills a neighbor. A later cell must still see that neighbor's old live value when computing this same generation. Reading partly updated next_q would mix two generations and make the result depend on loop traversal order. Reading only q avoids this contamination."),
        code("// Between rising edges:\nnext_q = F(q);\n\n// At the rising edge:\nif (load) q <= data;\nelse      q <= next_q;"),
        p("next_q is a signal, not a function call", "H2"),
        p("The combinational process already calculates next_q as q changes. At the edge, q &lt;= next_q samples that calculated value and schedules the register update. After q changes, the combinational logic settles to the following generation's candidate. There is still only one registered advance per clock."),
        p("When a separate next value is optional", "H2"),
        p("A single clocked process can instead assign each q bit with a nonblocking expression that reads only old q. In that version no next_q signal is needed. Keep the two-process form here because it clearly separates neighbor calculation from storage. Do not register next_q in another clocked block unless an additional pipeline cycle is intended."),
        source("HDLBits Conwaylife", "https://hdlbits.01xz.net/wiki/Conwaylife", "Rules and the one-generation-per-clock requirement."), PageBreak(),
    ]
    story += page_title("COMPLETE RTL  /  ONE OWNER FOR q", HEADINGS[3],
        "This is the editor solution with formatting and comments clarified. The combinational block assigns next_q; the rising-edge block alone assigns q.")
    story += [code(RTL.read_text(), font_size=8.2, leading=10.4),
        p("load has priority: the loading edge stores data unchanged. The first evolved generation is stored on the next rising edge with load low. There is no reset port in this interface; load supplies the initial grid.", "Small"), PageBreak()]
    story += page_title("EXECUTION  /  WIDTHS AND STORAGE", HEADINGS[4],
        "Verilog source order describes how to calculate a result within a process. Clock edges determine when the stored grid changes. These are different kinds of sequencing.")
    story += [
        p("The nested loops do not take 256 clocks", "H2"),
        p("Each fixed-bound loop visits 16 coordinates during one evaluation of the combinational block. Together they describe the next-value logic for all 256 cells. Synthesis can expand these constant bounds into hardware; one cell is not processed per edge. A resource-shared multi-cycle design would need an explicit controller, address counter and different timing."),
        p("Use blocking assignments for the calculation", "H2"),
        p("up, down, left and right must be available before the neighbor sum is evaluated. count must be available before the if statement reads it. Blocking = gives that immediate procedural calculation order. Nonblocking &lt;= is used for the clocked q update so the old grid is sampled before the new grid becomes visible."),
        p("Why integer count does not overflow at eight", "H2"),
        p("An integer is a 32-bit signed variable in Verilog. In this assignment, the addition is context-sized by that 32-bit destination, so the eight one-bit values are added at a sufficient width. All known inputs are 0 or 1, giving a result from 0 through 8. This code does not truncate each pairwise sum to one bit."),
        p("If refactoring the count into a function, concatenation or differently sized intermediate, check that expression's sizing rules again. Four unsigned bits are enough to represent 0..8. Explicitly zero-extending each bit to four bits before addition is a clear portable way to make the required width visible."),
        code("// Example of explicit width for one summand:\n{3'b000, q[up*16+left]}"),
        p("Defaults, latches and temporary variables", "H2"),
        p("next_q = q provides a complete default before the loop. In this exact code, all 256 bits also receive an assignment through the complete if/else chain, so the default is redundant but safe. The count==2 branch still explicitly implements hold. Removing both default coverage and an assignment path would risk a latch in a combinational process."),
        p("The integer declarations do not themselves create flip-flops. Here the loop coordinates and count are procedural calculation temporaries. q is the clocked storage. The synthesized circuit still needs the logic for all cell results; using one source-level count variable does not promise one time-shared physical adder."),
        p("Connect this to the timer-series question", "H2"),
        p("state &lt;= next_state and q &lt;= next_q both store a precomputed next value. In a timer, a test of state asks what state we are leaving; a test of next_state asks the chosen destination. Conway has no named controller states: q and next_q are the present and next complete board configurations. Neither name is a function invocation."), PageBreak(),
    ]
    story += page_title("WORKED TRACE  /  REVISION CHECKS", HEADINGS[5],
        "The seed 256'h7 lights row 0, columns 0, 1 and 2. It is a useful boundary test because its next generation reaches row 15 across the top seam.")
    story += [
        table([["Stored generation", "Live coordinates", "Set bit indices"],
               ["After load", "(0,0), (0,1), (0,2)", "0, 1, 2"],
               ["After one advance", "(15,1), (0,1), (1,1)", "241, 1, 17"],
               ["After two advances", "(0,0), (0,1), (0,2)", "0, 1, 2"]], [118,225,156]),
        p("Explain the first transition cell by cell", "H2"),
        p("The center (0,1) sees two live neighbors and stays alive. The endpoints (0,0) and (0,2) each see only one and die. The dead cells directly above and below the center each see all three original live cells, so they are born. Above row 0 means row 15, giving the seam-crossing vertical line."),
        p("A loading edge is not an evolution edge", "H2"),
        p("If load=1 and data=256'h7, that edge must leave q equal to 7, not the vertical line. While load remains high, each edge reloads the current data input. Once load becomes 0, each subsequent rising edge stores one generation. In simulation, inspect q after the nonblocking update has taken effect."),
        p("Useful independent checks", "H2"),
        table([["Case", "Expected behavior / defect exposed"],
               ["All zero", "Stays zero; no spontaneous births"],
               ["All one", "Every cell has eight neighbors, so the next grid is zero"],
               ["Single live cell", "Dies after one advance"],
               ["2 x 2 block", "Each live cell has three neighbors; the block remains fixed"],
               ["256'h7 blinker", "Two-cycle oscillation across the top seam"],
               ["Random loaded grids", "Compare every output bit to an independently indexed model"],
               ["All 512 local configurations", "Both center values for all 256 eight-neighbor patterns"]], [153,346]),
        p("Final mental check", "H2"),
        p("For any bit, recover row and col, wrap each neighbor coordinate, count eight old-q bits, apply the rule, and store the result on one edge. If a result differs, check coordinate wrapping before changing the rule. If the result is one generation late, check whether next_q was accidentally registered."),
        source("HDLBits Conwaylife", "https://hdlbits.01xz.net/wiki/Conwaylife", "The seed-7 oscillator is the problem's boundary-test hint."),
    ]
    tmp = ROOT / "internal/tmp/day12_conway/body.pdf"
    tmp.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(tmp), pagesize=A4, leftMargin=48, rightMargin=48,
                            topMargin=53, bottomMargin=52)
    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    pdf = fitz.open(tmp)
    assert len(pdf) == 6, len(pdf)
    for page, heading in zip(pdf, HEADINGS):
        assert heading in " ".join(page.get_text().split()), (page.number, heading)
        for xref in page.get_contents():
            stream = pdf.xref_stream(xref)
            pdf.update_stream(xref, re.sub(rb"BT /F1 [0-9.]+ Tf [0-9.]+ TL ET", b"", stream))
    for xref in range(1, pdf.xref_length()):
        obj = pdf.xref_object(xref, compressed=False)
        cleaned = re.sub(r"/F1\s+\d+\s+0\s+R", "", obj)
        if cleaned != obj:
            pdf.update_object(xref, cleaned)
    pdf.set_metadata({"title": "Conway: grid indexing and next-state timing", "author": "Kapil Tripathi",
                      "subject": "HDLBits Attempt 2 entry 177"})
    pdf.save(OUTPUT, garbage=4, deflate=True)
    pdf.close()
    print(OUTPUT)


if __name__ == "__main__":
    build()
