# Day 11 — 2026-07-04

Two Lemmings FSMs were completed. Both full HDLBits pages now show the complete question, the loaded successful submission, and the successful-submission timestamp.

## Index

| # | Problem | Result | Submitted |
|---:|---|---|---|
| 159 | [Lemmings 2](#159--lemmings-2) | Completed | 5:14:31 PM |
| 160 | [Lemmings 3](#160--lemmings-3) | Completed | 5:57:22 PM |

## 159 — Lemmings 2

[Problem note](problems/Day%2011/159-lemmings2.md) · [HDLBits](https://hdlbits.01xz.net/wiki/lemmings2)

![Lemmings 2 complete question and loaded successful submission](images/Day%2011/159-lemmings2-question-and-successful-submission.png)

The key correction was preserving direction while falling. `fallLeft` and `fallRight` are separate states because bumps must be ignored during a fall but the Lemming must resume its previous direction when the ground returns. The earlier one-bit direction plus separate falling flag could not represent both facts cleanly and assigned state from multiple blocks.

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

## 160 — Lemmings 3

[Problem note](problems/Day%2011/160-lemmings3.md) · [HDLBits](https://hdlbits.01xz.net/wiki/lemmings3)

![Lemmings 3 complete question and loaded successful submission](images/Day%2011/160-lemmings3-question-and-successful-submission.png)

Digging adds another remembered mode. Once digging begins, bumps and `dig` are irrelevant; the Lemming keeps digging while ground exists, then falls in the direction it had before digging. This requires separate dig-left/dig-right and dig-fall-left/dig-fall-right states.

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

## Remaining after Day 11

Nineteen questions remained: 18 not started and the unresolved `exams/2013_q2afsm` review item.
