# Day 14 — 2026-07-07

Completed problems: **5**

Each screenshot is rendered directly in this page for revision. The image is not wrapped in a click-only link.

## Index

| # | Time | Problem | Section | Problem note | Page contents | Source |
|---:|---|---:|---|---|---|---|
| 1 | 12:59:38 AM | [175](#problem-175) | Sequential Logic | [Rule 90](problems/Day%2014/175-rule90.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/rule90) |
| 2 | 1:30:23 AM | [176](#problem-176) | Sequential Logic | [Rule 110](problems/Day%2014/176-rule110.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/rule110) |
| 3 | 1:36:14 AM | [177](#problem-177) | Sequential Logic | [Q2a: Arbiter FSM](problems/Day%2014/177-exams__2013_q2afsm.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/2013_q2afsm) |
| 4 | 12:49:56 PM | [178](#problem-178) | Building Larger Circuits | [FSM: One-hot logic equations](problems/Day%2014/178-exams__review2015_fsmonehot.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/review2015_fsmonehot) |
| 5 | 1:36:17 PM | [179](#problem-179) | Sequential Logic | [Conway's Game of Life 16x16](problems/Day%2014/179-conwaylife.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/conwaylife) |

---

<a id="problem-175"></a>
## 175 — Rule 90

[Problem note](problems/Day%2014/175-rule90.md) · [Verilog file](solutions/Day%2014/175-rule90.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/rule90)

![Rule 90 question and submitted solution](images/Day%2014/175-rule90-question-and-successful-submission.png)

### What the question is asking

Rule 90 is a one-dimensional cellular automaton in which every cell's next value is the XOR of its left and right neighbors; the current value of the cell itself is irrelevant. For a 512-bit row, the interior equation is q_next[i] = q[i-1] ^ q[i+1]. The two boundaries have an implied zero neighbor, so the leftmost cell uses only its one real neighbor and the rightmost cell does the same.

The implementation computes the complete next row from the old registered q and loads it on one rising edge with a nonblocking assignment. The load input has priority and synchronously replaces all 512 cells with data. Concatenated shifted versions of q provide the zero padding compactly and avoid 512 handwritten equations. Verification should test a single live cell, an alternating pattern, both edges, and load priority; each expected row must be calculated from the same pre-edge generation, never from partially updated cells.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input load,
    input [511:0] data,
    output reg [511:0] q
);
    integer i;

    always @(posedge clk) begin
        if (load)
            q <= data;
        else begin
            for (i = 0; i < 512; i = i + 1) begin
                if (i == 0)
                    q[i] <= q[i+1] ^ 1'b0;
                else if (i == 511)
                    q[i] <= q[i-1] ^ 1'b0;
                else
                    q[i] <= q[i-1] ^ q[i+1];
            end
        end
    end
endmodule
```

---

<a id="problem-176"></a>
## 176 — Rule 110

[Problem note](problems/Day%2014/176-rule110.md) · [Verilog file](solutions/Day%2014/176-rule110.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/rule110)

![Rule 110 question and submitted solution](images/Day%2014/176-rule110-question-and-successful-submission.png)

### What the question is asking

Rule 110 updates each cell from the three-bit neighborhood {left, center, right}. Its truth table produces 0 for 111, 100, and 000, and 1 for 110, 101, 011, 010, and 001. The saved design evaluates that Boolean rule across all 512 cells in parallel, with nonexistent neighbors outside the row treated as zero.

As with Rule 90, q is the only state. A synchronous load has priority over evolution and installs the entire data row on a rising edge. Otherwise one clock advances exactly one generation, because every right-hand side reads the old q before any nonblocking update becomes visible. Boundary padding is part of the functional specification and must be checked separately from interior cells. A robust review compares the coded expression against all eight neighborhood combinations, then checks edge neighborhoods and two consecutive generations to detect reversed neighbor order or in-place-update mistakes.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input load,
    input [511:0] data,
    output reg [511:0] q
);
    integer i;
    reg lsb, center, msb;

    always @(posedge clk) begin
        if (load)
            q <= data;
        else begin
            for (i = 0; i < 512; i = i + 1) begin
                if (i == 0)
                    lsb = 1'b0;
                else
                    lsb = q[i-1];

                center = q[i];
                if (i == 511)
                    msb = 1'b0;
                else
                    msb = q[i+1];

                case ({msb, center, lsb})
                    3'b000: q[i] <= 1'b0;
                    3'b001: q[i] <= 1'b1;
                    3'b010: q[i] <= 1'b1;
                    3'b011: q[i] <= 1'b1;
                    3'b100: q[i] <= 1'b0;
                    3'b101: q[i] <= 1'b1;
                    3'b110: q[i] <= 1'b1;
                    3'b111: q[i] <= 1'b0;
                endcase
            end
        end
    end
endmodule
```

---

<a id="problem-177"></a>
## 177 — Q2a: Arbiter FSM

[Problem note](problems/Day%2014/177-exams__2013_q2afsm.md) · [Verilog file](solutions/Day%2014/177-exams__2013_q2afsm.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/2013_q2afsm)

![Q2a: Arbiter FSM question and submitted solution](images/Day%2014/177-exams__2013_q2afsm-question-and-successful-submission.png)

### What the question is asking

This arbiter FSM grants access according to the request conditions in the supplied state diagram. Each state represents the currently selected ownership or idle condition, and the combinational transition block follows the diagram for every request combination. The clocked state register applies the specified reset and makes grants stable for a complete cycle. Outputs are Moore decodes of the registered state, preventing combinational request glitches from appearing directly on grant lines.

The earlier attempt evidence is retained because it shows why a complete transition table matters: missing request combinations or an incorrect priority can strand the controller or grant the wrong requester. The corrected version assigns next_state for every legal state, includes a safe default for unused encodings, and decodes mutually exclusive grants from state. Verification should cover idle entry, each independent request, simultaneous requests, request withdrawal, and reset from every grant state.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input resetn,
    input [3:1] r,
    output [3:1] g
);
    reg [1:0] state, next_state;
    parameter idle = 2'b00;
    parameter s1 = 2'b01;
    parameter s2 = 2'b10;
    parameter s3 = 2'b11;

    always @(posedge clk) begin
        if (!resetn)
            state <= idle;
        else
            state <= next_state;
    end

    always @(*) begin
        case (state)
            idle: begin
                if (r[1])
                    next_state = s1;
                else if (r[2])
                    next_state = s2;
                else if (r[3])
                    next_state = s3;
                else
                    next_state = idle;
            end
            s1: next_state = r[1] ? s1 : idle;
            s2: next_state = r[2] ? s2 : idle;
            s3: next_state = r[3] ? s3 : idle;
            default: next_state = idle;
        endcase
    end

    assign g[1] = (state == s1);
    assign g[2] = (state == s2);
    assign g[3] = (state == s3);
endmodule
```

---

<a id="problem-178"></a>
## 178 — FSM: One-hot logic equations

[Problem note](problems/Day%2014/178-exams__review2015_fsmonehot.md) · [Verilog file](solutions/Day%2014/178-exams__review2015_fsmonehot.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/review2015_fsmonehot)

![FSM: One-hot logic equations question and submitted solution](images/Day%2014/178-exams__review2015_fsmonehot-question-and-successful-submission.png)

### What the question is asking

This exercise extracts only selected one-hot equations from the complete timer controller. The supplied `state[9:0]` vector already represents the present state, so the module must not create a state register or recode the FSM. Each requested `*_next` output is the OR of every transition entering that destination state.

For example, `B3_next` is high only when the current state is `B2`, because the B0-B3 shift phase advances unconditionally one state per clock. `Count_next` is high when the current state is `B3` or when the controller is already in `Count` and `done_counting` is still low. `Wait_next` is high when counting has just completed or when the controller is already waiting and `ack` has not arrived.

The output equations are direct Moore decodes from the current one-hot state: `done` is `state[Wait]`, `counting` is `state[Count]`, and `shift_ena` is the OR of B0 through B3. The key review habit is destination-first derivation: list incoming arrows for each requested destination bit and translate those arrows directly into sum-of-products logic.

### Saved Verilog solution

```verilog
module top_module(
    input d,
    input done_counting,
    input ack,
    input [9:0] state,
    output B3_next,
    output S_next,
    output S1_next,
    output Count_next,
    output Wait_next,
    output done,
    output counting,
    output shift_ena
);
    parameter S=0, S1=1, S11=2, S110=3, B0=4, B1=5, B2=6, B3=7, Count=8, Wait=9;

    assign B3_next = state[B2];
    assign S_next = (state[S] & ~d) | (state[S1] & ~d) |
                    (state[S110] & ~d) | (state[Wait] & ack);
    assign S1_next = state[S] & d;
    assign Count_next = state[B3] | (state[Count] & ~done_counting);
    assign Wait_next = (state[Count] & done_counting) | (state[Wait] & ~ack);

    assign done = state[Wait];
    assign counting = state[Count];
    assign shift_ena = state[B0] | state[B1] | state[B2] | state[B3];
endmodule
```

---

<a id="problem-179"></a>
## 179 — Conway's Game of Life 16x16

[Problem note](problems/Day%2014/179-conwaylife.md) · [Verilog file](solutions/Day%2014/179-conwaylife.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/conwaylife)

![Conway's Game of Life 16x16 question and submitted solution](images/Day%2014/179-conwaylife-question-and-successful-submission.png)

### What the question is asking

The Game of Life state is a 16 by 16 toroidal grid packed into `q[255:0]`, with each row occupying a 16-bit slice. A cell's next value depends on the count of its eight neighbours, while the load input synchronously replaces the whole grid with `data` for initialization.

The toroidal boundary condition is the important part: row 0's upper neighbour is row 15, row 15's lower neighbour is row 0, column 0's left neighbour is column 15, and column 15's right neighbour is column 0. The implementation computes those wrapped row and column indices for every cell, accumulates the eight one-bit neighbour values into an integer count, and writes the corresponding bit of `next_q`.

The update rule follows the problem statement exactly. A cell becomes alive when it has exactly three neighbours. With exactly two neighbours it keeps its previous state, so the expression is `neighbours == 3 || (q[index] && neighbours == 2)`. All `next_q` bits are computed combinationally from the old registered `q`, then one clock edge commits the whole generation with a nonblocking assignment. This avoids accidentally updating one cell early and letting that new value affect another cell in the same generation.

### Saved Verilog solution

```verilog
module top_module(
    input clk,
    input load,
    input [255:0] data,
    output reg [255:0] q
);
    reg [255:0] next_q;
    integer row;
    integer col;
    integer up;
    integer down;
    integer left;
    integer right;
    integer index;
    integer neighbours;

    always @(*) begin
        next_q = 256'b0;
        for (row = 0; row < 16; row = row + 1) begin
            for (col = 0; col < 16; col = col + 1) begin
                up = (row == 0) ? 15 : row - 1;
                down = (row == 15) ? 0 : row + 1;
                left = (col == 0) ? 15 : col - 1;
                right = (col == 15) ? 0 : col + 1;
                index = row * 16 + col;

                neighbours = 0;
                neighbours = neighbours + q[up * 16 + left];
                neighbours = neighbours + q[up * 16 + col];
                neighbours = neighbours + q[up * 16 + right];
                neighbours = neighbours + q[row * 16 + left];
                neighbours = neighbours + q[row * 16 + right];
                neighbours = neighbours + q[down * 16 + left];
                neighbours = neighbours + q[down * 16 + col];
                neighbours = neighbours + q[down * 16 + right];

                next_q[index] = (neighbours == 3) ||
                                (q[index] && (neighbours == 2));
            end
        end
    end

    always @(posedge clk) begin
        if (load)
            q <= data;
        else
            q <= next_q;
    end
endmodule
```
