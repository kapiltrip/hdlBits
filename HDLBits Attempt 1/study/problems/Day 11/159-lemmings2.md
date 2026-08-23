# 159 — Lemmings 2

| Field | Value |
|---|---|
| Day | Day 11 |
| Last successful submission | 2026-07-04 5:14:31 PM |
| HDLBits ID | `lemmings2` |
| Attempts | 21 total: 1 success, 13 incorrect, 7 compile errors, 0 simulation errors |
| Success rate | 5% |
| Source | [HDLBits](https://hdlbits.01xz.net/wiki/lemmings2) |
| Files | [Screenshot](../../images/Day%2011/159-lemmings2-question-and-successful-submission.png) · [Verilog](../../solutions/Day%2011/159-lemmings2.sv) · [Mistake review](../../Mistakes.md#14-lemmings-fsm-revision-falling-must-remember-direction) |

![Lemmings 2 complete question and loaded successful submission](../../images/Day%2011/159-lemmings2-question-and-successful-submission.png)

## Design reasoning

The machine must remember two independent facts: whether the Lemming is walking or falling, and which direction it had before the fall. Four Moore states encode the Cartesian product. Loss of ground has priority over bumps; falling states ignore bumps; landing returns to the remembered direction.

The prior attempt used a single direction bit plus a separate falling register and assigned the state from multiple clocked blocks. The successful design gives `state` one owner and computes `next_state` combinationally.

## Saved successful solution

```verilog
module top_module(
    input clk,
    input areset,
    input bump_left,
    input bump_right,
    input ground,
    output walk_left,
    output walk_right,
    output aaah
);

    reg [1:0] state, next_state;
    parameter left      = 2'b00;
    parameter right     = 2'b01;
    parameter fallRight = 2'b10;
    parameter fallLeft  = 2'b11;

    always @(*) begin
        case (state)
            left: begin
                if (!ground)
                    next_state = fallLeft;
                else if (bump_right && bump_left)
                    next_state = right;
                else if (bump_left)
                    next_state = right;
                else
                    next_state = left;
            end
            right: begin
                if (!ground)
                    next_state = fallRight;
                else if (bump_right && bump_left)
                    next_state = left;
                else if (bump_right)
                    next_state = left;
                else
                    next_state = right;
            end
            fallRight: begin
                if (!ground)
                    next_state = fallRight;
                else
                    next_state = right;
            end
            fallLeft: begin
                if (!ground)
                    next_state = fallLeft;
                else
                    next_state = left;
            end
            default: next_state = left;
        endcase
    end

    always @(posedge clk or posedge areset) begin
        if (areset)
            state <= left;
        else
            state <= next_state;
    end

    assign walk_left  = (state == left);
    assign walk_right = (state == right);
    assign aaah = (state == fallRight) || (state == fallLeft);

endmodule
```

## Points to remember

- If behavior after an event depends on pre-event direction, direction is state.
- Give each register one procedural owner.
- Moore outputs decode registered state, not speculative `next_state`.
