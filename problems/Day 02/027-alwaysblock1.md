# 027 — Always blocks (combinational)

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 3:23:21 PM |
| Course location | Verilog Language → Procedures |
| HDLBits identifier | `alwaysblock1` |
| Attempts | 1 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/alwaysblock1) |
| Files | [Open screenshot at full resolution](../../images/Day%2002/027-alwaysblock1.png) · [Verilog solution](../../solutions/Day%2002/027-alwaysblock1.sv) |

## Question and submitted solution

<a href="../../images/Day%2002/027-alwaysblock1.png"><img src="../../images/Day%2002/027-alwaysblock1.png" alt="Always blocks (combinational) question and submitted solution" width="100%"></a>

## What the question is asking

Describe the same combinational logic with both a continuous assignment and an always block.

## Saved Verilog solution

```verilog
// synthesis verilog_input_version verilog_2001
module top_module(
    input a,
    input b,
    output wire out_assign,
    output reg out_alwaysblock
);
assign out_assign= a&b;
    always @(*)begin
        out_alwaysblock=a&b;
    end
endmodule
```

## What I learned

_Fill this in during revision._
