# 038 — Combinational for-loop: Vector reversal 2

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 6:22:35 PM |
| Course location | Verilog Language → More Verilog Features |
| HDLBits identifier | `vector100r` |
| Attempts | 8 total: 1 incorrect, 4 compile error, 0 simulation error |
| Success rate | 38% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/vector100r) |
| Files | [Screenshot](../../images/Day%2002/038-vector100r.png) · [Verilog solution](../../solutions/Day%2002/038-vector100r.sv) |

## Problem and saved submission

![Combinational for-loop: Vector reversal 2 problem and saved submission](../../images/Day%2002/038-vector100r.png)

## Saved Verilog solution

```verilog
module top_module( 
    input [99:0] in,
    output [99:0] out
);
//to reverse the bit ordering 
genvar i ;
    
    generate
        for(i=0;i<100;i=i+1)begin : reversingBits
               assign out[i]=in[99-i];
             end
    endgenerate 
endmodule
```

## What I learned

_Fill this in during revision._
