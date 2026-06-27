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
| Files | [Screenshot](../../images/Day%2003/064-hadd.png) · [Verilog solution](../../solutions/Day%2003/064-hadd.sv) |

## Problem and saved submission

![Half adder problem and saved submission](../../images/Day%2003/064-hadd.png)

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
