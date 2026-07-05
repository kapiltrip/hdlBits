# 125 — Add/sub

| Field | Value |
|---|---|
| Day | Day 06 |
| Last successful submission | 2026-06-28 1:31:18 AM |
| Course location | Verification: Reading Simulations → Finding bugs in code |
| HDLBits identifier | `bugs_addsubz` |
| Attempts | 12 total: 6 incorrect, 4 compile error, 0 simulation error |
| Success rate | 17% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/bugs_addsubz) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2006/125-bugs_addsubz.sv) |

## Question and submitted solution

![Add/sub question and submitted solution](../../images/Day%2006/125-bugs_addsubz.png)

## What the question is asking

The combinational block first computes either `a+b` or `a-b` according to `do_sub`, then derives `result_is_zero` from the newly computed `out`.

Blocking assignments are important here. With `out = ...`, the following zero comparison sees the current combinational result in the same evaluation. A nonblocking assignment could make the flag observe the previous value during simulation and create a mismatch between intent and behaviour.

The zero test is placed after the `case`, so it applies equally to addition and subtraction. Both outputs are declared `reg` because they are assigned procedurally.

**Revision pitfall:** calculating the zero flag in only one case branch, or omitting an assignment on a path, would infer storage or leave stale flag data.

## Saved Verilog solution

```verilog
// synthesis verilog_input_version verilog_2001
module top_module (
    input do_sub,
    input [7:0] a,
    input [7:0] b,
    output reg [7:0] out,
    output reg result_is_zero
);

    always @(*) begin
        case (do_sub)
            1'b0: out = a + b;
            1'b1: out = a - b;
        endcase
        result_is_zero = (out == 8'd0);
    end

endmodule
```

## What I learned

_Fill this in during revision._
