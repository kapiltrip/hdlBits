# 115 — Simple one-hot state transitions 3

| Field | Value |
|---|---|
| Day | Day 05 |
| Last successful submission | 2026-06-27 4:45:28 PM |
| Course location | Circuits → Sequential Logic → Finite State Machines |
| HDLBits identifier | `fsm3onehot` |
| Attempts | 6 total: 4 incorrect, 1 compile error, 0 simulation error |
| Success rate | 17% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/fsm3onehot) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2005/115-fsm3onehot.sv) |

## Question and submitted solution

![Simple one-hot state transitions 3 question and submitted solution](../../images/Day%2005/115-fsm3onehot.png)

## What the question is asking

This problem gives the four-state Moore machine as a transition table, but supplies the current state as a one-hot vector instead of asking for a state register. The implementation therefore derives each bit of `next_state` from the incoming transitions to that state.

For example, state A is reached from A or C only when `in=0`, so `next_state[A] = ~in & (state[A] | state[C])`. State B is reached from A, B, or D when `in=1`; C is reached from B or D when `in=0`; and D is reached only from C when `in=1`. The Moore output is high only in D, so it is simply `state[D]`.

**Why the direct equations matter:** HDLBits deliberately supplies non-one-hot test vectors. A `case` statement that assumes exactly one active state, or logic that forces illegal states back to A, would implement different behaviour. The sum-of-products equations preserve every simultaneously active incoming term.

**Trace example:** with `state=4'b0100` (C), `in=1` asserts only `next_state[D]`; with the same state and `in=0`, only `next_state[A]` is asserted.

## Saved Verilog solution

```verilog
module top_module(
    input in,
    input [3:0] state,
    output [3:0] next_state,
    output out
);

    parameter A = 0, B = 1, C = 2, D = 3;

    // State transition logic: derive an equation for each state flip-flop.
    assign next_state[A] = ~in & (state[A] | state[C]);
    assign next_state[B] = in & (state[A] | state[B] | state[D]);
    assign next_state[C] = ~in & (state[B] | state[D]);
    assign next_state[D] = in & state[C];

    assign out = state[D];

endmodule
```

## What I learned

_Fill this in during revision._
