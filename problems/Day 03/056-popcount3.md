# 056 — 3-bit population count

| Field | Value |
|---|---|
| Day | Day 03 |
| Last successful submission | 2026-06-25 12:58:42 AM |
| Course location | Circuits → Combinational Logic → Basic Gates |
| HDLBits identifier | `popcount3` |
| Attempts | 2 total: 1 incorrect, 0 compile error, 0 simulation error |
| Success rate | 50% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/popcount3) |
| Files | [Open screenshot at full resolution](../../images/Day%2003/056-popcount3.png) · [Verilog solution](../../solutions/Day%2003/056-popcount3.sv) |

## Question and submitted solution

<a href="../../images/Day%2003/056-popcount3.png"><img src="../../images/Day%2003/056-popcount3.png" alt="3-bit population count question and submitted solution" width="100%"></a>

## What the question is asking

Count the number of asserted bits in a 3-bit input and return that count as a binary value.

## Saved Verilog solution

```verilog
module top_module(
    input [2:0] in,
    output [1:0] out
);
    integer i;
    always @(*)begin
        out = 2'b00;
        for(i=0;i<3;i=i+1)begin
            out=out +in[i];
        end
    end
endmodule
```

## What I learned

_Fill this in during revision._
