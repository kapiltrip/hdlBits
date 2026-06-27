# 013 — Four-input gates

| Field | Value |
|---|---|
| Day | Day 01 |
| Last successful submission | 2026-06-23 10:24:24 PM |
| Course location | Verilog Language → Vectors |
| HDLBits identifier | `gates4` |
| Attempts | 8 total: 0 incorrect, 7 compile error, 0 simulation error |
| Success rate | 13% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/gates4) |
| Files | [Screenshot](../../images/Day%2001/013-gates4.png) · [Verilog solution](../../solutions/Day%2001/013-gates4.sv) |

## Problem and saved submission

![Four-input gates problem and saved submission](../../images/Day%2001/013-gates4.png)

## Saved Verilog solution

```verilog
module top_module( 
    input [3:0] in,
    output out_and,
    output out_or,
    output out_xor
);
assign out_and = &in;
assign out_or = |in ;
assign out_xor  =^in;
    
endmodule
```

## What I learned

_Fill this in during revision._
