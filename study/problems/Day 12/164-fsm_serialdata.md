# 164 — Serial receiver and datapath

| Field | Value |
|---|---|
| Day | Day 12 |
| Last successful submission | 2026-07-05 11:48:46 PM |
| HDLBits ID | `fsm_serialdata` |
| Attempts | 11 total: 1 success, 8 incorrect, 2 compile errors, 0 simulation errors |
| Success rate | 9% |
| Source | [HDLBits](https://hdlbits.01xz.net/wiki/fsm_serialdata) |
| Files | [Screenshot](../../images/Day%2012/164-fsm_serialdata-question-and-successful-submission.png) · [Verilog](../../solutions/Day%2012/164-fsm_serialdata.sv) · [Mistake log](../../Mistakes.md#17-serial-receiver-datapath-align-done-stop-validation-and-byte-capture) |

![Serial receiver and datapath complete question and loaded successful submission](../../images/Day%2012/164-fsm_serialdata-question-and-successful-submission.png)

## Design reasoning

The control FSM determines which cycles are data; the datapath uses the same counter as a bit index. Since the protocol is LSB-first, assigning `latch[count] <= in` stores the stream directly in natural bit positions. `out_byte` is only semantically required when `done` is high.

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

## Points to remember

- Separate frame control from byte storage.
- Align `done` with the registered completed state.
- Debug the first mismatching cycle before inspecting later waveform differences.
