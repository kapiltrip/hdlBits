# 136 — Sequential circuit 10

| Field | Value |
|---|---|
| Day | Day 06 |
| Last successful submission | 2026-06-28 4:28:35 PM |
| Course location | Verification: Reading Simulations → Build a circuit from a simulation waveform |
| HDLBits identifier | `sim/circuit10` |
| Attempts | 1 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/sim/circuit10) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2006/136-sim__circuit10.sv) |

## Question and submitted solution

![Sequential circuit 10 question and submitted solution](../../images/Day%2006/136-sim__circuit10.png)

## What the question is asking

This circuit behaves like a serial full adder with one stored carry bit. The combinational output `q = a ^ b ^ state` is the one-bit sum of A, B, and the previous carry.

At each rising edge, `state` is updated to the majority function `ab | b·state | a·state`, which is exactly the carry-out of a full adder. The new carry then participates in Q during the following cycle.

| a | b | carry-in | q (sum) | next state (carry-out) |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 | 1 |
| 0 | 0 | 1 | 1 | 0 |

The absence of reset means the testbench must establish or tolerate the initial carry state before checking deterministic sequences.

## Saved Verilog solution

```verilog
module top_module (
    input clk,
    input a,
    input b,
    output q,
    output reg state
);

    assign q = a ^ b ^ state;

    always @(posedge clk) begin
        state <= (a & b) | (b & state) | (a & state);
    end

endmodule
```

## What I learned

_Fill this in during revision._
