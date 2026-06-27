# 089 — Mux and DFF

| Field | Value |
|---|---|
| Day | Day 04 |
| Last successful submission | 2026-06-26 12:09:54 AM |
| Course location | Circuits → Sequential Logic → Latches and Flip-Flops |
| HDLBits identifier | `mt2015_muxdff` |
| Attempts | 2 total: 0 incorrect, 1 compile error, 0 simulation error |
| Success rate | 50% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/mt2015_muxdff) |
| Files | [Screenshot](../../images/Day%2004/089-mt2015_muxdff.png) · [Verilog solution](../../solutions/Day%2004/089-mt2015_muxdff.sv) |

## Problem and saved submission

![Mux and DFF problem and saved submission](../../images/Day%2004/089-mt2015_muxdff.png)

## Saved Verilog solution

```verilog
module top_module (
    input clk,
    input L,
    input r_in,
    input q_in,
    output reg Q
);
    
    always @(posedge clk)begin
         Q <= (L)?r_in:q_in;
    end
endmodule
```

## What I learned

_Fill this in during revision._
