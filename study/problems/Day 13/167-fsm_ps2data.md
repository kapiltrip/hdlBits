# 167 — PS/2 packet parser and datapath

| Field | Value |
|---|---|
| Day | Day 13 |
| Last successful submission | 2026-07-06 3:28:06 PM |
| HDLBits ID | `fsm_ps2data` |
| Attempts | 8 total: 1 success, 7 incorrect, 0 compile errors, 0 simulation errors |
| Success rate | 13% |
| Source | [HDLBits](https://hdlbits.01xz.net/wiki/fsm_ps2data) |
| Files | [Screenshot](../../images/Day%2013/167-fsm_ps2data-question-and-successful-submission.png) · [Verilog](../../solutions/Day%2013/167-fsm_ps2data.sv) · [Mistake log](../../Mistakes.md#19-ps2-datapath-count-bytes-not-bits) |

![PS/2 packet parser and datapath complete question and loaded successful submission](../../images/Day%2013/167-fsm_ps2data-question-and-successful-submission.png)

## Design reasoning

Control and datapath advance together: `start` captures byte 1, the two `sample` cycles capture bytes 2 and 3, and `donee` exposes the assembled 24-bit packet. Whole-byte part-selects are mandatory because a scalar indexed bit cannot accept an eight-bit input.

## Saved successful solution

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

## Points to remember

- `vector[index]` selects one bit; use `[high:low]` for a byte.
- Capture byte 1 in the search state on the same edge that recognizes it.
- Do not discard the input present during the done cycle.
