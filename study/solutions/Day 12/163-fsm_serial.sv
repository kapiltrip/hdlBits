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
