# Day 05 — 2026-06-27

Completed problems: **7**

Each screenshot is embedded at the full width of the GitHub page. Select an image to open its original-resolution file.

## Index

| # | Time | Problem | Section | Problem note | Solution | Source |
|---:|---|---:|---|---|---|---|
| 1 | 12:13:30 AM | [108](#problem-108) | Sequential Logic | [Shift register](problems/Day%2005/108-exams__2014_q4b.md) | [Code](solutions/Day%2005/108-exams__2014_q4b.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/exams/2014_q4b) |
| 2 | 12:36:42 AM | [109](#problem-109) | Sequential Logic | [3-input LUT](problems/Day%2005/109-exams__ece241_2013_q12.md) | [Code](solutions/Day%2005/109-exams__ece241_2013_q12.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/exams/ece241_2013_q12) |
| 3 | 1:04:37 AM | [110](#problem-110) | Sequential Logic | [Simple FSM 1 (asynchronous reset)](problems/Day%2005/110-fsm1.md) | [Code](solutions/Day%2005/110-fsm1.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/fsm1) |
| 4 | 1:25:24 AM | [111](#problem-111) | Sequential Logic | [Simple FSM 1 (synchronous reset)](problems/Day%2005/111-fsm1s.md) | [Code](solutions/Day%2005/111-fsm1s.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/fsm1s) |
| 5 | 1:59:48 AM | [112](#problem-112) | Sequential Logic | [Simple FSM 2 (asynchronous reset)](problems/Day%2005/112-fsm2.md) | [Code](solutions/Day%2005/112-fsm2.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/fsm2) |
| 6 | 2:04:20 AM | [113](#problem-113) | Sequential Logic | [Simple FSM 2 (synchronous reset)](problems/Day%2005/113-fsm2s.md) | [Code](solutions/Day%2005/113-fsm2s.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/fsm2s) |
| 7 | 2:15:08 AM | [114](#problem-114) | Sequential Logic | [Simple state transitions 3](problems/Day%2005/114-fsm3comb.md) | [Code](solutions/Day%2005/114-fsm3comb.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/fsm3comb) |

---

<a id="problem-108"></a>
## 108 — Shift register

[Problem note](problems/Day%2005/108-exams__2014_q4b.md) · [Open screenshot at full resolution](images/Day%2005/108-exams__2014_q4b.png) · [Verilog file](solutions/Day%2005/108-exams__2014_q4b.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/2014_q4b)

<a href="images/Day%2005/108-exams__2014_q4b.png"><img src="images/Day%2005/108-exams__2014_q4b.png" alt="Shift register question and submitted solution" width="100%"></a>

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

[Problem note](problems/Day%2005/109-exams__ece241_2013_q12.md) · [Open screenshot at full resolution](images/Day%2005/109-exams__ece241_2013_q12.png) · [Verilog file](solutions/Day%2005/109-exams__ece241_2013_q12.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/ece241_2013_q12)

<a href="images/Day%2005/109-exams__ece241_2013_q12.png"><img src="images/Day%2005/109-exams__ece241_2013_q12.png" alt="3-input LUT question and submitted solution" width="100%"></a>

### What the question is asking

Build a 3-input lookup table from a shift register and multiplexer so its truth table can be loaded serially.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input enable,
    input S,
    input A, B, C,
    output Z
);
//8 bit shift register
    reg [7:0] Q;
    always @(posedge clk)begin
        //S is the input to the shift, reg
        if(enable)begin
            Q[0]<=S;
            Q[7:1]=Q[6:0];
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

[Problem note](problems/Day%2005/110-fsm1.md) · [Open screenshot at full resolution](images/Day%2005/110-fsm1.png) · [Verilog file](solutions/Day%2005/110-fsm1.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/fsm1)

<a href="images/Day%2005/110-fsm1.png"><img src="images/Day%2005/110-fsm1.png" alt="Simple FSM 1 (asynchronous reset) question and submitted solution" width="100%"></a>

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

[Problem note](problems/Day%2005/111-fsm1s.md) · [Open screenshot at full resolution](images/Day%2005/111-fsm1s.png) · [Verilog file](solutions/Day%2005/111-fsm1s.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/fsm1s)

<a href="images/Day%2005/111-fsm1s.png"><img src="images/Day%2005/111-fsm1s.png" alt="Simple FSM 1 (synchronous reset) question and submitted solution" width="100%"></a>

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

[Problem note](problems/Day%2005/112-fsm2.md) · [Open screenshot at full resolution](images/Day%2005/112-fsm2.png) · [Verilog file](solutions/Day%2005/112-fsm2.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/fsm2)

<a href="images/Day%2005/112-fsm2.png"><img src="images/Day%2005/112-fsm2.png" alt="Simple FSM 2 (asynchronous reset) question and submitted solution" width="100%"></a>

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

[Problem note](problems/Day%2005/113-fsm2s.md) · [Open screenshot at full resolution](images/Day%2005/113-fsm2s.png) · [Verilog file](solutions/Day%2005/113-fsm2s.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/fsm2s)

<a href="images/Day%2005/113-fsm2s.png"><img src="images/Day%2005/113-fsm2s.png" alt="Simple FSM 2 (synchronous reset) question and submitted solution" width="100%"></a>

### What the question is asking

Implement the second FSM with a synchronous reset while preserving the transition and output behaviour.

### Saved Verilog solution

```verilog
module top_module(
    input clk,
    input reset,    // Synchronous reset to OFF
    input j,
    input k,
    output out); //

    parameter OFF=0, ON=1;
    reg state, next_state;

    always @(*) begin
        // State transition logic
    end

    always @(posedge clk) begin
        // State flip-flops with synchronous reset
    end

    // Output logic
    // assign out = (state == ...);

endmodule
```

---

<a id="problem-114"></a>
## 114 — Simple state transitions 3

[Problem note](problems/Day%2005/114-fsm3comb.md) · [Open screenshot at full resolution](images/Day%2005/114-fsm3comb.png) · [Verilog file](solutions/Day%2005/114-fsm3comb.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/fsm3comb)

<a href="images/Day%2005/114-fsm3comb.png"><img src="images/Day%2005/114-fsm3comb.png" alt="Simple state transitions 3 question and submitted solution" width="100%"></a>

### What the question is asking

Write only the combinational next-state logic for the supplied state-transition diagram.

### Saved Verilog solution

```verilog
module top_module(
    input in,
    input [1:0] state,
    output [1:0] next_state,
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
