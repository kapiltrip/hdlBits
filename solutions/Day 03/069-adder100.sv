module top_module(
    input [99:0] a, b,
    input cin,
    output cout,
    output [99:0] sum
);
genvar i ;
    wire [100:0] carry ;
    assign carry[0]=cin;
    generate
        for(i=0;i<100;i++)begin : calling
            fa fa1(
                .a(a[i]),
                .b(b[i]),
                .cin(carry[i]),
                .cout(carry[i+1]),
                .sum(sum[i])
            );
        end
    endgenerate
    assign cout = carry [100];
endmodule
module fa(
    input wire a,b,cin,
    output wire cout,sum
);
    assign sum = a^b^cin ;
    assign cout = a&b | b&cin| a&cin;
endmodule
