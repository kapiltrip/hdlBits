# 160 — Lemmings 3

| Field | Value |
|---|---|
| Day | Day 11 |
| Last successful submission | 2026-07-04 5:57:22 PM |
| HDLBits ID | `lemmings3` |
| Attempts | 3 total: 1 success, 1 incorrect, 1 compile error, 0 simulation errors |
| Success rate | 33% |
| Source | [HDLBits](https://hdlbits.01xz.net/wiki/lemmings3) |
| Files | [Screenshot](../../images/Day%2011/160-lemmings3-question-and-successful-submission.png) · [Verilog](../../solutions/Day%2011/160-lemmings3.sv) |

![Lemmings 3 complete question and loaded successful submission](../../images/Day%2011/160-lemmings3-question-and-successful-submission.png)

## Design reasoning

Digging is a persistent mode, not a one-cycle output. Once a grounded walking Lemming accepts `dig`, it remains in a direction-specific digging state until the ground disappears. Direction-specific falling states then preserve the direction for landing. Bumps cannot alter direction while digging or falling.

## Saved successful solution

```verilog
module top_module(
    input clk,
    input areset,
    input bump_left,
    input bump_right,
    input ground,
    input dig,
    output walk_left,
    output walk_right,
    output aaah,
    output digging
);

    reg [3:0] state, next_state;
    parameter left             = 3'b000;
    parameter right            = 3'b001;
    parameter fallRight        = 3'b010;
    parameter fallLeft         = 3'b011;
    parameter digWorkFromLeft  = 3'b100;
    parameter digWorkFromRight = 3'b101;
    parameter digWorkFallRight = 3'b110;
    parameter digWorkFallLeft  = 3'b111;

    always @(*) begin
        case (state)
            left: begin
                if (!ground)
                    next_state = fallLeft;
                else if (dig && ground)
                    next_state = digWorkFromLeft;
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
                else if (dig && ground)
                    next_state = digWorkFromRight;
                else if (bump_right && bump_left)
                    next_state = left;
                else if (bump_right)
                    next_state = left;
                else
                    next_state = right;
            end
            fallRight: next_state = !ground ? fallRight : right;
            fallLeft:  next_state = !ground ? fallLeft : left;
            digWorkFromLeft:
                next_state = ground ? digWorkFromLeft : digWorkFallLeft;
            digWorkFromRight:
                next_state = ground ? digWorkFromRight : digWorkFallRight;
            digWorkFallLeft:
                next_state = ground ? left : digWorkFallLeft;
            digWorkFallRight:
                next_state = ground ? right : digWorkFallRight;
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
    assign aaah = (state == digWorkFallLeft) ||
                  (state == digWorkFallRight) ||
                  (state == fallRight) ||
                  (state == fallLeft);
    assign digging = (state == digWorkFromLeft) ||
                     (state == digWorkFromRight);

endmodule
```

## Points to remember

- A command such as `dig` can cause a state transition; it need not remain high afterward.
- Encode mutually exclusive modes directly in the FSM.
- Preserve direction across both ordinary falling and post-dig falling.
