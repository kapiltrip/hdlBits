# 124 — Mux

| Field | Value |
|---|---|
| Day | Day 06 |
| Last successful submission | 2026-06-28 1:01:34 AM |
| Course location | Verification: Reading Simulations → Finding bugs in code |
| HDLBits identifier | `bugs_mux4` |
| Attempts | 7 total: 6 incorrect, 0 compile error, 0 simulation error |
| Success rate | 14% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/bugs_mux4) |
| Files | [Open screenshot at full resolution](../../images/Day%2006/124-bugs_mux4.png) · [Verilog solution](../../solutions/Day%2006/124-bugs_mux4.sv) |

## Question and submitted solution

<a href="../../images/Day%2006/124-bugs_mux4.png"><img src="../../images/Day%2006/124-bugs_mux4.png" alt="Mux question and submitted solution" width="100%"></a>

## What the question is asking

A 4-to-1 bus multiplexer can be built as a two-level tree of the supplied 2-to-1 muxes. The first level uses `sel[0]` to choose A/B and C/D independently. The second level uses `sel[1]` to choose between those two intermediate buses.

The intermediate signals must be 8-bit vectors; scalar wires would truncate seven bits. The corrected third instance also uses a unique instance name and selects with `sel[1]`, not `sel[0]`.

| sel | output |
|---|---|
| 00 | A |
| 01 | B |
| 10 | C |
| 11 | D |

This table is a quick way to trace both levels and catch swapped select bits.

## Saved Verilog solution

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

## What I learned

_Fill this in during revision._
