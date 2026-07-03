# 151 — Getting Started

| Field | Value |
|---|---|
| Day | Day 09 |
| Last successful submission | 2026-07-02 9:12:14 PM |
| Course location | Getting Started |
| HDLBits identifier | `step_one` |
| Attempts | 1 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Verification | Confirmed from the logged-in HDLBits statistics and saved successful submission |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/step_one) |
| Files | [Question screenshot](../../images/Day%2009/151-step_one.png) · [Successful solution screenshot](../../images/Day%2009/151-step_one-solution.png) · [Verilog solution](../../solutions/Day%2009/151-step_one.sv) |

## Question and successful submission

<a href="../../images/Day%2009/151-step_one.png"><img src="../../images/Day%2009/151-step_one.png" alt="Getting Started problem statement and verified success timestamp" width="100%"></a>

<a href="../../images/Day%2009/151-step_one-solution.png"><img src="../../images/Day%2009/151-step_one-solution.png" alt="Getting Started loaded successful Verilog submission" width="100%"></a>

## What the question is asking

This introductory problem asks for a circuit with no inputs and one output that is permanently logic high. There is no clock, state, or conditional behavior. The output is a constant combinational net.

`assign one = 1'b1;` is a continuous assignment. The right-hand side is a one-bit constant whose value is 1. The explicit width and base in `1'b1` make the intended hardware value unambiguous: one bit, binary, high.

No `always` block is needed because nothing changes procedurally. Synthesis implements the output as a tie-high connection rather than a flip-flop or gate network.

## Saved Verilog solution

```verilog
module top_module (
    output one
);
    assign one = 1'b1;
endmodule
```

## Points to remember

- A constant output is valid combinational hardware.
- Use `assign` for a continuously driven net.
- A sized literal such as `1'b1` documents the exact width and value.
