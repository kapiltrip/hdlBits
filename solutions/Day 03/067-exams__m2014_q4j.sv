module top_module (
    input [3:0] x,
    input [3:0] y, 
    output [4:0] sum
);
//4 bit addition 
    wire [4:0] carry;
    assign carry[0]=0;
    
    genvar i;
    generate
        for(i=0;i<4;i=i+1)begin : generating
            fa fullAdders(
                .a(x[i]),
                .b(y[i]),
                .cin(carry[i]),
                .sum(sum[i]),
                .cout(carry[i+1])
            );
        end
    endgenerate
    assign sum[4]= carry[4];
endmodule
module fa(
    input wire a,b,cin,
    output wire cout, sum
);
    assign sum= a^b^cin;
    assign cout = a&b | b&cin | a &cin ;
    
endmodule
