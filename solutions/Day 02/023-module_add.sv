module top_module(
    input [31:0] a,
    input [31:0] b,
    output [31:0] sum
);
    wire [15:0] a1Input=a[15:0];
    wire [15:0] b1Input=b[15:0];
    wire [15:0] a2Input=a[31:16];
    wire [15:0] b2Input=b[31:16];   
    wire [15:0] coutAdder1;
    wire [15:0] coutAdder2;
    wire [15:0] sum1,sum2;
    add16 adder1(
        .a(a1Input),
        .b(b1Input),
        .cin(0),
        .cout(coutAdder1),
        .sum(sum1)
    );
    add16 adder2(
        .a(a2Input),
        .b(b2Input),
        .cin(coutAdder1),
        .cout(coutAdder2),  // to ignore this
        .sum(sum2)
    );
    assign sum = {sum2,sum1};
endmodule
