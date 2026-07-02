module top_module (
    input clk,
    input shift_ena,
    input count_ena,
    input data,
    output [3:0] q
);
    reg [3:0] shift_count;

    always @(posedge clk) begin
        if (shift_ena)
            shift_count <= {shift_count[2:0], data};
        if (count_ena) begin
            if (shift_count == 4'd0)
                shift_count <= 4'd15;
            else
                shift_count <= shift_count - 4'd1;
        end
    end

    assign q = shift_count;
endmodule
