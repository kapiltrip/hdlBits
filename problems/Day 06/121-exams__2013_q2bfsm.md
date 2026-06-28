# 121 — Q2b: Another FSM

| Field | Value |
|---|---|
| Day | Day 06 |
| Last successful submission | 2026-06-28 12:22:36 AM |
| Course location | Circuits → Sequential Logic → Finite State Machines |
| HDLBits identifier | `exams/2013_q2bfsm` |
| Attempts | 2 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/exams/2013_q2bfsm) |
| Files | [Open screenshot at full resolution](../../images/Day%2006/121-exams__2013_q2bfsm.png) · [Verilog solution](../../solutions/Day%2006/121-exams__2013_q2bfsm.sv) |

## Question and submitted solution

<a href="../../images/Day%2006/121-exams__2013_q2bfsm.png"><img src="../../images/Day%2006/121-exams__2013_q2bfsm.png" alt="Q2b: Another FSM question and submitted solution" width="100%"></a>

## What the question is asking

This controller combines a one-cycle start pulse, a serial sequence detector, a two-cycle deadline, and two absorbing terminal outcomes.

After active-low **synchronous** reset, state A is held. Once reset is released, A→B makes `f=1` for exactly one clock, then B→C begins monitoring `x`. States C, D, and E recognize the overlapping sequence 1-0-1: C waits for the first 1, D remembers a trailing 1, and E remembers 10. A 1 in E completes the sequence and enters F.

States F and G implement the “within at most two cycles” check for `y`. If `y` is high in either state, the machine enters H, where `g` stays high until reset. If both checks fail, it enters I, where `g` stays low until reset. The output expression keeps `g` high during F and G as required while the decision window is open.

**Important timing point:** outputs are Moore decodes of registered state. Sequence completion on one edge changes the state to F, and `g` becomes high during the following cycle.

## Saved Verilog solution

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

## What I learned

_Fill this in during revision._
