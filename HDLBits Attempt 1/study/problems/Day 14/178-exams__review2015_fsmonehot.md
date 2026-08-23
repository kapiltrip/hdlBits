# 178 — FSM: One-hot logic equations

| Field | Value |
|---|---|
| Day | Day 14 |
| Last successful submission | 2026-07-07 12:49:56 PM |
| Course location | Circuits → Building Larger Circuits |
| HDLBits identifier | `exams/review2015_fsmonehot` |
| Attempts | 5 total: 1 incorrect, 1 compile error, 0 simulation error |
| Success rate | 60% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/exams/review2015_fsmonehot) |
| Files | Screenshot rendered below · [Mistake review](../../Mistakes.md#23-review2015-one-hot-selected-equations-and-unused-state-warnings) · [Verilog solution](../../solutions/Day%2014/178-exams__review2015_fsmonehot.sv) |

## Question and submitted solution

![FSM: One-hot logic equations question and submitted solution](../../images/Day%2014/178-exams__review2015_fsmonehot-question-and-successful-submission.png)

## Supporting review screenshots

[Prompt top](../../images/Mistakes/Screenshot%202026-07-07%20120850.png) · [module detail](../../images/Mistakes/Screenshot%202026-07-07%20120950.png) · [port/detail crop](../../images/Mistakes/Screenshot%202026-07-07%20121000.png) · [successful submission warning](../../images/Mistakes/Screenshot%202026-07-07%20125016.png)

The successful HDLBits page still reports an unused-input style warning for one of the state bits. That is expected here because HDLBits asks for only selected next-state equations and three decoded outputs, not the complete ten-bit next-state vector. A state bit should appear only when an incoming arrow to a requested destination or an output decode actually needs it.

## What the question is asking

This exercise extracts only selected one-hot equations from the complete timer controller. The supplied `state[9:0]` vector already represents the present state, so the module must not create a state register or recode the FSM. Each requested `*_next` output is the OR of every transition entering that destination state.

For example, `B3_next` is high only when the current state is `B2`, because the B0-B3 shift phase advances unconditionally one state per clock. `Count_next` is high when the current state is `B3` or when the controller is already in `Count` and `done_counting` is still low. `Wait_next` is high when counting has just completed or when the controller is already waiting and `ack` has not arrived.

The output equations are direct Moore decodes from the current one-hot state: `done` is `state[Wait]`, `counting` is `state[Count]`, and `shift_ena` is the OR of B0 through B3. The key review habit is destination-first derivation: list incoming arrows for each requested destination bit and translate those arrows directly into sum-of-products logic.

## Saved Verilog solution

```verilog
module top_module(
    input d,
    input done_counting,
    input ack,
    input [9:0] state,
    output B3_next,
    output S_next,
    output S1_next,
    output Count_next,
    output Wait_next,
    output done,
    output counting,
    output shift_ena
);
    parameter S=0, S1=1, S11=2, S110=3, B0=4, B1=5, B2=6, B3=7, Count=8, Wait=9;

    assign B3_next = state[B2];
    assign S_next = (state[S] & ~d) | (state[S1] & ~d) |
                    (state[S110] & ~d) | (state[Wait] & ack);
    assign S1_next = state[S] & d;
    assign Count_next = state[B3] | (state[Count] & ~done_counting);
    assign Wait_next = (state[Count] & done_counting) | (state[Wait] & ~ack);

    assign done = state[Wait];
    assign counting = state[Count];
    assign shift_ena = state[B0] | state[B1] | state[B2] | state[B3];
endmodule
```

## What I learned

_Fill this in during revision._
