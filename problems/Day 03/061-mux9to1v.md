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
| Files | [Screenshot](../../images/Day%2003/061-mux9to1v.png) · [Verilog solution](../../solutions/Day%2003/061-mux9to1v.sv) |

## Problem and saved submission

![9-to-1 multiplexer problem and saved submission](../../images/Day%2003/061-mux9to1v.png)

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
