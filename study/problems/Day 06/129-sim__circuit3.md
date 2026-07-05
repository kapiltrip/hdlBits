# 129 — Combinational circuit 3

| Field | Value |
|---|---|
| Day | Day 06 |
| Last successful submission | 2026-06-28 3:26:19 PM |
| Course location | Verification: Reading Simulations → Build a circuit from a simulation waveform |
| HDLBits identifier | `sim/circuit3` |
| Attempts | 1 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/sim/circuit3) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2006/129-sim__circuit3.sv) |

## Question and submitted solution

![Combinational circuit 3 question and submitted solution](../../images/Day%2006/129-sim__circuit3.png)

## What the question is asking

The submitted expression factors to `q = (a | b) & (c | d)`. Thus at least one signal from the A/B pair and at least one signal from the C/D pair must be high.

The unfactored form, `d&(a|b) | c&(a|b)`, makes the waveform-derived product terms visible; Boolean factoring exposes the simpler two-ORs-into-an-AND circuit.

**Checks:** if A=B=0, Q is always 0 regardless of C/D. If C=D=0, Q is also always 0. With A=1 and C=1, Q is 1 regardless of B/D. These controlled waveform comparisons distinguish the grouped function from a four-input OR.

## Saved Verilog solution

```verilog
module top_module (
    input a,
    input b,
    input c,
    input d,
    output q
);

    assign q = (d & (a | b)) | (c & (a | b));

endmodule
```

## What I learned

_Fill this in during revision._
