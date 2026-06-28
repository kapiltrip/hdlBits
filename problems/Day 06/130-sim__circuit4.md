# 130 — Combinational circuit 4

| Field | Value |
|---|---|
| Day | Day 06 |
| Last successful submission | 2026-06-28 3:35:24 PM |
| Course location | Verification: Reading Simulations → Build a circuit from a simulation waveform |
| HDLBits identifier | `sim/circuit4` |
| Attempts | 4 total: 2 incorrect, 1 compile error, 0 simulation error |
| Success rate | 25% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/sim/circuit4) |
| Files | [Open screenshot at full resolution](../../images/Day%2006/130-sim__circuit4.png) · [Verilog solution](../../solutions/Day%2006/130-sim__circuit4.sv) |

## Question and submitted solution

<a href="../../images/Day%2006/130-sim__circuit4.png"><img src="../../images/Day%2006/130-sim__circuit4.png" alt="Combinational circuit 4 question and submitted solution" width="100%"></a>

## What the question is asking

The waveform shows that only `b` and `c` affect the output. Q is high whenever either is high, giving `q = b | c`; inputs A and D are observable distractors with no functional influence.

**How to infer this:** find intervals where A or D toggles while B and C remain fixed. Q does not change. Then compare the four B/C combinations: only 00 produces 0, while 01, 10, and 11 produce 1.

Ignoring irrelevant inputs is an important waveform-reading skill: a port’s presence does not guarantee that synthesized logic uses it.

## Saved Verilog solution

```verilog
module top_module (
    input a,
    input b,
    input c,
    input d,
    output q
);

    assign q = b | c;

endmodule
```

## What I learned

_Fill this in during revision._
