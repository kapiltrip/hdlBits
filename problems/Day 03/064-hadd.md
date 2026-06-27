# 064 — Half adder

| Field | Value |
|---|---|
| Day | Day 03 |
| Last successful submission | 2026-06-25 3:25:33 PM |
| Course location | Circuits → Combinational Logic → Arithmetic Circuits |
| HDLBits identifier | `hadd` |
| Attempts | 1 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/hadd) |
| Files | [Open screenshot at full resolution](../../images/Day%2003/064-hadd.png) · [Verilog solution](../../solutions/Day%2003/064-hadd.sv) |

## Question and submitted solution

<a href="../../images/Day%2003/064-hadd.png"><img src="../../images/Day%2003/064-hadd.png" alt="Half adder question and submitted solution" width="100%"></a>

## What the question is asking

Implement a half adder that produces a one-bit sum and carry from two input bits.

## Saved Verilog solution

```verilog
module top_module(
    input a, b,
    output cout, sum
);
assign cout = a &b;
    assign sum = a^b;
endmodule
```

## What I learned

_Fill this in during revision._
