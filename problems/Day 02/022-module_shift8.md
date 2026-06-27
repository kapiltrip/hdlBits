# 022 — Modules and vectors

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 1:53:37 PM |
| Course location | Verilog Language → Modules: Hierarchy |
| HDLBits identifier | `module_shift8` |
| Attempts | 7 total: 2 incorrect, 4 compile error, 0 simulation error |
| Success rate | 14% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/module_shift8) |
| Files | [Open screenshot at full resolution](../../images/Day%2002/022-module_shift8.png) · [Verilog solution](../../solutions/Day%2002/022-module_shift8.sv) |

## Question and submitted solution

<a href="../../images/Day%2002/022-module_shift8.png"><img src="../../images/Day%2002/022-module_shift8.png" alt="Modules and vectors question and submitted solution" width="100%"></a>

## What the question is asking

Instantiate the supplied 8-bit module and connect vector signals correctly through the hierarchy.

## Saved Verilog solution

```verilog
module top_module (
    input clk,
    input [7:0] d,
    input [1:0] sel,
    output [7:0] q
);

endmodule
```

## What I learned

_Fill this in during revision._
