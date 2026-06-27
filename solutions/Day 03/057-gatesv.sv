module top_module( 
    input [3:0] in,
    output [2:0] out_both,
    output [3:1] out_any,
    output [3:0] out_different 
);
    assign out_both= in[3:1] & in[2:0]; // out_both[2] should indicate if in[2] and in[3] are both 1
    assign out_any= in[3:1] | in[2:0];//out_any[2] should indicate if either in[2] or in[1] are 1
    assign out_different= in^ {in[0],in[3:1]};//out_different[2] should indicate if in[2] is different from in[3] , msb and lsb are neighbours
endmodule
