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
| Files | [Open screenshot at full resolution](../../images/Day%2003/083-dff8ar.png) · [Verilog solution](../../solutions/Day%2003/083-dff8ar.sv) |

## Question and submitted solution

<a href="../../images/Day%2003/083-dff8ar.png"><img src="../../images/Day%2003/083-dff8ar.png" alt="DFF with asynchronous reset question and submitted solution" width="100%"></a>

## What the question is asking

Create an 8-bit register with asynchronous reset, allowing reset to change the output without waiting for a clock edge.

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
