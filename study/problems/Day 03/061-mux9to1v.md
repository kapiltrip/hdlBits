# 061 — 9-to-1 multiplexer

| Field | Value |
|---|---|
| Day | Day 03 |
| Last successful submission | 2026-06-25 2:44:03 PM |
| Course location | Circuits → Combinational Logic → Multiplexers |
| HDLBits identifier | `mux9to1v` |
| Attempts | 10 total: 7 incorrect, 2 compile error, 0 simulation error |
| Success rate | 10% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/mux9to1v) |
| Files | [Open screenshot at full resolution](../../images/Day%2003/061-mux9to1v.png) · [Verilog solution](../../solutions/Day%2003/061-mux9to1v.sv) |

## Question and submitted solution

<a href="../../images/Day%2003/061-mux9to1v.png"><img src="../../images/Day%2003/061-mux9to1v.png" alt="9-to-1 multiplexer question and submitted solution" width="100%"></a>

## What the question is asking

Select one of nine 16-bit inputs; produce the required default value when the selector is outside the valid range.

## Saved Verilog solution

```verilog
module top_module(
    input [15:0] a, b, c, d, e, f, g, h, i,
    input [3:0] sel,
    output [15:0] out );

endmodule
```

## What I learned

_Fill this in during revision._
