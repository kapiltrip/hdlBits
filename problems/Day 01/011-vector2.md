# 011 — Vector part select

| Field | Value |
|---|---|
| Day | Day 01 |
| Last successful submission | 2026-06-23 9:56:38 PM |
| Course location | Verilog Language → Vectors |
| HDLBits identifier | `vector2` |
| Attempts | 3 total: 0 incorrect, 2 compile error, 0 simulation error |
| Success rate | 33% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/vector2) |
| Files | [Screenshot](../../images/Day%2001/011-vector2.png) · [Verilog solution](../../solutions/Day%2001/011-vector2.sv) |

## Problem and saved submission

![Vector part select problem and saved submission](../../images/Day%2001/011-vector2.png)

## Saved Verilog solution

```verilog
module top_module( 
    input [31:0] in,
    output [31:0] out );//

    // assign out[31:24] = ...;
    wire [7:0] a,b,c,d;
    assign a=in[31:24];//msb
    assign b=in[23:16];
    assign c=in[15:8];
    assign d=in[7:0];
   assign  out ={d,c,b,a};    
endmodule
```

## What I learned

_Fill this in during revision._
