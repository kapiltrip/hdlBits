# Day 13 — 2026-07-06

Completed problems: **10**

Each screenshot is rendered directly in this page for revision. The image is not wrapped in a click-only link.

## Index

| # | Time | Problem | Section | Problem note | Page contents | Source |
|---:|---|---:|---|---|---|---|
| 1 | 1:59:50 PM | [165](#problem-165) | Sequential Logic | [Serial receiver with parity checking](problems/Day%2013/165-fsm_serialdp.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/fsm_serialdp) |
| 2 | 2:56:49 PM | [166](#problem-166) | Sequential Logic | [PS/2 packet parser](problems/Day%2013/166-fsm_ps2.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/fsm_ps2) |
| 3 | 3:28:06 PM | [167](#problem-167) | Sequential Logic | [PS/2 packet parser and datapath](problems/Day%2013/167-fsm_ps2data.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/fsm_ps2data) |
| 4 | 4:21:20 PM | [168](#problem-168) | Sequential Logic | [Sequence recognition](problems/Day%2013/168-fsm_hdlc.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/fsm_hdlc) |
| 5 | 6:24:56 PM | [169](#problem-169) | Sequential Logic | [Q5a: Serial two's complementer (Moore FSM)](problems/Day%2013/169-exams__ece241_2014_q5a.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q5a) |
| 6 | 6:50:12 PM | [170](#problem-170) | Sequential Logic | [Q5b: Serial two's complementer (Mealy FSM)](problems/Day%2013/170-exams__ece241_2014_q5b.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q5b) |
| 7 | 9:53:56 PM | [171](#problem-171) | Sequential Logic | [Q6b: FSM next-state logic](problems/Day%2013/171-exams__m2014_q6b.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/m2014_q6b) |
| 8 | 10:01:46 PM | [172](#problem-172) | Sequential Logic | [Q6: FSM](problems/Day%2013/172-exams__m2014_q6.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/m2014_q6) |
| 9 | 10:06:12 PM | [173](#problem-173) | Sequential Logic | [Q2a: FSM](problems/Day%2013/173-exams__2012_q2fsm.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/2012_q2fsm) |
| 10 | 10:38:05 PM | [174](#problem-174) | Sequential Logic | [Q2b: One-hot FSM equations](problems/Day%2013/174-exams__2012_q2b.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/2012_q2b) |

---

<a id="problem-165"></a>
## 165 — Serial receiver with parity checking

[Problem note](problems/Day%2013/165-fsm_serialdp.md) · [Verilog file](solutions/Day%2013/165-fsm_serialdp.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/fsm_serialdp)

![Serial receiver with parity checking question and submitted solution](images/Day%2013/165-fsm_serialdp-question-and-successful-submission.png)

### What the question is asking

Parity checking adds a distinct parity phase after the eight data cycles and before stop validation. The parity accumulator is cleared when a new frame begins, XORs each data bit, and then XORs the received parity bit. For odd parity, the accumulated result must be one; the frame is accepted only when that condition and a high stop bit are both satisfied. The earlier attempts mixed the parity bit with either data bit seven or the stop bit, producing a one-cycle boundary error. A dedicated parity state, explicit counter limit, and frame-local reset make every sampled symbol unambiguous and prevent parity from leaking between consecutive frames.

### Saved Verilog solution

```verilog
module top_module(
    input clk,
    input in,
    input reset,
    output [7:0] out_byte,
    output done
);

    reg [7:0] latch;
    reg parityReg;
    reg [2:0] state, next_state;
    reg [3:0] count;

    parameter idle      = 3'b000;
    parameter data      = 3'b001;
    parameter parity    = 3'b010;
    parameter stop      = 3'b011;
    parameter completed = 3'b100;
    parameter error     = 3'b101;

    always @(posedge clk) begin
        if (reset) begin
            count <= 3'b000;
            state <= idle;
            latch <= 8'd0;
            parityReg <= 1'b0;
        end
        else begin
            state <= next_state;
            if (state == data) begin
                latch[count] <= in;
                parityReg <= parityReg ^ in;
                if (count == 4'd8)
                    count <= 3'd0;
                else
                    count <= count + 3'd1;
            end
            else if (state == parity) begin
                parityReg = parityReg ^ in;
                count <= 3'd0;
            end
            else begin
                count <= 3'd0;
                if (state == completed || state == idle || state == error)
                    parityReg <= 1'b0;
            end
        end
    end

    always @(*) begin
        case (state)
            idle: next_state = in ? idle : data;
            data: next_state = (count == 3'd7) ? parity : data;
            parity: next_state = stop;
            stop: begin
                if (in)
                    next_state = parityReg ? completed : idle;
                else
                    next_state = error;
            end
            completed: next_state = !in ? data : idle;
            error: next_state = in ? idle : error;
            default: next_state = idle;
        endcase
    end

    assign done = (state == completed);
    assign out_byte = latch;

endmodule
```

---

<a id="problem-166"></a>
## 166 — PS/2 packet parser

[Problem note](problems/Day%2013/166-fsm_ps2.md) · [Verilog file](solutions/Day%2013/166-fsm_ps2.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/fsm_ps2)

![PS/2 packet parser question and submitted solution](images/Day%2013/166-fsm_ps2-question-and-successful-submission.png)

### What the question is asking

The PS/2 parser receives one complete byte per clock. In the search state, only in[3] identifies a legal first byte; once found, the next two bytes are consumed positionally regardless of their contents. The third byte produces a one-cycle done indication. A subtle back-to-back case occurs because the input present during the done cycle may already be the first byte of the next packet, so the transition out of done must test in[3] instead of blindly returning to search. Earlier attempts treated the input like a serial bit stream or discarded the done-cycle byte. The corrected four-state controller models byte positions directly and preserves throughput.

### Saved Verilog solution

```verilog
module top_module(
    input clk,
    input [7:0] in,
    input reset,
    output done
);

    reg [1:0] state, next_state;
    reg [1:0] count;

    parameter start  = 2'b00;
    parameter sample = 2'b01;
    parameter donee  = 2'b10;

    always @(posedge clk) begin
        if (reset) begin
            state <= start;
            count <= 2'b00;
        end
        else begin
            state <= next_state;
            if (state == sample) begin
                if (count == 2'b01)
                    count <= 2'b00;
                else
                    count <= count + 2'b01;
            end
            else
                count <= 2'b00;
        end
    end

    always @(*) begin
        case (state)
            start:  next_state = in[3] ? sample : start;
            sample: next_state = (count == 2'b01) ? donee : sample;
            donee:  next_state = in[3] ? sample : start;
            default: next_state = start;
        endcase
    end

    assign done = (state == donee);

endmodule
```

---

<a id="problem-167"></a>
## 167 — PS/2 packet parser and datapath

[Problem note](problems/Day%2013/167-fsm_ps2data.md) · [Verilog file](solutions/Day%2013/167-fsm_ps2data.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/fsm_ps2data)

![PS/2 packet parser and datapath question and submitted solution](images/Day%2013/167-fsm_ps2data-question-and-successful-submission.png)

### What the question is asking

The datapath stores each incoming eight-bit value into a fixed slice of the 24-bit packet: byte one in out_bytes[23:16], byte two in [15:8], and byte three in [7:0]. A scalar index selects one bit, so using an index where a whole-byte part-select was required caused the original data corruption. Control state determines which slice is written, and the byte recognized during the done cycle must also be captured as a possible byte one of the next packet. This keeps the data path aligned with the parser during back-to-back traffic. The completed packet remains stable for the done pulse, while subsequent writes replace slices only at their proper positions.

### Saved Verilog solution

```verilog
module top_module(
    input clk,
    input [7:0] in,
    input reset,
    output [23:0] out_bytes,
    output done
);

    reg [1:0] state, next_state;
    reg [1:0] count;
    reg [23:0] latching;

    parameter start  = 2'b00;
    parameter sample = 2'b01;
    parameter donee  = 2'b10;

    always @(posedge clk) begin
        if (reset) begin
            state <= start;
            count <= 2'b00;
            latching <= 24'd0;
        end
        else begin
            state <= next_state;
            case (state)
                start: begin
                    if (in[3])
                        latching[23:16] <= in;
                end
                sample: begin
                    if (count == 2'b00) begin
                        latching[15:8] <= in;
                        count <= 2'b01;
                    end
                    else begin
                        latching[7:0] <= in;
                        count <= 2'b00;
                    end
                end
                donee: begin
                    count <= 2'b00;
                    if (in[3])
                        latching[23:16] <= in;
                end
                default: count <= 2'b00;
            endcase
        end
    end

    always @(*) begin
        case (state)
            start:  next_state = in[3] ? sample : start;
            sample: next_state = (count == 2'b01) ? donee : sample;
            donee:  next_state = in[3] ? sample : start;
            default: next_state = start;
        endcase
    end

    assign done = (state == donee);
    assign out_bytes = done ? latching : 24'd0;

endmodule
```

---

<a id="problem-168"></a>
## 168 — Sequence recognition

[Problem note](problems/Day%2013/168-fsm_hdlc.md) · [Verilog file](solutions/Day%2013/168-fsm_hdlc.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/fsm_hdlc)

![Sequence recognition question and submitted solution](images/Day%2013/168-fsm_hdlc-question-and-successful-submission.png)

### What the question is asking

Prefix states encode the exact run length of consecutive ones, which turns each output condition into a precise transition. A zero after five ones is a discard event, a zero after six ones is a flag event, and the seventh consecutive one is an error event. Any earlier zero resets the run to zero, while longer one runs remain in the error region until a zero restarts recognition. The failed solution asserted outputs from a state representing the previous count, so pulses appeared one clock early. The corrected transition/output alignment evaluates the symbol that completes each pattern, producing single-cycle discard, flag, and error indications at the required boundary.

### Saved Verilog solution

```verilog
module top_module(
    input clk,
    input reset,
    input in,
    output disc,
    output flag,
    output err
);

    reg [3:0] state, next_state;

    parameter s0    = 4'b0000;
    parameter s1    = 4'b0001;
    parameter s2    = 4'b0010;
    parameter s3    = 4'b0011;
    parameter s4    = 4'b0100;
    parameter s5    = 4'b0101;
    parameter s6    = 4'b0110;
    parameter discc = 4'b0111;
    parameter flagg = 4'b1000;
    parameter errr  = 4'b1001;

    always @(posedge clk) begin
        if (reset)
            state <= s0;
        else
            state <= next_state;
    end

    always @(*) begin
        case (state)
            s0:    next_state = in ? s1 : s0;
            s1:    next_state = in ? s2 : s0;
            s2:    next_state = in ? s3 : s0;
            s3:    next_state = in ? s4 : s0;
            s4:    next_state = in ? s5 : s0;
            s5:    next_state = in ? s6 : discc;
            discc: next_state = in ? s1 : s0;
            s6:    next_state = in ? errr : flagg;
            flagg: next_state = in ? s1 : s0;
            errr:  next_state = in ? errr : s0;
            default: next_state = s0;
        endcase
    end

    assign disc = (state == discc);
    assign flag = (state == flagg);
    assign err  = (state == errr);

endmodule
```

---

<a id="problem-169"></a>
## 169 — Q5a: Serial two's complementer (Moore FSM)

[Problem note](problems/Day%2013/169-exams__ece241_2014_q5a.md) · [Verilog file](solutions/Day%2013/169-exams__ece241_2014_q5a.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q5a)

![Q5a: Serial two's complementer (Moore FSM) question and submitted solution](images/Day%2013/169-exams__ece241_2014_q5a-question-and-successful-submission.png)

### What the question is asking

A serial two's-complementer copies input bits from least significant to most significant until it encounters the first 1. That first 1 is copied unchanged; every later bit is inverted. The Moore implementation stores whether the first 1 has already appeared. In the COPY state, output z is 0 and input 0 keeps the machine in COPY, while input 1 moves it to INVERT. In INVERT, z is the complement of the current input and the state remains there for the rest of the word.

Because a Moore output depends only on registered state, the transition cycle must be designed carefully: the first 1 is produced while the machine is still in COPY, so z must equal the required copied value on that boundary. Reset synchronously returns to COPY for the start of a new number. The key verification cases are all-zero input, a word whose least-significant bit is 1, and long leading runs of zeros before the first 1.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input areset,
    input x,
    output z
);
    reg [1:0] state, next_state;
    parameter s0 = 2'b00;
    parameter s1 = 2'b01;
    parameter s2 = 2'b10;

    always @(posedge clk or posedge areset) begin
        if (areset)
            state <= s0;
        else
            state <= next_state;
    end

    always @(*) begin
        case (state)
            s0: next_state = x ? s1 : s0;
            s1: next_state = x ? s2 : s1;
            s2: next_state = x ? s2 : s1;
            default: next_state = s0;
        endcase
    end

    assign z = (state == s1);
endmodule
```

---

<a id="problem-170"></a>
## 170 — Q5b: Serial two's complementer (Mealy FSM)

[Problem note](problems/Day%2013/170-exams__ece241_2014_q5b.md) · [Verilog file](solutions/Day%2013/170-exams__ece241_2014_q5b.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q5b)

![Q5b: Serial two's complementer (Mealy FSM) question and submitted solution](images/Day%2013/170-exams__ece241_2014_q5b-question-and-successful-submission.png)

### What the question is asking

The Mealy version implements the same least-significant-bit-first two's-complement algorithm with only two states. Before the first 1, output z follows x directly: zeros remain zero and the first 1 remains one. Once that 1 is observed, the FSM enters the INVERT state and every later output is NOT x. Since z depends on both present state and current input, the first 1 can be emitted correctly on the same cycle that causes the state transition.

This is the central Moore-versus-Mealy distinction in the paired exam questions. State records only the historical fact that the first 1 has occurred; it does not store the data word. Synchronous reset clears that history between words. A useful trace is x=0,0,1,0,1: z=0,0,1,1,0. Combinational defaults and a recovery branch keep next-state and output fully assigned for every encoding.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input areset,
    input x,
    output z
);
    reg zr;
    reg [1:0] state, next_state;
    parameter s0 = 2'b00;
    parameter s1 = 2'b01;

    always @(posedge clk or posedge areset) begin
        if (areset)
            state <= s0;
        else
            state <= next_state;
    end

    always @(*) begin
        case (state)
            s0: begin
                if (x) begin
                    next_state = s1;
                    zr = x;
                end
                else begin
                    next_state = s0;
                    zr = 1'b0;
                end
            end
            s1: begin
                next_state = s1;
                zr = ~x;
            end
            default: begin
                next_state = s0;
                zr = 1'b0;
            end
        endcase
    end

    assign z = zr;
endmodule
```

---

<a id="problem-171"></a>
## 171 — Q6b: FSM next-state logic

[Problem note](problems/Day%2013/171-exams__m2014_q6b.md) · [Verilog file](solutions/Day%2013/171-exams__m2014_q6b.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/m2014_q6b)

![Q6b: FSM next-state logic question and submitted solution](images/Day%2013/171-exams__m2014_q6b-question-and-successful-submission.png)

### What the question is asking

This problem asks only for the combinational next-state equation for state Y. The transition diagram must be read as incoming arcs to Y, not as every arc leaving the current state. Each product term combines a present-state condition with the input value that enables its transition, and the terms are ORed because any one incoming arc is sufficient to assert Y on the next clock.

No state register is required: the supplied state bits already represent the present state, and the output is the Boolean equation for the requested destination bit. The safest derivation method is to list every arrow whose head is Y, write one AND term per arrow, then OR those terms and simplify only after the unsimplified equation has been checked. This avoids the common errors of reversing arrow direction, omitting a self-loop, or applying priority where the diagram defines parallel sum-of-products logic.

### Saved Verilog solution

```verilog
module top_module (
    input [3:1] y,
    input w,
    output Y2
);
    assign Y2 = ((~y[2] & y[1]) | (w & y[3]) | (w & y[2] & ~y[1]));
endmodule
```

---

<a id="problem-172"></a>
## 172 — Q6: FSM

[Problem note](problems/Day%2013/172-exams__m2014_q6.md) · [Verilog file](solutions/Day%2013/172-exams__m2014_q6.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/m2014_q6)

![Q6: FSM question and submitted solution](images/Day%2013/172-exams__m2014_q6-question-and-successful-submission.png)

### What the question is asking

This complete FSM separates registered state, combinational transition logic, and output decoding. The transition table is translated literally so each legal state defines its next state for both input values. A synchronous reset loads the specified initial state at the next rising edge, while ordinary state changes also occur only on rising edges. The output is decoded from the registered present state, so its timing follows the Moore interpretation shown in the problem.

The default transition returns the machine to a safe legal state if an unused binary encoding appears. That is useful both for simulation determinism and hardware recovery. Verification should include both branches from every state, the reset edge, and at least one path that reaches the output-asserting state. Keeping the three responsibilities in separate blocks makes it clear that combinational logic cannot accidentally infer storage and that reset timing is not confused with asynchronous behavior.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,
    input w,
    output z
);
    reg [2:0] state, next_state;
    parameter A = 3'b000;
    parameter B = 3'b001;
    parameter C = 3'b010;
    parameter D = 3'b011;
    parameter E = 3'b100;
    parameter F = 3'b101;

    always @(posedge clk) begin
        if (reset)
            state <= A;
        else
            state <= next_state;
    end

    always @(*) begin
        case (state)
            A: next_state = w ? A : B;
            B: next_state = w ? D : C;
            C: next_state = w ? D : E;
            D: next_state = w ? A : F;
            E: next_state = w ? D : E;
            F: next_state = w ? D : C;
            default: next_state = A;
        endcase
    end

    assign z = (state == E) || (state == F);
endmodule
```

---

<a id="problem-173"></a>
## 173 — Q2a: FSM

[Problem note](problems/Day%2013/173-exams__2012_q2fsm.md) · [Verilog file](solutions/Day%2013/173-exams__2012_q2fsm.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/2012_q2fsm)

![Q2a: FSM question and submitted solution](images/Day%2013/173-exams__2012_q2fsm-question-and-successful-submission.png)

### What the question is asking

The state diagram is implemented as a conventional Moore machine. Each named state represents the history needed to decide future transitions, the combinational case statement selects the next state from the current state and input, and a clocked register advances the machine once per rising edge. The output is decoded only from the registered state, so it changes after the transition into an output-producing state rather than directly with the input.

Reset is handled with the timing required by the prompt and returns the controller to its initial state. A default branch provides deterministic recovery from unused encodings. The most reliable way to validate this design is to trace one row at a time from the diagram: record current state, input, expected destination, then compare the code. Finally trace a complete input sequence through reset, state transitions, and output timing to catch a one-cycle shift between transition recognition and Moore output assertion.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,
    input w,
    output z
);
    reg [2:0] state, next_state;
    parameter A = 3'b000;
    parameter B = 3'b001;
    parameter C = 3'b010;
    parameter D = 3'b011;
    parameter E = 3'b100;
    parameter F = 3'b101;

    always @(posedge clk) begin
        if (reset)
            state <= A;
        else
            state <= next_state;
    end

    always @(*) begin
        case (state)
            A: next_state = w ? B : A;
            B: next_state = w ? C : D;
            C: next_state = w ? E : D;
            D: next_state = w ? F : A;
            E: next_state = w ? E : D;
            F: next_state = w ? C : D;
            default: next_state = A;
        endcase
    end

    assign z = (state == E) || (state == F);
endmodule
```

---

<a id="problem-174"></a>
## 174 — Q2b: One-hot FSM equations

[Problem note](problems/Day%2013/174-exams__2012_q2b.md) · [Verilog file](solutions/Day%2013/174-exams__2012_q2b.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/2012_q2b)

![Q2b: One-hot FSM equations question and submitted solution](images/Day%2013/174-exams__2012_q2b-question-and-successful-submission.png)

### What the question is asking

The current state is supplied as a one-hot vector, so the task is pure combinational next-state and output logic. For each destination bit, collect every transition entering that state. An incoming transition contributes current_state[source] AND its input condition; ORing all such terms produces the destination's next-state equation. The output is a direct decode of whichever present-state bits are marked as output-producing in the diagram.

Direct equations are preferable to a priority case because they preserve the Boolean behavior even if a test vector contains zero or multiple asserted state bits. There is no internal register and the clock input is therefore intentionally unused. The essential checks are that every diagram arrow appears exactly once in an incoming equation, input polarities match the arrow labels, self-loops are included, and next_state is driven in full on every combinational evaluation.

### Saved Verilog solution

```verilog
module top_module (
    input [5:0] y,
    input w,
    output Y1,
    output Y3
);
    assign Y3 = ~w & (y[1] | y[2] | y[4] | y[5]);
    assign Y1 = w & y[0];
endmodule
```
