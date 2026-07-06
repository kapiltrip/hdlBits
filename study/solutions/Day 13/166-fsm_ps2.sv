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
