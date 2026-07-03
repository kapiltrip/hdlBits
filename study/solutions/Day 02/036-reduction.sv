module top_module (
    input [7:0] in,
    output parity
);
assign parity= ^in;
//odd no of ones will be known by this
endmodule
