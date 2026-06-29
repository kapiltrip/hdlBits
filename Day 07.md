# Day 07 — 2026-06-29

Completed problems: **1**

Each screenshot is embedded at the full width of the GitHub page. Select an image to open its original-resolution file.

## Index

| # | Time | Problem | Section | Problem note | Solution | Source |
|---:|---|---:|---|---|---|---|
| 1 | 12:02:40 AM | [142](#problem-142) | Sequential Logic | [Q8: Design a Mealy FSM](problems/Day%2007/142-exams__ece241_2013_q8.md) | [Code](solutions/Day%2007/142-exams__ece241_2013_q8.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/exams/ece241_2013_q8) |

---

<a id="problem-142"></a>
## 142 — Q8: Design a Mealy FSM

[Problem note](problems/Day%2007/142-exams__ece241_2013_q8.md) · [Open screenshot at full resolution](images/Day%2007/142-exams__ece241_2013_q8.png) · [Verilog file](solutions/Day%2007/142-exams__ece241_2013_q8.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/ece241_2013_q8)

<a href="images/Day%2007/142-exams__ece241_2013_q8.png"><img src="images/Day%2007/142-exams__ece241_2013_q8.png" alt="Q8: Design a Mealy FSM question and submitted solution" width="100%"></a>

### What the question is asking

This is a three-state Mealy sequence detector for the overlapping bit pattern 101. The states store the longest useful prefix of the target sequence that has already been seen: S0 means no useful prefix, S1 means the last bit can serve as the leading 1, and S10 means the input stream currently ends in 10.

The next-state table follows that prefix meaning. From S0, input 1 enters S1 and input 0 stays in S0. From S1, another 1 still leaves a valid leading 1, while 0 advances to S10. From S10, input 1 completes 101 and also becomes the leading 1 of a possible overlapping next match, so the machine goes to S1; input 0 breaks the prefix and returns to S0.

The output is Mealy-style: `z = (state == S10) && x`. It asserts during the same cycle that the final 1 arrives, not one clock later. The reset is active-low and asynchronous because the state register is sensitive to `negedge aresetn`; when reset is asserted, state returns immediately to S0.

**Trace example:** for input stream 10101, the machine visits S0 -> S1 -> S10, asserts z on the third bit, returns to S1, moves to S10, and asserts z again on the fifth bit. That is the overlapping behavior the problem asks for.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input aresetn,    // Asynchronous active-low reset
    input x,
    output z );

    parameter S0 = 2'd0, S1 = 2'd1, S10 = 2'd2;
    reg [1:0] state, next_state;

    always @(*) begin
        case (state)
            S0: next_state = x ? S1 : S0;
            S1: next_state = x ? S1 : S10;
            S10: next_state = x ? S1 : S0;
            default: next_state = S0;
        endcase
    end

    always @(posedge clk or negedge aresetn) begin
        if (!aresetn)
            state <= S0;
        else
            state <= next_state;
    end

    assign z = (state == S10) && x;

endmodule
```
