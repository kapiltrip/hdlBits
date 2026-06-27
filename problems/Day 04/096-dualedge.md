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
| Files | [Screenshot](../../images/Day%2004/096-dualedge.png) · [Verilog solution](../../solutions/Day%2004/096-dualedge.sv) |

## Problem and saved submission

![Dual-edge triggered flip-flop problem and saved submission](../../images/Day%2004/096-dualedge.png)

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
