# 114 — Simple state transitions 3

| Field | Value |
|---|---|
| Day | Day 05 |
| Last successful submission | 2026-06-27 2:15:08 AM |
| Course location | Circuits → Sequential Logic → Finite State Machines |
| HDLBits identifier | `fsm3comb` |
| Attempts | 7 total: 1 incorrect, 5 compile error, 0 simulation error |
| Success rate | 14% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/fsm3comb) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2005/114-fsm3comb.sv) |

## Question and submitted solution

![Simple state transitions 3 question and submitted solution](../../images/Day%2005/114-fsm3comb.png)

## What the question is asking

Write only the combinational next-state logic for the supplied state-transition diagram.

## Saved Verilog solution

```verilog
module top_module(
    input in,
    input [1:0] state,
    output reg [1:0] next_state,
    output out
); //

    parameter A=0, B=1, C=2, D=3;

    // State transition logic: next_state = f(state, in)

    // Output logic:  out = f(state) for a Moore state machine
    always @(*)begin
        next_state=state;
        case (state)
            A:next_state=(in)?B:A;
            B:next_state=(in)?B:C;
            C:next_state=(in)?D:A;
            D:next_state=(in)?B:C;
        endcase
    end
    assign out = (state==D);
endmodule
```

## What I learned

_Fill this in during revision._
