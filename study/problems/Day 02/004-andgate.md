# 004 — AND gate

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 12:29:06 AM |
| Course location | Verilog Language → Basics |
| HDLBits identifier | `andgate` |
| Attempts | 1 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/andgate) |
| Files | [Open screenshot at full resolution](../../images/Day%2002/004-andgate.png) · [Verilog solution](../../solutions/Day%2002/004-andgate.sv) |

## Question and submitted solution

<a href="../../images/Day%2002/004-andgate.png"><img src="../../images/Day%2002/004-andgate.png" alt="AND gate question and submitted solution" width="100%"></a>

## What the question is asking

Produce an output that is high only when both input signals are high.

## Saved Verilog solution

```verilog
module top_module(
    input a,
    input b,
    output out
);
    and g1(out ,a , b);
endmodule
```

## What I learned

_Fill this in during revision._
