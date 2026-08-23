# 173 — Q2a: FSM

| Field | Value |
|---|---|
| Day | Day 13 |
| Last successful submission | 2026-07-06 10:06:12 PM |
| Course location | Circuits → Sequential Logic → Finite State Machines |
| HDLBits identifier | `exams/2012_q2fsm` |
| Attempts | 1 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/exams/2012_q2fsm) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2013/173-exams__2012_q2fsm.sv) |

## Question and submitted solution

![Q2a: FSM question and submitted solution](../../images/Day%2013/173-exams__2012_q2fsm-question-and-successful-submission.png)


## What the question is asking

The state diagram is implemented as a conventional Moore machine. Each named state represents the history needed to decide future transitions, the combinational case statement selects the next state from the current state and input, and a clocked register advances the machine once per rising edge. The output is decoded only from the registered state, so it changes after the transition into an output-producing state rather than directly with the input.

Reset is handled with the timing required by the prompt and returns the controller to its initial state. A default branch provides deterministic recovery from unused encodings. The most reliable way to validate this design is to trace one row at a time from the diagram: record current state, input, expected destination, then compare the code. Finally trace a complete input sequence through reset, state transitions, and output timing to catch a one-cycle shift between transition recognition and Moore output assertion.

## Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,
    input w,
    output z
);
    reg [2:0] state, next_state;
    parameter A = 3'b000;
    parameter B = 3'b001;
    parameter C = 3'b010;
    parameter D = 3'b011;
    parameter E = 3'b100;
    parameter F = 3'b101;

    always @(posedge clk) begin
        if (reset)
            state <= A;
        else
            state <= next_state;
    end

    always @(*) begin
        case (state)
            A: next_state = w ? B : A;
            B: next_state = w ? C : D;
            C: next_state = w ? E : D;
            D: next_state = w ? F : A;
            E: next_state = w ? E : D;
            F: next_state = w ? C : D;
            default: next_state = A;
        endcase
    end

    assign z = (state == E) || (state == F);
endmodule
```

## What I learned

_Fill this in during revision._
