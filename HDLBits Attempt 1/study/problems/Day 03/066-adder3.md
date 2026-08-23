# 066 — 3-bit binary adder

| Field | Value |
|---|---|
| Day | Day 03 |
| Last successful submission | 2026-06-25 3:24:38 PM |
| Course location | Circuits → Combinational Logic → Arithmetic Circuits |
| HDLBits identifier | `adder3` |
| Attempts | 3 total: 1 incorrect, 1 compile error, 0 simulation error |
| Success rate | 33% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/adder3) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2003/066-adder3.sv) |

## Question and submitted solution

![3-bit binary adder question and submitted solution](../../images/Day%2003/066-adder3.png)

## What the question is asking

Chain three full adders to add two 3-bit numbers and expose the intermediate carry signals.

## Saved Verilog solution

```verilog
module top_module(
    input [2:0] a, b,
    input cin,
    output [2:0] cout,
    output [2:0] sum
);
//4 bit addition
    wire [3:0] carry;
    assign carry[0]=cin;

    genvar i;
    generate
        for(i=0;i<3;i=i+1)begin : generating
            fa fullAdders(
                .a(a[i]),
                .b(b[i]),
                .cin(carry[i]),
                .sum(sum[i]),
                .cout(carry[i+1])
            );
        end
    endgenerate
    assign cout=carry[3:1];
endmodule
module fa(
    input wire a,b,cin,
    output wire cout, sum
);
    assign sum= a^b^cin;
    assign cout = a&b | b&cin | a &cin ;

endmodule
```

## What I learned

_Fill this in during revision._
