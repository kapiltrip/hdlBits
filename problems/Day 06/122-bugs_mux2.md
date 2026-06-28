# 122 — Mux

| Field | Value |
|---|---|
| Day | Day 06 |
| Last successful submission | 2026-06-28 12:54:12 AM |
| Course location | Verification: Reading Simulations → Finding bugs in code |
| HDLBits identifier | `bugs_mux2` |
| Attempts | 4 total: 2 incorrect, 0 compile error, 1 simulation error |
| Success rate | 25% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/bugs_mux2) |
| Files | [Open screenshot at full resolution](../../images/Day%2006/122-bugs_mux2.png) · [Verilog solution](../../solutions/Day%2006/122-bugs_mux2.sv) |

## Question and submitted solution

<a href="../../images/Day%2006/122-bugs_mux2.png"><img src="../../images/Day%2006/122-bugs_mux2.png" alt="Mux question and submitted solution" width="100%"></a>

## What the question is asking

The broken circuit mixed two independent mistakes: the output was declared as a scalar even though both data inputs are 8-bit buses, and the selection expression did not implement the required bus mux correctly.

The fixed output is `[7:0]`, and the ternary operator selects the entire vector in one expression: when `sel=1`, output A; otherwise output B. This is width-preserving and synthesizes to eight parallel 2-to-1 multiplexers sharing the same select line.

**Check:** `sel=0` must copy every bit of B, and `sel=1` must copy every bit of A. A one-bit output declaration could appear to work for bit 0 while silently discarding bits 7:1.

## Saved Verilog solution

```verilog
module top_module (
    input sel,
    input [7:0] a,
    input [7:0] b,
    output [7:0] out
);

    assign out = sel ? a : b;

endmodule
```

## What I learned

_Fill this in during revision._
