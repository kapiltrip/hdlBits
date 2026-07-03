# 028 — Always blocks (clocked)

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 3:25:20 PM |
| Course location | Verilog Language → Procedures |
| HDLBits identifier | `alwaysblock2` |
| Attempts | 1 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/alwaysblock2) |
| Files | [Open screenshot at full resolution](../../images/Day%2002/028-alwaysblock2.png) · [Verilog solution](../../solutions/Day%2002/028-alwaysblock2.sv) |

## Question and submitted solution

<a href="../../images/Day%2002/028-alwaysblock2.png"><img src="../../images/Day%2002/028-alwaysblock2.png" alt="Always blocks (clocked) question and submitted solution" width="100%"></a>

## What the question is asking

Describe clocked storage in an always block so the output captures the input on each active clock edge.

## Saved Verilog solution

```verilog
// synthesis verilog_input_version verilog_2001
module top_module(
    input clk,
    input a,
    input b,
    output wire out_assign,
    output reg out_always_comb,
    output reg out_always_ff   );

endmodule
```

## What I learned

_Fill this in during revision._
