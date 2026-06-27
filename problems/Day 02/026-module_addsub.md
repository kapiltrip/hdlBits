# 026 — Adder-subtractor

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 3:21:30 PM |
| Course location | Verilog Language → Modules: Hierarchy |
| HDLBits identifier | `module_addsub` |
| Attempts | 1 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/module_addsub) |
| Files | [Screenshot](../../images/Day%2002/026-module_addsub.png) · [Verilog solution](../../solutions/Day%2002/026-module_addsub.sv) |

## Problem and saved submission

![Adder-subtractor problem and saved submission](../../images/Day%2002/026-module_addsub.png)

## Saved Verilog solution

```verilog
module top_module(
    input [31:0] a,
    input [31:0] b,
    input sub,
    output [31:0] sum
);
    wire [15:0] alower=a[15:0];
    wire [15:0] ahigher=a[31:16];       
    //b will change , i.e blower and bupper will change, based, on sum , 
    //i can extend sub and then make them xor 
    wire [15:0] blower = {16{sub}}^b[15:0];
    wire [15:0] bhigher = {16{sub}}^b[31:16];
    wire [15:0] sumlower,sumUpper;
    wire coutA , ignoreCoutB;
//instantiate twice, the module add16
    
    add16 a1(
        .a(alower),
        .b(blower),
        .cin(sub),
        .cout(coutA),
        .sum(sumlower)
    );
    add16 a2(
        .a(ahigher),
        .b(bhigher),
        .cin(coutA),
        .cout(ignoreCoutB),
        .sum(sumUpper)
    );
    assign sum = {sumUpper,sumlower};
endmodule
```

## What I learned

_Fill this in during revision._
