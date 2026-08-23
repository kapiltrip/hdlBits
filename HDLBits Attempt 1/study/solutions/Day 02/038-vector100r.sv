module top_module(
    input [99:0] in,
    output [99:0] out
);
//to reverse the bit ordering
genvar i ;

    generate
        for(i=0;i<100;i=i+1)begin : reversingBits
               assign out[i]=in[99-i];
             end
    endgenerate
endmodule
