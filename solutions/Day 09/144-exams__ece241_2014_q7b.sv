module top_module (
    input clk,
    input reset,
    output OneHertz,
    output [2:0] c_enable
);
    reg [3:0] msb, middle, lsb;

    assign c_enable[0] = 1'b1;
    assign c_enable[1] = (lsb == 4'd9);
    assign c_enable[2] = (lsb == 4'd9) && (middle == 4'd9);

    bcdcount counter0 (clk, reset, c_enable[0], lsb);
    bcdcount counter1 (clk, reset, c_enable[1], middle);
    bcdcount counter2 (clk, reset, c_enable[2], msb);

    assign OneHertz = (msb == 4'd9) && (middle == 4'd9) && (lsb == 4'd9);
endmodule
