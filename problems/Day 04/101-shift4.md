# 101 — 4-bit shift register

| Field | Value |
|---|---|
| Day | Day 04 |
| Last successful submission | 2026-06-26 4:10:18 PM |
| Course location | Circuits → Sequential Logic → Shift Registers |
| HDLBits identifier | `shift4` |
| Attempts | 4 total: 3 incorrect, 0 compile error, 0 simulation error |
| Success rate | 25% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/shift4) |
| Files | [Screenshot](../../images/Day%2004/101-shift4.png) · [Verilog solution](../../solutions/Day%2004/101-shift4.sv) |

## Problem and saved submission

![4-bit shift register problem and saved submission](../../images/Day%2004/101-shift4.png)

## Saved Verilog solution

```verilog
module top_module(
    input clk,
    input areset,  // async active-high reset to zero
    input load,
    input ena,
    input [3:0] data,
    output reg [3:0] q); 

endmodule
```

## What I learned

_Fill this in during revision._
