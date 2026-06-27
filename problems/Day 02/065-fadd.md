# 065 — Full adder

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 10:21:26 PM |
| Course location | Circuits → Combinational Logic → Arithmetic Circuits |
| HDLBits identifier | `fadd` |
| Attempts | 1 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/fadd) |
| Files | [Open screenshot at full resolution](../../images/Day%2002/065-fadd.png) · [Verilog solution](../../solutions/Day%2002/065-fadd.sv) |

## Question and submitted solution

<a href="../../images/Day%2002/065-fadd.png"><img src="../../images/Day%2002/065-fadd.png" alt="Full adder question and submitted solution" width="100%"></a>

## What the question is asking

Implement a full adder that includes carry-in and produces both sum and carry-out.

## Saved Verilog solution

```verilog
module top_module(
    input a, b, cin,
    output cout, sum
);
wire w1,w2,w3,w4;
    xor g1(sum, a,b,cin);
    //now the carry out part
    xor g2(w1,a,b);
    and g3(w2,w1,cin);
    and g4(w3,a,b);
    or g5(cout,w2,w3);
endmodule
```

## What I learned

_Fill this in during revision._
