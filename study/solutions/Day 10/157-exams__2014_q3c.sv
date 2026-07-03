module top_module (
    input clk,
    input [2:0] y,
    input x,
    output Y0,
    output z
);
    assign Y0 = (~x & (y[0] | y[2])) |
                ( x & ~y[0] & ~y[2]);
    assign z = (y == 3'b011) || (y == 3'b100);
endmodule
