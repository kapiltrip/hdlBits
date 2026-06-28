module top_module (
    input clk,
    input a,
    output [3:0] q
);
    reg [3:0] count;

    always @(posedge clk) begin
        if (!a) begin
            if (count == 4'b0110)
                count <= 4'b0000;
            else
                count <= count + 1'b1;
        end else begin
            count <= 4'b0100;
        end
    end

    assign q = count;

endmodule
