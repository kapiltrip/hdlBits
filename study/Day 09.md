# Day 09 — 2026-07-02

Completed problems: **11**

Each screenshot is embedded at the full width of the GitHub page. Select an image to open its original-resolution file.

## Index

| # | Time | Problem | Section | Problem note | Solution | Source |
|---:|---|---:|---|---|---|---|
| 1 | 3:09:43 PM | [144](#problem-144) | Sequential Logic | [Counter 1000](problems/Day%2009/144-exams__ece241_2014_q7b.md) | [Code](solutions/Day%2009/144-exams__ece241_2014_q7b.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q7b) |
| 2 | 12:08:54 AM | [145](#problem-145) | Sequential Logic | [4-digit decimal counter](problems/Day%2009/145-countbcd.md) | [Code](solutions/Day%2009/145-countbcd.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/countbcd) |
| 3 | 2:55:03 PM | [146](#problem-146) | Sequential Logic | [12-hour clock](problems/Day%2009/146-count_clock.md) | [Code](solutions/Day%2009/146-count_clock.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/count_clock) |
| 4 | 4:31:18 PM | [147](#problem-147) | Building Larger Circuits | [Counter with period 1000](problems/Day%2009/147-exams__review2015_count1k.md) | [Code](solutions/Day%2009/147-exams__review2015_count1k.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/exams/review2015_count1k) |
| 5 | 4:47:48 PM | [148](#problem-148) | Building Larger Circuits | [4-bit shift register and down counter](problems/Day%2009/148-exams__review2015_shiftcount.md) | [Code](solutions/Day%2009/148-exams__review2015_shiftcount.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/exams/review2015_shiftcount) |
| 6 | 5:30:53 PM | [149](#problem-149) | Building Larger Circuits | [FSM: Sequence 1101 recognizer](problems/Day%2009/149-exams__review2015_fsmseq.md) | [Code](solutions/Day%2009/149-exams__review2015_fsmseq.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/exams/review2015_fsmseq) |
| 7 | 6:02:39 PM | [150](#problem-150) | Building Larger Circuits | [FSM: Enable shift register](problems/Day%2009/150-exams__review2015_fsmshift.md) | [Code](solutions/Day%2009/150-exams__review2015_fsmshift.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/exams/review2015_fsmshift) |
| 8 | 9:12:14 PM | [151](#problem-151) | Getting Started | [Getting Started](problems/Day%2009/151-step_one.md) | [Code](solutions/Day%2009/151-step_one.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/step_one) |
| 9 | 9:12:38 PM | [152](#problem-152) | Getting Started | [Output Zero](problems/Day%2009/152-zero.md) | [Code](solutions/Day%2009/152-zero.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/zero) |
| 10 | 10:20:45 PM | [153](#problem-153) | Building Larger Circuits | [FSM: The complete FSM](problems/Day%2009/153-exams__review2015_fsm.md) | [Code](solutions/Day%2009/153-exams__review2015_fsm.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/exams/review2015_fsm) |
| 11 | 11:38:15 PM | [154](#problem-154) | Building Larger Circuits | [The complete timer](problems/Day%2009/154-exams__review2015_fancytimer.md) | [Code](solutions/Day%2009/154-exams__review2015_fancytimer.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/exams/review2015_fancytimer) |

---

<a id="problem-144"></a>
## 144 — Counter 1000

[Problem note](problems/Day%2009/144-exams__ece241_2014_q7b.md) · [Open screenshot at full resolution](images/Day%2009/144-exams__ece241_2014_q7b.png) · [Verilog file](solutions/Day%2009/144-exams__ece241_2014_q7b.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q7b)

<a href="images/Day%2009/144-exams__ece241_2014_q7b.png"><img src="images/Day%2009/144-exams__ece241_2014_q7b.png" alt="Counter 1000 question and submitted solution" width="100%"></a>

### What the question is asking

The 1000 Hz input is divided by cascading three synchronous decade counters. Every counter receives the same clock; the hierarchy is created entirely with enable pulses, so this is a synchronous design rather than a ripple-clock chain.

The least-significant decade runs every cycle, making `c_enable[0]=1`. The middle decade advances only while the least-significant digit is 9, and the most-significant decade advances only while both lower digits are 9. On the 999th terminal state all three enable conditions are active. The next rising edge rolls the digits to 000, so the terminal decode `msb==9 && middle==9 && lsb==9` is high for exactly one 1000 Hz cycle before that edge.

That one-cycle terminal decode is the requested `OneHertz` pulse. It repeats every 1000 input cycles, or once per second. The important design rule is that carry enables are combinational functions of the pre-edge digit values; registering them would delay the carry and corrupt the decimal sequence.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,
    output OneHertz,
    output [2:0] c_enable
);
    reg [3:0] msb, middle, lsb;

    assign c_enable[0] = 1'b1;
    assign c_enable[1] = (lsb == 4'd9);
    assign c_enable[2] = (lsb == 4'd9) && (middle == 4'd9);

    bcdcount counter0 (clk, reset, c_enable[0], lsb);
    bcdcount counter1 (clk, reset, c_enable[1], middle);
    bcdcount counter2 (clk, reset, c_enable[2], msb);

    assign OneHertz = (msb == 4'd9) && (middle == 4'd9) && (lsb == 4'd9);
endmodule
```

---

<a id="problem-145"></a>
## 145 — 4-digit decimal counter

[Problem note](problems/Day%2009/145-countbcd.md) · [Open screenshot at full resolution](images/Day%2009/145-countbcd.png) · [Verilog file](solutions/Day%2009/145-countbcd.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/countbcd)

<a href="images/Day%2009/145-countbcd.png"><img src="images/Day%2009/145-countbcd.png" alt="4-digit decimal counter question and submitted solution" width="100%"></a>

### What the question is asking

This is a four-digit synchronous BCD counter. Each four-bit digit stores only 0 through 9, and every digit is clocked by the same rising edge. The ones digit advances on every enabled cycle of the overall design. Each higher digit advances only when every less-significant digit is currently 9.

The enable outputs expose those carry conditions: `ena[1]` is high at x9, `ena[2]` at x99, and `ena[3]` at x999. Because nonblocking assignments evaluate their right-hand sides from the old state, the same edge that changes 0099 to 0100 sees both lower digits at 9, clears them, and increments the hundreds digit.

The output concatenation `{digit3,digit2,digit1,digit0}` places the thousands nibble in q[15:12] and the ones nibble in q[3:0]. Reset is synchronous and clears all four digits together. The key pitfall is checking an already-updated lower digit; synchronous carry must be derived from the values present immediately before the active edge.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,
    output [3:1] ena,
    output [15:0] q
);
    reg [3:0] digit0, digit1, digit2, digit3;

    assign ena[1] = (digit0 == 4'd9);
    assign ena[2] = (digit0 == 4'd9) && (digit1 == 4'd9);
    assign ena[3] = (digit0 == 4'd9) && (digit1 == 4'd9) && (digit2 == 4'd9);

    always @(posedge clk) begin
        if (reset) begin
            digit0 <= 4'd0;
            digit1 <= 4'd0;
            digit2 <= 4'd0;
            digit3 <= 4'd0;
        end
        else begin
            if (digit0 == 4'd9)
                digit0 <= 4'd0;
            else
                digit0 <= digit0 + 1'b1;

            if (ena[1]) begin
                if (digit1 == 4'd9)
                    digit1 <= 4'd0;
                else
                    digit1 <= digit1 + 1'b1;
            end

            if (ena[2]) begin
                if (digit2 == 4'd9)
                    digit2 <= 4'd0;
                else
                    digit2 <= digit2 + 1'b1;
            end

            if (ena[3]) begin
                if (digit3 == 4'd9)
                    digit3 <= 4'd0;
                else
                    digit3 <= digit3 + 1'b1;
            end
        end
    end

    assign q = {digit3, digit2, digit1, digit0};
endmodule
```

---

<a id="problem-146"></a>
## 146 — 12-hour clock

[Problem note](problems/Day%2009/146-count_clock.md) · [Open screenshot at full resolution](images/Day%2009/146-count_clock.png) · [Verilog file](solutions/Day%2009/146-count_clock.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/count_clock)

<a href="images/Day%2009/146-count_clock.png"><img src="images/Day%2009/146-count_clock.png" alt="12-hour clock question and submitted solution" width="100%"></a>

### What the question is asking

The clock contains six BCD digits plus one AM/PM state bit. The outer enable gates the entire time update, while synchronous reset has priority and loads the required 12:00:00 AM state. If enable is low, every register retains its previous value.

Seconds normally increment their ones nibble. At x9, the ones nibble clears and the tens nibble increments; at 59, the complete seconds byte clears and the same edge advances minutes. Minutes use the identical BCD rollover pattern. Only when both seconds and minutes are 59 does the hour update.

Hours require a non-decimal sequence: 01 through 12. The 09-to-10 transition uses the BCD nibble carry, 11 advances to 12 and toggles PM, and 12 rolls to 01 without toggling PM. This places the AM/PM transition at 11:59:59 to 12:00:00, not at 12:59:59 to 01:00:00.

All state changes use nonblocking assignments in one clocked process, so each decision observes the same pre-edge time. That property lets the nested terminal-count tests propagate a one-cycle carry from seconds through minutes into hours without generating derived clocks.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,
    input ena,
    output reg pm,
    output reg [7:0] hh,
    output reg [7:0] mm,
    output reg [7:0] ss
);
    always @(posedge clk) begin
        if (reset) begin
            pm <= 1'b0;
            hh <= 8'h12;
            mm <= 8'h00;
            ss <= 8'h00;
        end
        else if (ena) begin
            if (ss == 8'h59) begin
                ss <= 8'h00;

                if (mm == 8'h59) begin
                    mm <= 8'h00;

                    if (hh == 8'h11) begin
                        hh <= 8'h12;
                        pm <= ~pm;
                    end
                    else if (hh == 8'h12) begin
                        hh <= 8'h01;
                    end
                    else if (hh[3:0] == 4'd9) begin
                        hh[3:0] <= 4'd0;
                        hh[7:4] <= hh[7:4] + 4'd1;
                    end
                    else begin
                        hh[3:0] <= hh[3:0] + 4'd1;
                    end
                end
                else if (mm[3:0] == 4'd9) begin
                    mm[3:0] <= 4'd0;
                    mm[7:4] <= mm[7:4] + 4'd1;
                end
                else begin
                    mm[3:0] <= mm[3:0] + 4'd1;
                end
            end
            else if (ss[3:0] == 4'd9) begin
                ss[3:0] <= 4'd0;
                ss[7:4] <= ss[7:4] + 4'd1;
            end
            else begin
                ss[3:0] <= ss[3:0] + 4'd1;
            end
        end
    end
endmodule
```

---

<a id="problem-147"></a>
## 147 — Counter with period 1000

[Problem note](problems/Day%2009/147-exams__review2015_count1k.md) · [Open screenshot at full resolution](images/Day%2009/147-exams__review2015_count1k.png) · [Verilog file](solutions/Day%2009/147-exams__review2015_count1k.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/review2015_count1k)

<a href="images/Day%2009/147-exams__review2015_count1k.png"><img src="images/Day%2009/147-exams__review2015_count1k.png" alt="Counter with period 1000 question and submitted solution" width="100%"></a>

### What the question is asking

This design is a modulo-1000 synchronous counter. Its legal sequence is 0, 1, 2, ... 999, then back to 0, which gives exactly 1000 distinct states and therefore a period of 1000 clock cycles. Ten bits are required because nine bits can represent only 0 through 511, while ten bits can represent the terminal value 999.

The clocked process gives synchronous reset the highest priority. When reset is sampled high on a rising edge, the register becomes zero. Otherwise, the terminal-count comparison is evaluated using the old value: 999 loads zero, and every other value increments by one. A nonblocking assignment is appropriate because q represents registered state and changes only after the active clock edge.

The explicit terminal comparison is essential. Letting a 10-bit binary register overflow naturally would produce a modulo-1024 counter, so values 1000 through 1023 would incorrectly appear in the sequence. The separate internal register is connected continuously to q, although q could equivalently be declared as a register and updated directly.

**Boundary trace:** 998 advances to 999; 999 advances to 0; asserting reset while the count is 417 loads 0 at the next rising edge.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,
    output [9:0] q
);
    reg [9:0] count;

    always @(posedge clk) begin
        if (reset)
            count <= 10'd0;
        else if (count == 10'd999)
            count <= 10'd0;
        else
            count <= count + 10'd1;
    end

    assign q = count;
endmodule
```

---

<a id="problem-148"></a>
## 148 — 4-bit shift register and down counter

[Problem note](problems/Day%2009/148-exams__review2015_shiftcount.md) · [Open screenshot at full resolution](images/Day%2009/148-exams__review2015_shiftcount.png) · [Verilog file](solutions/Day%2009/148-exams__review2015_shiftcount.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/review2015_shiftcount)

<a href="images/Day%2009/148-exams__review2015_shiftcount.png"><img src="images/Day%2009/148-exams__review2015_shiftcount.png" alt="4-bit shift register and down counter question and submitted solution" width="100%"></a>

### What the question is asking

One four-bit register performs two different operations. When shift_ena is asserted, the existing bits move toward the most-significant end and the serial data bit enters bit 0 through {register[2:0], data}. Supplying a four-bit word most-significant bit first therefore reconstructs that word after four enabled shifts.

When count_ena is asserted, the same storage acts as a modulo-16 down counter. Values 15 through 1 decrement normally, while 0 explicitly wraps to 15. Four-bit subtraction would also wrap naturally, but the terminal branch makes the intended rollover unambiguous.

The specification guarantees that shift_ena and count_ena are never high together, so their relative priority is intentionally irrelevant. The saved solution uses two independent if statements to reflect that contract. If both controls were asserted despite the contract, the later nonblocking assignment would win; a production interface without the guarantee should instead define priority explicitly with if/else if.

With both controls low, no assignment occurs and the register holds its value. There is no reset input, so the environment must shift in a complete value before relying on the state.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input shift_ena,
    input count_ena,
    input data,
    output [3:0] q
);
    reg [3:0] shift_count;

    always @(posedge clk) begin
        if (shift_ena)
            shift_count <= {shift_count[2:0], data};
        if (count_ena) begin
            if (shift_count == 4'd0)
                shift_count <= 4'd15;
            else
                shift_count <= shift_count - 4'd1;
        end
    end

    assign q = shift_count;
endmodule
```

---

<a id="problem-149"></a>
## 149 — FSM: Sequence 1101 recognizer

[Problem note](problems/Day%2009/149-exams__review2015_fsmseq.md) · [Open screenshot at full resolution](images/Day%2009/149-exams__review2015_fsmseq.png) · [Verilog file](solutions/Day%2009/149-exams__review2015_fsmseq.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/review2015_fsmseq)

<a href="images/Day%2009/149-exams__review2015_fsmseq.png"><img src="images/Day%2009/149-exams__review2015_fsmseq.png" alt="FSM: Sequence 1101 recognizer question and submitted solution" width="100%"></a>

### What the question is asking

This Moore finite-state machine recognizes the serial bit pattern 1101 and then latches a permanent command to begin shifting. States S0 through S3 record how much of the target prefix has been matched: no useful prefix, 1, 11, and 110. DONE means the complete 1101 sequence has appeared.

The transitions preserve useful overlap. From S2 (the suffix 11), another 1 remains in S2 because the newest two bits are still 11; a 0 advances to S3. From S3, a 1 completes 1101 and enters DONE, while a 0 has no useful suffix and returns to S0. Earlier mismatches similarly return to the correct prefix state.

DONE is absorbing: both possible data values leave the machine in DONE. Therefore start_shifting, decoded solely from the registered state, stays asserted forever after recognition and can be cleared only by reset. Reset is synchronous because it is tested inside an always @(posedge clk) process rather than included in the sensitivity list.

**Example trace:** after reset, inputs 1,1,0,1 move S0→S1→S2→S3→DONE. The output becomes high after the edge accepting the final 1 and remains high on all later edges.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,
    input data,
    output start_shifting
);
    localparam S0   = 3'b000;
    localparam S1   = 3'b001;
    localparam S2   = 3'b010;
    localparam S3   = 3'b011;
    localparam DONE = 3'b100;

    reg [2:0] state;
    reg [2:0] next_state;

    always @(posedge clk) begin
        if (reset)
            state <= S0;
        else
            state <= next_state;
    end

    always @(*) begin
        case (state)
            S0:      next_state = data ? S1 : S0;
            S1:      next_state = data ? S2 : S0;
            S2:      next_state = data ? S2 : S3;
            S3:      next_state = data ? DONE : S0;
            DONE:    next_state = DONE;
            default: next_state = S0;
        endcase
    end

    assign start_shifting = (state == DONE);
endmodule
```

---

<a id="problem-150"></a>
## 150 — FSM: Enable shift register

[Problem note](problems/Day%2009/150-exams__review2015_fsmshift.md) · [Open screenshot at full resolution](images/Day%2009/150-exams__review2015_fsmshift.png) · [Verilog file](solutions/Day%2009/150-exams__review2015_fsmshift.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/review2015_fsmshift)

<a href="images/Day%2009/150-exams__review2015_fsmshift.png"><img src="images/Day%2009/150-exams__review2015_fsmshift.png" alt="FSM: Enable shift register question and submitted solution" width="100%"></a>

### What the question is asking

This control circuit produces a pulse window measured in clock cycles rather than detecting a data pattern. A three-bit saturating counter records how many post-reset rising edges have occurred. Synchronous reset loads zero; while the value is below four, each later edge increments it; after reaching four, the missing assignment deliberately holds the state.

shift_ena is a Moore-style combinational decode of the registered count. It is high for count values 0, 1, 2, and 3, giving exactly four complete clock intervals, and becomes low when the fourth post-reset edge changes the count to 4. Saturation prevents the counter from wrapping back to zero and accidentally reasserting the enable after eight cycles.

Reset timing matters. Because reset is synchronous, asserting it between clock edges does not immediately modify count or the output. The next rising edge loads zero, after which the output is high and the four-cycle window starts again. No explicit else count <= count assignment is needed in clocked logic: when no branch assigns the register, the flip-flops retain their previous value.

**Cycle trace:** reset edge→0/high, then successive edges produce 1/high, 2/high, 3/high, 4/low, followed by 4/low indefinitely until another reset edge.

### Saved Verilog solution

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

---

<a id="problem-151"></a>
## 151 — Getting Started

[Problem note](problems/Day%2009/151-step_one.md) · [Question screenshot](images/Day%2009/151-step_one.png) · [Successful solution screenshot](images/Day%2009/151-step_one-solution.png) · [Verilog file](solutions/Day%2009/151-step_one.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/step_one)

<a href="images/Day%2009/151-step_one.png"><img src="images/Day%2009/151-step_one.png" alt="Getting Started problem statement and success timestamp" width="100%"></a>

<a href="images/Day%2009/151-step_one-solution.png"><img src="images/Day%2009/151-step_one-solution.png" alt="Getting Started successful submitted solution" width="100%"></a>

### What the question is asking

This introductory circuit has no inputs and continuously drives output `one` high. The saved solution uses `assign one = 1'b1;`, which synthesizes as a constant tie-high connection with no state or procedural logic.

The logged-in HDLBits page confirms one successful attempt at 9:12:14 PM with no failed attempts.

---

<a id="problem-152"></a>
## 152 — Output Zero

[Problem note](problems/Day%2009/152-zero.md) · [Screenshot](images/Day%2009/152-zero.png) · [Verilog file](solutions/Day%2009/152-zero.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/zero)

<a href="images/Day%2009/152-zero.png"><img src="images/Day%2009/152-zero.png" alt="Output Zero successful submitted solution" width="100%"></a>

### What the question is asking

This circuit continuously drives output `zero` low using `assign zero = 1'b0;`. It reinforces that constant hardware connections are valid combinational logic and do not require an `always` block.

The logged-in HDLBits page confirms one successful attempt at 9:12:38 PM with no failed attempts.

---

<a id="problem-153"></a>
## 153 — FSM: The complete FSM

[Problem note](problems/Day%2009/153-exams__review2015_fsm.md) · [Open screenshot at full resolution](images/Day%2009/153-exams__review2015_fsm-question-and-successful-submission.png) · [Verilog file](solutions/Day%2009/153-exams__review2015_fsm.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/review2015_fsm)

<a href="images/Day%2009/153-exams__review2015_fsm-question-and-successful-submission.png"><img src="images/Day%2009/153-exams__review2015_fsm-question-and-successful-submission.png" alt="Complete FSM question and loaded successful submission" width="100%"></a>

### What the question is asking

This ten-state Moore FSM combines sequence recognition, a four-cycle shift-enable window, a counter-wait phase, and an acknowledgment phase. `S`, `S1`, `S11`, and `S110` search for `1101`; `B0` through `B3` assert `shift_ena`; `COUNT` asserts `counting` until `done_counting`; and `WAIT` asserts `done` until `ack`.

The live record confirms the last successful submission at 10:20:45 PM: 2 successes, 5 incorrect attempts, and 1 compile error across 8 attempts.

### Saved Verilog solution

The editable implementation is in [153-exams__review2015_fsm.sv](solutions/Day%2009/153-exams__review2015_fsm.sv).

---

<a id="problem-154"></a>
## 154 — The complete timer

[Problem note with wrong-attempt discussion](problems/Day%2009/154-exams__review2015_fancytimer.md) · [Open successful-submission screenshot](images/Day%2009/154-exams__review2015_fancytimer-question-and-successful-submission.png) · [Verilog file](solutions/Day%2009/154-exams__review2015_fancytimer.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/review2015_fancytimer)

<a href="images/Day%2009/154-exams__review2015_fancytimer-question-and-successful-submission.png"><img src="images/Day%2009/154-exams__review2015_fancytimer-question-and-successful-submission.png" alt="Complete timer question and loaded successful submission" width="100%"></a>

### What the question is asking

The final timer adds the datapath to the complete FSM. After recognizing `1101`, it shifts in four delay bits, then displays and decrements that delay once per 1000 clock cycles. It finishes only after zero has also been displayed for 1000 cycles, giving exactly `(delay+1)×1000` counting clocks.

The implementation keeps three concerns separate: next-state logic chooses the phase, `delay` captures serial bits, `count_remaining` performs the visible down-count, and a ten-bit modulo-1000 counter measures each interval. This separation fixes the wrong attempt, which wrote stored datapath values inside combinational next-state logic.

All five screenshots are embedded and explained in the [problem-specific note](problems/Day%2009/154-exams__review2015_fancytimer.md#wrong-attempt-and-why-it-failed). They document the original code structure, the duplicated shift expression, and the nonblocking-assignment old-value trap. The live record confirms the last successful submission at 11:38:15 PM with two successful attempts and no failures.

### Saved Verilog solution

The editable implementation is in [154-exams__review2015_fancytimer.sv](solutions/Day%2009/154-exams__review2015_fancytimer.sv).
