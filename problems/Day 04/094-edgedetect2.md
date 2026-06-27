# 094 — Detect both edges

| Field | Value |
|---|---|
| Day | Day 04 |
| Last successful submission | 2026-06-26 2:31:22 PM |
| Course location | Circuits → Sequential Logic → Latches and Flip-Flops |
| HDLBits identifier | `edgedetect2` |
| Attempts | 1 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/edgedetect2) |
| Files | [Screenshot](../../images/Day%2004/094-edgedetect2.png) · [Verilog solution](../../solutions/Day%2004/094-edgedetect2.sv) |

## Problem and saved submission

![Detect both edges problem and saved submission](../../images/Day%2004/094-edgedetect2.png)

## Saved Verilog solution

```verilog
module top_module (
    input clk,
    input [7:0] in,
    output [7:0] anyedge
);
    reg [7:0] positive;
    reg [7:0] negative ;
    always @(posedge clk)begin
        positive<=in;
        negative<=in;
        anyedge <= (~positive& in) | (negative& ~ in);
    end
endmodule
```

## What I learned

_Fill this in during revision._
