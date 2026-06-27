# 024 — Adder 2

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 2:44:10 PM |
| Course location | Verilog Language → Modules: Hierarchy |
| HDLBits identifier | `module_fadd` |
| Attempts | 4 total: 1 incorrect, 2 compile error, 0 simulation error |
| Success rate | 25% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/module_fadd) |
| Files | [Screenshot](../../images/Day%2002/024-module_fadd.png) · [Verilog solution](../../solutions/Day%2002/024-module_fadd.sv) |

## Problem and saved submission

![Adder 2 problem and saved submission](../../images/Day%2002/024-module_fadd.png)

## Saved Verilog solution

```verilog
module top_module (
    input [31:0] a,
    input [31:0] b,
    output [31:0] sum
);//

endmodule

module add1 ( input a, input b, input cin,   output sum, output cout );

// Full adder module here

endmodule
```

## What I learned

_Fill this in during revision._
