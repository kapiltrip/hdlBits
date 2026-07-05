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
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2004/101-shift4.sv) |

## Question and submitted solution

![4-bit shift register question and submitted solution](../../images/Day%2004/101-shift4.png)

## What the question is asking

Build a 4-bit shift register with the specified load/shift controls and expose the requested stage output.

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
