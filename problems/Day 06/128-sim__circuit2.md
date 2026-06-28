# 128 — Combinational circuit 2

| Field | Value |
|---|---|
| Day | Day 06 |
| Last successful submission | 2026-06-28 3:19:03 PM |
| Course location | Verification: Reading Simulations → Build a circuit from a simulation waveform |
| HDLBits identifier | `sim/circuit2` |
| Attempts | 2 total: 1 incorrect, 0 compile error, 0 simulation error |
| Success rate | 50% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/sim/circuit2) |
| Files | [Open screenshot at full resolution](../../images/Day%2006/128-sim__circuit2.png) · [Verilog solution](../../solutions/Day%2006/128-sim__circuit2.sv) |

## Question and submitted solution

<a href="../../images/Day%2006/128-sim__circuit2.png"><img src="../../images/Day%2006/128-sim__circuit2.png" alt="Combinational circuit 2 question and submitted solution" width="100%"></a>

## What the question is asking

The waveform corresponds to four-input even parity, implemented as the inverse of a four-way XOR: `q = ~(a ^ b ^ c ^ d)`.

An XOR reduction is 1 when an odd number of inputs are high. Inverting it makes Q high for 0, 2, or 4 asserted inputs and low for 1 or 3 asserted inputs. The same function could be written with the reduction-XNOR operator `~^{a,b,c,d}`.

**Trace examples:** 0000 has zero ones and produces 1; 0001 has one one and produces 0; 1010 has two ones and produces 1. Counting asserted bits is often the fastest way to recognize parity in a waveform.

## Saved Verilog solution

```verilog
module top_module (
    input a,
    input b,
    input c,
    input d,
    output q
);

    assign q = ~(a ^ b ^ c ^ d);

endmodule
```

## What I learned

_Fill this in during revision._
