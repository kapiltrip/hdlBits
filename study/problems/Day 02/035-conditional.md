# 035 — Conditional ternary operator

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 6:09:15 PM |
| Course location | Verilog Language → More Verilog Features |
| HDLBits identifier | `conditional` |
| Attempts | 1 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/conditional) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2002/035-conditional.sv) |

## Question and submitted solution

![Conditional ternary operator question and submitted solution](../../images/Day%2002/035-conditional.png)

## What the question is asking

Use nested ternary operators to select the smallest unsigned value from several inputs.

## Saved Verilog solution

```verilog
module top_module (
    input [7:0] a, b, c, d,
    output [7:0] min);//

    // assign intermediate_result1 = compare? true: false;
    //to find, the mininum
    //compare a and b ,
    wire [7:0] minAB,minCD;
    assign minAB= (a<b)?a:b;
    assign minCD= (c<d)?c:d;
    assign min = (minAB<minCD)?minAB:minCD;
endmodule
```

## What I learned

_Fill this in during revision._
