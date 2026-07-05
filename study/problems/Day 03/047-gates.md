# 047 — More logic gates

| Field | Value |
|---|---|
| Day | Day 03 |
| Last successful submission | 2026-06-25 12:04:10 AM |
| Course location | Circuits → Combinational Logic → Basic Gates |
| HDLBits identifier | `gates` |
| Attempts | 2 total: 0 incorrect, 1 compile error, 0 simulation error |
| Success rate | 50% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/gates) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2003/047-gates.sv) |

## Question and submitted solution

![More logic gates question and submitted solution](../../images/Day%2003/047-gates.png)

## What the question is asking

Implement several basic gates at once, including bitwise outputs and their logical complements.

## Saved Verilog solution

```verilog
module top_module(
    input a, b,
    output out_and,
    output out_or,
    output out_xor,
    output out_nand,
    output out_nor,
    output out_xnor,
    output out_anotb
);
    assign out_and=a&b;
    assign out_or = a|b;
    assign out_xor =a^b;
    assign out_nand = ~(a&b);
    assign out_nor = ~(a|b);
    assign out_xnor= ~(a^b);
    assign out_anotb = a & ~(b);
endmodule
```

## What I learned

_Fill this in during revision._
