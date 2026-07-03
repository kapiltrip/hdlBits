module top_module (
    input clock,
    input a,
    output reg p,
    output reg q
);

    // p is transparent while clock is high.
    always @(*) begin
        if (clock)
            p = a;
    end

    // q samples p when the clock falls.
    always @(negedge clock) begin
        q <= p;
    end

endmodule
