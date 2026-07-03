# 095 — Edge capture register

| Field | Value |
|---|---|
| Day | Day 04 |
| Last successful submission | 2026-06-26 2:50:42 PM |
| Course location | Circuits → Sequential Logic → Latches and Flip-Flops |
| HDLBits identifier | `edgecapture` |
| Attempts | 7 total: 5 incorrect, 1 compile error, 0 simulation error |
| Success rate | 14% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/edgecapture) |
| Files | [Open screenshot at full resolution](../../images/Day%2004/095-edgecapture.png) · [Verilog solution](../../solutions/Day%2004/095-edgecapture.sv) |

## Question and submitted solution

<a href="../../images/Day%2004/095-edgecapture.png"><img src="../../images/Day%2004/095-edgecapture.png" alt="Edge capture register question and submitted solution" width="100%"></a>

## What the question is asking

Set a register bit when a falling edge occurs and keep it set until a synchronous reset clears it.

## Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,
    input [31:0] in,
    output [31:0] out
);

endmodule
```

## What I learned

_Fill this in during revision._
