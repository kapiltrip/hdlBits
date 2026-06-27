# 083 — DFF with asynchronous reset

| Field | Value |
|---|---|
| Day | Day 03 |
| Last successful submission | 2026-06-25 10:29:11 PM |
| Course location | Circuits → Sequential Logic → Latches and Flip-Flops |
| HDLBits identifier | `dff8ar` |
| Attempts | 2 total: 0 incorrect, 1 compile error, 0 simulation error |
| Success rate | 50% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/dff8ar) |
| Files | [Screenshot](../../images/Day%2003/083-dff8ar.png) · [Verilog solution](../../solutions/Day%2003/083-dff8ar.sv) |

## Problem and saved submission

![DFF with asynchronous reset problem and saved submission](../../images/Day%2003/083-dff8ar.png)

## Saved Verilog solution

```verilog
module top_module (
    input clk,
    input areset,   // active high asynchronous reset
    input [7:0] d,
    output [7:0] q
);
    always @(posedge clk or posedge areset)begin
        if(areset)
            q<=8'd0;
        else 
            q<=d;
    end
endmodule
```

## What I learned

_Fill this in during revision._
