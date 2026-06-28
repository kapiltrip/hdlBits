module top_module (
    input [1:0] sel,
    input [7:0] a,
    input [7:0] b,
    input [7:0] c,
    input [7:0] d,
    output [7:0] out
);
    wire [7:0] w1, w2;

    mux2 mux0 (sel[0], a, b, w1);
    mux2 mux1 (sel[0], c, d, w2);
    mux2 mux3 (sel[1], w1, w2, out);

endmodule
