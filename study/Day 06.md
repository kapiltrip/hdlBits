# Day 06 — 2026-06-28

Completed problems: **21**

Each screenshot is embedded at the full width of the GitHub page. Select an image to open its original-resolution file.

## Index

| # | Time | Problem | Section | Problem note | Page contents | Source |
|---:|---|---:|---|---|---|---|
| 1 | 12:22:36 AM | [121](#problem-121) | Sequential Logic | [Q2b: Another FSM](problems/Day%2006/121-exams__2013_q2bfsm.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/2013_q2bfsm) |
| 2 | 12:54:12 AM | [122](#problem-122) | Finding bugs in code | [Mux](problems/Day%2006/122-bugs_mux2.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/bugs_mux2) |
| 3 | 1:04:51 AM | [123](#problem-123) | Finding bugs in code | [NAND](problems/Day%2006/123-bugs_nand3.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/bugs_nand3) |
| 4 | 1:01:34 AM | [124](#problem-124) | Finding bugs in code | [Mux](problems/Day%2006/124-bugs_mux4.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/bugs_mux4) |
| 5 | 1:31:18 AM | [125](#problem-125) | Finding bugs in code | [Add/sub](problems/Day%2006/125-bugs_addsubz.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/bugs_addsubz) |
| 6 | 1:28:42 AM | [126](#problem-126) | Finding bugs in code | [Case statement](problems/Day%2006/126-bugs_case.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/bugs_case) |
| 7 | 1:33:25 AM | [127](#problem-127) | Build a circuit from a simulation waveform | [Combinational circuit 1](problems/Day%2006/127-sim__circuit1.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/sim/circuit1) |
| 8 | 3:19:03 PM | [128](#problem-128) | Build a circuit from a simulation waveform | [Combinational circuit 2](problems/Day%2006/128-sim__circuit2.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/sim/circuit2) |
| 9 | 3:26:19 PM | [129](#problem-129) | Build a circuit from a simulation waveform | [Combinational circuit 3](problems/Day%2006/129-sim__circuit3.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/sim/circuit3) |
| 10 | 3:35:24 PM | [130](#problem-130) | Build a circuit from a simulation waveform | [Combinational circuit 4](problems/Day%2006/130-sim__circuit4.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/sim/circuit4) |
| 11 | 3:57:19 PM | [131](#problem-131) | Build a circuit from a simulation waveform | [Combinational circuit 5](problems/Day%2006/131-sim__circuit5.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/sim/circuit5) |
| 12 | 4:07:13 PM | [132](#problem-132) | Build a circuit from a simulation waveform | [Combinational circuit 6](problems/Day%2006/132-sim__circuit6.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/sim/circuit6) |
| 13 | 2:20:37 PM | [133](#problem-133) | Build a circuit from a simulation waveform | [Sequential circuit 7](problems/Day%2006/133-sim__circuit7.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/sim/circuit7) |
| 14 | 2:46:53 PM | [134](#problem-134) | Build a circuit from a simulation waveform | [Sequential circuit 8](problems/Day%2006/134-sim__circuit8.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/sim/circuit8) |
| 15 | 2:35:52 PM | [135](#problem-135) | Build a circuit from a simulation waveform | [Sequential circuit 9](problems/Day%2006/135-sim__circuit9.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/sim/circuit9) |
| 16 | 4:28:35 PM | [136](#problem-136) | Build a circuit from a simulation waveform | [Sequential circuit 10](problems/Day%2006/136-sim__circuit10.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/sim/circuit10) |
| 17 | 5:45:53 PM | [137](#problem-137) | Writing Testbenches | [Clock](problems/Day%2006/137-tb__clock.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/tb/clock) |
| 18 | 5:51:57 PM | [138](#problem-138) | Writing Testbenches | [Testbench1](problems/Day%2006/138-tb__tb1.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/tb/tb1) |
| 19 | 6:15:10 PM | [139](#problem-139) | Writing Testbenches | [AND gate](problems/Day%2006/139-tb__and.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/tb/and) |
| 20 | 11:14:42 PM | [140](#problem-140) | Writing Testbenches | [Testbench2](problems/Day%2006/140-tb__tb2.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/tb/tb2) |
| 21 | 6:29:03 PM | [141](#problem-141) | Writing Testbenches | [T flip-flop](problems/Day%2006/141-tb__tff.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/tb/tff) |

---

<a id="problem-121"></a>
## 121 — Q2b: Another FSM

[Problem note](problems/Day%2006/121-exams__2013_q2bfsm.md) · [Verilog file](solutions/Day%2006/121-exams__2013_q2bfsm.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/2013_q2bfsm)

![Q2b: Another FSM question and submitted solution](images/Day%2006/121-exams__2013_q2bfsm.png)

### What the question is asking

This controller combines a one-cycle start pulse, a serial sequence detector, a two-cycle deadline, and two absorbing terminal outcomes.

After active-low **synchronous** reset, state A is held. Once reset is released, A→B makes `f=1` for exactly one clock, then B→C begins monitoring `x`. States C, D, and E recognize the overlapping sequence 1-0-1: C waits for the first 1, D remembers a trailing 1, and E remembers 10. A 1 in E completes the sequence and enters F.

States F and G implement the “within at most two cycles” check for `y`. If `y` is high in either state, the machine enters H, where `g` stays high until reset. If both checks fail, it enters I, where `g` stays low until reset. The output expression keeps `g` high during F and G as required while the decision window is open.

**Important timing point:** outputs are Moore decodes of registered state. Sequence completion on one edge changes the state to F, and `g` becomes high during the following cycle.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input resetn,
    input x,
    input y,
    output f,
    output g
);

    reg [3:0] state, next_state;

    parameter A = 4'd0;
    parameter B = 4'd1;
    parameter C = 4'd2;
    parameter D = 4'd3;
    parameter E = 4'd4;
    parameter F = 4'd5;
    parameter G = 4'd6;
    parameter H = 4'd7;
    parameter I = 4'd8;

    always @(posedge clk) begin
        if (!resetn)
            state <= A;
        else
            state <= next_state;
    end

    always @(*) begin
        case (state)
            A: next_state = B;
            B: next_state = C;
            C: next_state = x ? D : C;
            D: next_state = x ? D : E;
            E: next_state = x ? F : C;
            F: next_state = y ? H : G;
            G: next_state = y ? H : I;
            H: next_state = H;
            I: next_state = I;
            default: next_state = A;
        endcase
    end

    assign f = (state == B);
    assign g = (state == F) || (state == G) || (state == H);

endmodule
```

---

<a id="problem-122"></a>
## 122 — Mux

[Problem note](problems/Day%2006/122-bugs_mux2.md) · [Verilog file](solutions/Day%2006/122-bugs_mux2.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/bugs_mux2)

![Mux question and submitted solution](images/Day%2006/122-bugs_mux2.png)

### What the question is asking

The broken circuit mixed two independent mistakes: the output was declared as a scalar even though both data inputs are 8-bit buses, and the selection expression did not implement the required bus mux correctly.

The fixed output is `[7:0]`, and the ternary operator selects the entire vector in one expression: when `sel=1`, output A; otherwise output B. This is width-preserving and synthesizes to eight parallel 2-to-1 multiplexers sharing the same select line.

**Check:** `sel=0` must copy every bit of B, and `sel=1` must copy every bit of A. A one-bit output declaration could appear to work for bit 0 while silently discarding bits 7:1.

### Saved Verilog solution

```verilog
module top_module (
    input sel,
    input [7:0] a,
    input [7:0] b,
    output [7:0] out
);

    assign out = sel ? a : b;

endmodule
```

---

<a id="problem-123"></a>
## 123 — NAND

[Problem note](problems/Day%2006/123-bugs_nand3.md) · [Verilog file](solutions/Day%2006/123-bugs_nand3.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/bugs_nand3)

![NAND question and submitted solution](images/Day%2006/123-bugs_nand3.png)

### What the question is asking

The required primitive is a five-input AND gate with positional port order `(out, a, b, c, d, e)`. To create a three-input AND, the unused inputs must be tied to the AND identity value 1, not 0. The intermediate `ando` is therefore `a & b & c & 1 & 1`.

A separate NOT gate inverts that intermediate value to produce the requested NAND function. The resulting truth rule is simple: `out` is low only for `a=b=c=1`; every other input combination produces high.

**Debugging lessons:** positional module connections must follow the declaration order exactly, intermediate nets need explicit declarations, and unused AND inputs must be tied high. Named port connections would reduce the risk of an ordering error.

### Saved Verilog solution

```verilog
module top_module (
    input a,
    input b,
    input c,
    output out
);
    wire and_result;

    andgate inst1 (and_result, a, b, c, 1'b1, 1'b1);
    not g1 (out, and_result);

endmodule
```

---

<a id="problem-124"></a>
## 124 — Mux

[Problem note](problems/Day%2006/124-bugs_mux4.md) · [Verilog file](solutions/Day%2006/124-bugs_mux4.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/bugs_mux4)

![Mux question and submitted solution](images/Day%2006/124-bugs_mux4.png)

### What the question is asking

A 4-to-1 bus multiplexer can be built as a two-level tree of the supplied 2-to-1 muxes. The first level uses `sel[0]` to choose A/B and C/D independently. The second level uses `sel[1]` to choose between those two intermediate buses.

The intermediate signals must be 8-bit vectors; scalar wires would truncate seven bits. The corrected third instance also uses a unique instance name and selects with `sel[1]`, not `sel[0]`.

| sel | output |
|---|---|
| 00 | A |
| 01 | B |
| 10 | C |
| 11 | D |

This table is a quick way to trace both levels and catch swapped select bits.

### Saved Verilog solution

```verilog
module top_module (
    input [1:0] sel,
    input [7:0] a,
    input [7:0] b,
    input [7:0] c,
    input [7:0] d,
    output [7:0] out
);
    wire [7:0] w1, w2;

    mux2 mux0 (sel[0], a, b, w1);
    mux2 mux1 (sel[0], c, d, w2);
    mux2 mux3 (sel[1], w1, w2, out);

endmodule
```

---

<a id="problem-125"></a>
## 125 — Add/sub

[Problem note](problems/Day%2006/125-bugs_addsubz.md) · [Verilog file](solutions/Day%2006/125-bugs_addsubz.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/bugs_addsubz)

![Add/sub question and submitted solution](images/Day%2006/125-bugs_addsubz.png)

### What the question is asking

The combinational block first computes either `a+b` or `a-b` according to `do_sub`, then derives `result_is_zero` from the newly computed `out`.

Blocking assignments are important here. With `out = ...`, the following zero comparison sees the current combinational result in the same evaluation. A nonblocking assignment could make the flag observe the previous value during simulation and create a mismatch between intent and behaviour.

The zero test is placed after the `case`, so it applies equally to addition and subtraction. Both outputs are declared `reg` because they are assigned procedurally.

**Revision pitfall:** calculating the zero flag in only one case branch, or omitting an assignment on a path, would infer storage or leave stale flag data.

### Saved Verilog solution

```verilog
// synthesis verilog_input_version verilog_2001
module top_module (
    input do_sub,
    input [7:0] a,
    input [7:0] b,
    output reg [7:0] out,
    output reg result_is_zero
);

    always @(*) begin
        case (do_sub)
            1'b0: out = a + b;
            1'b1: out = a - b;
        endcase
        result_is_zero = (out == 8'd0);
    end

endmodule
```

---

<a id="problem-126"></a>
## 126 — Case statement

[Problem note](problems/Day%2006/126-bugs_case.md) · [Verilog file](solutions/Day%2006/126-bugs_case.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/bugs_case)

![Case statement question and submitted solution](images/Day%2006/126-bugs_case.png)

### What the question is asking

This decoder recognizes the PS/2 scan codes for decimal keys 0 through 9. Each recognized hexadecimal code assigns the corresponding 4-bit digit and asserts `valid`.

The critical repair is to provide defaults before the `case`: `out=0` and `valid=0`. Every recognized branch overrides both values. Any unlisted scan code therefore produces a deterministic invalid result instead of retaining the previous output and inferring latches.

Examples: `8'h45` maps to digit 0, `8'h16` to 1, and `8'h46` to 9. The `default` branch repeats the safe values, making the intended behaviour explicit.

**Debugging checklist:** verify literal width, hexadecimal code, digit mapping, and assignments to every combinational output on every path.

### Saved Verilog solution

```verilog
module top_module (
    input [7:0] code,
    output reg [3:0] out,
    output reg valid
);

    always @(*) begin
        out = 4'd0;
        valid = 1'b0;

        case (code)
            8'h45: begin out = 4'd0; valid = 1'b1; end
            8'h16: begin out = 4'd1; valid = 1'b1; end
            8'h1e: begin out = 4'd2; valid = 1'b1; end
            8'h26: begin out = 4'd3; valid = 1'b1; end
            8'h25: begin out = 4'd4; valid = 1'b1; end
            8'h2e: begin out = 4'd5; valid = 1'b1; end
            8'h36: begin out = 4'd6; valid = 1'b1; end
            8'h3d: begin out = 4'd7; valid = 1'b1; end
            8'h3e: begin out = 4'd8; valid = 1'b1; end
            8'h46: begin out = 4'd9; valid = 1'b1; end
            default: begin out = 4'd0; valid = 1'b0; end
        endcase
    end

endmodule
```

---

<a id="problem-127"></a>
## 127 — Combinational circuit 1

[Problem note](problems/Day%2006/127-sim__circuit1.md) · [Verilog file](solutions/Day%2006/127-sim__circuit1.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/sim/circuit1)

![Combinational circuit 1 question and submitted solution](images/Day%2006/127-sim__circuit1.png)

### What the question is asking

The waveform shows a combinational AND function. Output `q` is high only during intervals in which both `a` and `b` are high, so the implementation is `q = a & b`.

Because there is no clock or storage, output changes propagate whenever either input changes. The four-row truth table is 00→0, 01→0, 10→0, and 11→1.

**Waveform method:** compare each transition of one input while holding the other fixed. When B is 0, changing A has no effect; when B is 1, Q follows A. That uniquely identifies AND rather than OR or XOR.

### Saved Verilog solution

```verilog
module top_module (
    input a,
    input b,
    output q
);

    assign q = a & b;

endmodule
```

---

<a id="problem-128"></a>
## 128 — Combinational circuit 2

[Problem note](problems/Day%2006/128-sim__circuit2.md) · [Verilog file](solutions/Day%2006/128-sim__circuit2.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/sim/circuit2)

![Combinational circuit 2 question and submitted solution](images/Day%2006/128-sim__circuit2.png)

### What the question is asking

The waveform corresponds to four-input even parity, implemented as the inverse of a four-way XOR: `q = ~(a ^ b ^ c ^ d)`.

An XOR reduction is 1 when an odd number of inputs are high. Inverting it makes Q high for 0, 2, or 4 asserted inputs and low for 1 or 3 asserted inputs. The same function could be written with the reduction-XNOR operator `~^{a,b,c,d}`.

**Trace examples:** 0000 has zero ones and produces 1; 0001 has one one and produces 0; 1010 has two ones and produces 1. Counting asserted bits is often the fastest way to recognize parity in a waveform.

### Saved Verilog solution

```verilog
module top_module (
    input a,
    input b,
    input c,
    input d,
    output q
);

    assign q = ~(a ^ b ^ c ^ d);

endmodule
```

---

<a id="problem-129"></a>
## 129 — Combinational circuit 3

[Problem note](problems/Day%2006/129-sim__circuit3.md) · [Verilog file](solutions/Day%2006/129-sim__circuit3.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/sim/circuit3)

![Combinational circuit 3 question and submitted solution](images/Day%2006/129-sim__circuit3.png)

### What the question is asking

The submitted expression factors to `q = (a | b) & (c | d)`. Thus at least one signal from the A/B pair and at least one signal from the C/D pair must be high.

The unfactored form, `d&(a|b) | c&(a|b)`, makes the waveform-derived product terms visible; Boolean factoring exposes the simpler two-ORs-into-an-AND circuit.

**Checks:** if A=B=0, Q is always 0 regardless of C/D. If C=D=0, Q is also always 0. With A=1 and C=1, Q is 1 regardless of B/D. These controlled waveform comparisons distinguish the grouped function from a four-input OR.

### Saved Verilog solution

```verilog
module top_module (
    input a,
    input b,
    input c,
    input d,
    output q
);

    assign q = (d & (a | b)) | (c & (a | b));

endmodule
```

---

<a id="problem-130"></a>
## 130 — Combinational circuit 4

[Problem note](problems/Day%2006/130-sim__circuit4.md) · [Verilog file](solutions/Day%2006/130-sim__circuit4.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/sim/circuit4)

![Combinational circuit 4 question and submitted solution](images/Day%2006/130-sim__circuit4.png)

### What the question is asking

The waveform shows that only `b` and `c` affect the output. Q is high whenever either is high, giving `q = b | c`; inputs A and D are observable distractors with no functional influence.

**How to infer this:** find intervals where A or D toggles while B and C remain fixed. Q does not change. Then compare the four B/C combinations: only 00 produces 0, while 01, 10, and 11 produce 1.

Ignoring irrelevant inputs is an important waveform-reading skill: a port’s presence does not guarantee that synthesized logic uses it.

### Saved Verilog solution

```verilog
module top_module (
    input a,
    input b,
    input c,
    input d,
    output q
);

    assign q = b | c;

endmodule
```

---

<a id="problem-131"></a>
## 131 — Combinational circuit 5

[Problem note](problems/Day%2006/131-sim__circuit5.md) · [Verilog file](solutions/Day%2006/131-sim__circuit5.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/sim/circuit5)

![Combinational circuit 5 question and submitted solution](images/Day%2006/131-sim__circuit5.png)

### What the question is asking

This circuit is a 4-bit lookup/multiplexer controlled by `c`. For selector values 0 through 3, Q chooses different input buses: 0→B, 1→E, 2→A, and 3→D. All other selector values produce `4'hf`.

The `case` statement is combinational and assigns Q in every branch, including `default`, so no latch is inferred. Input bus C is used as the selector, while the data buses retain their full 4-bit widths.

**Waveform technique:** locate periods where one candidate bus has a distinctive value, then see whether Q matches it for a particular C value. Repeating that across multiple simulations disambiguates buses that happen to share a value temporarily.

### Saved Verilog solution

```verilog
module top_module (
    input [3:0] a,
    input [3:0] b,
    input [3:0] c,
    input [3:0] d,
    input [3:0] e,
    output reg [3:0] q
);

    always @(*) begin
        case (c)
            4'd0: q = b;
            4'd1: q = e;
            4'd2: q = a;
            4'd3: q = d;
            default: q = 4'hf;
        endcase
    end

endmodule
```

---

<a id="problem-132"></a>
## 132 — Combinational circuit 6

[Problem note](problems/Day%2006/132-sim__circuit6.md) · [Verilog file](solutions/Day%2006/132-sim__circuit6.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/sim/circuit6)

![Combinational circuit 6 question and submitted solution](images/Day%2006/132-sim__circuit6.png)

### What the question is asking

The waveform describes a small combinational ROM. The 3-bit address `a` selects one of eight fixed 16-bit words.

| a | q |
|---:|---:|
| 0 | 16'h1232 |
| 1 | 16'haee0 |
| 2 | 16'h27d4 |
| 3 | 16'h5a0e |
| 4 | 16'h2066 |
| 5 | 16'h64ce |
| 6 | 16'hc526 |
| 7 | 16'h2f19 |

All eight address values are covered, so the combinational `case` fully specifies Q without a default. This pattern synthesizes as decode/multiplexer logic or a ROM structure, depending on the target technology.

### Saved Verilog solution

```verilog
module top_module (
    input [2:0] a,
    output reg [15:0] q
);

    always @(*) begin
        case (a)
            3'd0: q = 16'h1232;
            3'd1: q = 16'haee0;
            3'd2: q = 16'h27d4;
            3'd3: q = 16'h5a0e;
            3'd4: q = 16'h2066;
            3'd5: q = 16'h64ce;
            3'd6: q = 16'hc526;
            3'd7: q = 16'h2f19;
        endcase
    end

endmodule
```

---

<a id="problem-133"></a>
## 133 — Sequential circuit 7

[Problem note](problems/Day%2006/133-sim__circuit7.md) · [Verilog file](solutions/Day%2006/133-sim__circuit7.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/sim/circuit7)

![Sequential circuit 7 question and submitted solution](images/Day%2006/133-sim__circuit7.png)

### What the question is asking

This is a positive-edge-triggered register whose D input is the inverse of `a`. On each rising edge, `q <= ~a`; between rising edges Q holds its previous value even if A changes.

The nonblocking assignment models simultaneous flip-flop sampling. A waveform trace should therefore read A immediately before each rising edge and compare its inverse with Q immediately after that edge.

**Distinguishing feature:** if Q followed `~a` continuously, it would be combinational. The observed hold intervals between clock edges prove that memory is present.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input a,
    output reg q
);

    always @(posedge clk) begin
        q <= ~a;
    end

endmodule
```

---

<a id="problem-134"></a>
## 134 — Sequential circuit 8

[Problem note](problems/Day%2006/134-sim__circuit8.md) · [Verilog file](solutions/Day%2006/134-sim__circuit8.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/sim/circuit8)

![Sequential circuit 8 question and submitted solution](images/Day%2006/134-sim__circuit8.png)

### What the question is asking

The waveform is reproduced by two level/edge-sensitive storage stages. P is a transparent-high latch: while `clock=1`, P follows A; while the clock is low, P holds the last value seen during the high phase. The incomplete assignment inside the combinational block intentionally infers that latch.

Q updates on the falling edge with `q <= p`. Since P has just been tracking A during the high phase, Q captures the final latched value at the high-to-low transition and then holds it.

**Trace method:** during a high clock phase, changes on A appear on P but not immediately on Q. At the falling edge, Q takes P. During the low phase, later A changes affect neither stored output. This timing distinguishes a latch-plus-negedge-flip-flop chain from two ordinary flip-flops.

### Saved Verilog solution

```verilog
module top_module (
    input clock,
    input a,
    output reg p,
    output reg q
);

    // p is transparent while clock is high.
    always @(*) begin
        if (clock)
            p = a;
    end

    // q samples p when the clock falls.
    always @(negedge clock) begin
        q <= p;
    end

endmodule
```

---

<a id="problem-135"></a>
## 135 — Sequential circuit 9

[Problem note](problems/Day%2006/135-sim__circuit9.md) · [Verilog file](solutions/Day%2006/135-sim__circuit9.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/sim/circuit9)

![Sequential circuit 9 question and submitted solution](images/Day%2006/135-sim__circuit9.png)

### What the question is asking

The circuit is a modulo-7 counter with a synchronous load-like control. When `a=0`, the 4-bit state counts 0,1,2,3,4,5,6 and then wraps to 0. When `a=1` at a rising edge, the state is loaded with 4 instead of incrementing.

Q continuously exposes the registered count. All changes therefore occur after rising clock edges, not when A changes between edges.

**Trace examples:** count=6 and A=0 produces 0 on the next edge; count=2 and A=0 produces 3; any current count with A=1 produces 4. Priority is clear because the A branch is tested before the wrap/increment logic.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input a,
    output [3:0] q
);
    reg [3:0] count;

    always @(posedge clk) begin
        if (!a) begin
            if (count == 4'b0110)
                count <= 4'b0000;
            else
                count <= count + 1'b1;
        end else begin
            count <= 4'b0100;
        end
    end

    assign q = count;

endmodule
```

---

<a id="problem-136"></a>
## 136 — Sequential circuit 10

[Problem note](problems/Day%2006/136-sim__circuit10.md) · [Verilog file](solutions/Day%2006/136-sim__circuit10.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/sim/circuit10)

![Sequential circuit 10 question and submitted solution](images/Day%2006/136-sim__circuit10.png)

### What the question is asking

This circuit behaves like a serial full adder with one stored carry bit. The combinational output `q = a ^ b ^ state` is the one-bit sum of A, B, and the previous carry.

At each rising edge, `state` is updated to the majority function `ab | b·state | a·state`, which is exactly the carry-out of a full adder. The new carry then participates in Q during the following cycle.

| a | b | carry-in | q (sum) | next state (carry-out) |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 | 1 |
| 0 | 0 | 1 | 1 | 0 |

The absence of reset means the testbench must establish or tolerate the initial carry state before checking deterministic sequences.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input a,
    input b,
    output q,
    output reg state
);

    assign q = a ^ b ^ state;

    always @(posedge clk) begin
        state <= (a & b) | (b & state) | (a & state);
    end

endmodule
```

---

<a id="problem-137"></a>
## 137 — Clock

[Problem note](problems/Day%2006/137-tb__clock.md) · [Verilog file](solutions/Day%2006/137-tb__clock.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/tb/clock)

![Clock question and submitted solution](images/Day%2006/137-tb__clock.png)

### What the question is asking

This exercise moves from describing hardware to controlling simulation time. The top-level testbench has no ports because it is the simulation root. It declares an internal `reg clk`, connects that signal to the supplied `dut` instance, initializes it to zero at time 0, and toggles it every 5 ps.

Two half-periods make the required 10 ps period. Starting from zero means the first scheduled toggle is a rising edge at 5 ps, exactly matching the requested waveform. The `initial` block runs once, while `always #5` repeats forever; these are simulation constructs and are not intended to synthesize into physical logic.

**Timing trace:** `clk=0` at t=0, 1 at t=5, 0 at t=10, 1 at t=15, and so on. A common error is using `#10` for each toggle, which produces a 20 ps full period. Another is leaving the clock uninitialized: negating an unknown `X` still produces `X`, so the clock never becomes usable.

### Saved Verilog solution

```verilog
module top_module ();
    reg clk;

    dut dut_instance (
        .clk(clk)
    );

    initial
        clk = 1'b0;

    always #5
        clk = ~clk;
endmodule
```

---

<a id="problem-138"></a>
## 138 — Testbench1

[Problem note](problems/Day%2006/138-tb__tb1.md) · [Verilog file](solutions/Day%2006/138-tb__tb1.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/tb/tb1)

![Testbench1 question and submitted solution](images/Day%2006/138-tb__tb1.png)

### What the question is asking

The goal is to generate two output waveforms directly from procedural stimulus. Because A and B are assigned inside an `initial` block, the module declares them as `output reg`. Both begin low at time 0, then the delays reproduce each transition in chronological order.

| Simulation time | A | B | Event |
|---:|---:|---:|---|
| 0 | 0 | 0 | initialize both outputs |
| 10 | 1 | 0 | raise A |
| 15 | 1 | 1 | raise B five time units later |
| 20 | 0 | 1 | lower A |
| 40 | 0 | 0 | lower B after its long high interval |

Delay statements are relative to the current process time, not absolute timestamps. Thus `#10 A=1; #5 B=1;` places the second event at t=15. Keeping the entire timeline in one ordered block makes that accumulation explicit and avoids accidental races between several independent stimulus processes.

### Saved Verilog solution

```verilog
module top_module (
    output reg A,
    output reg B
);
    initial begin
        A = 1'b0;
        B = 1'b0;
        #10 A = 1'b1;
        #5 B = 1'b1;
        #5 A = 1'b0;
        #20 B = 1'b0;
    end
endmodule
```

---

<a id="problem-139"></a>
## 139 — AND gate

[Problem note](problems/Day%2006/139-tb__and.md) · [Verilog file](solutions/Day%2006/139-tb__and.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/tb/and)

![AND gate question and submitted solution](images/Day%2006/139-tb__and.png)

### What the question is asking

This testbench verifies a two-input AND gate exhaustively. The DUT input is a 2-bit procedural register, while the DUT output is a wire because it is driven by the instantiated module. A loop enumerates the four binary input combinations 00, 01, 10, and 11, holding each combination for 10 simulation time units.

Using `in = i[1:0]` makes the mapping from loop counter to stimulus width explicit. The observed output should remain zero for the first three patterns and become one only for `2'b11`. This is exhaustive verification because a two-input combinational circuit has exactly four possible input states.

The important separation is stimulus versus response: the testbench drives `in`, but only observes `out`. Declaring the response as a procedural variable or assigning to it from the testbench would create an additional driver and invalidate the test. For larger circuits, the same enumeration idea scales until the input space becomes too large, at which point constrained or directed vectors are preferable.

### Saved Verilog solution

```verilog
module top_module ();
    reg [1:0] in;
    wire out;
    integer i;

    andgate dut_instance (
        .in(in),
        .out(out)
    );

    initial begin
        for (i = 0; i < 4; i = i + 1) begin
            in = i[1:0];
            #10;
        end
    end
endmodule
```

---

<a id="problem-140"></a>
## 140 — Testbench2

[Problem note](problems/Day%2006/140-tb__tb2.md) · [Verilog file](solutions/Day%2006/140-tb__tb2.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/tb/tb2)

![Testbench2 question and submitted solution](images/Day%2006/140-tb__tb2.png)

### What the question is asking

This testbench coordinates two independent timelines: a free-running clock and a directed sequence for `in` and the 3-bit bus `s`. One `initial` block initializes the clock and toggles it every 5 time units, producing a 10-unit period. A second block applies the waveform values at the required boundaries, while the `q7` instance connects all generated signals to the supplied DUT.

| Time interval | in | s |
|---|---:|---:|
| 0-10 | 0 | 2 |
| 10-20 | 0 | 6 |
| 20-30 | 1 | 2 |
| 30-40 | 0 | 7 |
| 40-70 | 1 | 0 |
| 70 onward | 0 | 0 |

The sequence uses cumulative delays, so each `#10` advances from the preceding event, and `#30` creates the long final high interval for `in`. Changes occur on falling-clock boundaries in this waveform, giving the DUT stable inputs before the following rising edge. A frequent failure is to treat the delay values as absolute times or to forget that concurrent `initial` blocks begin together at t=0.

### Saved Verilog solution

```verilog
module top_module ();
    reg clk;
    reg in;
    reg [2:0] s;
    wire out;

    q7 dut_instance (
        .clk(clk),
        .in(in),
        .s(s),
        .out(out)
    );

    initial begin
        clk = 1'b0;
        forever #5 clk = ~clk;
    end

    initial begin
        in = 1'b0;
        s = 3'd2;
        #10 s = 3'd6;
        #10 begin in = 1'b1; s = 3'd2; end
        #10 begin in = 1'b0; s = 3'd7; end
        #10 begin in = 1'b1; s = 3'd0; end
        #30 in = 1'b0;
    end
endmodule
```

---

<a id="problem-141"></a>
## 141 — T flip-flop

[Problem note](problems/Day%2006/141-tb__tff.md) · [Verilog file](solutions/Day%2006/141-tb__tff.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/tb/tff)

![T flip-flop question and submitted solution](images/Day%2006/141-tb__tff.png)

### What the question is asking

The testbench instantiates the supplied T flip-flop and creates separate clock and control processes. The clock starts low and toggles every 5 time units. Reset starts high and `t` starts low, so the first rising edge samples the synchronous reset and forces Q to its reset state. After 10 time units, reset is deasserted and T is asserted; subsequent rising edges toggle Q.

The word *synchronous* is crucial: changing reset does not immediately change Q. Reset only has an effect when a rising edge occurs while reset is high. With this timeline, the rising edge at t=5 performs the reset, reset becomes low at t=10, and the edge at t=15 performs the first toggle.

The DUT output is a wire because the T flip-flop drives it. Clock, reset, and T are registers because the testbench drives them procedurally. Keeping the free-running clock and one-time stimulus in separate `initial` processes is intentional concurrency: both timelines advance together under the simulator's event scheduler.

### Saved Verilog solution

```verilog
module top_module ();
    reg clk;
    reg reset;
    reg t;
    wire q;

    tff dut_instance (
        .clk(clk),
        .reset(reset),
        .t(t),
        .q(q)
    );

    initial begin
        clk = 1'b0;
        forever #5 clk = ~clk;
    end

    initial begin
        reset = 1'b1;
        t = 1'b0;
        #10 begin
            reset = 1'b0;
            t = 1'b1;
        end
    end
endmodule
```
