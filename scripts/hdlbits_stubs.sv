// Verification-only models for helper modules supplied by HDLBits.
`ifdef HDL_STUB_ANDGATE5
module andgate(output out, input a, input b, input c, input d, input e);
    assign out = a & b & c & d & e;
endmodule
`endif

`ifdef HDL_STUB_ANDGATE2
module andgate(input [1:0] in, output out);
    assign out = &in;
endmodule
`endif

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

module dut(input clk);
endmodule

module q7(input clk, input in, input [2:0] s, output out);
    assign out = in ^ ^s;
endmodule

module tff(input clk, input reset, input t, output reg q);
    always @(posedge clk) begin
        if (reset)
            q <= 1'b0;
        else if (t)
            q <= ~q;
    end
endmodule
