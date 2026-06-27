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
| Files | [Screenshot](../../images/Day%2002/022-module_shift8.png) · [Verilog solution](../../solutions/Day%2002/022-module_shift8.sv) |

## Problem and saved submission

![Modules and vectors problem and saved submission](../../images/Day%2002/022-module_shift8.png)

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
