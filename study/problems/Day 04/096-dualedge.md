# 096 — Dual-edge triggered flip-flop

| Field | Value |
|---|---|
| Day | Day 04 |
| Last successful submission | 2026-06-26 3:07:56 PM |
| Course location | Circuits → Sequential Logic → Latches and Flip-Flops |
| HDLBits identifier | `dualedge` |
| Attempts | 7 total: 4 incorrect, 2 compile error, 0 simulation error |
| Success rate | 14% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/dualedge) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2004/096-dualedge.sv) |

## Question and submitted solution

![Dual-edge triggered flip-flop question and submitted solution](../../images/Day%2004/096-dualedge.png)

## What the question is asking

Emulate dual-edge-triggered storage using logic that captures data on both rising and falling clock edges.

## Saved Verilog solution

```verilog
module top_module (
    input clk,
    input d,
    output q
);
reg pos,neg;
    always @(posedge clk)begin
        pos<=d;
    end
    always @(negedge clk)begin
        neg<=d;
    end
    assign q= (clk) ?  pos:neg;
endmodule
```

## What I learned

_Fill this in during revision._
