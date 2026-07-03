module top_module (input x, input y, output z);
wire w1;
    xor g1(w1,x,y);
    and g2(z,w1,x);
endmodule
