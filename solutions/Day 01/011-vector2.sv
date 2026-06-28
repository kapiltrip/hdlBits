module top_module(
    input [31:0] in,
    output [31:0] out );//

    // assign out[31:24] = ...;
    wire [7:0] a,b,c,d;
    assign a=in[31:24];//msb
    assign b=in[23:16];
    assign c=in[15:8];
    assign d=in[7:0];
   assign  out ={d,c,b,a};
endmodule
