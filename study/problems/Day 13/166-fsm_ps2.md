# 166 — PS/2 packet parser

| Field | Value |
|---|---|
| Day | Day 13 |
| Last successful submission | 2026-07-06 2:56:49 PM |
| HDLBits ID | `fsm_ps2` |
| Attempts | 11 total: 3 successes, 6 incorrect, 2 compile errors, 0 simulation errors |
| Success rate | 27% |
| Source | [HDLBits](https://hdlbits.01xz.net/wiki/fsm_ps2) |
| Files | [Screenshot](../../images/Day%2013/166-fsm_ps2-question-and-successful-submission.png) · [Verilog](../../solutions/Day%2013/166-fsm_ps2.sv) |

![PS/2 packet parser complete question and loaded successful submission](../../images/Day%2013/166-fsm_ps2-question-and-successful-submission.png)

## Design reasoning

The parser receives one byte per clock. Only byte 1 has a recognizable marker (`in[3]==1`). After detecting it, the next two bytes belong to the same packet regardless of their bit 3 values. The done state checks the current byte for a new packet marker, preserving back-to-back packets without a wasted cycle.

## Saved successful solution

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

## Points to remember

- The input width tells you the sampling unit: this problem receives bytes, not serial bits.
- Detect only byte 1; byte 2 and byte 3 are positional.
- Evaluate the done-cycle input to support adjacent packets.
