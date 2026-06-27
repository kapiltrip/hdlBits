module top_module (input x, input y, output z);

    wire za1, zb1, za2, zb2;
    wire or_out, and_out;

    A IA1 (
        .x(x),
        .y(y),
        .z(za1)
    );

    B IB1 (
        .x(x),
        .y(y),
        .z(zb1)
    );

    A IA2 (
        .x(x),
        .y(y),
        .z(za2)
    );

    B IB2 (
        .x(x),
        .y(y),
        .z(zb2)
    );

    or  g1(or_out,  za1, zb1);
    and g2(and_out, za2, zb2);
    xor g3(z,       or_out, and_out);

endmodule


module A (input x, input y, output z);
    assign z = (x ^ y) & x;
endmodule


module B (input x, input y, output z);
    assign z = ~(x ^ y);
endmodule
