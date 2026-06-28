# 133 — Sequential circuit 7

| Field | Value |
|---|---|
| Day | Day 06 |
| Last successful submission | 2026-06-28 2:20:37 PM |
| Course location | Verification: Reading Simulations → Build a circuit from a simulation waveform |
| HDLBits identifier | `sim/circuit7` |
| Attempts | 5 total: 4 incorrect, 0 compile error, 0 simulation error |
| Success rate | 20% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/sim/circuit7) |
| Files | [Open screenshot at full resolution](../../images/Day%2006/133-sim__circuit7.png) · [Verilog solution](../../solutions/Day%2006/133-sim__circuit7.sv) |

## Question and submitted solution

<a href="../../images/Day%2006/133-sim__circuit7.png"><img src="../../images/Day%2006/133-sim__circuit7.png" alt="Sequential circuit 7 question and submitted solution" width="100%"></a>

## What the question is asking

This is a positive-edge-triggered register whose D input is the inverse of `a`. On each rising edge, `q <= ~a`; between rising edges Q holds its previous value even if A changes.

The nonblocking assignment models simultaneous flip-flop sampling. A waveform trace should therefore read A immediately before each rising edge and compare its inverse with Q immediately after that edge.

**Distinguishing feature:** if Q followed `~a` continuously, it would be combinational. The observed hold intervals between clock edges prove that memory is present.

## Saved Verilog solution

```verilog
module top_module (
    input clk,
    input a,
    output reg q
);

    always @(posedge clk) begin
        q <= ~a;
    end

endmodule
```

## What I learned

_Fill this in during revision._
