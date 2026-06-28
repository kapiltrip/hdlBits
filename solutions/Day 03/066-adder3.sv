module top_module(
    input [2:0] a, b,
    input cin,
    output [2:0] cout,
    output [2:0] sum
);
//4 bit addition
    wire [3:0] carry;
    assign carry[0]=cin;

    genvar i;
    generate
        for(i=0;i<3;i=i+1)begin : generating
            fa fullAdders(
                .a(a[i]),
                .b(b[i]),
                .cin(carry[i]),
                .sum(sum[i]),
                .cout(carry[i+1])
            );
        end
    endgenerate
    assign cout=carry[3:1];
endmodule
module fa(
    input wire a,b,cin,
    output wire cout, sum
);
    assign sum= a^b^cin;
    assign cout = a&b | b&cin | a &cin ;

endmodule
