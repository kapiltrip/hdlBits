# 029 — If statement

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 3:30:54 PM |
| Course location | Verilog Language → Procedures |
| HDLBits identifier | `always_if` |
| Attempts | 1 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/always_if) |
| Files | [Open screenshot at full resolution](../../images/Day%2002/029-always_if.png) · [Verilog solution](../../solutions/Day%2002/029-always_if.sv) |

## Question and submitted solution

<a href="../../images/Day%2002/029-always_if.png"><img src="../../images/Day%2002/029-always_if.png" alt="If statement question and submitted solution" width="100%"></a>

## What the question is asking

Use an if/else statement in combinational logic to implement the requested multiplexer behaviour.

## Saved Verilog solution

```verilog
// synthesis verilog_input_version verilog_2001
module top_module(
    input a,
    input b,
    input sel_b1,
    input sel_b2,
    output wire out_assign,
    output reg out_always   );

endmodule
```

## What I learned

_Fill this in during revision._
