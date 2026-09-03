# HDLBits Attempt 2 - Original Submission Audit Through Entry 93

The original audit is based on the HDLBits problem pages and saved submission history visible in Kapil's signed-in Chrome session on 2026-09-02. A 2026-09-03 follow-up extends the progress frontier through entry 93 using Kapil's explicit completion confirmation and a captured set of eight matching HDLBits tabs. The newer rows deliberately do not invent submission timestamps that were not visible to the audit tool.

## Result

- Entries **1 through 85** retain the detailed original-page and saved-submission-selector audit from 2026-09-02.
- **All entries 1 through 93 are now Done in Attempt 2**. Entries 86-93 were updated on 2026-09-03 from Kapil's completion confirmation and the matching open problem tabs.
- Entries **80, 83, 84, and 85** retain their timestamped success evidence from 2026-09-02. The Day 6 entries use `current pass; user-confirmed` instead of guessed timestamps.
- The earlier 15 explicit questions remain documented. Day 6 adds Q&A for Dualedge (entry 87), Sim/circuit5 (entry 89), and Exams/2014 q3fsm (entry 90). Entry 90 has its own [standalone FSM deep dive](HDLBits_Entry90_Exams_2014_Q3FSM_Three_Sample_Window_Deep_Dive.pdf); the other two are kept in the separate [Day 6 non-FSM Q&A](HDLBits_Day6_Non_FSM_QA_Dualedge_and_Circuit5.pdf).
- A successful submission followed by later experimentation does not erase the earlier success. `Done` means a fresh Attempt 2 success exists, not that the most recently loaded editor contents are necessarily successful.

## Previously documented questions confirmed against the original code

| Entry | Exact subject found in submitted code | Existing answer |
|---:|---|---|
| 7 | Why the Lemmings4 fall counter does not need another reset | [Combined questions PDF](HDLBits_Combined_Questions_and_Day2_Review.pdf), section 7 |
| 13 | Why bitwise operators are used in the vector mux | [Combined questions PDF](HDLBits_Combined_Questions_and_Day2_Review.pdf), section 6 |
| 26 | Why `initial` cannot initialize a live population count and when to use procedural versus generate loops | [Combined questions PDF](HDLBits_Combined_Questions_and_Day2_Review.pdf), sections 2, 3, and 5 |
| 29 | How `sel[0]` and `sel[1]` divide work between the two mux levels | [Combined questions PDF](HDLBits_Combined_Questions_and_Day2_Review.pdf), section 6 |
| 30 | Whether the 101-node carry chain should be a wire or register | [Combined questions PDF](HDLBits_Combined_Questions_and_Day2_Review.pdf), section 4 |
| 31 | Difference between bitwise `~` and logical `!` | [Combined questions PDF](HDLBits_Combined_Questions_and_Day2_Review.pdf), section 9 |
| 36 | Why `&` and `&&` happen to choose the same branch with an all-ones mask | [Combined questions PDF](HDLBits_Combined_Questions_and_Day2_Review.pdf), section 10 |
| 38 | What latch inference means for an intentionally incomplete assignment | [Combined questions PDF](HDLBits_Combined_Questions_and_Day2_Review.pdf), section 11 |
| 67 | Meaning and tokenization of indexed part-select operators `+:` and `-:` | [Day 4 questions PDF](HDLBits_Day4_Questions_Vector_DFF_PS2.pdf), section 1 |
| 70 | Why the PS/2 data register must not be cleared in an unmatched clocked `else` branch | [Day 4 questions PDF](HDLBits_Day4_Questions_Vector_DFF_PS2.pdf), PS/2 datapath section |

## Newly recovered question 1 - Entry 54, water-level Moore FSM

Original code comment:

> `//localparam s2 // i dont need the check for specific cases cause they are already in the input`

The input tells the controller which water-level sensors are currently asserted, but it does not necessarily contain all the history needed by the outputs. In this problem, the ordinary flow outputs are determined by the current level band, while the supplemental-flow decision also distinguishes whether the level arrived from above or below. Two moments can therefore have the same current sensor pattern but require different `dfr` behavior because their preceding level was different.

`localparam` declarations do not test inputs. They give readable binary encodings to internal states. States such as `belows2` and `aboves2` preserve the direction/history that the input vector alone cannot express. The combinational next-state block must still test the valid sensor bands to decide which history state comes next.

If the HDLBits statement guarantees physically valid sensor patterns, it is reasonable to prioritize the highest asserted sensor rather than enumerate impossible patterns separately. That does not remove the need for the history states. A safe coding pattern is:

```verilog
always @(*) begin
    next_state = state;
    if (s[3])
        next_state = ABOVE_S3;
    else if (s[2])
        next_state = (state_was_higher) ? BELOW_S3 : ABOVE_S2;
    else if (s[1])
        next_state = (state_was_higher) ? BELOW_S2 : ABOVE_S1;
    else
        next_state = BELOW_S1;
end
```

The exact state names may differ, but the principle is fixed: sensor bits describe the present level; state bits preserve any past information the outputs still need.

## Newly recovered question 2 - Entry 74, sampled positive-edge detection

Original code comment:

> `// is it like 0 to 1 transition for any clock edge ? like in any 2 clock edges its that, transition`

Yes, but "edge" here means a change between **two consecutive rising-clock samples**, not every physical transition that might occur between clocks. For each vector bit:

- `previous[i] = 0` at the preceding rising edge,
- `in[i] = 1` at the current rising edge,
- therefore `in[i] & ~previous[i] = 1` for one cycle.

The sequential implementation is:

```verilog
reg [7:0] previous;

always @(posedge clk) begin
    previous <= in;
    pedge    <= in & ~previous;
end
```

Both right-hand sides see the old `previous` value because nonblocking assignments update after the block has evaluated. The result is one pulse per sampled 0-to-1 transition. A pulse that rises and falls entirely between two clock edges may be missed because this is synchronous sampling, not an asynchronous edge detector.

The unsuccessful submission used `~in & previous`, which detects the opposite sampled transition: 1-to-0.

## Newly recovered question 3 - Entry 75, asynchronous-reset sensitivity list

Original code comment:

> `// why i have to write, asynchronous reset in the sensitivity list`

An asynchronous reset must change the state register immediately when reset is asserted, without waiting for a clock edge. The event control must therefore wake the block for either event:

```verilog
always @(posedge clk or negedge aresetn) begin
    if (!aresetn)
        state <= S0;
    else
        state <= next_state;
end
```

`aresetn` is active low, so assertion is its falling edge, written `negedge aresetn`. A bare `aresetn` in the event list does not describe the required flip-flop primitive and does not state which transition asserts reset. Omitting reset from the list would make the reset synchronous because the block could react only at `posedge clk`.

In physical designs, asynchronous assertion is often paired with synchronized deassertion to avoid recovery/removal timing problems, but the HDLBits problem specifically tests the basic active-low asynchronous-reset behavior.

## Newly recovered question 4 - Entry 77, reduction versus bitwise versus logical operators

Original code comment:

> `// tell me difference b/w clearly b/w reduction and logical and bitwise`

| Operator class | Example | Input/output width | Meaning for `in = 4'b1011` |
|---|---|---|---|
| Unary reduction | `&in`, `|in`, `^in` | Vector to one bit | `&in=0`, `|in=1`, `^in=1` |
| Bitwise binary | `a & b`, `a | b`, `a ^ b` | One result bit per aligned input bit | Combines corresponding bits independently |
| Logical | `a && b`, `a || b`, `!a` | Operands become true/false; result is one bit | Tests whether each whole operand is zero or nonzero |

The original problem asks for one output from all four bits, so unary reduction operators are the direct answer:

```verilog
assign out_and = &in;
assign out_or  = |in;
assign out_xor = ^in;
```

The unsuccessful forms `out_and &= in`, `out_or |= in`, and `out_xor ^= in` are compound read-modify-write assignments. They read the old output and combine it with `in`; they are not reduction operators. In combinational logic, reading an output while assigning that same output can also create an unintended feedback dependency.

## Current Day 5 original submissions - entries 80 through 85

| Entry | Chrome evidence | Attempt 2 state | Finding |
|---:|---|---|---|
| 80 | Last success 2026-09-02 16:28:11; last non-success 16:18:12 | Done | The corrected Moore implementation passed, and its new in-code explanation request is answered in a dedicated PDF. |
| 81 | Last success 2026-09-01 23:26:08 | Done | Waveform implements `q = b | c`; inputs `a` and `d` are irrelevant. |
| 82 | Last success 2026-09-01 23:23:20 | Done | Correct 32-bit concatenation includes two trailing one bits. |
| 83 | Last success 2026-09-02 17:00:08; last non-success 16:57:13 | Done | The successful version keeps captured falling edges sticky and initializes the previous sample during reset. |
| 84 | Last success 2026-09-02 16:54:21; last non-success 16:53:47 | Done | The successful motor equation now requires both `ring` and `vibrate_mode`. |
| 85 | Last success 2026-09-02 16:44:54; last non-success 16:31:02 | Done | The two-state Mealy behavior passed; the internal encoding is still not literally one-hot. |

### Entry 80 - Q5a serial two's complementer, Moore FSM

For an LSB-first stream, two's complement can be produced by copying zeros until the first 1, copying that first 1, and inverting every later bit. A Moore output cannot depend directly on the current input, so the output value must be represented by the state reached after sampling that input. This needs three functional states:

- `COPY_ZERO`, output 0, before the first 1;
- `OUTPUT_1`, output 1, for the first 1 or a later inverted 0;
- `OUTPUT_0`, output 0, for a later inverted 1.

The latest successful code follows this rule, includes a `default` transition for illegal-state recovery, and now has a fresh Attempt 2 success. Its submitted comments explicitly ask for a deeper explanation of the algorithm, timing, and need for each state; see the [Entry 80 Moore FSM deep-dive PDF](HDLBits_Entry80_Moore_Serial_Twos_Complement_Deep_Dive.pdf).

### Entry 81 - Combinational circuit 4

The waveform shows that `q` depends only on `b` and `c`:

```verilog
assign q = b | c;
```

The old `b + c` expression is arithmetic addition, not Boolean OR. When `b=c=1`, the mathematical sum is binary 2 and the carry cannot be represented by the one-bit output, while OR must remain 1. This counterexample distinguishes the two immediately.

### Entry 82 - Vector concatenation

Six five-bit inputs contain 30 bits, while `{w,x,y,z}` contains 32 bits. The original prompt explicitly requires two one bits after the six vectors:

```verilog
assign {w, x, y, z} = {a, b, c, d, e, f, 2'b11};
```

Omitting the final two bits does not merely leave `z[1:0]` unspecified. The 30-bit value is extended to the 32-bit destination from the left, so the grouping of all output bytes is shifted relative to the required concatenation.

### Entry 83 - Sticky falling-edge capture

The latest non-success overwrote `solution` with only the newest falling-edge mask. The prompt requires every detected bit to remain set until reset, so the new mask must be ORed with the old output. The previous input must also be sampled on every edge, including reset edges, so the first comparison after reset has a defined predecessor. The latest successful submission applies both corrections.

```verilog
reg [31:0] previous;

always @(posedge clk) begin
    previous <= in;
    if (reset)
        out <= 32'b0;
    else
        out <= out | (previous & ~in);
end
```

Reset has priority over capture. `previous & ~in` detects bits that were 1 at the preceding sample and are 0 now. The OR makes the result sticky.

### Entry 84 - Ring or vibrate

The required truth table is:

| `ring` | `vibrate_mode` | `ringer` | `motor` |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

Therefore:

```verilog
assign ringer = ring & ~vibrate_mode;
assign motor  = ring &  vibrate_mode;
```

The unsuccessful equation used `vibrate_mode & !ring`, which turns the motor on when no call is arriving and turns it off for the exact `ring=1, vibrate_mode=1` case that should activate it. For one-bit signals, `!ring` and `~ring` have the same 0/1 result, so the failure is the reversed `ring` condition, not merely the choice of NOT operator.

### Entry 85 - Q5b serial two's complementer, true one-hot Mealy FSM

The original problem explicitly says to use one-hot encoding. The latest successful code uses `s0=2'b00` and `s1=2'b01`; `2'b00` has no asserted state bit, so it is not one-hot even though HDLBits accepts the external behavior. Functional tests cannot necessarily observe the internal encoding.

The older unsuccessful submission also omitted `zr=0` in one branch of its combinational block. That leaves `zr` unassigned on that path and infers a latch. A genuinely one-hot, fully assigned implementation is:

```verilog
localparam [1:0] BEFORE_FIRST_ONE = 2'b01;
localparam [1:0] AFTER_FIRST_ONE  = 2'b10;

reg [1:0] state, next_state;

always @(posedge clk or posedge areset) begin
    if (areset)
        state <= BEFORE_FIRST_ONE;
    else
        state <= next_state;
end

always @(*) begin
    next_state = state;
    z = 1'b0;

    case (1'b1)
        state[0]: begin
            z = x;                 // Copy zeros and the first one.
            if (x)
                next_state = AFTER_FIRST_ONE;
        end
        state[1]: begin
            z = ~x;                // Invert all later bits.
            next_state = AFTER_FIRST_ONE;
        end
        default: begin
            next_state = BEFORE_FIRST_ONE;
            z = x;
        end
    endcase
end
```

## Day 6 completion follow-up - entries 86 through 93

Kapil reported these eight problems completed in the current pass. The Chrome tab strip captured on 2026-09-03 contains the same eight HDLBits pages, in the same progress block. Because page-body attachment was unavailable during this follow-up, the evidence column records the confirmation exactly and does not claim unseen success timestamps.

| Entry | Problem | Attempt 2 state | Question/reference |
|---:|---|---|---|
| 86 | [Vectorr](https://hdlbits.01xz.net/wiki/vectorr) | Done | No questions asked |
| 87 | [Dualedge](https://hdlbits.01xz.net/wiki/dualedge) | Done | [Day 6 non-FSM Q&A PDF](HDLBits_Day6_Non_FSM_QA_Dualedge_and_Circuit5.pdf) |
| 88 | [Thermostat](https://hdlbits.01xz.net/wiki/thermostat) | Done | No questions asked |
| 89 | [Sim/circuit5](https://hdlbits.01xz.net/wiki/sim/circuit5) | Done | [Day 6 non-FSM Q&A PDF](HDLBits_Day6_Non_FSM_QA_Dualedge_and_Circuit5.pdf) |
| 90 | [Exams/2014 q3fsm](https://hdlbits.01xz.net/wiki/exams/2014_q3fsm) | Done | [Standalone three-sample-window FSM PDF](HDLBits_Entry90_Exams_2014_Q3FSM_Three_Sample_Window_Deep_Dive.pdf) |
| 91 | [Vector4](https://hdlbits.01xz.net/wiki/vector4) | Done | No questions asked |
| 92 | [Count15](https://hdlbits.01xz.net/wiki/count15) | Done | No questions asked |
| 93 | [Popcount3](https://hdlbits.01xz.net/wiki/popcount3) | Done | No questions asked |

The saved Edge conversations add three review topics:

- In Dualedge, `qpos | qneg` can preserve a stale 1 from the register that was not updated at the latest edge. The primary HDLBits solution selects `qpos` while `clk` is high and `qneg` while it is low. The expanded PDF now distinguishes simulator acceptance from FPGA implementability: ordinary fabric registers are normally single-edge, whereas real DDR capture and launch use device-specific I/O resources such as AMD IDDR/ODDR or Intel/Altera DDIO. It also covers half-cycle timing, duty-cycle, glitch, metastability, reset, and XOR-startup concerns using primary vendor documentation.
- In Sim/circuit5, the waveform implies `c=0 -> b`, `c=1 -> e`, `c=2 -> a`, `c=3 -> d`, and all other selector values -> `4'hf`. Therefore `c` belongs in `case(c)`; input bus `b` is an identifier, not hexadecimal digit B.
- In Exams/2014 q3fsm, `ticks==2` means two samples have already been processed before the current third edge. Because nonblocking assignments expose old register values within the block, the third-sample decision uses `count + w`. The window counters must reset after every third sample, not only when the group contains exactly two ones. Both earlier wrong versions and the corrected two-state RTL are preserved in the standalone PDF.

## Local verification

The reusable testbench [day5_original_submission_selfcheck.sv](internal/Verification/day5_original_submission_selfcheck.sv) checks:

- all 16 input combinations for entry 77;
- sampled 0-to-1 pulses for entry 74;
- overlapping `10101` recognition and immediate reset assertion for entry 75;
- LSB-first Moore and true one-hot Mealy two's-complement streams for entries 80 and 85;
- all 16 waveform input combinations for entry 81;
- 200 randomized concatenations for entry 82;
- sticky falling-edge capture, reset priority, and post-reset behavior for entry 83;
- all four Ringer truth-table rows and mutual exclusion for entry 84.

Icarus Verilog result:

```text
PASS: Chrome-audit follow-up behavior checks passed (entries 74, 75, 77, 80-85).
```

The Day 6 checkers add:

```text
PASS: all 8 possible q3fsm groups plus back-to-back grouping; saved reset-only-on-match bug diverged as expected.
PASS: Dualedge MUX/XOR solutions and all 16 Circuit5 selector values; stale-register OR bug diverged as expected.
```

## Chrome evidence appendix

The table below records every original page in the audited range. For entries 1-85, dates are copied from the saved-submission selector displayed by HDLBits. For entries 86-93, `2026-09-03 current pass; user-confirmed` records the exact evidence available in the follow-up and avoids inventing an unseen timestamp.

| No. | Original HDLBits page | Last success shown in Chrome | Last non-success shown in Chrome | Attempt 2 state | Question/reference |
|---:|---|---|---|---|---|
| 1 | [Lemmings1](https://hdlbits.01xz.net/wiki/lemmings1) | 8/29/2026, 3:33:16 PM | 8/29/2026, 3:30:28 PM | Done | No explicit question recorded |
| 2 | [Fsm serial](https://hdlbits.01xz.net/wiki/fsm_serial) | 8/30/2026, 9:56:33 AM | 8/30/2026, 9:55:55 AM | Done | Serial discussion PDF |
| 3 | [Lemmings2](https://hdlbits.01xz.net/wiki/lemmings2) | 8/29/2026, 3:54:58 PM | 8/29/2026, 3:51:51 PM | Done | No explicit question recorded |
| 4 | [Fsm serialdata](https://hdlbits.01xz.net/wiki/fsm_serialdata) | 8/30/2026, 10:24:16 AM | 8/30/2026, 10:22:16 AM | Done | Serial discussion PDF |
| 5 | [Lemmings3](https://hdlbits.01xz.net/wiki/lemmings3) | 8/29/2026, 4:21:22 PM | 8/29/2026, 4:21:03 PM | Done | No explicit question recorded |
| 6 | [Fsm serialdp](https://hdlbits.01xz.net/wiki/fsm_serialdp) | 8/30/2026, 10:55:13 AM | 8/30/2026, 10:53:43 AM | Done | Serial discussion PDF |
| 7 | [Lemmings4](https://hdlbits.01xz.net/wiki/lemmings4) | 8/29/2026, 9:14:52 PM | 8/29/2026, 9:12:30 PM | Done | Combined questions PDF |
| 8 | [Fsm hdlc](https://hdlbits.01xz.net/wiki/fsm_hdlc) | 8/29/2026, 11:20:34 PM | 8/29/2026, 11:14:37 PM | Done | HDLC discussion PDF |
| 9 | [Conditional](https://hdlbits.01xz.net/wiki/conditional) | 8/30/2026, 3:40:27 PM | none | Done | No explicit question recorded |
| 10 | [Dff](https://hdlbits.01xz.net/wiki/dff) | 8/30/2026, 3:42:19 PM | none | Done | No explicit question recorded |
| 11 | [Step one](https://hdlbits.01xz.net/wiki/step_one) | 8/30/2026, 3:42:48 PM | none | Done | No explicit question recorded |
| 12 | [Fsm1](https://hdlbits.01xz.net/wiki/fsm1) | 8/30/2026, 3:49:25 PM | 8/30/2026, 3:48:09 PM | Done | No explicit question recorded |
| 13 | [Bugs mux2](https://hdlbits.01xz.net/wiki/bugs_mux2) | 8/30/2026, 4:09:04 PM | 8/30/2026, 4:08:09 PM | Done | Combined questions PDF |
| 14 | [Reduction](https://hdlbits.01xz.net/wiki/reduction) | 8/30/2026, 4:10:13 PM | 6/24/2026, 6:14:19 PM | Done | No explicit question recorded |
| 15 | [Dff8](https://hdlbits.01xz.net/wiki/dff8) | 8/30/2026, 4:12:23 PM | none | Done | No explicit question recorded |
| 16 | [Zero](https://hdlbits.01xz.net/wiki/zero) | 8/30/2026, 4:12:48 PM | none | Done | No explicit question recorded |
| 17 | [Fsm1s](https://hdlbits.01xz.net/wiki/fsm1s) | 8/30/2026, 4:21:45 PM | 8/30/2026, 4:23:11 PM | Done | No explicit question recorded |
| 18 | [Gates100](https://hdlbits.01xz.net/wiki/gates100) | 8/30/2026, 4:14:01 PM | none | Done | No explicit question recorded |
| 19 | [Dff8r](https://hdlbits.01xz.net/wiki/dff8r) | 8/30/2026, 5:06:27 PM | 6/25/2026, 10:23:54 PM | Done | Combined questions PDF |
| 20 | [Wire](https://hdlbits.01xz.net/wiki/wire) | 8/30/2026, 5:06:45 PM | none | Done | Combined questions PDF |
| 21 | [Bugs nand3](https://hdlbits.01xz.net/wiki/bugs_nand3) | 8/30/2026, 5:12:57 PM | 8/30/2026, 5:07:56 PM | Done | Combined questions PDF |
| 22 | [Fsm2](https://hdlbits.01xz.net/wiki/fsm2) | 8/30/2026, 5:15:53 PM | 8/30/2026, 5:15:28 PM | Done | Combined questions PDF |
| 23 | [Vector100r](https://hdlbits.01xz.net/wiki/vector100r) | 8/30/2026, 5:21:27 PM | 6/24/2026, 6:21:32 PM | Done | Combined questions PDF |
| 24 | [Dff8p](https://hdlbits.01xz.net/wiki/dff8p) | 8/30/2026, 6:12:50 PM | 8/30/2026, 5:30:37 PM | Done | Combined questions PDF |
| 25 | [Wire4](https://hdlbits.01xz.net/wiki/wire4) | 8/30/2026, 5:31:49 PM | 6/23/2026, 5:49:49 PM | Done | Combined questions PDF |
| 26 | [Popcount255](https://hdlbits.01xz.net/wiki/popcount255) | 8/30/2026, 5:50:16 PM | 8/30/2026, 5:46:15 PM | Done | Combined questions PDF |
| 27 | [Fsm2s](https://hdlbits.01xz.net/wiki/fsm2s) | 8/30/2026, 5:54:41 PM | 8/30/2026, 5:53:48 PM | Done | Combined questions PDF |
| 28 | [Dff8ar](https://hdlbits.01xz.net/wiki/dff8ar) | 8/30/2026, 5:58:16 PM | 6/25/2026, 10:28:54 PM | Done | Combined questions PDF |
| 29 | [Bugs mux4](https://hdlbits.01xz.net/wiki/bugs_mux4) | 8/30/2026, 6:09:06 PM | 8/30/2026, 6:08:27 PM | Done | Combined questions PDF |
| 30 | [Adder100i](https://hdlbits.01xz.net/wiki/adder100i) | 8/30/2026, 6:29:42 PM | 8/30/2026, 6:29:17 PM | Done | Combined questions PDF |
| 31 | [Notgate](https://hdlbits.01xz.net/wiki/notgate) | 8/30/2026, 7:09:37 PM | none | Done | Combined questions PDF |
| 32 | [Fsm3comb](https://hdlbits.01xz.net/wiki/fsm3comb) | 8/30/2026, 11:45:51 PM | 8/30/2026, 11:43:15 PM | Done | No explicit question recorded |
| 33 | [Dff16e](https://hdlbits.01xz.net/wiki/dff16e) | 8/30/2026, 7:26:48 PM | 6/25/2026, 10:39:59 PM | Done | No explicit question recorded |
| 34 | [Bcdadd100](https://hdlbits.01xz.net/wiki/bcdadd100) | 8/30/2026, 9:57:17 PM | 8/30/2026, 9:54:23 PM | Done | No explicit question recorded |
| 35 | [Andgate](https://hdlbits.01xz.net/wiki/andgate) | 8/30/2026, 7:11:50 PM | none | Done | No explicit question recorded |
| 36 | [Bugs addsubz](https://hdlbits.01xz.net/wiki/bugs_addsubz) | 8/30/2026, 10:07:09 PM | 8/30/2026, 10:02:03 PM | Done | Combined questions PDF |
| 37 | [Exams/m2014 q4h](https://hdlbits.01xz.net/wiki/exams/m2014_q4h) | 8/30/2026, 7:21:33 PM | none | Done | No explicit question recorded |
| 38 | [Exams/m2014 q4a](https://hdlbits.01xz.net/wiki/exams/m2014_q4a) | 8/30/2026, 7:32:02 PM | 8/30/2026, 7:30:55 PM | Done | Combined questions PDF |
| 39 | [Fsm3onehot](https://hdlbits.01xz.net/wiki/fsm3onehot) | 8/30/2026, 10:36:07 PM | 8/30/2026, 10:35:24 PM | Done | No explicit question recorded |
| 40 | [Norgate](https://hdlbits.01xz.net/wiki/norgate) | 8/30/2026, 7:22:24 PM | 6/24/2026, 12:31:16 AM | Done | No explicit question recorded |
| 41 | [Exams/m2014 q4i](https://hdlbits.01xz.net/wiki/exams/m2014_q4i) | 8/30/2026, 7:22:37 PM | none | Done | No explicit question recorded |
| 42 | [Exams/m2014 q4b](https://hdlbits.01xz.net/wiki/exams/m2014_q4b) | 8/30/2026, 7:37:09 PM | none | Done | No explicit question recorded |
| 43 | [Fsm3](https://hdlbits.01xz.net/wiki/fsm3) | 8/30/2026, 10:57:04 PM | none | Done | No explicit question recorded |
| 44 | [Xnorgate](https://hdlbits.01xz.net/wiki/xnorgate) | 8/30/2026, 7:38:46 PM | 8/30/2026, 7:38:25 PM | Done | No explicit question recorded |
| 45 | [Exams/m2014 q4e](https://hdlbits.01xz.net/wiki/exams/m2014_q4e) | 8/30/2026, 7:33:30 PM | 6/24/2026, 11:32:45 PM | Done | No explicit question recorded |
| 46 | [Exams/m2014 q4c](https://hdlbits.01xz.net/wiki/exams/m2014_q4c) | 8/30/2026, 10:40:45 PM | none | Done | No explicit question recorded |
| 47 | [Always case](https://hdlbits.01xz.net/wiki/always_case) | 8/30/2026, 10:43:52 PM | 8/30/2026, 10:43:30 PM | Done | No explicit question recorded |
| 48 | [Fsm3s](https://hdlbits.01xz.net/wiki/fsm3s) | 8/30/2026, 10:54:27 PM | 8/30/2026, 10:52:35 PM | Done | No explicit question recorded |
| 49 | [Wire decl](https://hdlbits.01xz.net/wiki/wire_decl) | 8/30/2026, 10:46:25 PM | none | Done | No explicit question recorded |
| 50 | [Exams/m2014 q4f](https://hdlbits.01xz.net/wiki/exams/m2014_q4f) | 8/30/2026, 7:35:50 PM | 8/30/2026, 7:35:13 PM | Done | No explicit question recorded |
| 51 | [Exams/m2014 q4d](https://hdlbits.01xz.net/wiki/exams/m2014_q4d) | 8/31/2026, 9:32:17 AM | 8/31/2026, 9:31:28 AM | Done | No explicit question recorded |
| 52 | [Exams/m2014 q4g](https://hdlbits.01xz.net/wiki/exams/m2014_q4g) | 8/31/2026, 9:34:10 AM | none | Done | No explicit question recorded |
| 53 | [7458](https://hdlbits.01xz.net/wiki/7458) | 8/31/2026, 9:39:14 AM | none | Done | No explicit question recorded |
| 54 | [Exams/ece241 2013 q4](https://hdlbits.01xz.net/wiki/exams/ece241_2013_q4) | 9/1/2026, 12:21:28 AM | 9/1/2026, 12:16:46 AM | Done | [Recovered questions PDF](HDLBits_Recovered_Code_Questions_54_74_75_77.pdf) |
| 55 | [Sim/circuit1](https://hdlbits.01xz.net/wiki/sim/circuit1) | 8/31/2026, 8:36:12 PM | 6/28/2026, 1:32:14 AM | Done | No explicit question recorded |
| 56 | [Mt2015 muxdff](https://hdlbits.01xz.net/wiki/mt2015_muxdff) | 9/1/2026, 12:32:44 AM | 9/1/2026, 12:32:23 AM | Done | No explicit question recorded |
| 57 | [Gates](https://hdlbits.01xz.net/wiki/gates) | 9/1/2026, 12:39:20 AM | 9/1/2026, 12:38:40 AM | Done | No explicit question recorded |
| 58 | [Vector0](https://hdlbits.01xz.net/wiki/vector0) | 9/1/2026, 12:43:49 AM | 9/1/2026, 12:40:57 AM | Done | No explicit question recorded |
| 59 | [Fsm onehot](https://hdlbits.01xz.net/wiki/fsm_onehot) | 9/1/2026, 12:58:13 AM | 7/5/2026, 5:07:43 PM | Done | No explicit question recorded |
| 60 | [Exams/2014 q4a](https://hdlbits.01xz.net/wiki/exams/2014_q4a) | 9/1/2026, 1:04:13 AM | 6/26/2026, 12:19:52 AM | Done | No explicit question recorded |
| 61 | [7420](https://hdlbits.01xz.net/wiki/7420) | 9/1/2026, 1:28:08 AM | none | Done | No explicit question recorded |
| 62 | [Vector1](https://hdlbits.01xz.net/wiki/vector1) | 9/1/2026, 1:30:34 AM | 6/23/2026, 9:44:41 PM | Done | No explicit question recorded |
| 63 | [Sim/circuit2](https://hdlbits.01xz.net/wiki/sim/circuit2) | 9/1/2026, 11:00:02 AM | 9/1/2026, 10:53:57 AM | Done | No explicit question recorded |
| 64 | [Fsm ps2](https://hdlbits.01xz.net/wiki/fsm_ps2) | 9/1/2026, 4:25:35 PM | 9/1/2026, 4:26:58 PM | Done | No explicit question recorded |
| 65 | [Truthtable1](https://hdlbits.01xz.net/wiki/truthtable1) | 9/1/2026, 5:12:37 PM | none | Done | No explicit question recorded |
| 66 | [Exams/ece241 2014 q4](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q4) | 9/1/2026, 5:28:19 PM | 9/1/2026, 5:26:37 PM | Done | Day 4 questions PDF |
| 67 | [Vector2](https://hdlbits.01xz.net/wiki/vector2) | 9/1/2026, 5:40:40 PM | 9/1/2026, 5:38:14 PM | Done | Day 4 questions PDF |
| 68 | [Mt2015 eq2](https://hdlbits.01xz.net/wiki/mt2015_eq2) | 9/1/2026, 6:30:47 PM | none | Done | No explicit question recorded |
| 69 | [Exams/ece241 2013 q7](https://hdlbits.01xz.net/wiki/exams/ece241_2013_q7) | 9/1/2026, 6:29:32 PM | none | Done | No explicit question recorded |
| 70 | [Fsm ps2data](https://hdlbits.01xz.net/wiki/fsm_ps2data) | 9/1/2026, 4:46:09 PM | 9/1/2026, 4:43:36 PM | Done | Day 4 questions PDF |
| 71 | [Sim/circuit3](https://hdlbits.01xz.net/wiki/sim/circuit3) | 9/1/2026, 10:21:36 PM | 9/1/2026, 10:17:52 PM | Done | No explicit question recorded |
| 72 | [Mt2015 q4a](https://hdlbits.01xz.net/wiki/mt2015_q4a) | 9/1/2026, 10:22:14 PM | none | Done | No explicit question recorded |
| 73 | [Vectorgates](https://hdlbits.01xz.net/wiki/vectorgates) | 9/1/2026, 10:24:57 PM | 9/1/2026, 10:23:57 PM | Done | No explicit question recorded |
| 74 | [Edgedetect](https://hdlbits.01xz.net/wiki/edgedetect) | 9/1/2026, 10:28:38 PM | 9/1/2026, 9:58:30 PM | Done | [Recovered questions PDF](HDLBits_Recovered_Code_Questions_54_74_75_77.pdf) |
| 75 | [Exams/ece241 2013 q8](https://hdlbits.01xz.net/wiki/exams/ece241_2013_q8) | 9/1/2026, 10:37:57 PM | 9/1/2026, 10:36:46 PM | Done | [Recovered questions PDF](HDLBits_Recovered_Code_Questions_54_74_75_77.pdf) |
| 76 | [Mt2015 q4b](https://hdlbits.01xz.net/wiki/mt2015_q4b) | 9/1/2026, 10:38:41 PM | none | Done | No explicit question recorded |
| 77 | [Gates4](https://hdlbits.01xz.net/wiki/gates4) | 9/1/2026, 10:44:37 PM | 6/23/2026, 10:15:40 PM | Done | [Recovered questions PDF](HDLBits_Recovered_Code_Questions_54_74_75_77.pdf) |
| 78 | [Edgedetect2](https://hdlbits.01xz.net/wiki/edgedetect2) | 9/1/2026, 10:47:42 PM | 9/1/2026, 10:47:07 PM | Done | No explicit question recorded |
| 79 | [Mt2015 q4](https://hdlbits.01xz.net/wiki/mt2015_q4) | 9/1/2026, 11:01:04 PM | 9/1/2026, 11:00:16 PM | Done | No explicit question recorded |
| 80 | [Exams/ece241 2014 q5a](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q5a) | 9/2/2026, 4:28:11 PM | 9/2/2026, 4:18:12 PM | Done | [Entry 80 Moore FSM PDF](HDLBits_Entry80_Moore_Serial_Twos_Complement_Deep_Dive.pdf) |
| 81 | [Sim/circuit4](https://hdlbits.01xz.net/wiki/sim/circuit4) | 9/1/2026, 11:26:08 PM | 6/28/2026, 3:34:12 PM | Done | Day 5 submission review |
| 82 | [Vector3](https://hdlbits.01xz.net/wiki/vector3) | 9/1/2026, 11:23:20 PM | 9/1/2026, 11:19:13 PM | Done | Day 5 submission review |
| 83 | [Edgecapture](https://hdlbits.01xz.net/wiki/edgecapture) | 9/2/2026, 5:00:08 PM | 9/2/2026, 4:57:13 PM | Done | Day 5 submission review |
| 84 | [Ringer](https://hdlbits.01xz.net/wiki/ringer) | 9/2/2026, 4:54:21 PM | 9/2/2026, 4:53:47 PM | Done | Day 5 submission review |
| 85 | [Exams/ece241 2014 q5b](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q5b) | 9/2/2026, 4:44:54 PM | 9/2/2026, 4:31:02 PM | Done | Day 5 submission review |
| 86 | [Vectorr](https://hdlbits.01xz.net/wiki/vectorr) | 2026-09-03 current pass; user-confirmed | not captured in follow-up | Done | No explicit question recorded |
| 87 | [Dualedge](https://hdlbits.01xz.net/wiki/dualedge) | 2026-09-03 current pass; user-confirmed | not captured in follow-up | Done | [Day 6 non-FSM Q&A PDF](HDLBits_Day6_Non_FSM_QA_Dualedge_and_Circuit5.pdf) |
| 88 | [Thermostat](https://hdlbits.01xz.net/wiki/thermostat) | 2026-09-03 current pass; user-confirmed | not captured in follow-up | Done | No explicit question recorded |
| 89 | [Sim/circuit5](https://hdlbits.01xz.net/wiki/sim/circuit5) | 2026-09-03 current pass; user-confirmed | not captured in follow-up | Done | [Day 6 non-FSM Q&A PDF](HDLBits_Day6_Non_FSM_QA_Dualedge_and_Circuit5.pdf) |
| 90 | [Exams/2014 q3fsm](https://hdlbits.01xz.net/wiki/exams/2014_q3fsm) | 2026-09-03 current pass; user-confirmed | not captured in follow-up | Done | [Standalone three-sample-window FSM PDF](HDLBits_Entry90_Exams_2014_Q3FSM_Three_Sample_Window_Deep_Dive.pdf) |
| 91 | [Vector4](https://hdlbits.01xz.net/wiki/vector4) | 2026-09-03 current pass; user-confirmed | not captured in follow-up | Done | No explicit question recorded |
| 92 | [Count15](https://hdlbits.01xz.net/wiki/count15) | 2026-09-03 current pass; user-confirmed | not captured in follow-up | Done | No explicit question recorded |
| 93 | [Popcount3](https://hdlbits.01xz.net/wiki/popcount3) | 2026-09-03 current pass; user-confirmed | not captured in follow-up | Done | No explicit question recorded |

Entries 1 through 93 are now Done. Entries 94-178 remain Pending and were not part of this follow-up; no current-window submission claim is made for them.
