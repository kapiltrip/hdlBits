# 019 — Connecting ports by position

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 1:28:26 PM |
| Course location | Verilog Language → Modules: Hierarchy |
| HDLBits identifier | `module_pos` |
| Attempts | 2 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/module_pos) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2002/019-module_pos.sv) |

## Question and submitted solution

![Connecting ports by position question and submitted solution](../../images/Day%2002/019-module_pos.png)

## What the question is asking

Instantiate a module and connect its ports by position, keeping the connection order exactly correct.

## Saved Verilog solution

```verilog
module top_module (
    input a,
    input b,
    input c,
    input d,
    output out1,
    output out2
);
    mod_a instant(
        out1,out2,a,b,c,d
    );
endmodule
```

## What I learned

_Fill this in during revision._
