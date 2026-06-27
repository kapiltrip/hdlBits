# 060 — 2-to-1 bus multiplexer

| Field | Value |
|---|---|
| Day | Day 03 |
| Last successful submission | 2026-06-25 1:07:52 AM |
| Course location | Circuits → Combinational Logic → Multiplexers |
| HDLBits identifier | `mux2to1v` |
| Attempts | 1 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/mux2to1v) |
| Files | [Open screenshot at full resolution](../../images/Day%2003/060-mux2to1v.png) · [Verilog solution](../../solutions/Day%2003/060-mux2to1v.sv) |

## Question and submitted solution

<a href="../../images/Day%2003/060-mux2to1v.png"><img src="../../images/Day%2003/060-mux2to1v.png" alt="2-to-1 bus multiplexer question and submitted solution" width="100%"></a>

## What the question is asking

Implement a 2-to-1 multiplexer that selects an entire vector rather than a single bit.

## Saved Verilog solution

```verilog
module top_module(
    input [99:0] a, b,
    input sel,
    output [99:0] out );

endmodule
```

## What I learned

_Fill this in during revision._
