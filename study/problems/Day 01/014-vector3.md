# 014 — Vector concatenation operator

| Field | Value |
|---|---|
| Day | Day 01 |
| Last successful submission | 2026-06-23 10:56:44 PM |
| Course location | Verilog Language → Vectors |
| HDLBits identifier | `vector3` |
| Attempts | 8 total: 0 incorrect, 7 compile error, 0 simulation error |
| Success rate | 13% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/vector3) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2001/014-vector3.sv) |

## Question and submitted solution

![Vector concatenation operator question and submitted solution](../../images/Day%2001/014-vector3.png)

## What the question is asking

Use concatenation to regroup the input vectors and assign the requested output vectors in the specified bit order.

## Saved Verilog solution

```verilog
module top_module (
    input [4:0] a, b, c, d, e, f,
    output [7:0] w, x, y, z );//

    // assign { ... } = { ... };

endmodule
```

## What I learned

_Fill this in during revision._
