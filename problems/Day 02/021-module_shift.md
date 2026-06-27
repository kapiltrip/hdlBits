# 021 — Three modules

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 1:37:32 PM |
| Course location | Verilog Language → Modules: Hierarchy |
| HDLBits identifier | `module_shift` |
| Attempts | 2 total: 0 incorrect, 1 compile error, 0 simulation error |
| Success rate | 50% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/module_shift) |
| Files | [Screenshot](../../images/Day%2002/021-module_shift.png) · [Verilog solution](../../solutions/Day%2002/021-module_shift.sv) |

## Problem and saved submission

![Three modules problem and saved submission](../../images/Day%2002/021-module_shift.png)

## Saved Verilog solution

```verilog
module top_module ( input clk, input d, output q );
    wire w1,w2,w3;
    my_dff d1(
        .clk(clk),
        .d(d),
        .q(w1)
    );
    my_dff d2(
        .clk(clk),
        .d(w1),
        .q(w2)
    );
    my_dff d3(
        .clk(clk),
        .d(w2),
        .q(q)
    );
    
endmodule
```

## What I learned

_Fill this in during revision._
