# HDLBits Review Queue

These two attempted problems remain deliberately excluded from the completed archive because neither has a captured successful submission. The Day 10 FSM set was verified live, given full question-and-answer screenshots, and promoted to the completed archive.

| Status | Problem | HDLBits ID | Attempts | Screenshot | Source |
|---|---|---|---:|---|---|
| Review | Lemmings 2 | `lemmings2` | 7 | Rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/lemmings2) |
| Review | Q2a: FSM | `exams/2013_q2afsm` | 3 | Rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/2013_q2afsm) |

## Review: Lemmings 2

[Open HDLBits problem](https://hdlbits.01xz.net/wiki/lemmings2)

![Complete Lemmings 2 question and previous attempt](images/Review/120-lemmings2.png)

This problem has 7 unsuccessful attempts and should be reviewed before continuing to Lemmings 3. The captured editor contains the last non-successful submission for debugging, but no draft is presented as a completed solution.

### Current 2026-07-04 attempt

The complete question remains visible above. These newer split screenshots preserve the latest editor attempt at readable resolution and are rendered in order rather than left as file links.

![Lemmings 2 current question and waveform](images/Mistakes/076-lemmings2-question-waveform.png)

![Lemmings 2 current attempt, top](images/Mistakes/077-lemmings2-attempt-top.png)

![Lemmings 2 current attempt, middle](images/Mistakes/078-lemmings2-attempt-middle.png)

![Lemmings 2 current attempt, bottom](images/Mistakes/079-lemmings2-attempt-bottom.png)

### Technical review

The current design has two fundamental issues:

- `state` is only one bit, so it cannot distinguish walking-left, walking-right, falling-left, and falling-right. A falling Lemming must remember its pre-fall direction while ignoring bumps.
- `state` is assigned in two clocked blocks. This creates multiple procedural drivers. Next-state logic must drive only `next_state`; one state-register block must be the sole owner of `state`.

Use four Moore states and give loss of ground priority over bumps while walking:

```verilog
localparam WALK_L = 2'd0,
           WALK_R = 2'd1,
           FALL_L = 2'd2,
           FALL_R = 2'd3;

reg [1:0] state, next_state;

always @(*) begin
    case (state)
        WALK_L: next_state = !ground ? FALL_L :
                             bump_left ? WALK_R : WALK_L;
        WALK_R: next_state = !ground ? FALL_R :
                             bump_right ? WALK_L : WALK_R;
        FALL_L: next_state = ground ? WALK_L : FALL_L;
        FALL_R: next_state = ground ? WALK_R : FALL_R;
        default: next_state = WALK_L;
    endcase
end

always @(posedge clk or posedge areset) begin
    if (areset)
        state <= WALK_L;
    else
        state <= next_state;
end

assign walk_left  = (state == WALK_L);
assign walk_right = (state == WALK_R);
assign aaah       = (state == FALL_L) || (state == FALL_R);
```

This is a review reference, not an archived completion. Lemmings 2 remains `Review` until HDLBits shows a successful submission.

---

## Review: Q2a: FSM

[Open HDLBits problem](https://hdlbits.01xz.net/wiki/exams/2013_q2afsm)

![Q2a FSM review screenshot](images/Review/review-exams__2013_q2afsm.png)

This arbiter FSM has 3 unsuccessful attempts and should be reviewed before continuing with the adjacent Q2b FSM exercise. The captured page preserves the full state diagram, prompt, module declaration, and editor context without presenting it as a completed solution.

---

## Day 10 FSM set promoted to Completed

- [Q3a](problems/Day%2010/155-exams__2014_q3fsm.md), [Q3b](problems/Day%2010/156-exams__2014_q3bfsm.md), [Q3c](problems/Day%2010/157-exams__2014_q3c.md), and [Q6c](problems/Day%2010/158-exams__m2014_q6c.md) now each have a live successful submission, standalone solution, and full question-and-answer screenshot.
- Q3c preserves the handwritten K-map and corrects its earlier mistaken `fsm_onehot` classification.
- Q3a keeps Kapil's clocked-block comment directly beside the explanation that resolves it.
