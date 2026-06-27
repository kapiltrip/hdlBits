# 057 — Gates and vectors

| Field | Value |
|---|---|
| Day | Day 03 |
| Last successful submission | 2026-06-25 9:45:17 PM |
| Course location | Circuits → Combinational Logic → Basic Gates |
| HDLBits identifier | `gatesv` |
| Attempts | 6 total: 5 incorrect, 0 compile error, 0 simulation error |
| Success rate | 17% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/gatesv) |
| Files | [Screenshot](../../images/Day%2003/057-gatesv.png) · [Verilog solution](../../solutions/Day%2003/057-gatesv.sv) |

## Problem and saved submission

![Gates and vectors problem and saved submission](../../images/Day%2003/057-gatesv.png)

## Saved Verilog solution

```verilog
module top_module( 
    input [3:0] in,
    output [2:0] out_both,
    output [3:1] out_any,
    output [3:0] out_different 
);
    assign out_both= in[3:1] & in[2:0]; // out_both[2] should indicate if in[2] and in[3] are both 1
    assign out_any= in[3:1] | in[2:0];//out_any[2] should indicate if either in[2] or in[1] are 1
    assign out_different= in^ {in[0],in[3:1]};//out_different[2] should indicate if in[2] is different from in[3] , msb and lsb are neighbours
endmodule
```

## What I learned

_Fill this in during revision._
