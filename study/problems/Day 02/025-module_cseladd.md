# 025 — Carry-select adder

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 3:06:09 PM |
| Course location | Verilog Language → Modules: Hierarchy |
| HDLBits identifier | `module_cseladd` |
| Attempts | 2 total: 0 incorrect, 1 compile error, 0 simulation error |
| Success rate | 50% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/module_cseladd) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2002/025-module_cseladd.sv) |

## Question and submitted solution

![Carry-select adder question and submitted solution](../../images/Day%2002/025-module_cseladd.png)

## What the question is asking

Build a carry-select adder by computing both possible upper sums and selecting the correct one using the lower carry.

## Saved Verilog solution

```verilog
module top_module(
    input [31:0] a,
    input [31:0] b,
    output [31:0] sum
);

endmodule
```

## What I learned

_Fill this in during revision._
