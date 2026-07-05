# Day 05 — 2026-06-27

Completed problems: **12**

Each screenshot is embedded at the full width of the GitHub page. Select an image to open its original-resolution file.

## Index

| # | Time | Problem | Section | Problem note | Page contents | Source |
|---:|---|---:|---|---|---|---|
| 1 | 12:13:30 AM | [108](#problem-108) | Sequential Logic | [Shift register](problems/Day%2005/108-exams__2014_q4b.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/2014_q4b) |
| 2 | 12:36:42 AM | [109](#problem-109) | Sequential Logic | [3-input LUT](problems/Day%2005/109-exams__ece241_2013_q12.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/ece241_2013_q12) |
| 3 | 1:04:37 AM | [110](#problem-110) | Sequential Logic | [Simple FSM 1 (asynchronous reset)](problems/Day%2005/110-fsm1.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/fsm1) |
| 4 | 1:25:24 AM | [111](#problem-111) | Sequential Logic | [Simple FSM 1 (synchronous reset)](problems/Day%2005/111-fsm1s.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/fsm1s) |
| 5 | 1:59:48 AM | [112](#problem-112) | Sequential Logic | [Simple FSM 2 (asynchronous reset)](problems/Day%2005/112-fsm2.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/fsm2) |
| 6 | 2:04:20 AM | [113](#problem-113) | Sequential Logic | [Simple FSM 2 (synchronous reset)](problems/Day%2005/113-fsm2s.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/fsm2s) |
| 7 | 2:15:08 AM | [114](#problem-114) | Sequential Logic | [Simple state transitions 3](problems/Day%2005/114-fsm3comb.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/fsm3comb) |
| 8 | 4:45:28 PM | [115](#problem-115) | Sequential Logic | [Simple one-hot state transitions 3](problems/Day%2005/115-fsm3onehot.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/fsm3onehot) |
| 9 | 5:05:31 PM | [116](#problem-116) | Sequential Logic | [Simple FSM 3 (asynchronous reset)](problems/Day%2005/116-fsm3.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/fsm3) |
| 10 | 5:07:35 PM | [117](#problem-117) | Sequential Logic | [Simple FSM 3 (synchronous reset)](problems/Day%2005/117-fsm3s.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/fsm3s) |
| 11 | 11:58:25 PM | [118](#problem-118) | Sequential Logic | [Design a Moore FSM](problems/Day%2005/118-exams__ece241_2013_q4.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/ece241_2013_q4) |
| 12 | 6:32:59 PM | [119](#problem-119) | Sequential Logic | [Lemmings 1](problems/Day%2005/119-lemmings1.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/lemmings1) |

---

<a id="problem-108"></a>
## 108 — Shift register

[Problem note](problems/Day%2005/108-exams__2014_q4b.md) · [Verilog file](solutions/Day%2005/108-exams__2014_q4b.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/2014_q4b)

![Shift register question and submitted solution](images/Day%2005/108-exams__2014_q4b.png)

### What the question is asking

Implement the shown shift register and its control logic exactly as specified by the exam circuit.

### Saved Verilog solution

```verilog
module top_module (
    input [3:0] SW,
    input [3:0] KEY,
    output [3:0] LEDR
);

    MUXDFF mux3 (
        .clk(KEY[0]),
        .w(KEY[3]),
        .R(SW[3]),
        .E(KEY[1]),
        .L(KEY[2]),
        .Q(LEDR[3])
    );

    MUXDFF mux2 (
        .clk(KEY[0]),
        .w(LEDR[3]),
        .R(SW[2]),
        .E(KEY[1]),
        .L(KEY[2]),
        .Q(LEDR[2])
    );

    MUXDFF mux1 (
        .clk(KEY[0]),
        .w(LEDR[2]),
        .R(SW[1]),
        .E(KEY[1]),
        .L(KEY[2]),
        .Q(LEDR[1])
    );

    MUXDFF mux0 (
        .clk(KEY[0]),
        .w(LEDR[1]),
        .R(SW[0]),
        .E(KEY[1]),
        .L(KEY[2]),
        .Q(LEDR[0])
    );

endmodule


module MUXDFF (
    input clk,
    input w, R, E, L,
    output reg Q
);

    always @(posedge clk) begin
        Q <= (L) ? R : (E) ? w : Q;
    end

endmodule
```

---

<a id="problem-109"></a>
## 109 — 3-input LUT

[Problem note](problems/Day%2005/109-exams__ece241_2013_q12.md) · [Verilog file](solutions/Day%2005/109-exams__ece241_2013_q12.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/ece241_2013_q12)

![3-input LUT question and submitted solution](images/Day%2005/109-exams__ece241_2013_q12.png)

### What the question is asking

Build a 3-input lookup table from a shift register and multiplexer so its truth table can be loaded serially.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input enable,
    input S,
    input A, B, C,
    output reg Z
);
//8 bit shift register
    reg [7:0] Q;
    always @(posedge clk)begin
        //S is the input to the shift, reg
        if(enable)begin
            Q[0]<=S;
            Q[7:1]<=Q[6:0];
        end
    end
    always @(*)begin
        case({A,B,C})
            3'b000:Z=Q[0];
            3'b001:Z=Q[1];
            3'b010:Z=Q[2];
            3'b011:Z=Q[3];
            3'b100:Z=Q[4];
            3'b101:Z=Q[5];
            3'b110:Z=Q[6];
            3'b111:Z=Q[7];
        endcase
    end
endmodule
```

---

<a id="problem-110"></a>
## 110 — Simple FSM 1 (asynchronous reset)

[Problem note](problems/Day%2005/110-fsm1.md) · [Verilog file](solutions/Day%2005/110-fsm1.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/fsm1)

![Simple FSM 1 (asynchronous reset) question and submitted solution](images/Day%2005/110-fsm1.png)

### What the question is asking

Implement the provided two-state FSM, using an asynchronous reset and the diagram's transition and output rules.

### Saved Verilog solution

```verilog
module top_module(
    input clk,
    input areset,    // Asynchronous reset to state B
    input in,
    output out
);//

    parameter A=0, B=1;
    reg state, next_state;

    always @(*) begin    // This is a combinational always block
        next_state=state;
        case (state)
            A:next_state=(in)?A:B;
            B:next_state=(in)?B:A;
        endcase
    end

    always @(posedge clk, posedge areset) begin    // This is a sequential always block
        // State flip-flops with asynchronous reset
        if(areset)
            state<=A;
        else
            state <=next_state;
    end

    // Output logic
    // assign out = (state == ...);
    assign out = (state == A);
endmodule
```

---

<a id="problem-111"></a>
## 111 — Simple FSM 1 (synchronous reset)

[Problem note](problems/Day%2005/111-fsm1s.md) · [Verilog file](solutions/Day%2005/111-fsm1s.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/fsm1s)

![Simple FSM 1 (synchronous reset) question and submitted solution](images/Day%2005/111-fsm1s.png)

### What the question is asking

Implement the same two-state FSM with a synchronous reset instead of an asynchronous reset.

### Saved Verilog solution

```verilog
module top_module(clk, reset, in, out);
    input clk;
    input reset;    // Synchronous reset to state B
    input in;
    output out;

    reg present_state, next_state;

    parameter A = 1'b0;
    parameter B = 1'b1;

    // State transition logic
    always @(*) begin
        case (present_state)
            A: next_state = in ? A : B;
            B: next_state = in ? B : A;
            default: next_state = B;
        endcase
    end

    // State flip-flop
    always @(posedge clk) begin
        if (reset)
            present_state <= B;
        else
            present_state <= next_state;
    end

    // Output logic
    assign out = (present_state == B);

endmodule
```

---

<a id="problem-112"></a>
## 112 — Simple FSM 2 (asynchronous reset)

[Problem note](problems/Day%2005/112-fsm2.md) · [Verilog file](solutions/Day%2005/112-fsm2.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/fsm2)

![Simple FSM 2 (asynchronous reset) question and submitted solution](images/Day%2005/112-fsm2.png)

### What the question is asking

Implement the second supplied finite-state machine, including its asynchronous reset, transitions, and output decoding.

### Saved Verilog solution

```verilog
module top_module(
    input clk,
    input areset,    // Asynchronous reset to OFF
    input j,
    input k,
    output out); //

    parameter OFF=0, ON=1;
    reg state, next_state;

    always @(*) begin
        // State transition logic
        next_state=state;
        case (state)
            OFF:next_state=(j)?ON:OFF;
            ON:next_state=(k)?OFF:ON;
        endcase
    end

    always @(posedge clk, posedge areset) begin
        // State flip-flops with asynchronous reset
        if(areset)begin
            state<=OFF;

        end else begin
            state<=next_state ;
        end
    end

    // Output logic
    // assign out = (state == ...);
    assign out = (state == ON);
endmodule
```

---

<a id="problem-113"></a>
## 113 — Simple FSM 2 (synchronous reset)

[Problem note](problems/Day%2005/113-fsm2s.md) · [Verilog file](solutions/Day%2005/113-fsm2s.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/fsm2s)

![Simple FSM 2 (synchronous reset) question and submitted solution](images/Day%2005/113-fsm2s.png)

### What the question is asking

Implement the second FSM with a synchronous reset while preserving the transition and output behaviour.

### Saved Verilog solution

```verilog
module top_module(
    input clk,
    input reset, // Synchronous reset to OFF
    input j,
    input k,
    output out
);

    parameter OFF = 1'b0;
    parameter ON  = 1'b1;

    reg state, next_state;

    always @(*) begin
        case (state)
            ON:      next_state = k ? OFF : ON;
            OFF:     next_state = j ? ON : OFF;
            default: next_state = OFF;
        endcase
    end

    always @(posedge clk) begin
        if (reset)
            state <= OFF;
        else
            state <= next_state;
    end

    assign out = (state == ON);
endmodule
```

---

<a id="problem-114"></a>
## 114 — Simple state transitions 3

[Problem note](problems/Day%2005/114-fsm3comb.md) · [Verilog file](solutions/Day%2005/114-fsm3comb.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/fsm3comb)

![Simple state transitions 3 question and submitted solution](images/Day%2005/114-fsm3comb.png)

### What the question is asking

Write only the combinational next-state logic for the supplied state-transition diagram.

### Saved Verilog solution

```verilog
module top_module(
    input in,
    input [1:0] state,
    output reg [1:0] next_state,
    output out
); //

    parameter A=0, B=1, C=2, D=3;

    // State transition logic: next_state = f(state, in)

    // Output logic:  out = f(state) for a Moore state machine
    always @(*)begin
        next_state=state;
        case (state)
            A:next_state=(in)?B:A;
            B:next_state=(in)?B:C;
            C:next_state=(in)?D:A;
            D:next_state=(in)?B:C;
        endcase
    end
    assign out = (state==D);
endmodule
```

---

<a id="problem-115"></a>
## 115 — Simple one-hot state transitions 3

[Problem note](problems/Day%2005/115-fsm3onehot.md) · [Verilog file](solutions/Day%2005/115-fsm3onehot.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/fsm3onehot)

![Simple one-hot state transitions 3 question and submitted solution](images/Day%2005/115-fsm3onehot.png)

### What the question is asking

This problem gives the four-state Moore machine as a transition table, but supplies the current state as a one-hot vector instead of asking for a state register. The implementation therefore derives each bit of `next_state` from the incoming transitions to that state.

For example, state A is reached from A or C only when `in=0`, so `next_state[A] = ~in & (state[A] | state[C])`. State B is reached from A, B, or D when `in=1`; C is reached from B or D when `in=0`; and D is reached only from C when `in=1`. The Moore output is high only in D, so it is simply `state[D]`.

**Why the direct equations matter:** HDLBits deliberately supplies non-one-hot test vectors. A `case` statement that assumes exactly one active state, or logic that forces illegal states back to A, would implement different behaviour. The sum-of-products equations preserve every simultaneously active incoming term.

**Trace example:** with `state=4'b0100` (C), `in=1` asserts only `next_state[D]`; with the same state and `in=0`, only `next_state[A]` is asserted.

### Saved Verilog solution

```verilog
module top_module(
    input in,
    input [3:0] state,
    output [3:0] next_state,
    output out
);

    parameter A = 0, B = 1, C = 2, D = 3;

    // State transition logic: derive an equation for each state flip-flop.
    assign next_state[A] = ~in & (state[A] | state[C]);
    assign next_state[B] = in & (state[A] | state[B] | state[D]);
    assign next_state[C] = ~in & (state[B] | state[D]);
    assign next_state[D] = in & state[C];

    assign out = state[D];

endmodule
```

---

<a id="problem-116"></a>
## 116 — Simple FSM 3 (asynchronous reset)

[Problem note](problems/Day%2005/116-fsm3.md) · [Verilog file](solutions/Day%2005/116-fsm3.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/fsm3)

![Simple FSM 3 (asynchronous reset) question and submitted solution](images/Day%2005/116-fsm3.png)

### What the question is asking

This is the complete four-state Moore FSM whose combinational transition table was implemented in the preceding exercises. The design separates three concerns: combinational next-state decoding, the clocked state register, and Moore output decoding.

The transition logic implements A: 0→A/1→B, B: 0→C/1→B, C: 0→A/1→D, and D: 0→C/1→B. A default assignment of `next_state = state` prevents an unintended latch and gives a safe hold value before the `case` overrides it.

The reset is **asynchronous** because `areset` appears in the event control: `always @(posedge clk or posedge areset)`. As soon as reset rises, the state becomes A without waiting for a clock. Ordinary transitions still occur only at a rising clock edge. Since this is a Moore machine, `out` depends only on the registered state and is asserted exactly in D.

**Revision pitfall:** putting reset only inside `always @(posedge clk)` would silently change this into the synchronous-reset version.

### Saved Verilog solution

```verilog
module top_module(
    input clk,
    input in,
    input areset,
    output out
);

    parameter A = 2'b00;
    parameter B = 2'b01;
    parameter C = 2'b10;
    parameter D = 2'b11;
    reg [1:0] state, next_state;

    always @(*) begin
        next_state = state;
        case (state)
            A: next_state = in ? B : A;
            B: next_state = in ? B : C;
            C: next_state = in ? D : A;
            D: next_state = in ? B : C;
        endcase
    end

    always @(posedge clk or posedge areset) begin
        if (areset)
            state <= A;
        else
            state <= next_state;
    end

    assign out = (state == D);

endmodule
```

---

<a id="problem-117"></a>
## 117 — Simple FSM 3 (synchronous reset)

[Problem note](problems/Day%2005/117-fsm3s.md) · [Verilog file](solutions/Day%2005/117-fsm3s.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/fsm3s)

![Simple FSM 3 (synchronous reset) question and submitted solution](images/Day%2005/117-fsm3s.png)

### What the question is asking

This exercise uses the same A/B/C/D transition graph and Moore output as `fsm3`, but changes the reset timing. The transition decoder still computes A: 0→A/1→B, B: 0→C/1→B, C: 0→A/1→D, and D: 0→C/1→B, while `out` is high only when the registered state is D.

The state register is sensitive only to `posedge clk`. Consequently, asserting `reset` between edges does not immediately change the state; reset is sampled at the next rising edge and then loads A. This is the defining behaviour of a synchronous reset.

**Cycle trace:** if the machine is in D and reset rises halfway through a cycle, `out` remains high until the next rising clock edge. At that edge state becomes A and `out` falls. In the asynchronous version, state and output would change as soon as reset rose.

**Revision pitfall:** the comment in the submitted starter code mentions an asynchronous reset, but the actual problem and sensitivity list require synchronous reset. The event control, not the comment, determines the hardware.

### Saved Verilog solution

```verilog
module top_module(
    input clk,
    input in,
    input reset,
    output out
);

    parameter A = 2'b00;
    parameter B = 2'b01;
    parameter C = 2'b10;
    parameter D = 2'b11;
    reg [1:0] state, next_state;

    always @(*) begin
        next_state = state;
        case (state)
            A: next_state = in ? B : A;
            B: next_state = in ? B : C;
            C: next_state = in ? D : A;
            D: next_state = in ? B : C;
        endcase
    end

    always @(posedge clk) begin
        if (reset)
            state <= A;
        else
            state <= next_state;
    end

    assign out = (state == D);

endmodule
```

---

<a id="problem-118"></a>
## 118 — Design a Moore FSM

[Problem note](problems/Day%2005/118-exams__ece241_2013_q4.md) · [Verilog file](solutions/Day%2005/118-exams__ece241_2013_q4.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/ece241_2013_q4)

![Design a Moore FSM question and submitted solution](images/Day%2005/118-exams__ece241_2013_q4.png)

### What the question is asking

This problem is more than a water-level decoder: the outputs depend on both the current sensor pattern and whether the water level was rising or falling. That history requirement makes it a Moore FSM rather than pure combinational logic.

Sensors `s[1]`, `s[2]`, and `s[3]` represent progressively higher levels. The six encoded states distinguish below-sensor-1, between sensors 1–2 while rising or falling, between sensors 2–3 while rising or falling, and above sensor 3. The next-state priority checks the highest asserted sensor first, which maps any valid thermometer-like sensor pattern to the appropriate level band.

The output vector is `{fr3, fr2, fr1, dfr}`. More fill valves are enabled at lower levels. The direction-sensitive `dfr` bit is clear while the level is rising and set while it is falling, preserving the required hysteresis. At the lowest state all four outputs are asserted; above the highest sensor all are clear.

Reset is active-high and synchronous, loading the below-sensor-1 state. The explicit default state and default output also recover deterministically from an unused 3-bit encoding.

**Key lesson:** whenever identical input values require different outputs depending on the path taken to reach them, the path must be stored as state.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,
    input [3:1] s,
    output reg fr3,
    output reg fr2,
    output reg fr1,
    output reg dfr
);
    reg [2:0] state, next_state;

    parameter belows1 = 3'd0;
    parameter s3s2fall = 3'd1;
    parameter s3s2rise = 3'd2;
    parameter s2s1fall = 3'd3;
    parameter s2s1rise = 3'd4;
    parameter s3above = 3'd5;

    always @(posedge clk) begin
        if (reset)
            state <= belows1;
        else
            state <= next_state;
    end

    always @(*) begin
        next_state = state;
        case (state)
            belows1: begin
                if (s[3])
                    next_state = s3above;
                else if (s[2])
                    next_state = s3s2rise;
                else if (s[1])
                    next_state = s2s1rise;
                else
                    next_state = belows1;
            end
            s2s1rise: begin
                if (s[3])
                    next_state = s3above;
                else if (s[2])
                    next_state = s3s2rise;
                else if (s[1])
                    next_state = s2s1rise;
                else
                    next_state = belows1;
            end
            s2s1fall: begin
                if (s[3])
                    next_state = s3above;
                else if (s[2])
                    next_state = s3s2rise;
                else if (s[1])
                    next_state = s2s1fall;
                else
                    next_state = belows1;
            end
            s3s2rise: begin
                if (s[3])
                    next_state = s3above;
                else if (s[2])
                    next_state = s3s2rise;
                else if (s[1])
                    next_state = s2s1fall;
                else
                    next_state = belows1;
            end
            s3s2fall: begin
                if (s[3])
                    next_state = s3above;
                else if (s[2])
                    next_state = s3s2fall;
                else if (s[1])
                    next_state = s2s1fall;
                else
                    next_state = belows1;
            end
            s3above: begin
                if (s[3])
                    next_state = s3above;
                else if (s[2])
                    next_state = s3s2fall;
                else if (s[1])
                    next_state = s2s1fall;
                else
                    next_state = belows1;
            end
            default: next_state = belows1;
        endcase
    end

    always @(*) begin
        case (state)
            belows1: {fr3, fr2, fr1, dfr} = 4'b1111;
            s2s1rise: {fr3, fr2, fr1, dfr} = 4'b0110;
            s2s1fall: {fr3, fr2, fr1, dfr} = 4'b0111;
            s3s2rise: {fr3, fr2, fr1, dfr} = 4'b0010;
            s3s2fall: {fr3, fr2, fr1, dfr} = 4'b0011;
            s3above: {fr3, fr2, fr1, dfr} = 4'b0000;
            default: {fr3, fr2, fr1, dfr} = 4'b1111;
        endcase
    end

endmodule
```

---

<a id="problem-119"></a>
## 119 — Lemmings 1

[Problem note](problems/Day%2005/119-lemmings1.md) · [Verilog file](solutions/Day%2005/119-lemmings1.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/lemmings1)

![Lemmings 1 question and submitted solution](images/Day%2005/119-lemmings1.png)

### What the question is asking

The Lemming has only two Moore states: walking left and walking right. Direction changes occur only when an obstacle is encountered on the side toward which it is currently walking.

In LEFT, `bump_left=1` sends the FSM to RIGHT; otherwise it stays LEFT. In RIGHT, `bump_right=1` sends it to LEFT; otherwise it stays RIGHT. If both bump inputs are high, the relevant condition for either current state is high, so the machine still reverses direction exactly once.

The asynchronous reset is implemented with `posedge areset` in the event control and immediately places the Lemming in LEFT. The two outputs are Moore decodes: `walk_left` is high only in LEFT and `walk_right` only in RIGHT, so they are mutually exclusive for every legal state.

**Trace example:** LEFT + right-side bump only remains LEFT because an obstacle behind the Lemming does not matter. LEFT + left-side bump changes the registered state to RIGHT at the next clock edge.

### Saved Verilog solution

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
