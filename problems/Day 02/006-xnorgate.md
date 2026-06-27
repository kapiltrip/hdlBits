# 006 — XNOR gate

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 12:33:10 AM |
| Course location | Verilog Language → Basics |
| HDLBits identifier | `xnorgate` |
| Attempts | 2 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/xnorgate) |
| Files | [Screenshot](../../images/Day%2002/006-xnorgate.png) · [Verilog solution](../../solutions/Day%2002/006-xnorgate.sv) |

## Problem and saved submission

![XNOR gate problem and saved submission](../../images/Day%2002/006-xnorgate.png)

## Saved Verilog solution

```verilog
module top_module( 
    input a, 
    input b, 
    output out 
);
    assign out = ~(a ^b); 
    
endmodule
```

## What I learned

_Fill this in during revision._
