# 165 — Serial receiver with parity checking

| Field | Value |
|---|---|
| Day | Day 13 |
| Last successful submission | 2026-07-06 1:59:50 PM |
| HDLBits ID | `fsm_serialdp` |
| Attempts | 7 total: 2 successes, 4 incorrect, 1 compile error, 0 simulation errors |
| Success rate | 29% |
| Source | [HDLBits](https://hdlbits.01xz.net/wiki/fsm_serialdp) |
| Files | [Screenshot](../../images/Day%2013/165-fsm_serialdp-question-and-successful-submission.png) · [Verilog](../../solutions/Day%2013/165-fsm_serialdp.sv) · [Mistake log](../../Mistakes.md#18-serial-parity-reset-per-frame-and-check-the-post-bit-value) |

![Serial receiver with parity complete question and loaded successful submission](../../images/Day%2013/165-fsm_serialdp-question-and-successful-submission.png)

## Design reasoning

The controller adds a parity state between the eighth data bit and the stop bit. The parity accumulator XORs each data bit and then the parity bit. For odd parity, a valid frame reaches the stop state with `parityReg==1`; `done` is asserted only when both parity and stop-bit checks pass.

## Saved successful solution

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

## Points to remember

- Reset parity once per frame, not once per bit.
- Include the parity bit in the XOR accumulation.
- Validate parity and stop-bit conditions before pulsing `done`.
