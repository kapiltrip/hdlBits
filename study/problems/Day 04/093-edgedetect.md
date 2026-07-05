# 093 — Detect an edge

| Field | Value |
|---|---|
| Day | Day 04 |
| Last successful submission | 2026-06-26 2:28:20 PM |
| Course location | Circuits → Sequential Logic → Latches and Flip-Flops |
| HDLBits identifier | `edgedetect` |
| Attempts | 1 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/edgedetect) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2004/093-edgedetect.sv) |

## Question and submitted solution

![Detect an edge question and submitted solution](../../images/Day%2004/093-edgedetect.png)

## What the question is asking

Generate a one-cycle pulse whenever each input bit makes a 0-to-1 transition.

## Saved Verilog solution

```verilog
module top_module (
    input clk,
    input [7:0] in,
    output reg [7:0] pedge
);
    reg [7:0] prev;
    always @(posedge clk)begin
        prev<=in;
        pedge<=~prev&in;
    end
endmodule
```

## What I learned

_Fill this in during revision._
