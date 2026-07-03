# 153 — FSM: The complete FSM

| Field | Value |
|---|---|
| Day | Day 09 |
| Last successful submission | 2026-07-02 10:20:45 PM |
| Course location | Circuits → Building Larger Circuits |
| HDLBits identifier | `exams/review2015_fsm` |
| Attempts | 8 total: 5 incorrect, 1 compile error, 0 simulation errors, 2 successful |
| Success rate | 25% |
| Verification | Confirmed from the logged-in HDLBits statistics and saved successful submission |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/exams/review2015_fsm) |
| Files | [Verilog solution](../../solutions/Day%2009/153-exams__review2015_fsm.sv) |

## What the question is asking

This problem joins the earlier sequence detector and four-cycle shift controller into one Moore FSM. It does not implement the timer datapath. Instead, it decides when an external shift register should accept four serial bits, when an external counter should run, and when the user should see the completion indication.

The search states store the longest useful suffix of the received stream: `S` has no match, `S1` has seen `1`, `S11` has seen `11`, and `S110` has seen `110`. The overlap transition in `S11` is important: another `1` keeps the machine in `S11` because the newest suffix is still `11`. A `1` in `S110` completes `1101` and enters the first bit-capture state.

States `B0` through `B3` make `shift_ena` high for exactly four complete cycles. Each state advances unconditionally, so the serial `data` input is deliberately ignored after the trigger sequence until the timer returns to search mode. After `B3`, the machine enters `COUNT`, asserts `counting`, and remains there until `done_counting` is sampled high.

`WAIT` asserts `done` and holds it high until `ack` is sampled. An acknowledged timer returns directly to `S`, ready to recognize another possibly overlapping input sequence. Synchronous reset has priority over all transitions and also returns to `S`.

### State/output map

| State group | Meaning | Active output |
|---|---|---|
| `S`, `S1`, `S11`, `S110` | Search for `1101` | none |
| `B0`, `B1`, `B2`, `B3` | Capture four delay bits | `shift_ena=1` |
| `COUNT` | Wait for the datapath counter | `counting=1` |
| `WAIT` | Timer expired; wait for acknowledgment | `done=1` |

## Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,
    input data,
    output shift_ena,
    output counting,
    input done_counting,
    output done,
    input ack
);
    localparam S=4'd0, S1=4'd1, S11=4'd2, S110=4'd3;
    localparam B0=4'd4, B1=4'd5, B2=4'd6, B3=4'd7;
    localparam COUNT=4'd8, WAIT=4'd9;
    reg [3:0] state, next_state;

    always @(posedge clk)
        if (reset) state <= S;
        else state <= next_state;

    always @(*) begin
        case (state)
            S:     next_state = data ? S1 : S;
            S1:    next_state = data ? S11 : S;
            S11:   next_state = data ? S11 : S110;
            S110:  next_state = data ? B0 : S;
            B0:    next_state = B1;
            B1:    next_state = B2;
            B2:    next_state = B3;
            B3:    next_state = COUNT;
            COUNT: next_state = done_counting ? WAIT : COUNT;
            WAIT:  next_state = ack ? S : WAIT;
            default: next_state = S;
        endcase
    end

    assign shift_ena = (state == B0) || (state == B1) ||
                       (state == B2) || (state == B3);
    assign counting = (state == COUNT);
    assign done = (state == WAIT);
endmodule
```

## Points to remember

- Four separate capture states make a four-cycle enable pulse easy to audit.
- Moore outputs depend only on the registered state, so they remain stable for the entire cycle.
- Inputs that are irrelevant in a state should not influence its transition logic.
- A default transition protects simulation and synthesis if the state register is ever corrupted.
