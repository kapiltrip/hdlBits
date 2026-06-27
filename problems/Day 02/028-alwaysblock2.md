# 028 — Always blocks (clocked)

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 3:25:20 PM |
| Course location | Verilog Language → Procedures |
| HDLBits identifier | `alwaysblock2` |
| Attempts | 1 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/alwaysblock2) |
| Files | [Screenshot](../../images/Day%2002/028-alwaysblock2.png) · [Verilog solution](../../solutions/Day%2002/028-alwaysblock2.sv) |

## Problem and saved submission

![Always blocks (clocked) problem and saved submission](../../images/Day%2002/028-alwaysblock2.png)

## Saved Verilog solution

```verilog
// synthesis verilog_input_version verilog_2001
module top_module(
    input clk,
    input a,
    input b,
    output wire out_assign,
    output reg out_always_comb,
    output reg out_always_ff   );

endmodule
```

## What I learned

_Fill this in during revision._
