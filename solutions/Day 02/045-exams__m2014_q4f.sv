module top_module (
    input in1,
    input in2,
    output out
);
wire w1;
    not g1(w1,in2);
    and g2(out,w1,in1);
endmodule
