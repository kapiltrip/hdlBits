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
