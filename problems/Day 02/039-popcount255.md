# 039 — Combinational for-loop: 255-bit population count

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 6:39:46 PM |
| Course location | Verilog Language → More Verilog Features |
| HDLBits identifier | `popcount255` |
| Attempts | 22 total: 5 incorrect, 16 compile error, 0 simulation error |
| Success rate | 5% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/popcount255) |
| Files | [Screenshot](../../images/Day%2002/039-popcount255.png) · [Verilog solution](../../solutions/Day%2002/039-popcount255.sv) |

## Problem and saved submission

![Combinational for-loop: 255-bit population count problem and saved submission](../../images/Day%2002/039-popcount255.png)

## Saved Verilog solution

```verilog
module top_module( 
    input [254:0] in,
    output [7:0] out 
);
//to count no of ones in the input vector 
    integer i ;
    reg [7:0] count;
    always @(*)begin
        count=8'd0;
        for(i=0;i<255;i=i+1)begin
            count=count+ in[i];
        end
    end
    always @(*)begin
        out = count;
        
    end
    
    
endmodule
```

## What I learned

_Fill this in during revision._
