# 023 — Adder 1

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 2:03:55 PM |
| Course location | Verilog Language → Modules: Hierarchy |
| HDLBits identifier | `module_add` |
| Attempts | 1 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/module_add) |
| Files | [Open screenshot at full resolution](../../images/Day%2002/023-module_add.png) · [Verilog solution](../../solutions/Day%2002/023-module_add.sv) |

## Question and submitted solution

<a href="../../images/Day%2002/023-module_add.png"><img src="../../images/Day%2002/023-module_add.png" alt="Adder 1 question and submitted solution" width="100%"></a>

## What the question is asking

Instantiate two 16-bit adders to create a 32-bit adder, propagating the carry between the lower and upper halves.

## Saved Verilog solution

```verilog
module top_module(
    input [31:0] a,
    input [31:0] b,
    output [31:0] sum
);
    wire [15:0] a1Input=a[15:0];
    wire [15:0] b1Input=b[15:0];
    wire [15:0] a2Input=a[31:16];
    wire [15:0] b2Input=b[31:16];
    wire coutAdder1;
    wire coutAdder2;
    wire [15:0] sum1,sum2;
    add16 adder1(
        .a(a1Input),
        .b(b1Input),
        .cin(1'b0),
        .cout(coutAdder1),
        .sum(sum1)
    );
    add16 adder2(
        .a(a2Input),
        .b(b2Input),
        .cin(coutAdder1),
        .cout(coutAdder2),  // to ignore this
        .sum(sum2)
    );
    assign sum = {sum2,sum1};
endmodule
```

## What I learned

_Fill this in during revision._
