# 154 — The complete timer

| Field | Value |
|---|---|
| Day | Day 09 |
| Last successful submission | 2026-07-02 11:38:15 PM |
| Course location | Circuits → Building Larger Circuits |
| HDLBits identifier | `exams/review2015_fancytimer` |
| Attempts | 2 total: 0 incorrect, 0 compile errors, 0 simulation errors, 2 successful |
| Success rate | 100% |
| Verification | Confirmed from the logged-in HDLBits statistics and saved successful submission |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/exams/review2015_fancytimer) |
| Files | [Successful-submission screenshot](../../images/Day%2009/154-exams__review2015_fancytimer-question-and-successful-submission.png) · [Verilog solution](../../solutions/Day%2009/154-exams__review2015_fancytimer.sv) · [Mistake log](../../Mistakes.md#13-the-complete-timer-separate-control-state-and-datapath-state) |

![Complete timer question and loaded successful submission](../../images/Day%2009/154-exams__review2015_fancytimer-question-and-successful-submission.png)

## What the question is asking

This is the complete timer built from three cooperating hardware blocks: a sequence-recognition FSM, a four-bit shift/down-count register, and a modulo-1000 counter. The controller must detect `1101`, capture the next four bits most-significant-bit first, count for exactly `(delay+1)×1000` clocks, assert `done`, and wait for `ack` before searching again.

The four captured bits form `delay`. On the fourth capture edge, the completed value is also loaded into `count_remaining`. During counting, `count` displays `count_remaining` for 1000 cycles, then one less for 1000 cycles, continuing through zero for a final 1000 cycles. This means a captured value of zero is not an immediate finish: it still requires one full 1000-cycle interval. The terminal event is therefore `count_1000==999 && count_remaining==0`.

The design keeps control and datapath separate. The FSM decides *which phase is active*. The datapath stores the serial delay value and performs the nested countdown. That separation avoids making `next_state` logic also mutate counters or shift registers.

### Cycle-level countdown example

For captured `delay=2`, the visible sequence is:

| Counting interval | `count` output | `count_1000` values | Terminal action |
|---:|---:|---|---|
| 1 | 2 | 0 through 999 | reload inner counter, decrement to 1 |
| 2 | 1 | 0 through 999 | reload inner counter, decrement to 0 |
| 3 | 0 | 0 through 999 | enter `WAIT`, assert `done` |

That is 3000 counting cycles, matching `(2+1)×1000`.

## Wrong attempt and why it failed

### 1. The controller and datapath were mixed together

![Complete timer wrong attempt showing many FSM states and delay register](../../images/Mistakes/070-fancytimer-wrong-attempt-state-and-registers.png)

![Complete timer wrong attempt with next-state logic writing datapath registers](../../images/Mistakes/071-fancytimer-wrong-attempt-next-state-logic.png)

The attempt correctly recognized that the problem needs search states, four shift states, a counting state, and a done state. The structural error was assigning `delay` and `counting` inside the combinational next-state `case`. `delay` is stored data, so it belongs in a clocked datapath block. `counting` is a Moore output, so it should be decoded from `state` on every path. Writing either only in selected `case` branches leaves incomplete combinational assignments and can infer latches.

There was also no complete behavior for `COUNTING`, `ack`, the modulo-1000 counter, or the `(delay+1)` outer countdown. State enumeration alone does not implement the timer.

### 2. Two blocks may calculate the same expression for different destinations

![Question about duplicate shift expressions](../../images/Mistakes/072-fancytimer-review-duplicate-expression-question.png)

![Comparison of continuous shifting and loading the countdown register](../../images/Mistakes/073-fancytimer-review-shift-versus-load.png)

The expression `{delay[2:0], data}` represents the *new* four-bit value after accepting the current serial bit. It is reasonable for that same calculated value to feed two destinations on the fourth capture edge: the shift register keeps the new value, and another register could load it as its initial countdown value. Identical right-hand expressions do not imply identical hardware jobs; the left-hand registers and their enable conditions define the jobs.

The verified saved solution uses two registers deliberately. `delay` accumulates all four serial bits. On the `B3` edge, `count_remaining` captures the same newly calculated four-bit value and then becomes the visible down counter. An alternative one-register architecture is possible because shifting and counting occur in mutually exclusive phases, but the two-register version cleanly separates capture history from the active countdown.

### 3. Nonblocking assignments read the old value during the whole edge

![Explanation that a nonblocking assignment reads the old delay value](../../images/Mistakes/074-fancytimer-review-nonblocking-old-value.png)

On the fourth shift edge, this pair is wrong if both statements are intended to capture the newly shifted value:

```verilog
delay <= {delay[2:0], data};
countRemaining <= delay;       // receives the old delay value
```

All right-hand sides of nonblocking assignments are evaluated before any left-hand side changes. If two registers are required, both must use the new expression directly:

```verilog
delay <= {delay[2:0], data};
countRemaining <= {delay[2:0], data};
```

The saved solution uses the correct second form: both `delay` and `count_remaining` receive `{delay[2:0], data}` on the fourth capture edge. This is why the duplicated expression is necessary in that architecture.

## Saved Verilog solution

See the complete, editable source in [154-exams__review2015_fancytimer.sv](../../solutions/Day%2009/154-exams__review2015_fancytimer.sv).

The key terminal equation is:

```verilog
wire finished = (count_1000 == 10'd999) &&
                (count_remaining == 4'd0);
```

and the datapath update is intentionally separate from next-state logic:

```verilog
if (state == B3) begin
    count_remaining <= {delay[2:0], data};
    count_1000 <= 10'd0;
end
else if (counting) begin
    if (count_1000 == 10'd999) begin
        count_1000 <= 10'd0;
        if (count_remaining != 4'd0)
            count_remaining <= count_remaining - 4'd1;
    end
    else
        count_1000 <= count_1000 + 10'd1;
end
```

## Points to remember

- Use FSM state for phase control and registers/counters for datapath values.
- `delay=0` still counts 1000 cycles; finish only at the end of that interval.
- In a clocked block, every nonblocking right-hand side sees the pre-edge values.
- Two blocks may reuse a combinational expression while storing it in different registers.
- When two registers capture the same new serial value on one edge, duplicate the next-value expression instead of reading the register that is also being updated.
