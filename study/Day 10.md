# Day 10 — 2026-07-03

Completed FSM problems: **4**. Every entry has a full-page HDLBits capture containing the question, complete submitted answer, and visible `Status: Success!` result. The original handwritten, partial-attempt, and ChatGPT discussion images remain beside the matching problem for revision.

## Index

| # | Problem | Page contents | Detailed note | Source |
|---:|---|---|---|---|
| 155 | [Q3a: FSM](#155--q3a-fsm) | Screenshot + code rendered below | [Counter/FSM discussion](problems/Day%2010/155-exams__2014_q3fsm.md) | [HDLBits](https://hdlbits.01xz.net/wiki/exams/2014_q3fsm) |
| 156 | [Q3b: FSM](#156--q3b-fsm) | Screenshot + code rendered below | [Complete state-machine note](problems/Day%2010/156-exams__2014_q3bfsm.md) | [HDLBits](https://hdlbits.01xz.net/wiki/exams/2014_q3bfsm) |
| 157 | [Q3c: FSM logic](#157--q3c-fsm-logic) | Screenshot + code rendered below | [Handwritten derivation and correction](problems/Day%2010/157-exams__2014_q3c.md) | [HDLBits](https://hdlbits.01xz.net/wiki/exams/2014_q3c) |
| 158 | [Q6c: FSM one-hot next-state logic](#158--q6c-fsm-one-hot-next-state-logic) | Screenshot + code rendered below | [Incoming-arrow derivation](problems/Day%2010/158-exams__m2014_q6c.md) | [HDLBits](https://hdlbits.01xz.net/wiki/exams/m2014_q6c) |

## 155 — Q3a: FSM

This complete primary capture includes the question, submitted answer, and successful result. Supporting working-attempt and discussion images remain in the [problem note](problems/Day%2010/155-exams__2014_q3fsm.md).

![Q3a FSM complete question, submitted answer, and success result](images/Day%2010/155-exams__2014_q3fsm-question-and-answer.png)

### Saved Verilog solution

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

## 156 — Q3b: FSM

![Q3b FSM complete question, submitted answer, and success result](images/Day%2010/156-exams__2014_q3bfsm-question-and-answer.png)

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,
    input x,
    output z
);
    localparam S0 = 3'd0, S1 = 3'd1, S2 = 3'd2,
               S3 = 3'd3, S4 = 3'd4;
    reg [2:0] state, next_state;

    always @(posedge clk) begin
        if (reset)
            state <= S0;
        else
            state <= next_state;
    end

    always @(*) begin
        case (state)
            S0: next_state = x ? S1 : S0;
            S1: next_state = x ? S4 : S1;
            S2: next_state = x ? S1 : S2;
            S3: next_state = x ? S2 : S1;
            S4: next_state = x ? S4 : S3;
            default: next_state = S0;
        endcase
    end

    assign z = (state == S3) || (state == S4);
endmodule
```

## 157 — Q3c: FSM logic

This is the complete primary capture. The handwritten derivation and earlier attempt are rendered separately in the [problem note](problems/Day%2010/157-exams__2014_q3c.md) as supporting close-ups.

![Q3c FSM logic complete question, submitted answer, and success result](images/Day%2010/157-exams__2014_q3c-question-and-answer.png)

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input [2:0] y,
    input x,
    output Y0,
    output z
);
    assign Y0 = (~x & (y[0] | y[2])) |
                ( x & ~y[0] & ~y[2]);
    assign z = (y == 3'b011) || (y == 3'b100);
endmodule
```

## 158 — Q6c: FSM one-hot next-state logic

![Q6c FSM one-hot logic complete question, submitted answer, and success result](images/Day%2010/158-exams__m2014_q6c-question-and-answer.png)

### Saved Verilog solution

```verilog
module top_module (
    input [6:1] y,
    input w,
    output Y2,
    output Y4
);
    assign Y2 = y[1] & ~w;
    assign Y4 = w & (y[2] | y[3] | y[5] | y[6]);
endmodule
```

## Revision priorities

- Distinguish phase state from counters and other datapath registers.
- Separate the state register, next-state logic, and Moore output decode.
- Derive a requested next-state bit from the selected bit of each table entry.
- For one-hot equations, OR together the enabled incoming transitions.
- Treat a full question + submitted answer + success result as the required screenshot boundary.
