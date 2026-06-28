// Verification-only models for helper modules supplied by HDLBits.
module andgate(output out, input a, input b, input c, input d, input e);
    assign out = a & b & c & d & e;
endmodule

module mux2(input sel, input [7:0] a, input [7:0] b, output [7:0] out);
    assign out = sel ? b : a;
endmodule

module mod_a(output out1, output out2, input a, input b, input c, input d);
    assign out1 = a;
    assign out2 = b;
endmodule

module my_dff(input clk, input d, output reg q);
    always @(posedge clk)
        q <= d;
endmodule

module add16(input [15:0] a, input [15:0] b, input cin, output cout, output [15:0] sum);
    assign {cout, sum} = a + b + cin;
endmodule

module bcd_fadd(input [3:0] a, input [3:0] b, input cin, output cout, output [3:0] sum);
    wire [4:0] value = a + b + cin;
    assign cout = value > 9;
    assign sum = cout ? value - 10 : value[3:0];
endmodule
