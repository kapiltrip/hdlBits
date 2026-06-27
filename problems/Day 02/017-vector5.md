# 017 — More replication

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 12:26:24 AM |
| Course location | Verilog Language → Vectors |
| HDLBits identifier | `vector5` |
| Attempts | 5 total: 0 incorrect, 4 compile error, 0 simulation error |
| Success rate | 20% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/vector5) |
| Files | [Screenshot](../../images/Day%2002/017-vector5.png) · [Verilog solution](../../solutions/Day%2002/017-vector5.sv) |

## Problem and saved submission

![More replication problem and saved submission](../../images/Day%2002/017-vector5.png)

## Saved Verilog solution

```verilog
module top_module (
    input a, b, c, d, e,
    output [24:0] out 
);//
    wire [24:0] top = {5{a,b,c,d,e}};
    wire [24:0] bottom= {{5{a}},{5{b}},{5{c}}, {5{d}}, {5{e}}};
    assign out = ~(top ^ bottom);
endmodule
```

## What I learned

_Fill this in during revision._
