# 123 — NAND

| Field | Value |
|---|---|
| Day | Day 06 |
| Last successful submission | 2026-06-28 1:04:51 AM |
| Course location | Verification: Reading Simulations → Finding bugs in code |
| HDLBits identifier | `bugs_nand3` |
| Attempts | 2 total: 1 incorrect, 0 compile error, 0 simulation error |
| Success rate | 50% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/bugs_nand3) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2006/123-bugs_nand3.sv) |

## Question and submitted solution

![NAND question and submitted solution](../../images/Day%2006/123-bugs_nand3.png)

## What the question is asking

The required primitive is a five-input AND gate with positional port order `(out, a, b, c, d, e)`. To create a three-input AND, the unused inputs must be tied to the AND identity value 1, not 0. The intermediate `ando` is therefore `a & b & c & 1 & 1`.

A separate NOT gate inverts that intermediate value to produce the requested NAND function. The resulting truth rule is simple: `out` is low only for `a=b=c=1`; every other input combination produces high.

**Debugging lessons:** positional module connections must follow the declaration order exactly, intermediate nets need explicit declarations, and unused AND inputs must be tied high. Named port connections would reduce the risk of an ordering error.

## Saved Verilog solution

```verilog
module top_module (
    input a,
    input b,
    input c,
    output out
);
    wire and_result;

    andgate inst1 (and_result, a, b, c, 1'b1, 1'b1);
    not g1 (out, and_result);

endmodule
```

## What I learned

_Fill this in during revision._
