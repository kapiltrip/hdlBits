# 127 — Combinational circuit 1

| Field | Value |
|---|---|
| Day | Day 06 |
| Last successful submission | 2026-06-28 1:33:25 AM |
| Course location | Verification: Reading Simulations → Build a circuit from a simulation waveform |
| HDLBits identifier | `sim/circuit1` |
| Attempts | 2 total: 1 incorrect, 0 compile error, 0 simulation error |
| Success rate | 50% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/sim/circuit1) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2006/127-sim__circuit1.sv) |

## Question and submitted solution

![Combinational circuit 1 question and submitted solution](../../images/Day%2006/127-sim__circuit1.png)

## What the question is asking

The waveform shows a combinational AND function. Output `q` is high only during intervals in which both `a` and `b` are high, so the implementation is `q = a & b`.

Because there is no clock or storage, output changes propagate whenever either input changes. The four-row truth table is 00→0, 01→0, 10→0, and 11→1.

**Waveform method:** compare each transition of one input while holding the other fixed. When B is 0, changing A has no effect; when B is 1, Q follows A. That uniquely identifies AND rather than OR or XOR.

## Saved Verilog solution

```verilog
module top_module (
    input a,
    input b,
    output q
);

    assign q = a & b;

endmodule
```

## What I learned

_Fill this in during revision._
