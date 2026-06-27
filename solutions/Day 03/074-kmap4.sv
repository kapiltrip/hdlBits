module top_module(
    input a,
    input b,
    input c,
    input d,
    output out  
); 
wire w1,w2,w3,w4,w5;
    not g1(w1,c); //c bar 
    not g2(w2,d);
    assign out= w1 & w2 & (a ^b) | w1 & d & ~(a ^ b ) | c & d & (a ^b)| c & w2 & ~(a ^ b);
endmodule
