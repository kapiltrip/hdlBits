module top_module(
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
