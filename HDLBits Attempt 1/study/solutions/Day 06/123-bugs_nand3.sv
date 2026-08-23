module top_module (
    input a,
    input b,
    input c,
    output out
);
    wire and_result;

    andgate inst1 (and_result, a, b, c, 1'b1, 1'b1);
    not g1 (out, and_result);

endmodule
