# 163 — Serial receiver

| Field | Value |
|---|---|
| Day | Day 12 |
| Last successful submission | 2026-07-05 11:29:35 PM |
| HDLBits ID | `fsm_serial` |
| Attempts | 16 total: 2 successes, 12 incorrect, 2 compile errors, 0 simulation errors |
| Success rate | 13% |
| Source | [HDLBits](https://hdlbits.01xz.net/wiki/fsm_serial) |
| Files | [Screenshot](../../images/Day%2012/163-fsm_serial-question-and-successful-submission.png) · [Verilog](../../solutions/Day%2012/163-fsm_serial.sv) |

![Serial receiver complete question and loaded successful submission](../../images/Day%2012/163-fsm_serial-question-and-successful-submission.png)

## Design reasoning

Idle is logic 1. A low input starts the frame; exactly eight data clocks follow; then the stop bit must be high. `completed` provides the one-cycle `done` pulse. If the stop bit is low, `error` waits until the line returns high so the middle of a malformed frame cannot be mistaken for a new start.

## Saved successful solution

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

## Points to remember

- Count the eight data cycles, not the start or stop bit.
- A malformed stop bit needs an explicit recovery state.
- Back-to-back frames can begin during the cycle after `done`.
