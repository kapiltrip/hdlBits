module top_module (
    input in1,
    input in2,
    input in3,
    output out
);
wire w1;
    xnor g1(w1,in1,in2);
    xor g2(out,in3,w1);
endmodule
