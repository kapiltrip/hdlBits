# 015 — Vector reversal 1

| Field | Value |
|---|---|
| Day | Day 01 |
| Last successful submission | 2026-06-23 11:34:51 PM |
| Course location | Verilog Language → Vectors |
| HDLBits identifier | `vectorr` |
| Attempts | 2 total: 0 incorrect, 1 compile error, 0 simulation error |
| Success rate | 50% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/vectorr) |
| Files | [Screenshot](../../images/Day%2001/015-vectorr.png) · [Verilog solution](../../solutions/Day%2001/015-vectorr.sv) |

## Problem and saved submission

![Vector reversal 1 problem and saved submission](../../images/Day%2001/015-vectorr.png)

## Saved Verilog solution

```verilog
module top_module( 
    input [7:0] in,
    output [7:0] out
);
genvar i ;
    generate
        for(i=0;i<8;i=i+1) begin : revloop 
            assign out[i]=in[7-i];
        end
    endgenerate 
endmodule
```

## What I learned

_Fill this in during revision._
