# 016 — Replication operator

| Field | Value |
|---|---|
| Day | Day 01 |
| Last successful submission | 2026-06-23 11:49:31 PM |
| Course location | Verilog Language → Vectors |
| HDLBits identifier | `vector4` |
| Attempts | 9 total: 0 incorrect, 8 compile error, 0 simulation error |
| Success rate | 11% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/vector4) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2001/016-vector4.sv) |

## Question and submitted solution

![Replication operator question and submitted solution](../../images/Day%2001/016-vector4.png)

## What the question is asking

Use the replication operator to repeat a bit pattern and form the required wider output vector.

## Saved Verilog solution

```verilog
module top_module (
    input [7:0] in,
    output [31:0] out );//

    // assign out = { replicate-sign-bit , the-input };
    //msb of in will be in[7]
    assign out= {{24{in[7]}},in};
endmodule
```

## What I learned

_Fill this in during revision._
