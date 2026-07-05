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
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2002/021-module_shift.sv) |

## Question and submitted solution

![Three modules question and submitted solution](../../images/Day%2002/021-module_shift.png)

## What the question is asking

Chain three copies of the provided module so each stage feeds the next stage.

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
