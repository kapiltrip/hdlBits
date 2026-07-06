# 162 — One-hot FSM

| Field | Value |
|---|---|
| Day | Day 12 |
| Last successful submission | 2026-07-05 5:09:39 PM |
| HDLBits ID | `fsm_onehot` |
| Attempts | 8 total: 2 successes, 3 incorrect, 3 compile errors, 0 simulation errors |
| Success rate | 25% |
| Source | [HDLBits](https://hdlbits.01xz.net/wiki/fsm_onehot) |
| Files | [Screenshot](../../images/Day%2012/162-fsm_onehot-question-and-successful-submission.png) · [Verilog](../../solutions/Day%2012/162-fsm_onehot.sv) · [Mistake log](../../Mistakes.md#15-one-hot-fsm-do-not-replace-the-supplied-state-interface) |

![One-hot FSM complete question and loaded successful submission](../../images/Day%2012/162-fsm_onehot-question-and-successful-submission.png)

## Design reasoning

This module receives the current one-hot state from outside. For each destination state, collect every incoming transition as a sum-of-products term. Direct equations also satisfy HDLBits' deliberate non-one-hot tests because each bit is independently computed from its specified source conditions.

## Saved successful solution

```verilog
module top_module(
    input in,
    input [9:0] state,
    output [9:0] next_state,
    output out1,
    output out2
);

    wire S0 = state[0];
    wire S1 = state[1];
    wire S2 = state[2];
    wire S3 = state[3];
    wire S4 = state[4];
    wire S5 = state[5];
    wire S6 = state[6];
    wire S7 = state[7];
    wire S8 = state[8];
    wire S9 = state[9];

    assign next_state[0] = ~in & (S0 | S1 | S2 | S3 | S4 | S7 | S8 | S9);
    assign next_state[1] =  in & (S0 | S8 | S9);
    assign next_state[2] =  in & S1;
    assign next_state[3] =  in & S2;
    assign next_state[4] =  in & S3;
    assign next_state[5] =  in & S4;
    assign next_state[6] =  in & S5;
    assign next_state[7] =  in & (S6 | S7);
    assign next_state[8] = ~in & S5;
    assign next_state[9] = ~in & S6;

    assign out1 = S8 | S9;
    assign out2 = S7 | S9;

endmodule
```

## Points to remember

- Derive one-hot transition logic from incoming arrows.
- Do not redeclare ports as smaller local state variables.
- `parameter` values are compile-time constants, not aliases for state bits.
