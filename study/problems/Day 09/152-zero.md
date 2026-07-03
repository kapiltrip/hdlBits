# 152 — Output Zero

| Field | Value |
|---|---|
| Day | Day 09 |
| Last successful submission | 2026-07-02 9:12:38 PM |
| Course location | Getting Started |
| HDLBits identifier | `zero` |
| Attempts | 1 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Verification | Confirmed from the logged-in HDLBits statistics and saved successful submission |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/zero) |
| Files | [Question and successful solution screenshot](../../images/Day%2009/152-zero.png) · [Verilog solution](../../solutions/Day%2009/152-zero.sv) |

## Question and successful submission

<a href="../../images/Day%2009/152-zero.png"><img src="../../images/Day%2009/152-zero.png" alt="Output Zero question and loaded successful Verilog submission" width="100%"></a>

## What the question is asking

This problem asks for the complementary constant circuit: no inputs and one output that is permanently logic low. The module header declares the output, and a continuous assignment ties it to a one-bit zero.

The statement `assign zero = 1'b0;` continuously drives the output. It does not execute once; it describes a permanent hardware connection. Since the output never depends on an input or stored state, no sensitivity list, clock, or register is required.

This exercise also reinforces ANSI-style Verilog-2001 port declarations, where the direction is written directly in the module header.

## Saved Verilog solution

```verilog
module top_module (
    output zero
);
    assign zero = 1'b0;
endmodule
```

## Points to remember

- Constant-low logic uses a continuous tie to `1'b0`.
- Do not introduce procedural logic when a direct connection is sufficient.
- Keep the required module and port names unchanged for HDLBits.
