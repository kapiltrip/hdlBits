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
