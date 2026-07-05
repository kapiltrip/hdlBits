# 020 — Connecting ports by name

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 1:31:10 PM |
| Course location | Verilog Language → Modules: Hierarchy |
| HDLBits identifier | `module_name` |
| Attempts | 1 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/module_name) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2002/020-module_name.sv) |

## Question and submitted solution

![Connecting ports by name question and submitted solution](../../images/Day%2002/020-module_name.png)

## What the question is asking

Instantiate a module and connect its ports by name so each signal is matched explicitly.

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

endmodule
```

## What I learned

_Fill this in during revision._
