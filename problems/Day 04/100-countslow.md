# 100 — Slow decade counter

| Field | Value |
|---|---|
| Day | Day 04 |
| Last successful submission | 2026-06-26 1:31:52 AM |
| Course location | Circuits → Sequential Logic → Counters |
| HDLBits identifier | `countslow` |
| Attempts | 3 total: 1 incorrect, 0 compile error, 0 simulation error |
| Success rate | 67% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/countslow) |
| Files | [Screenshot](../../images/Day%2004/100-countslow.png) · [Verilog solution](../../solutions/Day%2004/100-countslow.sv) |

## Problem and saved submission

![Slow decade counter problem and saved submission](../../images/Day%2004/100-countslow.png)

## Saved Verilog solution

```verilog
module top_module (
    input clk,
    input slowena,
    input reset,
    output [3:0] q
);
//0 to 9 inclusive 
    reg [3:0] count;
    always @(posedge clk)begin
        if(reset)begin
            count <= 4'b0000;
        end else begin
            if(count>= 4'b1001 && slowena)
                count<=4'b0000;
            else if(slowena)
                count<=count+1'b1;
            
        end
    end
    assign q=count ;
    
endmodule
```

## What I learned

_Fill this in during revision._
