# 150 — FSM: Enable shift register

| Field | Value |
|---|---|
| Day | Day 09 |
| Last successful submission | 2026-07-02 6:02:39 PM |
| Course location | Circuits → Building Larger Circuits |
| HDLBits identifier | `exams/review2015_fsmshift` |
| Attempts | 9 total: 4 incorrect, 4 compile error, 0 simulation error |
| Success rate | 11% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/exams/review2015_fsmshift) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2009/150-exams__review2015_fsmshift.sv) |

## Question and submitted solution

![FSM: Enable shift register question and submitted solution](../../images/Day%2009/150-exams__review2015_fsmshift.png)

## What the question is asking

This control circuit produces a pulse window measured in clock cycles rather than detecting a data pattern. A three-bit saturating counter records how many post-reset rising edges have occurred. Synchronous reset loads zero; while the value is below four, each later edge increments it; after reaching four, the missing assignment deliberately holds the state.

shift_ena is a Moore-style combinational decode of the registered count. It is high for count values 0, 1, 2, and 3, giving exactly four complete clock intervals, and becomes low when the fourth post-reset edge changes the count to 4. Saturation prevents the counter from wrapping back to zero and accidentally reasserting the enable after eight cycles.

Reset timing matters. Because reset is synchronous, asserting it between clock edges does not immediately modify count or the output. The next rising edge loads zero, after which the output is high and the four-cycle window starts again. No explicit else count <= count assignment is needed in clocked logic: when no branch assigns the register, the flip-flops retain their previous value.

**Cycle trace:** reset edge→0/high, then successive edges produce 1/high, 2/high, 3/high, 4/low, followed by 4/low indefinitely until another reset edge.

## Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,
    output shift_ena
);
    reg [2:0] count;

    always @(posedge clk) begin
        if (reset)
            count <= 3'd0;
        else if (count < 3'd4)
            count <= count + 3'd1;
    end

    assign shift_ena = (count < 3'd4);
endmodule
```

## What I learned

_Fill this in during revision._
