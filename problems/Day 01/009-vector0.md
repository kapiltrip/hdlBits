# 009 — Vectors

| Field | Value |
|---|---|
| Day | Day 01 |
| Last successful submission | 2026-06-23 6:24:20 PM |
| Course location | Verilog Language → Vectors |
| HDLBits identifier | `vector0` |
| Attempts | 1 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/vector0) |
| Files | [Screenshot](../../images/Day%2001/009-vector0.png) · [Verilog solution](../../solutions/Day%2001/009-vector0.sv) |

## Problem and saved submission

![Vectors problem and saved submission](../../images/Day%2001/009-vector0.png)

## Saved Verilog solution

```verilog
module top_module ( 
    input wire [2:0] vec,
    output wire [2:0] outv,
    output wire o2,
    output wire o1,
    output wire o0  
); // Module body starts after module declaration
    assign outv = vec;
    assign o2=vec[2];
    assign o1=vec[1];
    assign o0=vec[0];

endmodule
```

## What I learned

_Fill this in during revision._
