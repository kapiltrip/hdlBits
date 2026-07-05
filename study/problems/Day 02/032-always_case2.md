# 032 — Priority encoder

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 5:09:06 PM |
| Course location | Verilog Language → Procedures |
| HDLBits identifier | `always_case2` |
| Attempts | 15 total: 11 incorrect, 3 compile error, 0 simulation error |
| Success rate | 7% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/always_case2) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2002/032-always_case2.sv) |

## Question and submitted solution

![Priority encoder question and submitted solution](../../images/Day%2002/032-always_case2.png)

## What the question is asking

Implement a priority encoder whose output identifies the highest-priority asserted input bit.

## Saved Verilog solution

```verilog
// synthesis verilog_input_version verilog_2001
module top_module (
    input [3:0] in,
    output reg [1:0] pos  );

endmodule
```

## What I learned

_Fill this in during revision._
