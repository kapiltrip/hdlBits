# 036 — Reduction operators

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 6:14:36 PM |
| Course location | Verilog Language → More Verilog Features |
| HDLBits identifier | `reduction` |
| Attempts | 2 total: 1 incorrect, 0 compile error, 0 simulation error |
| Success rate | 50% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/reduction) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2002/036-reduction.sv) |

## Question and submitted solution

![Reduction operators question and submitted solution](../../images/Day%2002/036-reduction.png)

## What the question is asking

Compare bitwise and reduction operators by producing per-bit results and single-bit reductions from two vectors.

## Saved Verilog solution

```verilog
module top_module (
    input [7:0] in,
    output parity
);
assign parity= ^in;
//odd no of ones will be known by this
endmodule
```

## What I learned

_Fill this in during revision._
