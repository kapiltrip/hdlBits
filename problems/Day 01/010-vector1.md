# 010 — Vectors in more detail

| Field | Value |
|---|---|
| Day | Day 01 |
| Last successful submission | 2026-06-23 9:45:09 PM |
| Course location | Verilog Language → Vectors |
| HDLBits identifier | `vector1` |
| Attempts | 10 total: 0 incorrect, 9 compile error, 0 simulation error |
| Success rate | 10% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/vector1) |
| Files | [Screenshot](../../images/Day%2001/010-vector1.png) · [Verilog solution](../../solutions/Day%2001/010-vector1.sv) |

## Problem and saved submission

![Vectors in more detail problem and saved submission](../../images/Day%2001/010-vector1.png)

## Saved Verilog solution

```verilog
`default_nettype none     // Disable implicit nets. Reduces some types of bugs.
module top_module( 
    input wire [15:0] in,
    output wire [7:0] out_hi,
    output wire [7:0] out_lo 
);

    
        assign out_hi=  in[15:8];
        assign out_lo =  in[7:0];
    
endmodule
```

## What I learned

_Fill this in during revision._
