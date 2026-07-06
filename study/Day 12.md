# Day 12 — 2026-07-05

Four FSM problems were completed. The live HDLBits pages supplied the successful-submission timestamps and loaded answers used below.

## Index

| # | Problem | Result | Submitted |
|---:|---|---|---|
| 161 | [Lemmings 4](#161--lemmings-4) | Completed | 1:10:55 PM |
| 162 | [One-hot FSM](#162--one-hot-fsm) | Completed | 5:09:39 PM |
| 163 | [Serial receiver](#163--serial-receiver) | Completed | 11:29:35 PM |
| 164 | [Serial receiver and datapath](#164--serial-receiver-and-datapath) | Completed | 11:48:46 PM |

## 161 — Lemmings 4

[Problem note](problems/Day%2012/161-lemmings4.md) · [HDLBits](https://hdlbits.01xz.net/wiki/lemmings4)

![Lemmings 4 complete question and loaded successful submission](images/Day%2012/161-lemmings4-question-and-successful-submission.png)

This version adds terminal splatter after a fall longer than 20 clock cycles. The counter is datapath memory: the FSM controls whether the Lemming is falling, while `willCount` measures the duration. Landing checks the stored duration and either resumes walking or enters the absorbing `splatter` state.

```verilog
module top_module(
    input clk,
    input areset,
    input bump_left,
    input bump_right,
    input ground,
    input dig,
    output walk_left,
    output walk_right,
    output aaah,
    output digging
);

    reg [3:0] state, next_state;
    parameter left             = 4'b0000;
    parameter right            = 4'b0001;
    parameter fallRight        = 4'b0010;
    parameter fallLeft         = 4'b0011;
    parameter digWorkFromLeft  = 4'b0100;
    parameter digWorkFromRight = 4'b0101;
    parameter digWorkFallRight = 4'b0110;
    parameter digWorkFallLeft  = 4'b0111;
    parameter splatter         = 4'b1000;

    reg [4:0] willCount;

    always @(*) begin
        case (state)
            left: begin
                if (!ground)
                    next_state = fallLeft;
                else if (dig && ground)
                    next_state = digWorkFromLeft;
                else if (bump_right && bump_left)
                    next_state = right;
                else if (bump_left)
                    next_state = right;
                else
                    next_state = left;
            end
            right: begin
                if (!ground)
                    next_state = fallRight;
                else if (dig && ground)
                    next_state = digWorkFromRight;
                else if (bump_right && bump_left)
                    next_state = left;
                else if (bump_right)
                    next_state = left;
                else
                    next_state = right;
            end
            fallRight: begin
                if (!ground)
                    next_state = fallRight;
                else if (willCount >= 5'd20)
                    next_state = splatter;
                else
                    next_state = right;
            end
            fallLeft: begin
                if (!ground)
                    next_state = fallLeft;
                else if (willCount >= 5'd20)
                    next_state = splatter;
                else
                    next_state = left;
            end
            digWorkFromLeft:
                next_state = ground ? digWorkFromLeft : digWorkFallLeft;
            digWorkFromRight:
                next_state = ground ? digWorkFromRight : digWorkFallRight;
            digWorkFallLeft:
                next_state = ground ? left : digWorkFallLeft;
            digWorkFallRight:
                next_state = ground ? right : digWorkFallRight;
            splatter: next_state = splatter;
            default: next_state = left;
        endcase
    end

    always @(posedge clk or posedge areset) begin
        if (areset)
            state <= left;
        else
            state <= next_state;
    end

    always @(posedge clk or posedge areset) begin
        if (areset)
            willCount <= 5'd0;
        else if (state == fallLeft || state == fallRight) begin
            if (willCount == 5'd21)
                willCount <= willCount;
            else
                willCount <= willCount + 5'd1;
        end
        else
            willCount <= 5'd0;
    end

    assign walk_left  = (state == left);
    assign walk_right = (state == right);
    assign aaah = (state == digWorkFallLeft) ||
                  (state == digWorkFallRight) ||
                  (state == fallRight) ||
                  (state == fallLeft);
    assign digging = (state == digWorkFromLeft) ||
                     (state == digWorkFromRight);

endmodule
```

## 162 — One-hot FSM

[Problem note](problems/Day%2012/162-fsm_onehot.md) · [HDLBits](https://hdlbits.01xz.net/wiki/fsm_onehot)

![One-hot FSM complete question and loaded successful submission](images/Day%2012/162-fsm_onehot-question-and-successful-submission.png)

The earlier attempt redeclared the supplied ten-bit state interface as four-bit registers. The successful design keeps `state[9:0]` as an input and derives each `next_state` bit from the arrows entering that destination. There is no state-register block because HDLBits asks only for transition and output logic.

```verilog
module top_module(
    input in,
    input [9:0] state,
    output [9:0] next_state,
    output out1,
    output out2
);

    wire S0 = state[0];
    wire S1 = state[1];
    wire S2 = state[2];
    wire S3 = state[3];
    wire S4 = state[4];
    wire S5 = state[5];
    wire S6 = state[6];
    wire S7 = state[7];
    wire S8 = state[8];
    wire S9 = state[9];

    assign next_state[0] = ~in & (S0 | S1 | S2 | S3 | S4 | S7 | S8 | S9);
    assign next_state[1] =  in & (S0 | S8 | S9);
    assign next_state[2] =  in & S1;
    assign next_state[3] =  in & S2;
    assign next_state[4] =  in & S3;
    assign next_state[5] =  in & S4;
    assign next_state[6] =  in & S5;
    assign next_state[7] =  in & (S6 | S7);
    assign next_state[8] = ~in & S5;
    assign next_state[9] = ~in & S6;

    assign out1 = S8 | S9;
    assign out2 = S7 | S9;

endmodule
```

## 163 — Serial receiver

[Problem note](problems/Day%2012/163-fsm_serial.md) · [HDLBits](https://hdlbits.01xz.net/wiki/fsm_serial)

![Serial receiver complete question and loaded successful submission](images/Day%2012/163-fsm_serial-question-and-successful-submission.png)

The controller waits for a low start bit, counts eight data clocks, validates a high stop bit, and pulses `done`. A bad stop bit enters `error` and waits for the line to return high before searching for another frame.

```verilog
module top_module(
    input clk,
    input in,
    input reset,
    output done
);

    reg [2:0] state, next_state;
    reg [2:0] count;

    parameter idle      = 3'b000;
    parameter data      = 3'b001;
    parameter stop      = 3'b010;
    parameter completed = 3'b011;
    parameter error     = 3'b100;

    always @(posedge clk) begin
        if (reset) begin
            count <= 3'b000;
            state <= idle;
        end
        else begin
            state <= next_state;
            if (state == data) begin
                if (count == 3'd7)
                    count <= 3'd0;
                else
                    count <= count + 3'd1;
            end
            else
                count <= 3'd0;
        end
    end

    always @(*) begin
        case (state)
            idle: next_state = in ? idle : data;
            data: next_state = (count == 3'd7) ? stop : data;
            stop: next_state = in ? completed : error;
            completed: next_state = !in ? data : idle;
            error: next_state = in ? idle : error;
            default: next_state = idle;
        endcase
    end

    assign done = (state == completed);

endmodule
```

## 164 — Serial receiver and datapath

[Problem note](problems/Day%2012/164-fsm_serialdata.md) · [HDLBits](https://hdlbits.01xz.net/wiki/fsm_serialdata)

![Serial receiver and datapath complete question and loaded successful submission](images/Day%2012/164-fsm_serialdata-question-and-successful-submission.png)

The FSM is the same serial-frame controller, while the datapath writes each least-significant-bit-first input into `latch[count]`. The earlier mismatch where the reference pulsed `done` but the design did not was a control-cycle alignment problem at the data-to-stop-to-completed boundary.

```verilog
module top_module(
    input clk,
    input in,
    input reset,
    output [7:0] out_byte,
    output done
);

    reg [7:0] latch;
    reg [2:0] state, next_state;
    reg [3:0] count;

    parameter idle      = 3'b000;
    parameter data      = 3'b001;
    parameter stop      = 3'b010;
    parameter completed = 3'b011;
    parameter error     = 3'b100;

    always @(posedge clk) begin
        if (reset) begin
            count <= 3'b000;
            state <= idle;
        end
        else begin
            state <= next_state;
            if (state == data) begin
                latch[count] <= in;
                if (count == 4'd8)
                    count <= 3'd0;
                else
                    count <= count + 3'd1;
            end
            else
                count <= 3'd0;
        end
    end

    always @(*) begin
        case (state)
            idle: next_state = in ? idle : data;
            data: next_state = (count == 3'd7) ? stop : data;
            stop: next_state = in ? completed : error;
            completed: next_state = !in ? data : idle;
            error: next_state = in ? idle : error;
            default: next_state = idle;
        endcase
    end

    assign done = (state == completed);
    assign out_byte = latch;

endmodule
```

## Remaining after Day 12

Fifteen questions remained: 14 not started and the unresolved `exams/2013_q2afsm` review item.
