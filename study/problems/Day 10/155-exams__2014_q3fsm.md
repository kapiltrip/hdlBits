# 155 — Q3a: FSM

| Field | Value |
|---|---|
| Day | Day 10 — 2026-07-03 |
| Status | Completed — live HDLBits submission verified |
| Course location | Circuits → Sequential Logic → Finite State Machines |
| HDLBits identifier | `exams/2014_q3fsm` |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/exams/2014_q3fsm) |
| Files | [Successful question-and-answer screenshot](../../images/Day%2010/155-exams__2014_q3fsm-question-and-answer.png) · [Verilog solution](../../solutions/Day%2010/155-exams__2014_q3fsm.sv) |

## Complete question, submitted answer, and success result

<a href="../../images/Day%2010/155-exams__2014_q3fsm-question-and-answer.png"><img src="../../images/Day%2010/155-exams__2014_q3fsm-question-and-answer.png" alt="Q3a FSM full question, submitted solution, and successful result" width="100%"></a>

The full-page capture includes the prompt, timing diagram, two-state sketch, complete submitted code, and the authoritative `Status: Success!` result.

## What the question is asking

State A waits for `s=1`. The transition edge only starts the measurement phase; the three `w` samples are the **next** three clock edges in state B. State B then repeats forever in non-overlapping groups of three. Output `z` is high during the cycle after a group containing exactly two ones.

The FSM state records the phase—waiting or sampling. Two datapath registers remember progress within state B:

- `sample_count` identifies whether the current input is sample 1, 2, or 3.
- `ones_count` stores the number of ones seen before the current edge.

## Kapil's working attempt

<a href="../../images/Day%2010/155-exams__2014_q3fsm-working-attempt.png"><img src="../../images/Day%2010/155-exams__2014_q3fsm-working-attempt.png" alt="Kapil's Q3a FSM attempt with state, sample count, ones count, and correct flag declarations" width="100%"></a>

The two-state interpretation and counter declarations were correct. The remaining work was to give those registers clocked update rules and handle the third sample without accidentally reading an old nonblocking-assignment value.

## Kapil's comment and adjacent discussion

<a href="../../images/Day%2010/155-exams__2014_q3fsm-chat-question.png"><img src="../../images/Day%2010/155-exams__2014_q3fsm-chat-question.png" alt="Chat discussion showing Kapil's question about clocked counter logic" width="100%"></a>

> “I’m doing that in the clocked block, not in `next_state`; how does it make sense?”

Your objection was correct: counter assignments belong in a clocked block. Combinational next-state logic may **read** registered counters, but it should not own their stored updates. In this problem, `sample_count==2` does not need a state transition because the controller stays in B between groups. The terminal-count action is datapath timing: calculate `z`, clear both counters, and start the next group.

<a href="../../images/Day%2010/155-exams__2014_q3fsm-chat-explanation.png"><img src="../../images/Day%2010/155-exams__2014_q3fsm-chat-explanation.png" alt="Chat explanation comparing classical next-state style with a single clocked block" width="100%"></a>

Both a classical FSM split and a single clocked controller can work. The essential rule is signal ownership: every stored signal has one clocked owner, while combinational logic only calculates decisions and outputs.

## The third-sample boundary

When `sample_count==2`, the current `w` is sample 3. Nonblocking assignments read pre-edge values, so incrementing `ones_count` and then testing it would ignore that new increment. The successful solution instead includes the current input directly:

```verilog
z <= ((ones_count + w) == 2'd2);
```

After this edge, `z` reports the completed group for one cycle while both counters return to zero. The first sample of the next group clears `z` again.

## Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,
    input s,
    input w,
    output reg z
);
    localparam A = 1'b0, B = 1'b1;
    reg state;
    reg [1:0] sample_count;
    reg [1:0] ones_count;

    always @(posedge clk) begin
        if (reset) begin
            state        <= A;
            sample_count <= 2'd0;
            ones_count   <= 2'd0;
            z            <= 1'b0;
        end
        else if (state == A) begin
            z            <= 1'b0;
            sample_count <= 2'd0;
            ones_count   <= 2'd0;
            if (s)
                state <= B;
        end
        else begin
            if (sample_count == 2'd2) begin
                z            <= ((ones_count + w) == 2'd2);
                sample_count <= 2'd0;
                ones_count   <= 2'd0;
            end
            else begin
                z            <= 1'b0;
                sample_count <= sample_count + 2'd1;
                if (w)
                    ones_count <= ones_count + 2'd1;
            end
        end
    end
endmodule
```

## Points to remember

- `s` matters only while waiting in A.
- The three sampled values are the three edges after entering B.
- Include the current `w` in the third-sample decision.
- Clear the counters after each group, but remain in B.
- A counter is datapath state even when it helps control an FSM.
