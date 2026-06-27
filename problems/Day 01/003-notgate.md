# 003 — Inverter

| Field | Value |
|---|---|
| Day | Day 01 |
| Last successful submission | 2026-06-23 5:52:19 PM |
| Course location | Verilog Language → Basics |
| HDLBits identifier | `notgate` |
| Attempts | 1 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/notgate) |
| Files | [Open screenshot at full resolution](../../images/Day%2001/003-notgate.png) · [Verilog solution](../../solutions/Day%2001/003-notgate.sv) |

## Question and submitted solution

<a href="../../images/Day%2001/003-notgate.png"><img src="../../images/Day%2001/003-notgate.png" alt="Inverter question and submitted solution" width="100%"></a>

## What the question is asking

Drive the output with the logical inverse of the input, implementing a NOT gate.

## Saved Verilog solution

```verilog
module top_module( input in, output out );
    not g1(out , in );
endmodule
```

## What I learned

_Fill this in during revision._
