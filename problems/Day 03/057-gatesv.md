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
| Files | [Open screenshot at full resolution](../../images/Day%2003/057-gatesv.png) · [Verilog solution](../../solutions/Day%2003/057-gatesv.sv) |

## Question and submitted solution

<a href="../../images/Day%2003/057-gatesv.png"><img src="../../images/Day%2003/057-gatesv.png" alt="Gates and vectors question and submitted solution" width="100%"></a>

## What the question is asking

For two vectors, compute bitwise gate results and also indicate whether the vectors differ at any or every position.

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
