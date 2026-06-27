# 012 — Bitwise operators

| Field | Value |
|---|---|
| Day | Day 01 |
| Last successful submission | 2026-06-23 10:04:38 PM |
| Course location | Verilog Language → Vectors |
| HDLBits identifier | `vectorgates` |
| Attempts | 1 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/vectorgates) |
| Files | [Screenshot](../../images/Day%2001/012-vectorgates.png) · [Verilog solution](../../solutions/Day%2001/012-vectorgates.sv) |

## Problem and saved submission

![Bitwise operators problem and saved submission](../../images/Day%2001/012-vectorgates.png)

## Saved Verilog solution

```verilog
module top_module( 
    input [2:0] a,
    input [2:0] b,
    output [2:0] out_or_bitwise,
    output out_or_logical,
    output [5:0] out_not
);
    assign out_or_bitwise= a |b;
    assign out_or_logical= a ||b;
    assign out_not= {~b,~a};
endmodule
```

## What I learned

_Fill this in during revision._
