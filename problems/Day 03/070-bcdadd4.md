# 070 — 4-digit BCD adder

| Field | Value |
|---|---|
| Day | Day 03 |
| Last successful submission | 2026-06-25 5:16:55 PM |
| Course location | Circuits → Combinational Logic → Arithmetic Circuits |
| HDLBits identifier | `bcdadd4` |
| Attempts | 2 total: 0 incorrect, 1 compile error, 0 simulation error |
| Success rate | 50% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/bcdadd4) |
| Files | [Screenshot](../../images/Day%2003/070-bcdadd4.png) · [Verilog solution](../../solutions/Day%2003/070-bcdadd4.sv) |

## Problem and saved submission

![4-digit BCD adder problem and saved submission](../../images/Day%2003/070-bcdadd4.png)

## Saved Verilog solution

```verilog
module top_module ( 
    input [15:0] a, b,
    input cin,
    output cout,
    output [15:0] sum 
);
    wire [4:0] carry;
    assign carry[0]= cin;
genvar i ; 
    generate
        for(i=0;i<4;i=i+1)begin : callingTheAdder
            bcd_fadd call(
                .a(a[4*i+:4]),
                .b(b[4*i+:4]),
                .cin(carry[i]),
                .cout(carry[i+1]),
                .sum(sum[i*4+:4])
            );
        end
    endgenerate
    assign cout = carry [4];
endmodule
```

## What I learned

_Fill this in during revision._
