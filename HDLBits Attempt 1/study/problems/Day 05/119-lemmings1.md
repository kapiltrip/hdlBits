# 119 — Lemmings 1

| Field | Value |
|---|---|
| Day | Day 05 |
| Last successful submission | 2026-06-27 6:32:59 PM |
| Course location | Circuits → Sequential Logic → Finite State Machines |
| HDLBits identifier | `lemmings1` |
| Attempts | 2 total: 0 incorrect, 1 compile error, 0 simulation error |
| Success rate | 50% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/lemmings1) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2005/119-lemmings1.sv) |

## Question and submitted solution

![Lemmings 1 question and submitted solution](../../images/Day%2005/119-lemmings1.png)

## What the question is asking

The Lemming has only two Moore states: walking left and walking right. Direction changes occur only when an obstacle is encountered on the side toward which it is currently walking.

In LEFT, `bump_left=1` sends the FSM to RIGHT; otherwise it stays LEFT. In RIGHT, `bump_right=1` sends it to LEFT; otherwise it stays RIGHT. If both bump inputs are high, the relevant condition for either current state is high, so the machine still reverses direction exactly once.

The asynchronous reset is implemented with `posedge areset` in the event control and immediately places the Lemming in LEFT. The two outputs are Moore decodes: `walk_left` is high only in LEFT and `walk_right` only in RIGHT, so they are mutually exclusive for every legal state.

**Trace example:** LEFT + right-side bump only remains LEFT because an obstacle behind the Lemming does not matter. LEFT + left-side bump changes the registered state to RIGHT at the next clock edge.

## Saved Verilog solution

```verilog
module top_module(
    input clk,
    input areset,
    input bump_left,
    input bump_right,
    output walk_left,
    output walk_right
);

    reg state, next_state;
    parameter left = 1'b0;
    parameter right = 1'b1;

    always @(*) begin
        next_state = state;
        case (state)
            left: next_state = bump_left ? right : left;
            right: next_state = bump_right ? left : right;
        endcase
    end

    always @(posedge clk or posedge areset) begin
        if (areset)
            state <= left;
        else
            state <= next_state;
    end

    assign walk_left = (state == left);
    assign walk_right = (state == right);

endmodule
```

## What I learned

_Fill this in during revision._
