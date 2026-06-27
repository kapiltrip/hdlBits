module top_module( 
    input [99:0] a, b,
    input cin,
    output [99:0] cout,
    output [99:0] sum 
);
//instantiating 100 fa , 
    wire [100:0] carry;
    assign carry[0]=cin;
    assign cout=carry[100:1];
genvar i ; 
    generate
        for(i=0;i<100;i=i+1)begin : adder100
            full_adder(
                .a(a[i]),
                .b(b[i]),
                .cin(carry[i]),
                .sum(sum[i]),
                .cout(carry[i+1])
            );
        end
    endgenerate
endmodule
module full_adder( 
    input a, b, cin,
    output cout, sum 
);
wire w1,w2,w3,w4;
    xor g1(sum, a,b,cin);
    //now the carry out part 
    xor g2(w1,a,b);
    and g3(w2,w1,cin);
    and g4(w3,a,b);
    or g5(cout,w2,w3);
endmodule
