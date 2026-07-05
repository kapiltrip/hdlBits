# 007 — Declaring wires

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 12:35:55 AM |
| Course location | Verilog Language → Basics |
| HDLBits identifier | `wire_decl` |
| Attempts | 1 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/wire_decl) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2002/007-wire_decl.sv) |

## Question and submitted solution

![Declaring wires question and submitted solution](../../images/Day%2002/007-wire_decl.png)

## What the question is asking

Declare intermediate wires and connect the supplied gates so the module matches the shown circuit diagram.

## Saved Verilog solution

```verilog
`default_nettype none
module top_module(
    input a,
    input b,
    input c,
    input d,
    output out,
    output out_n   );

endmodule
```

## What I learned

_Fill this in during revision._
